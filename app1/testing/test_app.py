import unittest
from flask import url_for
from os import getenv
from unittest.mock import patch
from app import app, db
from app.models import Races, Classes, CreatedModels
from config import Config
from flask_testing import TestCase
from testing.test_setup import TestBase

class TestApp1(TestBase):
    def test_viewallpage(self):
        response = self.client.get(url_for("viewall"))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"View Content", response.data)
    def test_generateDragonBorn(self):
        with patch("requests.get") as g:
            g.return_value.text = "Bard Dragonborn"
            response = self.client.get(url_for("generate"), follow_redirects = True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"View Content", response.data)
    def test_generateDwarf(self):
        with patch("requests.get") as g:
            g.return_value.text = "Bard Dwarf"
            response = self.client.get(url_for("generate"), follow_redirects = True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"View Content", response.data)
    def test_generateElf(self):
        with patch("requests.get") as g:
            g.return_value.text = "Bard Elf"
            response = self.client.get(url_for("generate"), follow_redirects = True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"View Content", response.data)
    def test_generateGnome(self):
        with patch("requests.get") as g:
            g.return_value.text = "Bard Gnome"
            response = self.client.get(url_for("generate"), follow_redirects = True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"View Content", response.data)
    def test_generateHalfElf(self):
        with patch("requests.get") as g:
            g.return_value.text = "Bard Half-Elf"
            response = self.client.get(url_for("generate"), follow_redirects = True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"View Content", response.data)
    def test_generateHalfling(self):
        with patch("requests.get") as g:
            g.return_value.text = "Bard Halfling"
            response = self.client.get(url_for("generate"), follow_redirects = True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"View Content", response.data)
    def test_generateHalfOrc(self):
        with patch("requests.get") as g:
            g.return_value.text = "Bard Half-Orc"
            response = self.client.get(url_for("generate"), follow_redirects = True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"View Content", response.data)
    def test_generateHuman(self):
        with patch("requests.get") as g:
            g.return_value.text = "Bard Human"
            response = self.client.get(url_for("generate"), follow_redirects = True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"View Content", response.data)
    def test_generateTiefling(self):
        with patch("requests.get") as g:
            g.return_value.text = "Bard Tiefling"
            response = self.client.get(url_for("generate"), follow_redirects = True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"View Content", response.data)
    def test_viewspecificpage(self):
        response = self.client.get(url_for("viewspecific", model_id = 1))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"View Individual Content", response.data)

    # def test_viewspecificpageerror(self):
    #     response = self.client.get(url_for("viewspecific"), follow_redirects = True)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertIn(b"File Not Found", response.data)