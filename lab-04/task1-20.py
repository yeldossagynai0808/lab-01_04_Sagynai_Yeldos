# from flask import Flask
import random
from fastapi import FastAPI
from datetime import datetime

# app = Flask(__name__)
app = FastAPI()


### 1 ###
class  Player:
    def __init__(self,id, name, hp):
        self._id = id
        self._name = name.strip().title()
        if hp < 0:
            self._hp = 0
        else:
            self._hp = hp

    def __str__(self):
        return f"Player({self._id}, name = {self._name}, hp = {self._hp})"

    def __del__(self):
        print("Player ({self._name}) удален")

p = Player(1, "Yeldos", 100)



### 2 ###
class Player:
    def __init__(self, id, name, hp):
        self.id = id
        self.name = name.strip().title()
        self.hp = hp if hp > 0 else 0

    def __str__(self):
        return f"Player(id={self.id}, name='{self.name}', hp={self.hp})"

    @classmethod
    def from_string(cls, data: str):
        parts = data.split(",")

        if len(parts) != 3:
            raise ValueError("Неверный формат строки")

        try:
            id = int(parts[0].strip())
            name = parts[1].strip()
            hp = int(parts[2].strip())
        except:
            raise ValueError("Ошибка преобразования данных")

        return cls(id, name, hp)
                




### 3 ###
class Item:
    def __init__(self, id, name, power):
        self.id = id
        self.name = name.strip().title()
        self.power = power

    def __hash__(self):
        return self.hash()

    def __eq__(self):
        return 

    def __str__(self):
        return f"Item(id={self.id}, name = {self.name}, power={self.power})"

i = Item(1, "Sword", 50)
print(i)











### 4 ###
# class Item:
#     def __init__(self, id, name, power):
#         self.id = id
#         self.name = name
#         self.power = power

#     def __eq__(self, other):
#         if not isinstance(other, Item):
#             return False
#         return self.id == other.id

#     def __hash__(self):
#         return hash(self.id)

#     def __str__(self):
#         return f"Item(id={self.id}, name='{self.name}', power={self.power})"

#     def __repr__(self):
#         return self.__str__()

# class Inventory():
#     def __init__(self):
#         self._items = []

#     def add_item(self, item):
#         for i in self._items:
#             if i.id == item.id:
#                 return
#         self._items.append(item)

#     def remove_item(self, item_id):
#         self._items = [i for i in self._items if i.id != item_id]

#     def get_items(self):
#         return self._items



#     def unique_items(self):
#         return set(self._items)

#     def to_dict(self):
#         return {item.id: item for item in self._items}

# inv = Inventory()

# inv.add_item(Item(1, "Sword", 50))
# inv.add_item(Item(2, "Gun", 100))
# inv.add_item(Item(1, "Sword", 50))  

# print(inv.get_items())
# print(inv.unique_items())
# print(inv.to_dict())


### 5 ### 
#     def get_strong_items(self, min_power):
#          return list(filter(lambda item: item.power >= min_power, self._items))

# inv = Inventory()

# inv.add_item(Item(1, "Sword", 50))
# inv.add_item(Item(2, "Gun", 100))
# inv.add_item(Item(3, "Knife", 20))

# print(inv.get_strong_items(50))

### 6 ###
# class Event:
#     def __init__(self, type, data):
#         self.type = type
#         self.data = data
#         self.timestamp = datetime.now()

#     def __str__(self):
#         return f"Event(type='{self.type}', data={self.data}, timestamp='{self.timestamp}')"

# e = Event("ATTACK", {"damage": 20})
# print(e)


### 7 ###
# class Item:
#     def __init__(self, id, name, power):
#         self.id = id
#         self.name = name
#         self.power = power

#     def __str__(self):
#         return f"{self.name}({self.power})"

#     def __repr__(self):
#         return self.__str__()

# class Player:
#     def __init__(self, hp):
#         self.hp = hp
#         self.inventory = []

#     def handle_event(self, event):
#         if event.type == "ATTACK":
#             self.hp -= event.data["damage"]

#         elif event.type == "HEAL":
#             self.hp += event.data["heal"]

#         elif event.type == "LOOT":
#             self.inventory.append(event.data["item"])

#     def __str__(self):
#         return f"Player(hp ={self.hp}, inventory={self.inventory})"

# class Warrior(Player):
#     def handle_event(self, event):
#         if event.type == "ATTACK":
#             reduced_damage = event.data["damage"] * 0.9
#             self.hp -= reduced_damage

#         else:
#             super().handle_event(event)

# class Mage(Player):
#     def handle_event(self, event):
#         if event.type == "LOOT":
#             item = event.data["item"]
#             item.power *= 1.1
#             self.inventory.append(item)
#         else:
#             super().handle_event(event)
# w = Warrior(100)
# m = Mage(100)

# attack = Event("ATTACK", {"damage": 20})
# heal = Event("HEAL", {"heal": 10})
# loot = Event("LOOT", {"item": Item(1, "Sword", 50)})

# w.handle_event(attack)
# m.handle_event(attack)

# w.handle_event(heal)
# m.handle_event(heal)

# w.handle_event(loot)
# m.handle_event(loot)

# print(w)
# print(m)


### 8 ###
# class Player:
#     def __init__(self, id, hp):
#         self.id = id
#         self.hp = hp
#         self.inventory = []


# class Logger:
#     def log(self, event, player, filename):
#         line = f"{event.timestamp};{player.id};{event.type};{event.data}\n"

#         with open(filename, "a") as f:
#             f.write(line)

# logger = Logger()

