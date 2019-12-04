from lifeskill_api.blueprints.students.views import students_api_blueprint
from lifeskill_api.blueprints.calendar.views import calendar_api_blueprint
from app import app
from flask_cors import CORS
from flask_jwt_extended import JWTManager

cors = CORS(app, resources={r"*": {"origins": "*"}})


app.register_blueprint(students_api_blueprint, url_prefix='/api/v1/students')
app.register_blueprint(calendar_api_blueprint, url_prefix='/api/v1/calendar')

jwt = JWTManager(app)
