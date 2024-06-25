from sys import exit
from random import randint
from textwrap import dedent
from bs4 import BeautifulSoup
import requests

url = "https://blogs.transparent.com/latin/100-most-common-words-in-latin/"

r = requests.get(url)
r_text = r.text

soup = BeautifulSoup(r_text, 'html.parser')
table = soup.table

list = []

for child in table.stripped_strings:
    list.append(child)

list2 = []

for group in [list[i:i+3] for i in range(0, len(list), 3)]:
    list2.append(group)

dict = {}

for group in list2:
    number, word, definition = group
    dict[number] = {'latin': word, 'english': definition}

class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter()")
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map
    
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()


class Death(Scene):

    quips = [
        "Died. You suck at this game.",
        "You'd better be wasting your time reading Hegel or somethin'. Not good; no bueno.",
        "You're dead. Try again if you have the guts to die millions of times more.",
        "My one-year old is better than you. Sucker."
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
            Welcome to the nerdiest ship on the Galaxy.
            You will be required to prep your Latin skills. 
            Most used words. 1-1000. Ha-ha-ha! Evil!
            """))
        
            

class LaserWeaponArmory(Scene):

    def enter(self):
        pass

class TheBridge(Scene):

    def enter(self):
        pass

class EscapePod(Scene):

    def enter(self):
        pass

class Finished(Scene):

    def enter(self):
        pass

class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()