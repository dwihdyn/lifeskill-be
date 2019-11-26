from flask import Blueprint, jsonify, request
from models.student import Student

students_api_blueprint = Blueprint('students_api', __name__, template_folder='templates')


@students_api_blueprint.route('/test', methods=['GET'])
def test():
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



@students_api_blueprint.route('/signup', methods=['POST'])
def signup():
    id_number=request.json['id_number']
    full_name=request.json['full_name'] 
    password=request.json['password']
    accumulated_score='100'

    new_user = Student(id_number=id_number,full_name=full_name ,password=password, accumulated_score=accumulated_score)
    
    
    if Student.get_or_none(id_number=id_number):
        return jsonify(False) 

    new_user.save()
    return jsonify(True)






@students_api_blueprint.route('/login', methods=['POST'])
def login():
    id_number=request.json['id_number']
    password=request.json['password']

    # retrieve all student info
    user_check = Student.get_or_none(id_number=id_number)
    if not user_check:
        return jsonify(False)
    
    if not password == user_check.password:
        return jsonify(False)

    return jsonify(True)


