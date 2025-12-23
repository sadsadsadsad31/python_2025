character = {
    "Сила":10 ,
    "Ловкость":11,
    "Удача":53,
    "Мудрость":44,
    "Харизма":33,
    "Интелект":5664,
    "Баз. сила":385893420,
}

print(character)

class Hero:
    def __init__(self, lvl, name, last_name, lor, history, hp, old, spells,
                 radius, weaknesses, speed, intelligence, power, agility, lucky, power_damage, exp, gender):
        self.name = name
        self.last_name =last_name
        self.lor = lor
        self.history = history
        self.hp = hp
        self.old =old
        self.spells =spells
        self.radius = radius
        self.weaknesses = weaknesses
        self.gender = gender
        self.attr = {speed:speed,
                     intelligence:intelligence,
                     power:speed,
                     agility:speed,
                     lucky:speed,
                     power_damage:speed,
                     exp:speed,
        }
