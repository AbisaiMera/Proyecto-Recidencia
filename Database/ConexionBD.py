import mysql.connector

class ConexionMySQL:

    def conexionBD():
        
        try:
            # Conexion a MySQL
            conexion = mysql.connector.connect(user='root', password='1234567890', host='localhost', database='Prueba_sistema_CFE', port='3306')

            print("Conexion Exitosa")

            return(conexion)
        except mysql.connector.Error as error:

            print("Error al conectar a la BD {}".format(error))

            return conexion
    
    conexionBD()