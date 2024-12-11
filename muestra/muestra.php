<?php
include('db.php'); // Ingresamos la conexión de la base de datos para aplicar la muestra de datos.

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="muestra.css">
    <title>Muestra</title>
</head>
<body>
<!-- 
    Contenedor Principal: Sirve de base para la estructura html después del body. 
    Contenedor Tabla: Sirve para dar forma a la tabla dónde se mostrarán los datos. 
    Contenedor título: Sirve como base para el título de la tabla. 
    Contenedor Table: Especifica la tabla dónde se mostrarán los datos. 
-->
    <div class="Principal">
        <div class="Tabla">
            <div class="titulo">
                <h1>Usuarios registrados</h1>
            </div>
            <table>
                <tr>
                    <td class="unico">Usuario</td>
                    <td>Descripción</td>
                    <td>Rango</td>
                </tr>
                <?php

                // Hacemos la petición de datos a la tabla usuarios
                $sql = "SELECT *FROM usuarios"; 
                // Validamos la conexión y los datos para verificar si estos se han guardado correctamente. 
                $validacion = mysqli_query($conexion, $sql);

                /*
                Iniciamos el ciclo while y en su sentencia pondré el número de registro de la base de datos como registro.
                El ciclo no cierra hasta después de establecer los campos de la tabla, y con un echo mandamos a llamar los datos guardados en el array
                y mostrarlos en la tabla.
                */
                while ($muestra = mysqli_fetch_array($validacion)) {

                ?>
                <tr>
                    <td><?php echo $muestra['Usuario']?></td>
                    <td><?php echo $muestra['Descripcion']?></td>
                    <td><?php echo $muestra['Rango']?></td>

                    
                <?php
                } // Se cierra el ciclo para dar por finalizado el conteo de datos y son representados en la tabla. 
                ?>
                </tr>
            </table>
        </div>
    </div>
</body>
</html>