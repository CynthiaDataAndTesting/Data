# importo las bibliotecas que necesito
import requests
import sqlite3
import pandas as pd
from bs4 import BeautifulSoup # solo necesito BeautifulSoup del paquete bs4

# URL requerida para el proyecto. 
url = 'https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films'
db_name = 'Movies.db' # base de datos
table_name = 'Top_50' # Tabla para almacenar el registro
csv_path = '/home/project/top_50_films.csv' # CSV para almacenar el registro
# Entidades requeridas
df = pd.DataFrame(columns=["Film","Year", "Rotten Tomatoes' Top 100"])
# Contador del bucle inicializado en cero, ya que se necesitan los mejores 50 resultados
count = 0

# Primero cargo la web como un documento html
html_page = requests.get(url).text
# Con BeautifulSoup extraigo la información. 
data = BeautifulSoup(html_page, 'html.parser')

# La tabla que necesito es la primera que aparece en el código html
tables = data.find_all('tbody') # obtiene el cuerpo de todas las tablas en la web
rows = tables[0].find_all('tr') # obtiene todas las filas de la primera tabla

# Bucle for para extraer la información de la página web
for row in rows: # itera sobre la variable rows
    if count<25: # no se pone <=50 porque la cuenta arranca en cero.
        col = row.find_all('td') # Extrae todos los datos td y los guarda en col.
        if len(col)!=0: # verifica si la longitud de col es 0.
            year = int(col[2].contents[0])  # Convierte el año a entero
            
            # Filtra solo los años 2000 en adelante
            if year >= 2000:
            # Crea un diccionario con las claves iguales a las columnas del dataframe.
                data_dict = {"Film": col[1].contents[0],
                            "Year": col[2].contents[0],
                            "Rotten Tomatoes' Top 100": col[3].contents[0]}
            # Convierte el diccionario a un dataframe y lo concatena con el existente.
                df1 = pd.DataFrame(data_dict, index=[0])
                df = pd.concat([df,df1], ignore_index=True)
                count+=1
    else:
        break #cuando llega a 50 entradas se rompe el bucle for. 

# Por último, imprimo el contenido del dataframe.
print(df)

# Guardo el dataframe en un archivo CSV. 
df.to_csv(csv_path)

# Guardo los datos en una base de datos.
# Primero inicio la conexión a la base, luego guardo el dataframe como una tabla
# y por último, cierro la conexión. 
conn = sqlite3.connect(db_name)
df.to_sql(table_name, conn, if_exists='replace', index=False)
conn.close()