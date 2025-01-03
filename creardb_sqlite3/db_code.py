# Para crear una base de datos usando Python necesito sqlite3
import sqlite3
import pandas as pd

# Hay que crear una base de datos llamada STAFF y 
# cargar el contenido del archivo csv con una tabla llamada INSTRUCTORS.

conn = sqlite3.connect('STAFF.db')

# Creo una tabla en la base de datos con los atributos correspondientes.
# También es necesario conocer el tipo de dato de cada atributo. 

# El conjunto de datos es un registro de empleados que está disponible
# con un equipo de Recursos Humanos en un archivo CSV.

# ID: es el id del empleado
# FNAME: Nombre
# LNAME: Apellido
# CITY: Ciudad de residencia
# CCODE: Código de país (2 letras)

table_name = 'INSTRUCTOR'
attribute_list = ['ID', 'FNAME', 'LNAME', 'CITY', 'CCODE']

# Proceso el csv con read_csv()
# como el csv no tiene encabezados, uso las claves de attribute_list
file_path = '/home/project/INSTRUCTOR.csv'
df = pd.read_csv(file_path, names = attribute_list)

# Cargo los datos a la tabla 
df.to_sql(table_name, conn, if_exists = 'replace', index =False)
print('Table is ready') # identifico los pasos del código hasta este punto.

# Aquí comienzan las consultas SQL sobre los datos

# 1. Ver todos los datos de la tabla.
query_statement = f"SELECT * FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# 2. Visualizar solo la columna FNAME de datos.
query_statement = f"SELECT FNAME FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# 3. Ver la cantidad total de entradas en la tabla. 
query_statement = f"SELECT COUNT(*) FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# Agregando datos a la tabla. 

# creo un dataframe con los nuevos datos. 
data_dict = {'ID' : [100],
            'FNAME' : ['John'],
            'LNAME' : ['Doe'],
            'CITY' : ['Paris'],
            'CCODE' : ['FR']}
data_append = pd.DataFrame(data_dict)

# Agrego los datos a la tabla INSTRUCTORS
data_append.to_sql(table_name, conn, if_exists = 'append', index =False)
print('Data appended successfully')

# Verifico otra vez la cantidad de entradas en la tabla. 
# Tiene que haber aumentado en uno. 
query_statement = f"SELECT COUNT(*) FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

conn.close() # Cierro la conexión. 