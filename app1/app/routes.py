from app import app, db
import requests
from flask import render_template, url_for, flash, redirect, request, jsonify
from app.models import Classes, Races, CreatedModels
from app.classes import PlayerCharacter
import json

@app.route("/")
@app.route("/generate")
def generate():
	# response = requests.get("http://localhost:5001/api/getclass")
	# response = response.text

	# response2 = requests.get("http://localhost:5002/api/getrace")
	# # response2 = requests.post("http://localhost:5003/api/animal/noise", data = response)
	# response2 = response2.text

	# response = int(response)
	# response2 = int(response2)

	# classes = Classes.query.filter_by(class_id = response).first()
	# races = Races.query.filter_by(races_id = response2).first()
	response = requests.get("http://service4:5003/api/getmodel")
	#response = json.loads(modeldata)
	response = response.text
	response = response.split()

	classes = Classes.query.filter_by(class_name = response[0]).first()
	races = Races.query.filter_by(race_name = response[1]).first()

	newmodel = PlayerCharacter()
	if races.race_name == "Dragonborn":
		newmodel.addstrength(2)
		newmodel.addcharisma(1)
	elif races.race_name == "Dwarf":
		newmodel.addconstitution(2)
	elif races.race_name == "Elf":
		newmodel.adddexterity(2)
	elif races.race_name == "Gnome":
		newmodel.addintelligence(2)
	elif races.race_name == "Half-Elf":
		newmodel.addcharisma(2)
		newmodel.addintelligence(1)
		newmodel.addwisdom(1)
	elif races.race_name == "Halfling":
		newmodel.adddexterity(2)
	elif races.race_name == "Half-Orc":
		newmodel.addstrength(2)
		newmodel.addconstitution(1)
	elif races.race_name == "Human":
		newmodel.addstrength(1)
		newmodel.addconstitution(1)
		newmodel.adddexterity(1)
		newmodel.addcharisma(1)
		newmodel.addintelligence(1)
		newmodel.addwisdom(1)
	elif races.race_name == "Tiefling":
		newmodel.addcharisma(2)
		newmodel.addintelligence(1)
	
	model = newmodel
	if model:
		newmodel = CreatedModels(
			class_id = classes.class_id,
			races_id = races.races_id,
			strength = model.viewstrength(),
			constitution = model.viewconstitution(),
			dexterity = model.viewdexterity(),
			intelligence = model.viewintelligence(),
			wisdom = model.viewwisdom(),
			charisma = model.viewcharisma()
		)
		db.session.add(newmodel)
		db.session.commit()
		flash("New model added!")
		return redirect(url_for("viewall"))
	else:
		return "Something went wrong."

@app.route("/view/all")
def viewall():
	model = CreatedModels.query.all()
	if model is not None:
		return render_template("view/viewall.html", title = "View All", model = model)
	else:
		return "There are no pre-made models yet, why don't you click on 'generate' and make your own?"

@app.route("/view/<model_id>")
def viewspecific(model_id):
	data = CreatedModels.query.filter_by(id = model_id)
	if data is not None:
		return render_template("/view/viewspecific.html", model = data)
	else:
		render_template("errors/404.html")