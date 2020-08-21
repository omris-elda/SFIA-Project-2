from app import db
from app.models import Races, Classes, CreatedModels

db.drop_all()
db.create_all()

"""
We also want to populate the database with a default set of values, 
so that should the database ever be accidentally removed we will still have the default
classes and races in the database.
"""
"""
Populating the classes table
"""
barbarian = Classes(
    class_name = "Barbarian",
    class_description = "A fierce warrior of primitive background who can enter a battle rage.",
    hit_die = "d12",
    primary_ability = "Strength",
    saves = "Strength & Constitution"
)
bard = Classes(
    class_name = "Bard",
    class_description = "An inspiring magician whos power echos the music of creation.",
    hit_die = "d8",
    primary_ability = "Charisma",
    saves = "Dexterity & Charisma"
)
cleric = Classes(
    class_name = "Cleric",
    class_description = "A priestly champion who wields divine magic in service of a higher power.",
    hit_die = "d8",
    primary_ability = "Wisdom",
    saves = "Wisdom & Charisma"
)
druid = Classes(
    class_name = "Druid",
    class_description = "A priest of the Old Faith, wielding the powers of nature and adopting animal forms.",
    hit_die = "d8",
    primary_ability = "Wisdom",
    saves = "Intelligence & Wisdom"
)
fighter = Classes(
    class_name = "Fighter",
    class_description = "A master of martial combat, skilled with a variety of weapons and armour.",
    hit_die = "d10",
    primary_ability = "Strength or Dexterity",
    saves = "Strength & Constitution"
)
monk = Classes(
    class_name = "Monk",
    class_description = "A master of martial arts, harnessing the power of the body in pursuit of physical and spiritual perfection.",
    hit_die = "d8",
    primary_ability = "Dexterity & Wisdom",
    saves = "Strength & Dexterity"
)
paladin = Classes(
    class_name = "Paladin",
    class_description = "A holy warrior bound to a sacred oath.",
    hit_die = "d10",
    primary_ability = "Strength & Charisma",
    saves = "Wisdom & Charisma"
)
ranger = Classes(
    class_name = "Ranger",
    class_description = "A warrior who combats threats on the edges of civilisation.",
    hit_die = "d10",
    primary_ability = "Dexterity & Wisdom",
    saves = "Strength & Dexterity"
)
rogue = Classes(
    class_name = "Rogue",
    class_description = "A scoundrel who uses stealth and trickery to overcome obstacles and enemies.",
    hit_die = "d8",
    primary_ability = "Dexterity",
    saves = "Dexterity & Intelligence"
)
sorcerer = Classes(
    class_name = "Sorcerer",
    class_description = "A spellcaster who draws on inherent magic from a gift or bloodline.",
    hit_die = "d6",
    primary_ability = "Charisma",
    saves = "Charisma & Constitution"
)
warlock = Classes(
    class_name = "Warlock",
    class_description = "A wielder of magic that is derived from a bargain with an extraplanar entity.",
    hit_die = "d8",
    primary_ability = "Charisma",
    saves = "Wisdom & Charisma"
)
wizard = Classes(
    class_name = "Wizard",
    class_description = "A scholarly magic-user capable of manipulating the structures of reality.",
    hit_die = "d6",
    primary_ability = "Intelligence",
    saves = "Intelligence & Wisdom"
)
"""
Populating the races table
"""
dragonborn = Races(
    race_name = "Dragonborn",
    race_description = "Dragonborn look very much like dragons standing erect in humanoid form, though they lack wings or a tail.",
    racial_trait_1 = "Draconic Ancestry",
    racial_trait_2 = "Breath Weapon",
    racial_trait_3 = "Damage Resistance"
)
dwarf = Races(
    race_name = "Dwarf",
    race_description = "Bold and hardy, dwarves are known as skilled warriors, miners, and workers of stone and metal.",
    racial_trait_1 = "Darkvision",
    racial_trait_2 = "Dwarven Resilience",
    racial_trait_3 = "Dwarven Combat Training",
    racial_trait_4 = "Stonecunning"
)
elf = Races(
    race_name = "Elf",
    race_description = "Eleves are a magical people of otherworldly grace, living in the world but not entirely part of it.",
    racial_trait_1 = "Darkvision",
    racial_trait_2 = "Keen Senses",
    racial_trait_3 = "Fey Ancestry",
    racial_trait_4 = "Trance"
)
gnome = Races(
    race_name = "Gnome",
    race_description = "A gnome's energy and enthusiasm for living shines through every inch of their body.",
    racial_trait_1 = "Darkvision",
    racial_trait_2 = "Gnome Cunning"
)
halfelf = Races(
    race_name = "Half-Elf",
    race_description = "Half-elves combine what some say are the best qualities of their elf and human parents.",
    racial_trait_1 = "Darkvision",
    racial_trait_2 = "Fey Ancestry",
    racial_trait_3 = "Skill Versatility"
)
halfling = Races(
    race_name = "Halfling",
    race_description = "The diminutive halflings survive in a world full of larger creatures by avoiding notice or, barring that, avoiding offence.",
    racial_trait_1 = "Lucky",
    racial_trait_2 = "Brave",
    racial_trait_3 = "Halfling Nimbleness"
)
halforc = Races(
    race_name = "Half-Orc",
    race_description = "Half-orcs' greyish pigmentation, sloping foreheads, jutting jaws, prominent teeth, and towering builds make their orcish heritage plain for all to see.",
    racial_trait_1 = "Darkvision",
    racial_trait_2 = "Menacing",
    racial_trait_3 = "Relentless Endurance",
    racial_trait_4 = "Savage Attacks"
)
human = Races(
    race_name = "Human",
    race_description = "Humans are the most adaptable and ambitious people among the common races. Whatever drives them, humans are the innovators, the achievers, and the pioneers of the worlds.",
    racial_trait_1 = "Extra Language"
)
tiefling = Races(
    race_name = "Tiefling",
    race_description = "To be greeted with stares and whispers, to suffer violence and insult on the street, to see mistrust and fear in every eye: this is the lot of the tiefling.",
    racial_trait_1 = "Darkvision",
    racial_trait_2 = "Hellish Resistance",
    racial_trait_3 = "Infernal Legacy"
)

"""
Add a test created model
"""
example = CreatedModels(
    class_id = 1,
    races_id = 1,
    strength = 1,
    constitution = 1,
    dexterity = 1,
    intelligence = 1,
    wisdom = 1,
    charisma = 1
)
"""
End table population, now adding to database
"""
db.session.add(barbarian)
db.session.add(bard)
db.session.add(cleric)
db.session.add(druid)
db.session.add(fighter)
db.session.add(monk)
db.session.add(paladin)
db.session.add(ranger)
db.session.add(rogue)
db.session.add(sorcerer)
db.session.add(warlock)
db.session.add(wizard)
db.session.add(dragonborn)
db.session.add(dwarf)
db.session.add(elf)
db.session.add(gnome)
db.session.add(halfelf)
db.session.add(halfling)
db.session.add(halforc)
db.session.add(human)
db.session.add(tiefling)

db.session.add(example)

db.session.commit()
