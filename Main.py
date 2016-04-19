#The Main module to call other modules and run the game.

import Room_maps
import Rooms
import Game_Engine


#instances of Map , Engine created
a_map = Room_maps.Map('entrance')

#instance of Game Engine created.
a_game = Game_Engine.Engine(a_map)

#calling the play function from Engine to start game.
a_game.play()
