import peewee as pw
from models.base_model import BaseModel


class Teacher(BaseModel):
    id_number = pw.IntegerField(unique=True)
    full_name = pw.CharField()
    password = pw.CharField()
    
