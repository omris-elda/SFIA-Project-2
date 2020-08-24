import unittest
from flask import url_for
from os import getenv
import os
from app import app
from flask_testing import TestCase
from app.models import Races, Classes, CreatedModels
from unittest.mock import patch

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

    def test_getmodel(self):
        with patch("requests.get") as g:
            with patch("requests.get") as f:
                g.return_value.text = "1"
                f.return_value.text = "1"
                response = self.client.get(url_for("get_model"))
                self.assertEqual(response.status_code, 200)
