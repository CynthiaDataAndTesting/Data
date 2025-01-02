<h1 align = Center>Extracción, Transformación y Carga (ETL)</h1>
<br>
<br>
<div align = Center>
<p>En esta ocasión, he realizado mi primer proyecto aplicando un proceso ETL con Python.</p>
<p>El objetivo principal de la tarea es realizar la extracción de datos de diferentes tipos de archivos, la transformación de los datos y luego su carga en una base de datos para su posterior procesamiento. </p></div>
<br>
<br>
<h2>Sobre las fuentes de datos</h2>
<p>Nuestras fuentes son listados de autos usados. Estos listados vienen en formato CSV, JSON y XML. <br>
Los autos usados tienen cuatro atributos: modelo (car_model), año de fabricación (year_of_manufacture), precio (price) y tipo de combustible (fuel).</p>
<br>
<br>
<h2>Procedimiento</h2>
<ol>
  <li>Se creó la carpeta data_source y dentro de ésta el archivo etl.practice.py</li>
  <li>Se cargaron los distintos archivos al directorio. En este trabajo se utilizaron los tipos CSV, JSON y XML. (Puedes descargarlos <a href = https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0221EN-SkillsNetwork/labs/module%206/Lab%20-%20Extract%20Transform%20Load/data/datasource.zip >aquí</a>).</li>
  <li>Se crearon dos archivos: target_file y log_file.
    <ol>
    <li>log_file: almacena los registros de cada operación realizada dentro del proceso ETL.</li>
    <li>target_file: almacena los datos de salida que pueden ser cargados en una base de datos. target_file tiene formato .csv</li>
    </ol></li>
  <li>Se extrayeron los datos de cada archivo.</li>
  <li>Se creo un dataframe vacío que sirve de contenedor para los datos extraídos.</li>
  <li>Se procesan los archivos. Es decir, se aplica la etapa de extracción del proceso ETL.</li>
  <li>Se aplican transformaciones a los datos. En este caso, el precio de los autos se redondea a dos cifras decimales.</li>
  <li>Los datos se cargan en el dataframe. Y los procedimientos aplicados se registran en el archivo log_file</li>
</ol>
<br>
<br>
<h2>Estructura del Proyecto</h2>
<p><strong>data_source:</strong> carpeta que contiene todos los archivos importantes del proyecto. Tiene función de directorio.</p>
<br>
<p><strong>datasource.zip:</strong> carpeta comprimida que contiene los distintos archivos fuentes.</p>
<br>
<p><strong>etl_practice.py:</strong> script de python que contiene el código del proyecto.</p>
<br>
<p><a href = "Data\ETL process\data_source\log_file.txt"><strong>log_file.txt:</strong></a> archivo que lleva el registro en formato fecha de cada ejecución del proceso ETL.</p>
<br>
<p><strong>transformed_data.csv:</strong> archivo que contiene los datos finales.</p>
<br>
<p><strong>used_car_prices1.csv:</strong> archivo fuente que contiene un listado de autos usados en formato csv.</p>
<br>
<p><strong>used_car_prices1.json:</strong> archivo fuente que contiene un listado de autos usados en formato json.</p>
<br>
<p><strong>used_car_prices1.xml:</strong> archivo fuente que contiene un listado de autos usados en formato xml.</p>
<br>
<p><strong>used_car_prices2.csv:</strong> archivo fuente que contiene un listado de autos usados en formato csv.</p>
<br>
<p><strong>used_car_prices2.json:</strong> archivo fuente que contiene un listado de autos usados en formato json.</p>
<br>
<p><strong>used_car_prices2.xml:</strong> archivo fuente que contiene un listado de autos usados en formato xml.</p>
<br>
<p><strong>used_car_prices3.csv:</strong> archivo fuente que contiene un listado de autos usados en formato csv.</p>
<br>
<p><strong>used_car_prices3.json:</strong> archivo fuente que contiene un listado de autos usados en formato json.</p>
<br>
<p><strong>used_car_prices3.xml:</strong> archivo fuente que contiene un listado de autos usados en formato xml.</p>
<br>
