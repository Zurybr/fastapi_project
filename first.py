#python
from typing import Optional

#pydantic
from pydantic import BaseModel

#fastapi
from fastapi import FastAPI,Body,Query,Path

app = FastAPI()

#Models
class Person(BaseModel):
    first_name:str
    last_name:str
    hair:str
    age:str
    hair_color:Optional[str]=None #en base de datos es Null
    is_married:Optional[bool]=None #en base de datos es Null

@app.get("/")
def home():
    return {1:1}

@app.post("/person")
def create_person(person:Person = Body(...)):
    return person

#Validaciones Query Parameters
@app.get("/person/details")
def show_person(
    name:Optional[str]=Query(default=None,min_length=1,max_length=50
    ,title = "Person Name"
    ,description='this is the name of person'
    ), #None = NUll
    age:int=Query(...
    ,title = "Person age"
    ,description='this is the age of person') #tres puntos es igual a obligatorio
):
    return {name:age}

#validar path parameters
@app.get("/person/datails/{idperson}")
def show_person(
    idperson:int=Path(...,gt=0)
):
    return {idperson:'It exist'}