

                           PROYECTO INDIVIDUAL N°:01 DATA SCIENCE COHORTE 10

                                    Machine Learning Operations (MLOps)

Creacion de API de películas y sistema de recomendación atraves de fastAPI

Creacion de API de películas y sistema de recomendación atraves de fastAPI

En el primer proyecto individual del Bootcamp de la carrera de  Data Science en primera academia de tecnología de Latinoamérica soyhenrry.

Se nos pide crear un MVP (Minimum Viable Product) de un producto de Machine Learning en 1 semana, realizando limpieza y transformación de los datosy que algunas columnas tienen el formato json, se aplico json_normalize, para aplanar la data, creando un sistema de recomendación, y desplegando la API desde donde consumir tanto el modelo de Machine Learning como algunos consultas sobre los datos.

Durante el proyecto realicé las siguientes tareas:

Limpieza de datos con Python
Preprocesamiento de datos para Machine Learning
Desarrollo de un sistema de recomendación de películas para el usuario con Surprise
Desarrollo del API con Fastapi
Despliegue del API con Render

Objetivo del proyecto:
1. desarrollar una API en fastAPI para realizar la consulta atraves de una funcion
2. desarrollar un sistema de recomendacion de peliculas y deve de recomendar 5 peliculas con mayor puntaje

Transformaciones de los datos:

. Algunos campos, como belongs_to_collection, production_companies y otros (ver diccionario de datos) están anidados, esto es o bien tienen un diccionario o una lista como valores en cada fila, ¡deberán desanidarlos para poder y unirlos al dataset de nuevo hacer alguna de las consultas de la API! O bien buscar la manera de acceder a esos datos sin desanidarlos.

. Los valores nulos de los campos revenue, budget deben ser rellenados por el número 0.

. Los valores nulos del campo release date deben eliminarse.

. De haber fechas, deberán tener el formato AAAA-mm-dd, además deberán crear la columna release_year donde extraerán el año de la fecha de estreno.

. Crear la columna con el retorno de inversión, llamada return con los campos revenue y budget, dividiendo estas dos últimas revenue / budget, cuando no hay datos disponibles para calcularlo, deberá tomar el valor 0.

. Eliminar las columnas que no serán utilizadas, video,imdb_id,adult,original_title,vote_count,poster_path y homepage.


