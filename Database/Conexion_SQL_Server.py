import pyodbc

class ConexionSQL:

    def conexionBD():
        try:
            conexion = pyodbc.connect('DRIVER={SQL Server};SERVER=10.4.9.79;DATABASE=scintegral;UID=consultaDesarrollo;PWD=c0nsult42024')
            print('Conexion Exitosa')
            
            return(conexion)

        except Exception as ex:
            print(ex)

            return(conexion)
        
    conexionBD()

