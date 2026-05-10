import mysql.connector
import pandas as pd
import boto3
import os

# 1. Configuración de conexión (Asegúrate de que estos datos sean correctos)
DB_CONFIG = {
    'host': 'tu_host_mysql',      # Ej: localhost o la IP de tu contenedor/RDS
    'user': 'root',
    'password': 'tu_password',
    'database': 'nombre_bd'
}

FILE_NAME = "data.csv"
BUCKET_NAME = "gcr-output-01"

def ejecutar_ingesta():
    try:
        # 2. Extracción de MySQL
        print("Conectando a MySQL...")
        conn = mysql.connector.connect(**DB_CONFIG)
        query = "SELECT * FROM tu_tabla" # <--- Cambia esto por tu tabla real
        
        print("Extrayendo datos a Pandas...")
        df = pd.read_sql(query, conn)
        
        # 3. Guardado local temporal
        df.to_csv(FILE_NAME, index=False)
        print(f"Archivo {FILE_NAME} generado localmente.")

        # 4. Carga a S3 (Tu código original integrado)
        print(f"Subiendo a S3 bucket: {BUCKET_NAME}...")
        s3 = boto3.client('s3')
        s3.upload_file(FILE_NAME, BUCKET_NAME, FILE_NAME)
        
        print("Ingesta completada con éxito")

    except Exception as e:
        print(f"Error en el proceso: {e}")
    
    finally:
        if 'conn' in locals() and conn.is_connected():
            conn.close()
            print("Conexión a MySQL cerrada.")

if __name__ == "__main__":
    ejecutar_ingesta()