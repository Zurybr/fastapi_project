# python
from typing import Optional
from enum import Enum

# pydantic
from pydantic import BaseModel, Field

# checar los mas importantes para validarlos
from pydantic import NameEmail, EmailStr
# fastapi
from fastapi import FastAPI, Body, Query, Path

# # importar los Models
# from models import Person

class HairColor(Enum):
    white = "white"
    black = "black"
    brown = "brown"

class PersonBase(BaseModel):
    first_name:str = Field(..., min_length=1, max_length= 40, example = 'Brand')  #se puede o no poner la clase de abajo, pero tambien se puede poner aqu'i
    last_name:str
    hair:str
    age:int = Field(...,ge=1,lt=115)
    hair_color:Optional[HairColor]=Field(default=None)
    is_married:Optional[bool]=Field(default=None)

class Person(PersonBase):
    password:str = Field(...,min_length=8)



# inicializar el objeto FastAPI en variable app para usar los path operators
app = FastAPI()
@app.get("/")
def home():
    return {1: 1}


@app.post("/person",response_model=PersonBase)
def create_person(person: Person = Body(...)):
    return person
