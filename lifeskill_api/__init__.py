from lifeskill_api.blueprints.students.views import students_api_blueprint
from app import app
from flask_cors import CORS

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


app.register_blueprint(students_api_blueprint, url_prefix='/api/v1/students')
