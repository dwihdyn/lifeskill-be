from lifeskill_api.blueprints.students.views import students_api_blueprint
from lifeskill_api.blueprints.audio.views import audio_api_blueprint
from app import app
from flask_cors import CORS
from flask_jwt_extended import JWTManager

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


app.register_blueprint(students_api_blueprint, url_prefix='/api/v1/students')
app.register_blueprint(calendar_api_blueprint, url_prefix='/api/v1/calendar')
app.register_blueprint(audio_api_blueprint, url_prefix='/api/v1/audio')
jwt = JWTManager(app)
