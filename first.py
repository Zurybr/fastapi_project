#python
from re import S
from typing import Optional
from enum import Enum

#pydantic
from pydantic import BaseModel,Field #Field nos sirve para validar un modelo

from pydantic import NameEmail,EmailStr #checar los mas importantes para validarlos
#fastapi
from fastapi import FastAPI,Body,Query,Path

app = FastAPI()

#Models
class HairColor(Enum):
    white = "white"
    black = "black"



class Person(BaseModel):
    first_name:str = Field(..., min_length=1, max_length= 40, example = 'Brand')  #se puede o no poner la clase de abajo, pero tambien se puede poner aqu'i
    last_name:str
    hair:str
    age:int = Field(...,ge=1,lt=115)
    hair_color:Optional[HairColor]=Field(default=None) #en base de datos es Null
    #is_married:Optional[bool]=None #en base de datos es Null y puede comprobarse con Field o solo
    is_married:Optional[bool]=Field(default=None)
        #clase para probar la documentacion, va dentro del modelo
    # class Config:
    #     schema_extra = {
    #         "example": {
    #             "first_name": "Rodrigo",
    #             "last_name": "Lopez",
    #             "age": 30,
    #             "hair_color": "black",
    #             "is_married": False
    #         }
    #     }
class Location(BaseModel):
    latitude:int = Field(ge=1,lt=115,example = 10)
    longitude:int = Field(example = 10)

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
    idperson:int=Path(...,gt=0, example= 1)
):
    return {idperson:'It exist'}

#validar body parameters
@app.put("/person/{idPerson}")
def update_person(
    idPerson:int = Path(...,description="id de la persona a actualizar",gt = 0),
    person:Person = Body(...),
    location:Location = Body(...)
):
    # resultado = person.dict() & location.dict() #no se puede aun 
    resultado = person.dict()
    resultado.update(location.dict())
    return resultado