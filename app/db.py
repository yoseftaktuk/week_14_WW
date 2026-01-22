import mysql.connector
import os
from mysql.connector import MySQLConnection
from fastapi import HTTPException 


class MySQLManager:
    def __init__(self):
        self.config = {
        'user': os.getenv("MYSQL_USER"),
        'password': os.getenv("MYSQL_PASSWORD"),
        'host': os.getenv("MYSQL_HOST"),
        'database': os.getenv("MYSQL_DATABASE")
        }

    def get_cnx(self):
        try:
            cnx = mysql.connector.connect(**self.config)
            cnx.ping(reconnect=True, attempts=3, delay=0)
            return cnx
        except mysql.connector.Error as e:
            raise e
        
 
class Init_sql:
    def __init__(self, cnx: MySQLConnection):
        self.cnx = cnx
    def create_db(self):
        query = 'CREATE DATABASE IF NOT EXISTS Weapon_Warehouse;'
        try:
            cursor = self.cnx.cursor(dictionary=True)
            cursor.execute(query)
        except Exception as e:
            raise HTTPException(status_code=404, detail=str(e))
        
    def use_db(self):
        query = 'USE Weapon_Warehouse;'
        try:
            cursor = self.cnx.cursor(dictionary=True)
            cursor.execute(query)
        except Exception as e:
            raise HTTPException(status_code=404, detail=str(e))
        
    def create_table(self):
        query = """
                CREATE TABLE IF NOT EXISTS records_Warehouse (
                id INT AUTO_INCREMENT PRIMARY KEY,
                weapon_id VARCHAR,
                weapon_name VARCHAR,
                weapon_type VARCHAR,
                range_km INT,
                weight_kg FLOAT,
                manufacturer VARCHART,
                origin_country VARCHART,
                storage_location VARCHART,
                year_estimated INT,
                risk_level VARCHAR
            );
                """
        try:
            cursor = self.cnx.cursor(dictionary=True)
            cursor.execute(query)
        except Exception as e:
            raise HTTPException(status_code=404, detail=str(e))        
        
    def insert(self, data: dict):
            query = f'INSERT INTO records_Warehouse (weapon_id, weapon_name, weapon_type, range_km, weight_kg, manufacturer, origin_country, storage_location, year_estimated, risk_level)'\
            'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            cursor  = self.cnx.cursor()
            cursor.execute(query, data['weapon_id'], data['weapon_name'], data['weapon_type'], data['weight_kg'], data['manufacturer'], data['origin_country'], data['storage_location'], data['year_estimated'], data['risk_level)'])
    
    def init_db(self):
        try:
            self.create_db(self.cnx)
            self.use_db(self.cnxcnx)
            self.create_table(self.cnx)
            self.cnx.commit()
        except Exception as e:
            raise HTTPException(status_code=404, detail=str(e))