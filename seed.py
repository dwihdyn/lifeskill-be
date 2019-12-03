# DELETE LAST PART!!! student_activity & student_club part
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
from models.favourite import *
import random
import names


# restart database
Student_Activity.delete().execute()
Student_Club.delete().execute()
Student.delete().execute()
Teacher.delete().execute()
Club.delete().execute()
Activity.delete().execute()





# seeding
Teacher(id_number=0, full_name="Professor Albus Dumbledore", password="111").save()
Student(id_number=11, full_name="Hermione Granger", password="111", 
creativity_score=67, leadership_score=88,
respect_score=76).save()



# Activity
Activity(
    name="Student Exchange Program", 
    description=" Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.", 
    image="https://jw-nextagram.s3-ap-southeast-1.amazonaws.com/191202-112930-student_exchange_act.png",
    qualify_pts=random.randint(100,1000),
    event_date="2019-07-24").save()

Activity(
    name="Annual Talent Competition", 
    description=" Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.", 
    image="https://jw-nextagram.s3-ap-southeast-1.amazonaws.com/191202-112944-talent_comp_act.png",
    qualify_pts=random.randint(100,1000),
    event_date="2019-07-25").save()

Activity(
    name="Entrepreneurs Day", 
    description=" Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.", 
    image="https://jw-nextagram.s3-ap-southeast-1.amazonaws.com/191202-112849-ent_day_act.png",
    qualify_pts=random.randint(100,1000),
    event_date="2019-07-26").save()

Activity(
    name="Science Fair 2019", 
    description=" Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.", 
    image="https://jw-nextagram.s3-ap-southeast-1.amazonaws.com/191202-112915-science_fair_act.png",
    qualify_pts=random.randint(100,1000),
    event_date="2019-07-27").save()

Activity(
    name="Color Run", 
    description=" Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.", 
    image="https://jw-nextagram.s3-ap-southeast-1.amazonaws.com/191202-112833-color_run_act.png",
    qualify_pts=random.randint(100,1000),
    event_date="2019-07-28").save()






# Clubs
Club(
    name="Debate Club",
    description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    image="https://jw-nextagram.s3-ap-southeast-1.amazonaws.com/191202-112744-debate_club.png",
    qualify_pts=random.randint(100,1000)
).save()

Club(
    name="Film Society",
    description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    image="https://jw-nextagram.s3-ap-southeast-1.amazonaws.com/191202-112800-film_club.png",
    qualify_pts=random.randint(100,1000)
).save()

Club(
    name="Basketball Club",
    description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    image="https://jw-nextagram.s3-ap-southeast-1.amazonaws.com/191202-112702-basketball_club.png",
    qualify_pts=random.randint(100,1000)
).save()

Club(
    name="Cooking Club",
    description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    image="https://jw-nextagram.s3-ap-southeast-1.amazonaws.com/191202-112730-cooking_club.png",
    qualify_pts=random.randint(100,1000)
).save()

Club(
    name="Mathematics Club",
    description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    image="https://jw-nextagram.s3-ap-southeast-1.amazonaws.com/191202-112816-math_club.png",
    qualify_pts=random.randint(100,1000)
).save()





for i in random.sample(range(20,100),15):
    # Teacher
    tch_name = names.get_full_name()
    first, last = tch_name.split()
    Teacher(id_number=i, full_name=tch_name, password=last).save()

    # Student
    std_name = names.get_full_name()
    first, last = std_name.split()
    Student(id_number=i, full_name=std_name, password=last, 
    creativity_score=random.randint(20,100), leadership_score=random.randint(20,100),
    respect_score=random.randint(20,100)).save()
    


# DELETE ME LATER
Student_Club(student_id=1, club_id=2).save()
Student_Club(student_id=1, club_id=4).save()
Student_Activity(student_id=1, activity_id=3).save()
# =======