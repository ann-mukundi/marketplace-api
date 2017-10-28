from flask import jsonify
from . import api

@api.route('/users/<int:id>')
def get_user(id):

