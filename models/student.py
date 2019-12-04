from playhouse.hybrid import hybrid_property
import peewee as pw
from models.base_model import BaseModel


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

    
    def dropout_score(self, records):
        
        min_crea = min([record.creativity_score for record in records])
        max_crea = max([record.creativity_score for record in records])

        min_lead = min([record.leadership_score for record in records])
        max_lead = max([record.leadership_score for record in records])

        min_resp = min([record.respect_score for record in records])
        max_resp = max([record.respect_score for record in records])


        true_crea = (self.creativity_score - min_crea) / (max_crea - min_crea) * 34
        true_lead = (self.leadership_score - min_lead) / (max_lead - min_lead) * 33
        true_resp = (self.respect_score - min_resp) / (max_resp - min_resp) * 33

        return round(100 - (true_crea + true_lead + true_resp),2)