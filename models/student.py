import peewee as pw
from models.base_model import BaseModel


class Student(BaseModel):
    fullname = pw.CharField(null=False)
    creativity = pw.IntegerField(null=True)
    leadership = pw.IntegerField(null=True)
    respect = pw.IntegerField(null=True)
    accumulative = pw.IntegerField(null=True)
