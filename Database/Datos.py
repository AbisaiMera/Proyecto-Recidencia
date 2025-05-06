from Database.Conexion_SQL_Server import *

class BD:
    def datosRPU(RPU):
        try:
            # Conectar a la base de datos
            connection = ConexionSQL.conexionBD()
            with connection.cursor() as cursor:
                # Consulta SQL mejor estructurada
                query = """
                SELECT 
                    t2.c2s_rpu as RPU, 
                    t2.c2s_nombre as NOMBRE,   
                    (t5.i5_ciclo + t5.i5_division + t5.i5_zona + 
                    t5.i5_agencia + t5.i5_poblacion + 
                    t5.i5_ruta + t5.i5_folio) as CUENTA,
                    t5.i5_agencia as AGENCIA
                FROM SCM.CATAL2 AS t2
                LEFT JOIN SCM.CATAL5 as t5 ON t2.c2s_rpu = t5.i5_rpu
                LEFT JOIN SCM.CATAL3 as t3 ON t2.c2s_rpu = t3.I3_RPU
                WHERE t5.i5_zona = '13' AND t2.c2s_rpu = ?
                """
                cursor.execute(query, (RPU,))  # Aquí pasamos el parámetro correctamente
                resultado = cursor.fetchone()
        
            # Retornar el resultado
            return resultado

        except Exception as ex:
            print(f"Error: {ex}")
            return None
        
    def medidores(RPU):
        try:
            # Conectar a la base de datos
            connection = ConexionSQL.conexionBD()
            with connection.cursor() as cursor:
                # Consulta SQL mejor estructurada
                query = """
                SELECT 
                    t2.c2s_rpu as RPU,
                    t3.I3_NUMED as MEDIDOR
                FROM SCM.CATAL2 AS t2
                LEFT JOIN SCM.CATAL5 as t5 ON t2.c2s_rpu = t5.i5_rpu
                LEFT JOIN SCM.CATAL3 as t3 ON t2.c2s_rpu = t3.I3_RPU
                WHERE t5.i5_zona = 13 AND t2.c2s_rpu = ?
                """
                cursor.execute(query, (RPU,))  # Aquí pasamos el parámetro correctamente
                resultado = cursor.fetchall()
        
            # Retornar el resultado
            return resultado

        except Exception as ex:
            print(f"Error: {ex}")
            return None

    def mostrardatos(rpu, desde, hasta):

        try:
            # Conectar a la base de datos
            connection = ConexionSQL.conexionBD()
            with connection.cursor() as cursor:
                # Consulta SQL mejor estructurada
                query = """
                SELECT i4_fecha_ade, i4_periodo_consumo_desde, i4_periodo_consumo_hasta, i4_kwh 
                FROM (
                    SELECT i4_fecha_ade, i4_periodo_consumo_desde, i4_periodo_consumo_hasta, i4_kwh, i4_rpu, i4_tipo_ade 
                    FROM SCM.CATAL4
                    UNION ALL
                    SELECT i4_fecha_ade, i4_periodo_consumo_desde, i4_periodo_consumo_hasta, i4_kwh, i4_rpu, i4_tipo_ade 
                    FROM SCM.CATAL4_HIST
                ) AS union_data
                INNER JOIN SCM.CATAL5 AS t5 ON union_data.i4_rpu = t5.i5_rpu AND t5.i5_zona = '13'
                WHERE union_data.i4_rpu = ?
                AND ? < union_data.i4_periodo_consumo_hasta
                AND ? > union_data.i4_periodo_consumo_desde
                ORDER BY union_data.i4_periodo_consumo_desde;
                """
                cursor.execute(query, (rpu, desde, hasta))  # Aquí pasamos los parametros correctamente
                resultado = cursor.fetchall()
        
            # Retornar el resultado
            return resultado

        except Exception as ex:
            print(f"Error: {ex}")
            return None
        
    def tarifa(RPU, medidor):

        try:
            # Conectar a la base de datos
            connection = ConexionSQL.conexionBD()
            with connection.cursor() as cursor:
                # Consulta SQL mejor estructurada
                query = """
                SELECT 
					t2.c2s_tarifa as TARIFA
                FROM SCM.CATAL2 AS t2
                LEFT JOIN SCM.CATAL5 as t5 ON t2.c2s_rpu = t5.i5_rpu
                LEFT JOIN SCM.CATAL3 as t3 ON t2.c2s_rpu = t3.I3_RPU
                WHERE t5.i5_zona = 13 AND t2.c2s_rpu = ? AND t3.I3_NUMED = ?
                """
                cursor.execute(query, (RPU,medidor, ))  # Aquí pasamos los parametros correctamente
                resultado = cursor.fetchone()
        
            # Retornar el resultado
            return resultado

        except Exception as ex:
            print(f"Error: {ex}")
            return None

    def periodocalcular(rpu, desde, hasta):

        try:
            # Conectar a la base de datos
            connection = ConexionSQL.conexionBD()
            with connection.cursor() as cursor:
                # Consulta SQL mejor estructurada
                query = """
                SELECT i4_fecha_ade, i4_periodo_consumo_desde, i4_periodo_consumo_hasta, i4_kwh 
                FROM (
                    SELECT i4_fecha_ade, i4_periodo_consumo_desde, i4_periodo_consumo_hasta, i4_kwh, i4_rpu, i4_tipo_ade 
                    FROM SCM.CATAL4
                    UNION ALL
                    SELECT i4_fecha_ade, i4_periodo_consumo_desde, i4_periodo_consumo_hasta, i4_kwh, i4_rpu, i4_tipo_ade 
                    FROM SCM.CATAL4_HIST
                ) AS union_data
                INNER JOIN SCM.CATAL5 AS t5 ON union_data.i4_rpu = t5.i5_rpu AND t5.i5_zona = '13'
                WHERE union_data.i4_rpu = ?
                AND union_data.i4_tipo_ade = 1
                AND ? < union_data.i4_periodo_consumo_hasta
                AND ? > union_data.i4_periodo_consumo_desde
                ORDER BY union_data.i4_periodo_consumo_desde;
                """
                cursor.execute(query, (rpu, desde, hasta))  # Aquí pasamos los parametros correctamente
                resultado = cursor.fetchall()
        
            # Retornar el resultado
            return resultado

        except Exception as ex:
            print(f"Error: {ex}")
            return None    