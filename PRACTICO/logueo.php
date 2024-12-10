<?php

// iniciamos el lenguaje php
include('db.php'); # Incluimos la conexion al archivo

# Iniciamos variables para almacenar los datos del formulario
$usuario = $_POST['usuario']; 
$contrasena = $_POST['contrasena'];

session_start(); # Iniciamos una session

// Preparamos la consulta para evitar inyección SQL
$stmt = $conexion->prepare("SELECT * FROM usuarios WHERE usuario = ? AND contrasena = ?");
if ($stmt === false) {
    die("Error al preparar la consulta: " . $conexion->error);
}

// Vinculamos los parámetros
$stmt->bind_param("ss", $usuario, $contrasena);

// Ejecutamos la consulta
$stmt->execute();

// Obtenemos el resultado
$resultado = $stmt->get_result();

if ($resultado->num_rows > 0) {
    // Si se encuentra el usuario
    $_SESSION['usuario'] = $usuario;
    header('location:inicio.php');
} else {
    // Usuario o contraseña incorrectos
    echo "Usuario o contraseña incorrectos. Inténtalo nuevamente.";
}

// Cerramos el statement
$stmt->close();

// Cerramos la conexión
$conexion->close();