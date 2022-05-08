# EntregaFinal-IralaAriel
Proyecto Django 

Entrega final:

 1- Al momento de ingresar a la app en la ruta base ‘/’.
 2- Visualizar el home del blog.
 3- Poder listar todas las páginas del blog, poder ver en detalle cada una, poder crear, editar o borrar páginas del blog.
 4- Las páginas están formadas por un título, un contenido en editor de texto avanzado (ckeditor por ejemplo), una imagen, fecha de posteo de la imagen.
 5- Tener una app de registro donde se puedan registrar usuarios en el route accounts/signup, un usuario está compuesto por: email - contraseña - nombre de usuario.
 6- Tener una app de login en el route accounts/login/ la cual permite loguearse con los datos de administrador o de usuario normal.
 7- Herencia de HTML.
 8- Tener una app de perﬁles en el route accounts/proﬁle/ la cual muestra la info de nuestro usuario y permite poder modiﬁcar y/o borrar: imagen - nombre - descripción - un link a una página web - email y contraseña.
 9- Contar con un admin en route admin/ donde se puedan manejar las apps y los datos en las apps. 



 Entrega intermedia:
Link de GitHub con el proyecto totalmente subido a la plataforma.
Proyecto Web Django con patrón MVT que incluya:

 1. Herencia de HTML.
 2. Por lo menos 3 clases en models.
 3. Un formulario para insertar datos a todas las clases de tu models.
 4. Un formulario para buscar algo en la BD
 5. Readme que indique el orden en el que se prueban las cosas y/oo donde están las
funcionalidades.

Uso:

-> Iniciar el servidor e ingresar a la dirección IP de la misma en formato IP:PUERTO.    
-> La base de datos ya posee algunas entradas disponibles para explorar.    
-> Cuando se busca alguna entrada, se utiliza exactamente lo que se ingresa en el campo (sensible a mayúsculas).    
-> Todas las secciones permiten volver al menú principal, pero no navegar entre ellas.    


-> La página principal nos permite navegar por las 3 secciones principales: 

        1- Explorar la base de datos: ver todas las entradas de un modelo,        
        2- Buscar entrada en la base de datos: buscar todas las entradas de un modelo que coincidan con el parámetro ingresado,        
        3- Ingresar entrada en la base de datos: insertar una nueva entrada según el modelo y los parámetros deseados.
       

-> Cada sección nos otorga accesso a los 4 modelos disponibles:

        1- Jugadores,        
        2- Ítems,        
        3- Vehículos,        
        4- Administradores.
        
