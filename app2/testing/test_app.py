import unittest
import unittest
from flask import url_for
from os import getenv
import os
from app import app
from flask_testing import TestCase

"""
Reminder to use "pytest --cov application --cov-report term-missing"
"""

class TestBase(TestCase):

    def create_app(self):

        app.config.update(SECRET_KEY="test key",
        WTF_CSRF_ENABLED=False,
        DEBUG=True
        )
        return app

class TestService2(TestBase):

    def test_getclass(self):
        response = self.client.get(url_for("get_class"))
        self.assertEqual(response.status_code, 200)
