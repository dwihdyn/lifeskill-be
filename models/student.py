import peewee as pw
from models.base_model import BaseModel

class Student(BaseModel):
    name = pw.CharField()
    score = pw.IntegerField()
