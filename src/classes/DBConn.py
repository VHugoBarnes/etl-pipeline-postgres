#coding: utf-8

import psycopg2
from configparser import ConfigParser

class DBConn:

    def __init__(self) -> None:
        pass

    @staticmethod
    def config(filename='database.ini', section='postgresql'):
        # Crea un parser.
        parser = ConfigParser()
        # Leer el archivo de configuracion.
        parser.read(filename)

        # Obtener la section y lo coloca en un diccionario.
        db = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found in the {1} file.'.format(section, filename))
        
        return db;
    
    @staticmethod
    def connect(filename):
        conn = None
        try:
            
            # Leer los datos de la conexion.
            params = DBConn.config(filename=filename)
            # Conectar con el server de PostgreSQL.
            print('Connecting with PostgreSQL database...')
            conn = psycopg2.connect(**params)

            # Crear un cursor
            cur = conn.cursor()

            # Ejecuta un statement de prueba
            # print("PostgreSQL database version:")
            # cur.execute("SELECT version()")

            # Muestra la version del servidor de base de datos PostgreSQL
            # db_version = cur.fetchone()
            # print(db_version)

            # Cierra la comunicacion con PostgreSQL
            # cur.close()

            return cur

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    