import sqlite3
import pandas as pd

conn = sqlite3.connect('STAFF.db') # me conecto a la base de datos

# Crea una nueva tabla llamada Departments

# DEPT_ID: id del departamento
# DEP_NAME: nombre del departamento
# MANAGER_ID: id del gerente
# LOC_ID: id de ubicación

table_name = 'Departments'
attribute_list = ['DEPT_ID', 'DEP_NAME', 'MANAGER_ID', 'LOC_ID']

# Proceso el csv con read_csv()
# como el csv no tiene encabezados, uso las claves de attribute_list
file_path = '/home/project/Departments.csv'
df = pd.read_csv(file_path, names = attribute_list)

# Cargo los datos a la tabla 
df.to_sql(table_name, conn, if_exists = 'replace', index =False)
print('Table is ready') # identifico los pasos del código hasta este punto.

# creo un dataframe con los nuevos datos. 
data_dict = {'DEPT_ID' : [9],
            'DEP_NAME' : ['Quality assurance'],
            'MANAGER_ID' : ['30010'],
            'LOC_ID' : ['L0010']}
data_append = pd.DataFrame(data_dict)

# Agrego los datos a la tabla Departments
data_append.to_sql(table_name, conn, if_exists = 'append', index =False)
print('Data appended successfully')

# Aquí ejecuto consultas sql 

# 1. Ver todos los datos de la tabla.
query_statement = f"SELECT * FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# 2. Visualizar solo la columna FNAME de datos.
query_statement = f"SELECT DEP_NAME FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# 3. Ver la cantidad total de entradas en la tabla. 
query_statement = f"SELECT COUNT(*) FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

