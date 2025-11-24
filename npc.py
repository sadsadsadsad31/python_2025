class NPC:
    def init(self, name, hp):
        self.name = name
        self.hp = hp

    def attack(self):
        return 0


class Swordsman(NPC):
    def init(self, name, hp, min_damage, max_damage):
        super().init(name, hp)
        self.min_damage = min_damage
        self.max_damage = max_damage

    def attack(self):
        return self.min_damage, self.max_damage


class Mage(NPC):
    def init(self, name, hp, mana):
        super().init(name, hp)
        self.mana = mana

    def attack(self):
        return self.mana


swordsman = Swordsman("Jalin", 100, 5, 12)
mage = Mage("Jamal", 80, 250)

print("Воин наносит урон от", warrior.min_damage, "до", warrior.max_damage)
print("Мана мага:", mage.mana)
