

                           PROYECTO INDIVIDUAL N°:01 DATA SCIENCE COHORTE 10

                                    Machine Learning Operations (MLOps)

Creacion de API de películas y sistema de recomendación atraves de fastAPI

Creacion de API de películas y sistema de recomendación atraves de fastAPI

En el primer proyecto individual del Bootcamp de la carrera de  Data Science en primera academia de tecnología de Latinoamérica soyhenrry.

Se nos pide crear un MVP (Minimum Viable Product) de un producto de Machine Learning en una semana, realizando limpieza y transformación de los datos y que algunas columnas tenian el formato json se aplico json_normalize, para aplanar la data y desplegando la API desde donde consumimos los datos tanto el modelo de Machine Learning como algunos consultas sobre los datos.

Durante el proyecto se realizo los siguentes procesos:
- Extracion de los datos
- Limpieza de datos con Python
- Preprocesamiento de datos para Machine Learning
- Desarrollo de un sistema de recomendación de películas para el usuario
- Desarrollo del API con Fastapi
- Despliegue del API con Render

 Objetivo del Proyecto:
1. desarrollar una API en fastAPI para realizar la consulta atraves de una funcion
2. desarrollar un sistema de recomendacion de peliculas y deve de recomendar 5 peliculas con mayor puntaje

Para Realizar Recomendaciones Utilizando la Librería Surprise, es necesario seguir los siguientes pasos:

1. Importar las librerías necesarias y cargar los datos de las películas.

2. Crear un objeto de la clase Reader para definir el rango de calificaciones posibles.

3. Crear un objeto de la clase Dataset para cargar los datos en un formato que pueda ser utilizado por Surprise.

4. Divide los datos en conjuntos de entrenamiento y prueba.

5. Seleccione un algoritmo de recomendaciones, entrenamos con los datos de entrenamiento y prediga las valoraciones de las peliculas para un voto promedio que califico el usuario para dicha titulo de la pelicula.
Ordenar las películas según las calificaciones predichas y devolver las cinco películas con mayor puntaje.

Enlace a la API Listo para consumir: https://proyecto-api-recomendacion.onrender.com/docs#/

HERAMIENTAS QUE SE A UTILIZADO Y MATERIALES COMPLEMENTARIOS:

1. fastAPI(Gia de usuario de fastAPI):https://fastapi.tiangolo.com/tutorial/
2. Render(documentacion para el usuario sobre render):https://render.com/docs/free#free-web-services
3. Tutural de render:https://github.com/HX-FNegrete/render-fastapi-tutorial.git
4. como usar .gitignore en las diferentes herramientas:https://github.com/github/gitignore/blob/main/Python.gitignore 
5. ¡Bienvenidos al primer proyecto individual de la etapa de labs! En esta ocasión, deberá hacer un trabajo situándose en el rol de un MLOps Engineer y lo encuentras en el siguiente enlace de git:https://github.com/HX-PRomero/PI_ML_OPS.git
6. Pandas json_normalize():https://github.com/BindiChen/machine-learning/blob/main/data-analysis/028-pandas-json_normalize/pandas-json_normalize.ipynb
7. cuan estuve trabajando con entorno virtual me surgieron algunos errores como Set-ExecutionPolicy y lo encontramos en la siguiente 
   documentacion https://learn.microsoft.com/es-es/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.3
 8. Estoy tratando de instalar un paquete en Python, pero Python arroja un error al instalar paquetes. Recibo un error cada vez que intento instalar pip install surprise.
  . primero ejecutas para actualizar el setuptool con pip install --upgrade setuptool
  . si te sale el error: se requiere Microsoft Visual C ++ 14.0 o superior, lo instalas, mas respuestas: https://stackoverflow.com/questions/64261546/how-to-solve-error-microsoft-visual-c-14-0-or-greater-is-required-when-inst 
   
   VIDEOS DE APOYO
   . Error de Git Fatal: el origen remoto ya existe https://www.youtube.com/watch?v=H3KjgiBaakM
   
   RECOMENDACION DE ERRORES AL MOMENTO DE RENDERIZAR 
   1. en el requirementts.txt al renderizar no coloque la version en los siguiente:
     asttokens,pandas,numpy, matplotlibipy,kernel,ipython,jedi,contourpy y pythonwin, para que no te arroje el error o sino trabaja con.
     fastAPI, uvicorn, pandas y numpay , para que te evites problemas al momento de renderizar.
   2. cuando te arroja un error que no encuentra el directorio ejemplo si tu dataset al subir a git se encuetra en mi_dataset, por ende.
    Tienes que llamar de mi_dataset al renderizar no de la raiz como estubiste trabajando localmente  


