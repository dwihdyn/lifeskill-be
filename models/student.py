import peewee as pw
from models.base_model import BaseModel

from playhouse.hybrid import hybrid_property


class Student(BaseModel):
    id_number = pw.IntegerField(unique=True)
    full_name = pw.CharField()
    password = pw.CharField()
    creativity_score = pw.IntegerField()
    leadership_score = pw.IntegerField()
    respect_score = pw.IntegerField()
    
    @hybrid_property
    def accumulated_score(self):
        return self.creativity_score + self.leadership_score + self.respect_score


    
