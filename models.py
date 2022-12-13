from datetime import date
from enum import Enum
from uuid import UUID, uuid4
from  pydantic import BaseModel
from typing import Optional,List
from uuid import UUID,uuid4
class Gender(str,Enum):
    male = "male"
    female = "female"
    student = 'student'
class Role(str,Enum):
    admin ='admin'
    user = "user"
    student = 'student'



class Blog(BaseModel):
    id:Optional[UUID]= uuid4()
    title:str
    description:str 
    link:str
    published: Optional[bool]
    created_At : Optional[date]
    updated_At : Optional[date]

class update_Blog_Request(BaseModel):
    id:Optional[UUID]= uuid4()
    title:Optional[str]
    description:Optional[str]
    link:Optional[str]
    published: Optional[bool]
    created_At : Optional[date]
    updated_At : Optional[date]
    