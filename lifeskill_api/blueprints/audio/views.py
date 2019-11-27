import os
from flask import Blueprint, Flask, flash, request, redirect, url_for, session
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
import logging


audio_api_blueprint = Blueprint(
    'audio_api', __name__, template_folder='templates')


ALLOWED_EXTENSIONS = set(['wav'])


@audio_api_blueprint.route('/upload', methods=['POST'])
def takeAudio():
    audio = request.files['file']
    return audio
