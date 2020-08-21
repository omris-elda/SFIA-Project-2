import random
from app import app
from flask import request

@app.route("/api/getclass", methods=["GET"])
def get_class():
    randomno = random.randint(1, 12)
    # animal = animals[randomno]
    return str(randomno)

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
