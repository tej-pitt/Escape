#Game engine  module which runs the game with the method play and using the map methods to get from one scene to another.


class Engine(object):

#constructor with scene_map as argument
    def __init__(self,scene_map):
        self.scene_map = scene_map

        
#function to enter opening scene        
    def play(self):
        current_scene = self.scene_map.opening_scene()
        
        while current_scene is not None:
            print "<<<<<<<<<< MI-Escape from Rogue AI >>>>>>>>>>>>>> "
            next_scene_name = current_scene.enter() #enter the current scene calling 'enter' function.
            current_scene = self.scene_map.next_scene(next_scene_name) #to enter the next scene calling map function 
        
        
