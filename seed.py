# allow developer to run 'python seed.py', same idea as 'python migrate.py'
import os

os.environ['MIGRATION'] = '1'

if not os.getenv('FLASK_ENV') == 'production':
    print("Loading environment variables from .env")
    from dotenv import load_dotenv
    load_dotenv()

import peeweedbevolve
from models import *    # all import (*) being handled by __init__.py inside the 'models' folder  
from models.base_model import db

# =================================================================


from models.student import Student
from models.teacher import Teacher
from models.calendar import *
import random
import names

# seed teacher
Teacher(id_number=0, full_name="admin", password="111").save()
Student(id_number=11, full_name="fav student", password="111", accumulated_score=random.randint(1000,5000)).save()

# # Club
# clubs_name = ['Badminton Club', 'Volleyball Club', 'Tennis Club']
# clubs_desc = ['desc 1', 'desc 2', 'desc 3']


for i in random.sample(range(1,5),3):
    Teacher(id_number=i, full_name=names.get_full_name(), password=names.get_first_name()).save()
    Student(id_number=i, full_name=names.get_full_name(), password=names.get_first_name(), accumulated_score=random.randint(1000,5000)).save()
    Club(name=names.get_first_name(), description=names.get_full_name(), image=names.get_last_name(), qualify_pts=random.randint(3000,10000)).save()
