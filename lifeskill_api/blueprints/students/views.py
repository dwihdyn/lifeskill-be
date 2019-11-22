from flask import Blueprint, jsonify
from models.student import Student

students_api_blueprint = Blueprint('students_api', __name__, template_folder='templates')


@students_api_blueprint.route('/show', methods=['GET'])
def show():
    resp = {
    'message': 'hi im heree',
    'user': {
        'id': 'user id',
        'username': 'user name',
        'email': 'user email'
        },
    'ok': 'ya'
    }

    return jsonify(resp)

@students_api_blueprint.route('/update', methods=['POST'])
def update():
    breakpoint()
