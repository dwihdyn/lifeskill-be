import peewee as pw
from models.base_model import BaseModel


class Club(BaseModel):
    name = pw.CharField()
    description = pw.CharField()
    image = pw.CharField()
    qualify_pts = pw.IntegerField()


class Activity(BaseModel):
    name = pw.CharField()
    description = pw.CharField()
    image = pw.CharField()
    qualify_pts = pw.IntegerField()
    event_date = pw.DateField(null=True)