<?php

// Conectamos la base de datos
$conexion = mysqli_connect('localhost', 'root', '', 'muestra');

/* Utilizamos "mysqli_connect" para ingresar los datos de session dentro de la base de datos. 
    Dentro de los parámetros de mysqli_query encontramos los datos de inicio de sesión 
    y están constituídos de la siguiente manera ('Servidor', 'Usuario', 'Contraseña', 'DB')

    El campo contraseña no posee ningún parámetro porque el usuario ingresado no contiene una. */
    