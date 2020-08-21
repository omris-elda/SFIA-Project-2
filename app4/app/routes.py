import random
from app import app, db
from flask import request, jsonify
import requests
from app.models import Classes, Races
# @app.route("/api/getclass", methods=["GET"])
# def get_class():
#     randomno = random.randint(1, 12)
#     # animal = animals[randomno]
#     return str(randomno)

# @app.route("/api/getrace", methods=["GET"])
# def get_race():
#     randomno = random.randint(1, 9)
#     return str(randomno)

# @app.route("/api/animal/noise", methods=["GET", "POST"])
# def get_noise():
#     x = 0
#     response = request.data.decode("utf-8")
#     for i in animals:
#         if i == response:
#             noise = sounds[x]
#             break
#         else:
#             x += 1
#     return noise
@app.route("/api/getmodel", methods=["GET"])
def get_model():
	response = requests.get("http://service2:5001/api/getclass")
	response = response.text

	response2 = requests.get("http://service3:5002/api/getrace")
	# response2 = requests.post("http://localhost:5003/api/animal/noise", data = response)
	response2 = response2.text

	response = int(response)
	response2 = int(response2)

	classes = Classes.query.filter_by(class_id = response).first()
	races = Races.query.filter_by(races_id = response2).first()
	classname = classes.class_name
	racename = races.race_name

	return str(classname + " " + racename)