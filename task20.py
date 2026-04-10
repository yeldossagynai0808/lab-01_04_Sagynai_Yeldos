import random
from datetime import datetime


class Event:
    def __init__(self, event_type, data):
        self.type = event_type
        self.data = data
        self.timestamp = datetime.now()

    def __str__(self):
        return f"{self.timestamp} | {self.type} | {self.data}"


class Inventory:
    def __init__(self):
        self._items = []

    def add_item(self, name, power):
        self._items.append((name, power))

    def __iter__(self):
        return iter(self._items)

    @property
    def items(self):
        return self._items


class Player:
    def __init__(self, name, hp):
        self.name = name
        self._hp = hp
        self._inventory = Inventory()
        self.total_damage_taken = 0
        self.event_stats = {"ATTACK": 0, "HEAL": 0, "LOOT": 0}

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = max(0, value)

    @property
    def inventory(self):
        return self._inventory

    def handle_event(self, event):
        if event.type == "ATTACK":
            damage = event.data.get("damage", 0)
            self.hp -= damage
            self.total_damage_taken += damage
            self.event_stats["ATTACK"] += 1

        elif event.type == "HEAL":
            heal = event.data.get("heal", 0)
            self.hp += heal
            self.event_stats["HEAL"] += 1

        elif event.type == "LOOT":
            item_name = event.data.get("item")
            item_power = event.data.get("power", 0)
            if item_name:
                self.inventory.add_item(item_name, item_power)
            self.event_stats["LOOT"] += 1

    def __del__(self):
        print(f"Player {self.name} удалён")

    def __str__(self):
        return f"{self.name}: HP={self.hp}, Items={len(self.inventory.items)}"


class Warrior(Player):
    def handle_event(self, event):
        if event.type == "ATTACK":
            damage = event.data.get("damage", 0)
            damage *= 0.9
            damage = round(damage, 2)
            self.hp -= damage
            self.total_damage_taken += damage
            self.event_stats["ATTACK"] += 1
        else:
            super().handle_event(event)


class Mage(Player):
    def handle_event(self, event):
        if event.type == "LOOT":
            item_name = event.data.get("item")
            item_power = event.data.get("power", 0)
            if item_name:
                boosted_power = round(item_power * 1.1, 2)
                self.inventory.add_item(item_name, boosted_power)
            self.event_stats["LOOT"] += 1
        else:
            super().handle_event(event)


def generate_events(items, n):
    events = []
    event_types = ["ATTACK", "HEAL", "LOOT"]

    for _ in range(n):
        t = random.choice(event_types)

        if t == "ATTACK":
            data = {"damage": random.randint(10, 50)}

        elif t == "HEAL":
            data = {"heal": random.randint(5, 30)}

        else:
            item_name, item_power = random.choice(items)
            data = {"item": item_name, "power": item_power}

        events.append(Event(t, data))

    return events


def write_logs(filename, players, all_logs):
    with open(filename, "w", encoding="utf-8") as f:
        f.write("=== LOGS ===\n")
        for log in all_logs:
            f.write(log + "\n")

        f.write("\n=== PLAYERS ===\n")
        for player in players:
            f.write(f"{player.name};HP={player.hp};Items={len(player.inventory.items)}\n")


def read_logs(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.readlines()


def analyze_players(players):
    most_damaged_player = max(players, key=lambda p: p.total_damage_taken)
    most_items_player = max(players, key=lambda p: len(p.inventory.items))

    total_event_stats = {"ATTACK": 0, "HEAL": 0, "LOOT": 0}
    for player in players:
        for event_type, count in player.event_stats.items():
            total_event_stats[event_type] += count

    return {
        "most_damaged_player": most_damaged_player.name,
        "max_damage": most_damaged_player.total_damage_taken,
        "most_items_player": most_items_player.name,
        "items_count": len(most_items_player.inventory.items),
        "event_stats": total_event_stats
    }


def main():
    random.seed(42)

    items = [
        ("Sword", 50),
        ("Shield", 30),
        ("Axe", 70),
        ("Bow", 40),
        ("Staff", 60)
    ]

    players = [
        Warrior("Arman", 100),
        Mage("Aruzhan", 100),
        Player("Eldos", 100)
    ]

    events = generate_events(items, 10)

    all_logs = []

    for player in players:
        all_logs.append(f"\n--- Events for {player.name} ---")
        for event in events:
            before_hp = player.hp
            before_items = len(player.inventory.items)

            player.handle_event(event)

            after_hp = player.hp
            after_items = len(player.inventory.items)

            log_line = (
                f"{player.name} | {event.type} | {event.data} | "
                f"HP: {before_hp} -> {after_hp} | "
                f"Items: {before_items} -> {after_items}"
            )
            all_logs.append(log_line)

    log_file = "game_logs.txt"
    write_logs(log_file, players, all_logs)

    print("Логи записаны в файл.\n")

    print("Содержимое файла:")
    lines = read_logs(log_file)
    for line in lines[:15]:
        print(line.strip())

    print("\n--- Аналитика ---")
    result = analyze_players(players)

    print("Игрок с наибольшим уроном:", result["most_damaged_player"])
    print("Полученный урон:", result["max_damage"])
    print("Игрок с максимальным количеством предметов:", result["most_items_player"])
    print("Количество предметов:", result["items_count"])
    print("Общая статистика событий:", result["event_stats"])

    print("\n--- Итог игроков ---")
    for player in players:
        print(player)
        print("Предметы:", player.inventory.items)


if __name__ == "__main__":
    main()