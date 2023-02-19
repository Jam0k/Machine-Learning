from flask import Flask
from flask_login import UserMixin


app = Flask(__name__) 
class User(UserMixin):
    def __init__(self, id):
        self.id = id
