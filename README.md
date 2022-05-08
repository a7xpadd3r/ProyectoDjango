# Entrega Final - Irala Ariel - Comisión 28805
# Features

-> 4 categorías listas para el ingreso variado de datos:
>       1- Jugadores,        
>       2- Ítems,        
>       3- Vehículos y        
>       4- Administradores.

-> Las cuales poseen, además de los respectivos a cada categoría, los siguientes parámetros en común:
>       1. Fecha de creación,    
>       2. Quién lo creó,    
>       3. Fecha de modificación,    
>       4. Quién lo modificó y    
>       5. Una imagen de muestra.    

-> Dentro de cada categoría podemos realizar las siguientes interaciones (dependiendo del nivel de acceso):
>       1- Buscar una entrada,        
>       2- Agregar una entrada,       
>       3- Modificar una entrada y/o
>       4- Eliminar una entrada.


# Uso

*Se requiere Pillow en su entorno virtual para iniciar el servidor.*    

-> Iniciar entorno virtual y luego el servidor.    
-> Ingresar a la dirección IP de la misma en formato IP:PUERTO. *Por defecto, 127.0.0.1:8000.*    
-> La base de datos ya posee algunas entradas disponibles para explorar.    
-> Cuando se busca alguna entrada, se utiliza exactamente lo que se ingresa en el campo (sensible a mayúsculas).    
-> Todas las secciones permiten volver al menú principal, pero no navegar entre ellas.    
> No es necesario iniciar sesión para explorar y buscar entradas, pero sí para agregar/modificar. Algunas requerirán de privilegios de administrador.
        
# Vídeo de muestra
[![IMAGE ALT TEXT](http://img.youtube.com/vi/utxTCCqOEWs/0.jpg)](http://www.youtube.com/watch?v=utxTCCqOEWs "Demostración del Proyecto")
        
# Consignas de evaluación

-> Entrega final:
       
        1. Al momento de ingresar a la app en la ruta base ‘/’.
        2. Visualizar el home del blog.
        3. Poder listar todas las páginas del blog, poder ver en detalle cada una, poder crear, editar o borrar páginas del blog.
        4. Las páginas están formadas por un título, un contenido en editor de texto avanzado (ckeditor por ejemplo), una imagen, fecha de posteo de la imagen.
        5. Tener una app de registro donde se puedan registrar usuarios en el route accounts/signup, un usuario está compuesto por: email - contraseña - nombre de usuario.
        6. Tener una app de login en el route accounts/login/ la cual permite loguearse con los datos de administrador o de usuario normal.
        7. Herencia de HTML.
        9. Tener una app de perﬁles en el route accounts/proﬁle/ la cual muestra la info de nuestro usuario y permite poder modiﬁcar y/o borrar: imagen - nombre - descripción - un link a una página web - email y contraseña.
        10. Contar con un admin en route admin/ donde se puedan manejar las apps y los datos en las apps. 
        
-> Entrega intermedia:

        Link de GitHub con el proyecto totalmente subido a la plataforma.
        Proyecto Web Django con patrón MVT que incluya:
        1. Herencia de HTML.
        2. Por lo menos 3 clases en models.
        3. Un formulario para insertar datos a todas las clases de tu models.
        4. Un formulario para buscar algo en la BD
        5. Readme que indique el orden en el que se prueban las cosas y/oo donde están las funcionalidades.
        
# Pendientes

        1. Arreglar la subida de imágenes para los usuarios registrados.
        2. Implementar límite de objetos visibles en la vista general de cada categoría.
        3. Implementar "Ver más" cuando se llegue al límite de objetos máximos a mostrar en las vistas generales de cada categorías.
        4. Implementar el editor de texto avanzado Ckeditor.
