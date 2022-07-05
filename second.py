# python
from typing import Optional
from enum import Enum

# pydantic
from pydantic import BaseModel, Field

# checar los mas importantes para validarlos
from pydantic import NameEmail, EmailStr
# fastapi
from fastapi import Cookie, FastAPI, Body, Form, Header, Query, Path,UploadFile,File,status

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

class Login(BaseModel):
    username:str = Form(...)

# inicializar el objeto FastAPI en variable app para usar los path operators
app = FastAPI()
@app.get(path="/",status_code=status.HTTP_200_OK)
def home():
    return {1: 1}


@app.post(path="/person",response_model=PersonBase,status_code=status.HTTP_201_CREATED)
def create_person(person: Person = Body(...)):
    return person

@app.post(
    path="/login",
    status_code=status.HTTP_200_OK,
    response_model=Login
)
def login (username:str =Form(...),password:str =Form(...)):
    return Login(username=username)

#cookies y headers

@app.post(
    path='/contact',
    status_code=status.HTTP_200_OK    
)
def contact(
    first_name:str = Form(...,max_length=20,min_length=1),
    last_name:str = Form(...,max_length=20,min_length=1),
    email:EmailStr = Form(...),
    message:str =Form(...,min_length=1),
    user_agent:Optional[str] = Header(default=None),
    ads:Optional[str]=Cookie(default=None)


):
    return user_agent


#files

@app.post(
    path = '/post-image'
)
def post_image(
    image:UploadFile = File(...)
):
    return{
        'Filename': image.filename,
        "Format":image.content_type,
        "Size (kb)": round(len(image.file.read())/1024,ndigits=2)
    }