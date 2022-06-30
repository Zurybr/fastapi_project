#python
from typing import Optional
from enum import Enum

#pydantic
from pydantic import BaseModel,Field


#enumerable de python
class HairColor(Enum):
    white = "white"
    black = "black"
    brown = "brown"

class Person(BaseModel):
    first_name:str = Field(..., min_length=1, max_length= 40, example = 'Brand')  #se puede o no poner la clase de abajo, pero tambien se puede poner aqu'i
    last_name:str
    hair:str
    age:int = Field(...,ge=1,lt=115)
    hair_color:Optional[HairColor]=Field(default=None)
    is_married:Optional[bool]=Field(default=None)


