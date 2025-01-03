#importo las librerías que necesito
import glob 
import pandas as pd 
import xml.etree.ElementTree as ET 
from datetime import datetime 

#Rutas de archivo que estarán disponibles globalmente en el código 
#para todas las funciones.

log_file = "log_file.txt"  #almacena los registros.
target_file = "transformed_data.csv" #Almacena los datos de salida que puedo cargar en 
# la base de datos.

# Función para extraer los datos de un archivo CSV
def extract_from_csv(file_to_process): 
    dataframe = pd.read_csv(file_to_process)
    dataframe = dataframe.loc[:, ~dataframe.columns.str.contains('^Unnamed')] 
    return dataframe 

# Función para extraer datos de un archivo JSON.
def extract_from_json(file_to_process): 
    dataframe = pd.read_json(file_to_process, lines=True) 
    return dataframe 

# Función para extraer datos de un archivo XML
# Para extraer datos de un archivo «XML», 
# primero debo analizar los datos del archivo mediante la función «ElementTree».
# Debo conocer los encabezados de los datos extraídos para escribir esta función. 
# En estos datos, extraigo los encabezados «nombre», «altura» y «peso» de diferentes personas.
def extract_from_xml(file_to_process): 
    dataframe = pd.DataFrame(columns=["car_model", "year_of_manufacture", "price", "fuel"]) 
    tree = ET.parse(file_to_process) 
    root = tree.getroot() 
    for person in root: 
        car_model = person.find("car_model").text 
        year_of_manufacture = person.find("year_of_manufacture").text 
        price = float(person.find("price").text) 
        fuel = person.find("fuel").text
        dataframe = pd.concat([dataframe, pd.DataFrame([{"car_model":car_model, "year_of_manufacture":year_of_manufacture, "price":price, "fuel":fuel}])], ignore_index = True) 
    return dataframe 

def extract(): 
    extracted_data = pd.DataFrame(columns=['car_model','year_of_manufacture','price', 'fuel']) 
    # crea un dataframe vacío para almacenar los datos extraídos 
     
    # Procesa todos los archivos CSV 
    for csvfile in glob.glob("*.csv"): 
        temp_data = extract_from_csv(csvfile)
        extracted_data = pd.concat([extracted_data, temp_data], ignore_index=True) 
         
    # Procesa todos los archivos JSON 
    for jsonfile in glob.glob("*.json"): 
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_json(jsonfile))], ignore_index=True) 
     
    # Procesa todos los archivos XML 
    for xmlfile in glob.glob("*.xml"): 
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_xml(xmlfile))], ignore_index=True) 
         
    return extracted_data 

def transform(data): 
    # Redondea el precio a dos decimales 
    data['price'] = round(data.price,2) 
    data = data.loc[:, ~data.columns.str.contains('^Unnamed')]
    return data 

def load_data(target_file, transformed_data): 
    transformed_data.to_csv(target_file, index=False)

def log_progress(message): 
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second 
    now = datetime.now() # get current timestamp 
    timestamp = now.strftime(timestamp_format) 
    with open(log_file,"a") as f: 
        f.write(timestamp + ',' + message + '\n') 

# Registra la inicialización del proceso de ETL 
log_progress("ETL Job Started") 
 
# Registra el inicio del proceso de extracción 
log_progress("Extract phase Started") 
extracted_data = extract() 
 
# Registra la finalización del proceso de extracción 
log_progress("Extract phase Ended") 
 
# Registra el inicio del proceso de transformación 
log_progress("Transform phase Started") 
transformed_data = transform(extracted_data) 
print("Transformed Data") 
print(transformed_data) 
 
# Registra la finalización del proceso de transformación  
log_progress("Transform phase Ended") 
 
# Registra el inicio del proceso de carga
log_progress("Load phase Started") 
load_data(target_file,transformed_data) 
 
# Registra la finalización del proceso de carga
log_progress("Load phase Ended") 
 
# Registra la finalización del proceso de ETL. 
log_progress("ETL Job Ended") 