#scenes module with all the scenes of the game and navigation.

from sys import exit
from random import randint


#Abstract Base  class for scenes
class Scene(object):
#abstract class method enter to enter scenes.
    def enter(self):
        print "this scene not fully configured yet , implement enter()"
        exit(1)
 
#Inheriting from the Scene class 
class Death(Scene):
 #create a list of ways to mock when you die.   
    ways = ["You deserve to die if you are so dumb!",
    
    "Action without logic brings Death!",
    "such a loser! you die!" ,
    "my grandma plays better than you!",
    "my pet monkey plays this game better!"
    ]

#using the enter method from abstract class Scene    
    def enter(self):
        print Death.ways[randint(0,len(self.ways)-1)]
        exit(1)

#Opening scene  with decisions       
class Entrance(Scene):
    def enter(self):
        print "Welcome to your new mission ETHAN HUNT!"
        print "Your mission if you choose to accept it is to sneak in the Rogue AI unit - Matrix and steal the nuclear codes , "
        print "Then you have to place your bomb in the server room "
        print "and make your way through the roof for the waiting chopper to pick you up."
        print "Save the world from nuclear destruction."
        print "Caution: the AI master unit - The Brain is said to be most intelligent virtual entity in the world!"
        print "You have to defeat him in a math problem."
        print "do you accept the mission Ethan?"
        
        choice = raw_input("> ")
        
        if choice == "yes":
            print "Brilliant Ethan! The world depends on you!"
            print "Now you are outside the entrance: what will you do?"  
            print "You have 2 options: 1.sneak 2. shoot "            
            action = raw_input("> ")
        
            if action == "sneak":
                print "Well done! You are through the entrance on the way to control room."
                print "No one suspects you!"
                return 'control_room'
            
            elif action == "shoot":
                print "Was a dumb move! The guards overpower you and shoot you to bits!"
                return 'death'
            
            else: 
                print "Invalid input"
                return 'entrance' 
            
            
        elif choice == "no":
            print "Coward! We choose to terminate you instead! Now you die!"
            return 'death'
            
        else:
            print "Invalid input! Does Not Compute!"
            return 'entrance'
        
        

            
#Next scene with decisions           
class Control_Room(Scene):
    def enter(self):
        print "Now you are in the control room , your chance to proceed undetected!"
        print "you find the control room guards , you inform them of some fire mishap outside!"
        print "they leave to check the emergency.You meanwhile disable the CCTV cameras."
        print "You sneak out. But the guards notice you."
        print "They raise an alarm and quiz you!"
        print "what you gonna do?"
        print "You have 2 options : 1. shoot 2. joke "
        
        action = raw_input("> ")
        
        if action == "shoot":
            print "you raise an alarm! dumbass move!"
            print "they easily call other guards and shoot you to death!"
            return 'death'
            
        elif action == "joke":
            print '''you crack a random joke with the guards and tickle their funny bone.
             they dont suspect you  anymore
	          You sneak out from the Control room 
              Proceed on the mission Ethan!'''
            return 'AI_vault'
            
        else:
            print "invalid input"
            return 'control_room'


#Next scene             
class AI_Vault(Scene):
    def enter(self):
        print '''Welcome to the home of the Brain.... Human! , The Brain rumbles on you entering the Brain vault.
		 So you wish to surpass me? I am the World's most Brainiest entity! You cant better me!
        To get out from here alive ,  you have to solve 3 math problems  and destruct me!
         I cant handle anyone else being more brainy than me! It is Impossible!
        Here is your problem!'''
        print "what is: 4x4+4x4+4-4x4 "
        
        action = raw_input("> ")
        if action == "20":
            print "The Brain is furious , you got it right!"
            print "I am sure you cant answer this one though , you miserable Human!"
            print "Now to the next!"
            print '''
Imagine you're on a game show, and you're given the choice of three doors:
Behind one door is a million dollars, 
and behind the other two, nothing. You pick door #1, 
and the host, who knows what's behind the doors, opens another door, say #3, 
and it has nothing behind it. He then says to you, 
"Do you want to stick with your choice or switch?
What will increase your probability to win? stick to first choice  or switch? '''
        
            action = raw_input("> ")
            if action == "switch":
                print "The Brain's muscles are red with rage! "
                print "If you get this one right , he will self destruct with all the insult!!!"
            
        
            else:
                print "Now you die!"
                return 'death'

            print "what is the answer for: 6 / 2(1+2) ?"
                
            action = raw_input("> ")
            
            if  action == "9":
                print "Correct! You are a Math genius , that I never thought I would meet!"
                print "The brain lets out a painful groan....and he self destructs!"
                print "You just destroyed the Brain! Good going!" 
                return 'server_room'
    
            else:
                print "Wrong! Now you die!"
                return 'death'
        else:
            print "Wrong! Now you die!"
            return 'death'
        
        
    
        
            

       

 #server scene with use of random module                    
class Server_Room(Scene):
    def enter(self):
        print "Now you are in the server room , retrieve the key nuclear codes"
        print "You have to guess the keycode to open the case containing nuclear codes"
        print "after you guess , plant the bomb and escape to the roof."
        print "you have 5 guesses to guess the 2 digit  keycode for the container"
        print "the digits can only be between 1 and 3. Goodluck!"
        code = "%d%d" % (randint(1,3),randint(1,3))
        guess = raw_input("## ")
        chances = 0
        
        while guess != code and chances < 4:
            print "BZZZEEDDDD! Wrong!"
            guess = raw_input("[keypad]## ")
            chances += 1
            
        if guess == code:
            print "the container clicks open and you retrieve the nuclear codes. awesome!"
            print "now you plant the bomb!"
            print "the bomb starts ticking and its time to escape!"
            print " you escape to the Roof where the chopper awaits."
            return 'roof'
        else:
            print "the lock buzzes and the codes in papyrus roll melt away."
            print "you despair and wait for the guards to discover you."
            print "they capture you and put you through a dog's death!"
            return 'death'


            
#Final scene with a question             
class Roof(Scene):
    def enter(self):
        print "You escape to the rooftop using the AC ducts in the server room. "
        print "You reach the rooftop."
        print "Theres benjy waiting in the chopper hovering above."
        print "Now there is another challenge: Benjy needs to know its really you, Ethan."
        print "So you have to answer a random Science question."
        print "If you solve it , he throws the rope to you  , if not he shoots you."
        print "Which Scientist discovered Oxygen gas ?"
        guess = raw_input("> ")
        chances = 0
        
        while guess!= "Priestley" and chances < 4:
            print "wrong!"
            guess = raw_input("> ")
            chances += 1
            
        if guess == "Priestley":
            print "correct! Hop in Ethan!"
            print "you escape with the rope he throws and escape from the building bad ass style!" 
            print "As you fly away the city skyline , you enjoy the fireworks of the building. "
            print "Mission accomplished! Well done Ethan! That was hard!"
            return 'finished'

        else:
            print "We know rogue agents when we see one! you Impostor! Now you die!"
            print "Benjy shoots you with his sniper  and you die on the rooftop!"
            return 'death'            

