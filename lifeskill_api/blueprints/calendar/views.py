# for managing clubs & activities 

from flask import Blueprint, jsonify
from models.calendar import Club, Activity
import peewee as pw

calendar_api_blueprint = Blueprint('calendar_api', __name__, template_folder='templates')


# display all clubs
@calendar_api_blueprint.route('/club', methods=['GET'])
def show_clubs():
# get a club
# construct a dict that represents a club
# return all the dicts to a list
# convert the list into a JSON

    clubs = [{
        "name": club.name,
        "description": club.description,
        "image": club.image,
        "points": club.points_to_qualify,
        "isFavourite": club.favourited,
    } for club in Club.select()]

    return jsonify(clubs)


# add a club to favourites
@calendar_api_blueprint.route('/club/favourite', methods=['POST'])
def fave_club():
    club = Club.select()
    club.favourited = True
    club.save()


# display all activities
@calendar_api_blueprint.route('/activity', methods=['GET'])
def show_activities():

    activities = [{
        "name": activity.name,
        "description": activity.description,
        "image": activity.image,
        "points": activity.points_to_qualify,
        "isFavourite": activity.favourited,
    } for activity in Activity.select()]

    return jsonify(activities)


# add an activity to favourites
@calendar_api_blueprint.route('/activity/favourite', methods=['POST'])
def fave_activity():
    activity = Activity.select()
    activity.favourited = True
    activity.save()