# p = Player(1, 100)
# e = Event("ATTACK", {"damage": 20})

# logger.log(e, p, "log.txt")


### 9 ###


# class Event:
#     def __init__(self, type, data, timestamp=None):
#         self.type = type
#         self.data = data
#         self.timestamp = timestamp or datetime.now()

# class Logger:
#     def read_logs(self, filename):
#         events = []

#         with open(filename, "r", encoding="utf-8") as f:
#             for line in f:
#                 parts = line.strip().split(";")

#                 timestamp_str, player_id, event_type, data_str = parts

#                 data = eval(data_str)

#                 event = Event(event_type, data, timestamp_str)
#                 events.append(event)

#         return events

# logger = Logger()
# events = logger.read_logs("log.txt")

# for e in events:
#     print(e.type, e.data, e.timestamp)


### 10 ### 

# class Item:
#     def __init__(self, id, name, power):
#         self.id = id
#         self.name = name
#         self.power = power
#     def __str__(self):
#         return f"Item(id={self.id}, name='{self.name}', power={self.power})"

#     def __repr__(self):
#         return self.__str__()

# class EventIterator:
#     def __init__(self, events):
#         self.events = events
#         self.index = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.index >= len(self.events):
#             raise StopIteration

#         event = self.events[self.index]
#         self.index += 1
#         return event
        
# events = [
#     Event("ATTACK", {"damage": 10}),
#     Event("HEAL", {"heal": 5}),
#     Event("LOOT", {"item": Item(1, "Sword", 50)})
# ]

# iterator = EventIterator(events)

# for e in iterator:
#     print(e.type, e.data)


### 11 ###
# def damage_stream(events):
#     for event in events:
#         if event.type == "ATTACK":
#             yield event.data["damage"]

### 12 ###
# def generate_events(players, items, n):
#     events = []

#     event_type = lambda: random.choice(["ATTACK", "HEAL", "LOOT"])

#     for player in players:
#         for _ in range(n):
#             t = event_type()

#             if t == "ATTACK":
#                 data = {"damage": random.randint(10, 100)}

#             elif t == "HEAL":
#                 data = {"heal": random.randint(5, 50)}

#             else:
#                 item = random.choice(items)
#                 data = {"item": item}

#             event = Event(t, data)
#             events.append(event)

#     return events

# ### 13 ###
# def analyze_logs(events):
#     total_damage = sum(
#         event.data["damage"]
#         for event in events
#         if event.type == "ATTACK"
#     )

#     damage_by_player = {}
#     event_count = {}

#     for event in events:
        
#         event_count[event.type] = event_count.get(event.type, 0) + 1

    
#         if event.type == "ATTACK":
#             pid = event.player_id
#             damage = event.data["damage"]
#             damage_by_player[pid] = damage_by_player.get(pid, 0) + damage

#     top_player = max(damage_by_player, key=damage_by_player.get) if damage_by_player else None


#     most_common_event = max(event_count, key=event_count.get)

#     return {
#         "total_damage": total_damage,
#         "top_player": top_player,
#         "most_common_event": most_common_event
#     }

# ### 14 ###
# decide_action = lambda player: (
#     "HEAL" if player.hp < 30
#     else "LOOT" if len(player.inventory) == 0
#     else "ATTACK"
# )

# # p1 = Player(1, 20)
# # p2 = Player(2, 100)

# # p2.inventory.append(Item(1, "Sword", 50))

# # print(decide_action(p1))  # HEAL
# # print(decide_action(p2)) 


# ### 16 ###
# class Player:
#     def __init__(self, id, hp):
#         self.id = id
#         self._hp = hp
#         self._inventory = []

    
#     @property
#     def hp(self):
#         return self._hp

#     @hp.setter
#     def hp(self, value):
#         if value < 0:
#             self._hp = 0
#         else:
#             self._hp = value

    
#     @property
#     def inventory(self):
#         return self._inventory

    
#     def add_item(self, item):
#         self._inventory.append(item)

#     def remove_item(self, item_id):
#         self._inventory = [i for i in self._inventory if i.id != item_id]

#     def __str__(self):
#         return f"Player(id={self.id}, hp={self._hp}, inventory={self._inventory})"



# ### 17 ###
# class Player:
#     def __init__(self, id, name, hp):
#         self.id = id
#         self.name = name
#         self._hp = hp
#         self._inventory = []

#     def __del__(self):
#         print(f"Player {self.name} удалён")


# ### 18 ###
# class Inventory:
#     def __init__(self):
#         self._items = []

#     def add_item(self, item):
#         self._items.append(item)

#     def __iter__(self):
#         return iter(self._items)

# # inv = Inventory()

# # inv.add_item(Item(1, "Sword", 50))
# # inv.add_item(Item(2, "Gun", 100))
# # inv.add_item(Item(3, "Knife", 20))

# # for item in inv:
# #     print(item)

# ### 19 ### 
# def analyze_inventory(inventories):
#     all_items = [item for inv in inventories for item in inv]

#     unique_items = set(all_items)

#     top_item = max(all_items, key=lambda x: x.power) if all_items else None

#     return {
#         "unique_items": unique_items,
#         "top_power": top_item
#     }
# # inv1 = Inventory()
# # inv1.add_item(Item(1, "Sword", 50))
# # inv1.add_item(Item(2, "Gun", 100))

# # inv2 = Inventory()
# # inv2.add_item(Item(1, "Sword", 50))
# # inv2.add_item(Item(3, "Knife", 20))

# # result = analyze_inventory([inv1, inv2])

# # print(result)





    