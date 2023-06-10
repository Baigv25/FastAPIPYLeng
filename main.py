from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Pelicula(BaseModel):
    titulo: str
    genero: str
    director: str

peliculas_db = []

@app.get("/")
def index():
    return {"message": "Bienvenido a la API de Películas"}

@app.get("/peliculas")
def obtener_peliculas():
    return peliculas_db

@app.get("/peliculas/{id}")
def obtener_pelicula(id: int):
    for pelicula in peliculas_db:
        if pelicula["id"] == id:
            return pelicula
    return {"message": "Pelicula no encontrada"}

@app.post("/peliculas")
def agregar_pelicula(pelicula: Pelicula):
    pelicula_dict = pelicula.dict()
    pelicula_dict["id"] = len(peliculas_db) + 1
    peliculas_db.append(pelicula_dict)
    return {"message": "Pelicula agregada exitosamente"}

@app.put("/peliculas/{id}")
def actualizar_pelicula(id: int, pelicula: Pelicula):
    for p in peliculas_db:
        if p["id"] == id:
            p["titulo"] = pelicula.titulo
            p["genero"] = pelicula.genero
            p["director"] = pelicula.director
            return {"message": "Pelicula actualizada exitosamente"}
    return {"message": "Pelicula no encontrada"}

@app.delete("/peliculas/{id}")
def eliminar_pelicula(id: int):
    for pelicula in peliculas_db:
        if pelicula["id"] == id:
            peliculas_db.remove(pelicula)
            return {"message": "Pelicula eliminada exitosamente"}
    return {"message": "Pelicula no encontrada"}