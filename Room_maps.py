#Maps module , defining the 2 main methods of the class and a dictionary for all the scenes in it with key-value pairing.

import Rooms
import Game_Engine

#create class map with a dictionary for scene reference. 
class Map(object):
    scenes = {
    'entrance' : Rooms.Entrance(),
    'control_room' : Rooms.Control_Room(),
    'AI_vault' : Rooms.AI_Vault(),
    'server_room' : Rooms.Server_Room(),
    'roof' : Rooms.Roof(),
    'death' : Rooms.Death()
    }

    #constructor with start_scene as argument.    
    def __init__(self,start_scene):
        self.start_scene = start_scene


    #function to retrieve scenes from dictionary         
    def next_scene(self,scene_name):
        val = Map.scenes.get(scene_name)
        return val

    #using the next_scene function to display opening scene        
    def opening_scene(self):
        return self.next_scene(self.start_scene)
        
       
        
        
