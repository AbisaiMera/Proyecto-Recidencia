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

    def mostrardatos(RPU, medidor, desde, hasta):

        try:
            # Conectar a la base de datos
            connection = ConexionSQL.conexionBD()
            with connection.cursor() as cursor:
                # Consulta SQL mejor estructurada
                query = """
                SELECT t4.i4_fecha_ade as FECHA, t4.i4_periodo_consumo_desde as DESDE, t4.i4_periodo_consumo_hasta as HASTA, cll.CONSUMO
	            FROM SCM.CATAL2 AS t2
		            left join SCM.CATAL5 as t5 on t2.c2s_rpu=i5_rpu
		            left join SCM.CATAL3 as t3 on t2.c2s_rpu=I3_RPU
		            left join SCM.CATAL2A AS t2a on t2.c2s_rpu=t2a.i2a_rpu
		            left join SCM.CATALL as cll on t2.c2s_rpu=cll.RPU
		            left join SCM.CATAL4 as t4 on t2.c2s_rpu=t4.i4_rpu
                WHERE t5.i5_zona='13' AND t2.c2s_rpu = ? AND t3.I3_NUMED = ? AND cll.CONSUMO = t4.i4_kwh
		            AND ? <= t4.i4_periodo_consumo_hasta
			        AND ? >= t4.i4_periodo_consumo_desde
                GROUP BY t2.c2s_rpu, t2.c2s_nombre, t2.c2s_medidores, t2.c2s_tipo_suministro,
		            t3.I3_NUMED,  t5.i5_agencia, t2.c2s_tarifa,
		            t5.i5_ciclo,t5.i5_division,t5.i5_zona,t5.i5_agencia,t5.i5_poblacion,t5.i5_ruta, t5.i5_folio,
		            t2.c2s_tipo_suministro, cll.CONSUMO, t4.i4_kwh, t4.i4_fecha_ade, t4.i4_periodo_consumo_desde, t4.i4_periodo_consumo_hasta

                ORDER BY i4_fecha_ade
                """
                cursor.execute(query, (RPU,medidor,desde,hasta, ))  # Aquí pasamos los parametros correctamente
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