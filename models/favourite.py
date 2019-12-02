import peewee as pw
from models.base_model import BaseModel
from models.student import Student
from models.calendar import Club, Activity

class Student_Club(BaseModel):
    student_id = pw.ForeignKeyField(Student, backref='student_clubs')
    club_id = pw.ForeignKeyField(Club, backref='student_clubs')

class Student_Activity(BaseModel):
    student_id = pw.ForeignKeyField(Student, backref='student_activities')
    activity_id = pw.ForeignKeyField(Activity, backref='student_activities')
