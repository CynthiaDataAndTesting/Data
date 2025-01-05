# Code for ETL operations on Country-GDP data

# Importing the required libraries
import requests
import pandas as pd
import numpy as np
import sqlite3
from bs4 import BeautifulSoup
from datetime import datetime

# Variables
url = 'https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks'
csv_path = '/home/project/exchange_rate.csv'
csv_salida = '/home/project/Largest_banks_data,csv'
table_name = 'Largest_banks'
table_attribs = ['Name', 'MC_USD_Billion']
db_name = 'Banks.db'
log_file = "log_file.txt"  #almacena los registros.



def log_progress(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second 
    now = datetime.now() # get current timestamp 
    timestamp = now.strftime(timestamp_format) 
    with open(log_file,"a") as f: 
        f.write(timestamp + ':' + message + '\n') 

def extract(url, table_attribs):
    # Primero cargo la web como un documento html
    html_page = requests.get(url).text
    # Con BeautifulSoup extraigo la información. 
    data = BeautifulSoup(html_page, 'html.parser')

    # La tabla que necesito es la primera que aparece en el código html
    tables = data.find_all('tbody') # obtiene el cuerpo de todas las tablas en la web
    rows = tables[0].find_all('tr') # obtiene todas las filas de la primera tabla

    #Inicializo un dataframe vacío
    df = pd.DataFrame(columns=table_attribs)

    # Bucle for para extraer la información de la página web
    for row in rows: # itera sobre la variable rows
        col = row.find_all('td') # Extrae todos los datos td y los guarda en col.
        if len(col)!=0: # verifica si la longitud de col es 0.
                # Crea un diccionario con las claves iguales a las columnas del dataframe.
                data_dict = {"Name": col[1].get_text(strip=True),
                "MC_USD_Billion": float(col[2].get_text(strip=True))}
                # Convierte el diccionario a un dataframe y lo concatena con el existente.
                df1 = pd.DataFrame(data_dict, index=[0])
                df = pd.concat([df,df1], ignore_index=True) 

    return df

def transform(df, csv_path):
    ''' This function accesses the CSV file for exchange rate
    information, and adds three columns to the data frame, each
    containing the transformed version of Market Cap column to
    respective currencies'''

    # Primero cargo el archivo csv
    # Luego hago un diccionario con las tasas para fácil acceso
    exchange_rates = pd.read_csv(csv_path)
    rates_dict = dict(zip(exchange_rates['Currency'], exchange_rates['Rate']))

    # Creo columnas en el dataframe original
    df['MC_GBP_Billion'] = (df['MC_USD_Billion'] * rates_dict['GBP']).round(2)
    df['MC_EUR_Billion'] = (df['MC_USD_Billion'] * rates_dict['EUR']).round(2)
    df['MC_INR_Billion'] = (df['MC_USD_Billion'] * rates_dict['INR']).round(2)
    
    return df

def load_to_csv(df, output_path):
    ''' This function saves the final data frame as a CSV file in
    the provided path. Function returns nothing.'''
    df.to_csv(output_path)

def load_to_db(df, sql_connection, table_name):
    ''' This function saves the final data frame to a database
    table with the provided name. Function returns nothing.'''
    
    df.to_sql(table_name, sql_connection, if_exists = 'replace', index =False)

def run_query(query_statement, sql_connection):
    ''' This function runs the query on the database table and
    prints the output on the terminal. Function returns nothing. '''
    query_output = pd.read_sql(query_statement, sql_connection)
    print(query_statement)
    print(query_output)

''' Here, you define the required entities and call the relevant
functions in the correct order to complete the project. Note that this
portion is not inside any function.'''



extrac_data = extract(url, table_attribs)
print(extrac_data)
log_progress('Extraccion de datos completa. Iniciando el proceso ETL')

transform_data = transform(extrac_data, csv_path)
print(transform_data)
print(transform_data['MC_EUR_Billion'][4])
log_progress('Transformacion de datos completa. Iniciando proceso  de carga.')

load_to_csv(transform_data, csv_salida)
log_progress('Datos guardados en el archivo CSV')


# Abro conexión con la base de datos
conn = sqlite3.connect(db_name)
log_progress('Conexion SQL iniciada')

load_to_db(transform_data, conn, table_name)
print('Table is ready')
log_progress('Datos cargados a la base de datos como una tabla, ejecutando consultas.')

run_query(f'SELECT * FROM Largest_banks', conn)
run_query(f'SELECT AVG(MC_GBP_Billion) FROM Largest_banks', conn)
run_query(f'SELECT Name from Largest_banks LIMIT 5', conn)
log_progress('Proceso completo.')

# Cierro conexión con la base de datos.
conn.close()
log_progress('Conexion del servidor cerrada.')
