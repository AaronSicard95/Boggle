from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle
from status.models import Status


class FlaskTests(TestCase):

    app.config['TESTING']
    def setUp(self):
        global client
        global testBoard
        client = app.test_client()
        testBoard = [['b','a','t']['o','u','r']['t','a','r']]
    def test_checkword():
        global testBoard
        global client
        
        assert True == True

