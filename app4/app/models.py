from app import db


class CreatedModels(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    class_id = db.Column(db.Integer, db.ForeignKey("classes.class_id"))
    races_id = db.Column(db.Integer, db.ForeignKey("races.races_id"))
    strength = db.Column(db.Integer)
    constitution = db.Column(db.Integer)
    dexterity = db.Column(db.Integer)
    intelligence = db.Column(db.Integer)
    wisdom = db.Column(db.Integer)
    charisma = db.Column(db.Integer)
"""
This is the created class model, which will hold all of the previously made 
models for future reference/quick access
"""

class Classes(db.Model):
    class_id = db.Column(db.Integer, primary_key = True)
    class_name = db.Column(db.String(100), unique = True)
    class_description = db.Column(db.String(1000), unique = True)
    hit_die = db.Column(db.String(3))
    primary_ability = db.Column(db.String(50))
    saves = db.Column(db.String(50))
    class_fk = db.relationship("CreatedModels", backref = "class", lazy = "dynamic")
"""
This is the classes model, which will store all of the classes
"""

class Races(db.Model):
    races_id = db.Column(db.Integer, primary_key = True)
    race_name = db.Column(db.String(100), unique = True)
    race_description = db.Column(db.String(500), unique = True)
    racial_trait_1 = db.Column(db.String(100))
    racial_trait_2 = db.Column(db.String(100))
    racial_trait_3 = db.Column(db.String(100))
    racial_trait_4 = db.Column(db.String(100))
    race_fk = db.relationship("CreatedModels", backref = "races", lazy = "dynamic")
"""
This is the races model, which will store all of the races
"""
