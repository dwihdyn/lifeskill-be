# for managing clubs & activities

from flask import Blueprint, jsonify, request
from models.calendar import Club, Activity
from models.favourite import Student_Activity, Student_Club
import peewee as pw

calendar_api_blueprint = Blueprint(
    'calendar_api', __name__, template_folder='templates')


# display all clubs
@calendar_api_blueprint.route('/clubs', methods=['GET'])
def show_clubs():
    # get a club
    # construct a dict that represents a club
    # return all the dicts to a list
    # convert the list into a JSON
    fav_club = Student_Club.select().where(Student_Club.student_id == 1)
    favs = []
    for fav in fav_club:
        favs.append(fav.club_id.id)
    clubs = []
    for club in Club.select():
        clubs.append({
            "id": club.id,
            "fav": True if club.id in favs else False,
            "name": club.name,
            "description": club.description,
            "image": club.image,
            "points": club.qualify_pts,
        })

    return jsonify(clubs)


# add a club to favourites
@calendar_api_blueprint.route('/clubs/favourite', methods=['POST'])
def fave_club():
    student_id = int(request.json['student_id'])
    club_id = request.json['category_id']

    query = Student_Club.select().where(Student_Club.student_id ==
                                        student_id, Student_Club.club_id == club_id)
    if query.exists():
        query[0].delete_instance()
    else:
        Student_Club.create(student_id=student_id, club_id=club_id)

    return jsonify(True)


# display all activities
@calendar_api_blueprint.route('/activities', methods=['GET'])
def show_activities():
    fav_activity = Student_Activity.select().where(Student_Activity.student_id == 2)
    favs = []
    for fav in fav_activity:
        favs.append(fav.activity_id.id)
    activities = []
    for activity in Activity.select():
        activities.append({
            "id": activity.id,
            "fav": True if activity.id in favs else False,
            "name": activity.name,
            "description": activity.description,
            "image": activity.image,
            "points": activity.qualify_pts,
        })

    return jsonify(activities)


# add an activity to favourites
@calendar_api_blueprint.route('/activities/favourite', methods=['POST'])
def fave_activity():
    student_id = request.json['student_id']
    activity_id = request.json['category_id']

    query = Student_Activity.select().where(Student_Activity.student_id ==
                                            student_id, Student_Activity.activity_id == activity_id)
    if query.exists():
        query[0].delete_instance()
    else:
        Student_Activity.create(student_id=student_id, activity_id=activity_id)

    return jsonify(True)
