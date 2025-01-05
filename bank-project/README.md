<h1 align = Center>Los 10 bancos más grandes del mundo clasificados por capitalización en miles de millones de USD</h1>
<br>
<div align = Center>
<p>Este trabajo tuvo como objetivo crear un sistema automatizado que genere la información proveniente de la lista de los 10 bancos más grandes del mundo clasificados por capitalización en miles de millones de USD. <br>
Para llevar a cabo esta tarea se necesitaba transformar los datos y almacenarlos en USD, GBP, EUR y en INR según la información de tipo de cambio proporcionada por un archivo CSV. <br>
La tabla resultante sería consultada por los gerentes de diferentes países para extraer la lista y anotar el valor de capitalización de mercado en su propia moneda.</p></div>

<h2>Metodología</h2>
<div>
  <p>Fueron aplicadas operaciones de extracción, transformación y carga.</p>
</div>
<br>
<ul>
  <li> Se escribió una función para extraer la información tabular de la URL dada bajo el encabezado "Por capitalización de Mercado", y se guardó la información en un dataframe. </li>
  <li> Se escribió una función para transformar el dataframe añadiendo columnas para la Capitalización de mercado en GBP, EUR y INR, redondeadas a 2 decimales, basadas en la información de la tasa de cambio compartida como un archivo CSV.</li>
  <li>Se escribió una función para cargar el dataframe transformado en un archivo CSV de salida.</li>
  <li> Se escribió una función para cargar el dataframe transformado en un servidor de la base de datos SQL como una tabla.</li>
  <li> Se escribió una función para ejecutar consultas en la tabla de la base de datos.</li>
  <li> Se ejecutaron las siguientes consultas en la tabla de la base de datos: 
  <ol>
    <li> Extraer todos los datos de la tabla.</li>
    <li> Extraer los nombres de los bancos.</li>
    <li> Extraer el valor promedio de capitalización en GBP.</li>
  </ol></li>
  <li> Se escribió una función para registrar el progreso del código.</li>
</ul>

<h2>Recursos utilizados</h2>
<br>
<p>
  Para este trabajo se necesitaron las siguientes librerías de Python:
</p>
<ol>
  <li> Pandas: Para procesar los datos extraídos, almacenarlos en los formatos requeridos y comunicarse con las bases de datos.</li>
  <li> sqlite3: Necesaria para crear una conexión con el servidor de bases de datos.</li>
  <li> requests: Utilizada para acceder a la información desde la URL.</li>
  <li> bs4: Contiene la función BeautifulSoup utilizada para hacer el webscraping.</li>
  <li> numpy: Necesaria para las operaciones de redondeo matemático.</li>
  <li> datetime: Contiene la función datetime utilizada para extraer la marca de tiempo con fines de registro.</li>
</ol>
<br>
<p> URL utilizada: </p>
<p><a href = "https://web.archive.org/web/20230908091635 /https://en.wikipedia.org/wiki/List_of_largest_banks"> List of largest banks - Wikipedia </a></p>
<br>

<h2> Detalles del código: </h2>
<ul>
  <li> Nombre del código: <a href = "banks_project.py">banks_project.py</a></li>
  <li> Ruta del CSV de tasas de cambio: <a href = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/exchange_rate.csv">descarga</a></li>
  <li> Atributos de la tabla (solo al extraer): Name, MC_USD_Billion</li>
  <li> Atributos de la tabla final: Name, MC_USD_Billion, MC_GBP_Billion, MC_EUR_Billion, MC_INR_Billion</li>
  <li> Ruta del CSV de salida: ./Largest_banks_data.csv</li>
  <li> Nombre de la base de datos: <a href = "Banks.db">Banks.db</a></li>
  <li> Nombre de la tabla: <a href = "Largest_banks_data.csv">Largest_banks</a></li>
  <li> Archivo de registro: <a href = "code_log.txt">code_log.txt</a></li>
</ul>
<br>

<h2> Funciones creadas: </h2>
<ul>
  <li> log_progress() -> Registra el progreso del código en diferentes etapas en un archivo code_log.txt . Utiliza la lista de puntos de registro proporcionada para crear entradas de registro en cada etapa de código.</li>
  <li> extract() -> Extrae la información de la URL dada bajo el encabezado "Por capitalización de mercado" y la guarda en un dataframe.</li>
  <li> transform() -> Transforma el dataframe añadiendo columnas para la Capitalización de mercado en GBP, EUR e INR, redondeadas a 2 decimales, basadas en la información compartida como archivo CSV.</li>
  <li> load_to_csv() -> Carga el dataframe transformado a un archivo CSV de salida.</li>
  <li> load_to_db() -> Carga el dataframe transformado a un servidor de base de datos SQL como una tabla.</li>
</ul>
