from app import db, app
from app.models import Classes, Races, CreatedModels
from app.classes import PlayerCharacter

newchar = PlayerCharacter()
print(newchar.viewstrength())
newchar.addstrength(5)
print(newchar.viewstrength())

classdata = Classes.query.all()
print(classdata)


if __name__ == "__main__":
    app.run()