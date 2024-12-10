<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="login.css">
    <title>Login</title>
</head>
<body>
<!--
    Contenedor Clase Principal: Se utiliza como base para colocar dentro todo el contenido de la página web. 

    Contenedor Formulario: Sirve como base para el formulario, identificado con color negro.

    Form: Formulario dónde los usuarios ingresarán los datos y así poder ingresar a la página de inicio. 
        - action: Nos ayuda a redireccionar los datos ingresados al archivo logueo.php una vez pulsado el botón. 
        - method: Nos ayuda a mandar los datos de forma anónima

    Contenedor Subtitulo: Contiene el título del Login

    label: Están identificados con nombres específicos porque con esto aplicamos css correctamente.

    input: Están identificados con nombres específicos porque con esto aplicamos css correctamente. 
-->
<div class = "principal">

<div class = "formulario">
    <form action="logueo.php" method="post">
        <div class="subtitulo">
            <h2>Login</h2>
        </div>
        <label for="" class="tusuario">Usuario</label>
        <label for="" class="tcontrasena">Contraseña</label>
        <br><br>
        <input type="text" name="usuario" class="iusuario">
        <input type="password" name="contrasena" id="" class="icontrasena">
        <br>
        <button>Ingresar</button>
    </form>

</div>
</div>



</body>
</html>