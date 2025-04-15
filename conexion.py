from mysql.connector import pooling, Error

class Conexion:
    DATABASE = 'boutique_cef'
    USERNAME = 'root'
    PASSWORD = 'dipi1138'
    PORT = '3306'
    HOST = 'localhost'
    POOL_SIZE = 5
    POOL_NAME = 'boutique_cef_pool'
    pool = None

    @classmethod
    def obtener_pool(cls):
        if cls.pool == None:
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name=cls.POOL_NAME,
                    pool_size= cls.POOL_SIZE,
                    host= cls.HOST,
                    port= cls.PORT,
                    database= cls.DATABASE,
                    user= cls.USERNAME,
                    password= cls.PASSWORD)
                return cls.pool
            except Error as e:
                return f'Ocurrio un error al obtener el pool {e}'
        else:
            return cls.pool

    @classmethod
    def obtener_conexion(cls):
        return cls.obtener_pool().get_connection()

    @classmethod
    def liberar_conexion(cls, conexion):
        conexion.close()


if __name__ == '__main__':
    pool = Conexion.obtener_pool()
    print(pool)
    cnx1 = Conexion.obtener_conexion()
