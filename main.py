
from fastapi import FastAPI


import pandas as pd
# a fastapi lo paso un titulo del proyecto, vercion
app = FastAPI(title="PROYECTO INDIVIDUAL-N°1", 
              description="Machine Learning Operations (MLOps)",
              version="22.3.1")
@app.get("/")
async def root():
    return {"hola te damos la bienvenida": "a tu plataforma favorito de peliculas, series y comedia"}

@app.get("/index")
async def index():
    return {" bienvenida": "API REALIZADO POR BEDER RIVERA"}


df_fastapi=pd.read_csv("../trabajo_venv/Data_set/df_movies_dataset_actualizado_final.csv",sep=",")
                       

#Se ingresa el mes y la funcion retorna la cantidad de peliculas que se estrenaron ese mes 
# (nombre del mes, en str, ejemplo 'enero') historicamente return {mes:mes ,cantidad:respuesta}
@app.get("/peliculas_mes/")
def peliculas_mes(mes:str):
  # extraemos los datos unicamente del mes
  df_mes=df_fastapi.loc[df_fastapi["mes"]==mes]
  # arroga el total de peliculas que se extrenaron historicamente dedicho mes
  df_cantidad_mes =df_mes.index.size 
  return {"mese":mes ,"cantidad de pelicula":df_cantidad_mes}


#Se ingresa el dia y la funcion retorna la cantidad de peliculas que se estrenaron ese dia
#  (de la semana, en str, ejemplo 'lunes') historicamente return {'dia':dia,cantidad:respuesta}

@app.get("/peliculas_dia/{dia}")
def peliculas_dia(dia:str):
  df_dias=df_fastapi.loc[df_fastapi["dia"]==dia]
  df_cantidad_dia=df_dias.index.size
  return {"dias":dia ,"cantidad de pelicula":df_cantidad_dia}

#Se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total y promedio''' return
#{'franquicia':franquicia, 'cantidad':respuesta, 'ganancia_total':respuesta, 'ganancia_promedio' :respuesta}

@app.get("/franquicia/{franquicia}")
def franquicia(franquicia:str): 
  df_franquicia=df_fastapi.loc[df_fastapi["franquicia"]==franquicia]
  cantidad_franquicia=df_franquicia.index.size
  ganancia_total=df_franquicia["revenue"].sum()
  ganancia_promedio= ganancia_total-df_franquicia["budget"].sum()
  return {'franquicia es':franquicia, 'cantidad de peliculas ':cantidad_franquicia, 'ganancia_total en $/':ganancia_total, 'ganancia_promedio en $/' :ganancia_promedio}


#'''Ingresas el pais, retornando la cantidad de peliculas producidas en el mismo''' return {'pais':pais, 'cantidad':respuesta}
@app.get("/peliculas_pais/{pais}")
def peliculas_pais(pais:str):
  df_pais=df_fastapi.loc[df_fastapi["production_countries"]==pais]
  cantidad_pais=df_pais.index.size
  return {"pais":pais,"cantidad de pelicula producida":cantidad_pais}
#d'''Ingresas la productora, retornando la ganancia total y la cantidad de peliculas que producen'' return {'productora':productora, 'ganancia_total':respuesta, 'cantidad':respuesta}
@app.get("/productoras/{productoras}")
def productoras(productora:str):
  df_productora=df_fastapi.loc[df_fastapi["production_companies"]==productora]
  ganacia_total_productora=df_productora["revenue"].sum()
  cantidad_pelicula_producida=df_productora.index.nunique()
  return {'productora':productora, 'ganancia_total en $/':ganacia_total_productora, 'cantidad de pelicula producida':cantidad_pelicula_producida}
#'''Ingresas la pelicula, retornando la inversion, la ganancia, el retorno y el año en el que se lanzo'' return {'pelicula':pelicula, 'inversion':respuesta, 'ganacia' :respuesta,'retorno':respuesta, 'año':respuesta}

@app.get('/retorno/{pelicula}')
def retorno(pelicula:str):
  df_peliculas=df_fastapi.loc[df_fastapi["title"]==pelicula]
  inversion_pelicula= df_peliculas["budget"].sum()
  retorno_invercion=df_peliculas['return'].sum()
  ganancia_optenida= ((df_peliculas["revenue"].sum()-inversion_pelicula)+retorno_invercion)
  anio=df_peliculas['release_year'].to_list()
  return {'pelicula':pelicula, 'inversion en $/':inversion_pelicula, 'ganacia en $/' :ganancia_optenida,'retorno en $/':retorno_invercion, 'año':anio}
#SISTEMA DE RECOMENDACION DE PELICULAS
#def recomendacion('titulo'): '''Ingresas un nombre de pelicula y te recomienda las similares en una lista de 5 valores''' return {'lista recomendada': respuesta}

@app.get('/recomendar/{recomendar_peliculas}')
def recomendar_peliculas(titulo:str):
    # Obtener las películas no vistas por el usuario
    peliculas_vistas = df_fastapi[df_fastapi['title'] == titulo]['id']
    peliculas_no_vistas = df_fastapi[~df_fastapi['title'].isin(peliculas_vistas)]['id']
    
    # Crear una lista de tuplas de películas y sus puntajes de similitud
    scores_similitud = []
    for pelicula_id in peliculas_no_vistas:
        similitud =model.predict(titulo, pelicula_id).est
        scores_similitud.append((pelicula_id, similitud))
    
    # Ordenar las películas según su similitud de puntaje
    scores_similitud = sorted(scores_similitud, key=lambda x: x[1], reverse=True)
    
    # Obtener las 5 películas más similares
    peliculas_similares = [df_fastapi[df_fastapi['id'] == i[0]]['title'].values[0] for i in scores_similitud[:5]]
    
    # Devolver las películas recomendadas en una lista
    return {'lista recomendada': peliculas_similares}