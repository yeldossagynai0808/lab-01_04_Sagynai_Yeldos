class Player:
    def __init__(self, power, health):
        self.power = power
        self.health = 0 if health < 0 else health
        self.inventory = []

    def damage(self):
        return self.power   

    def heal(self):
        return self.health + 10


class Warrior(Player):
    def handle_event(self, event, attacker=None):
        if event == "ATTACK":
            self.health -= attacker.damage()
            return f"Warrior получил урон от {attacker.__class__.__name__}, hp = {self.health}"

        elif event == "HEAL":
            self.health += 10
            return f"Warrior восстановил hp {self.health}"

        elif event == "LOOT":
            pow_damage = self.damage() * 1.1
            return f"Warrior усилил урон до {pow_damage}"


class Tank(Player):
    def handle_event(self, event, attacker=None):
        if event == "ATTACK":
            self.health -= attacker.damage()
            return f"Tank получил урон от {attacker.__class__.__name__}, hp = {self.health}"

        elif event == "HEAL":
            self.health += 20
            return f"Tank восстановил hp {self.health}"

        elif event == "LOOT":
            pow_damage = self.damage() * 1.2
            return f"Tank усилил урон до {pow_damage}"


p = Player(100, 50)
w = Warrior(150, 60)
t = Tank(200, 80)

print(w.handle_event("ATTACK", attacker=p))
print(t.handle_event("ATTACK", attacker=w))

