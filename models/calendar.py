import peewee as pw
from models.base_model import BaseModel


class Club(BaseModel):
    name = pw.CharField()
    description = pw.CharField()
    image = pw.CharField()
    qualify_pts = pw.IntegerField()
    favourited = pw.BooleanField(default=False)


class Activity(BaseModel):
    name = pw.CharField()
    description = pw.CharField()
    image = pw.CharField()
    qualify_pts = pw.IntegerField()
    favourited = pw.BooleanField(default=False)
    event_date = pw.DateField()


