<?php

$conexion = mysqli_connect('localhost', 'root', '', 'login');
// A través de la variable conexión y msqli_connect se conecta con la base de datos.
// Los parámetros usados son ('servidor', 'contrasena', 'usuario', 'base de datos').

// El campo contrasena no está especificado debido a que la base de datos con el usuario root no posee una contraseña prestablecida. 