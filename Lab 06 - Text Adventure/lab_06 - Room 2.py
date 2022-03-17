def start():
    print('''
****************************************
*                                      *
*  Welcome to Chaerin's Text Adventure!  *
*                                      *
****************************************
''')

    balcony()

## Game functions

#def checkstats():
#    print('''

#********''')
#    print("Gold:", gold)
#    print("Health:", health,"/",fullhealth)
#    print("Melee:", melee)
#    print ("Energy:", energy)
#    global ranged
#    if ranged > 0:
#        print("Ranged:", ranged)
#        print("Ammo:", ammo)

def prompt():
    x = input("Type a command: ")
    return x



##Rooms*********************************************************


## Balcony////

def balcony():
    print("****************************************")
    print('''

You are in your balcony in a small home.
    ''')
    print('''Options:
1. Go Inside
2. Rest

''')

    command = prompt()
    if command == "1":
        north_hall()
    elif command == "2":
        print("********")
#        print ("You are back to full health. (",fullhealth,"/",fullhealth,")")
#        global health
#        health = fullhealth
#        balcony()
#    elif command == "9":
#        checkstats()
#        balcony()
    else:
        balcony()


## north_hall ////
def north_hall():
    print("****************************************")
    print ('''

You are in your north hall. You can walk around the small home.
    ''')

    print('''Options:
1. Go back to the balcony
2. Enter the bedroom
3. Walk to the coast
''')
    command = prompt()
    if command == "1":
        balcony()
    elif command == "2":
        bedroom()
    elif command == "3":
        kitchen()
#    elif command == "9":
#        checkstats()
#        north_hall()
    else:
        north_hall()








## Bedroom ////
def bedroom():
    print('''****************************************

You are in the bedroom. It's dark.
    ''')

    ## This is what happens when you enter the forest for the first time
#    global attacknum
#    if attacknum == 0:
#        print('''********
#You are attacked by a wild beast! OH NO!!
#(-1 health)


#''')### It says that you have been attacked
#        attacknum = 1 #It records that you have been attacked
#        global health
#        health = health - 1#Your health goes down


    ##This is what happens when you have already entered the bedroom before
    if attacknum == 1:
        print('''Options:
1. Go to your north_hall
2. Pick up stones
3. Explore deeper into the forest
9. Stats
    ''') ##It gives you your options
        command = prompt()
        if command == ("1"):
          north_hall()
        elif command == ("2"):
          find_stones()
          forest()
        elif command == "3":
            battle()
        elif command == "9":
          checkstats()
          bedroom()
        else:
          bedroom()






## Kitchen
def kitchen():
    print ('''****************************************

You at the kitchen. It smells lie pancakes.
    ''')
    print ('''Options:
1. Go to north hall
2. Talk to fisherman
3. Pick up stones
9. Stats''')
    command = prompt()
    if command == "1":
        north_hall()
    elif command == "2":
        fishconvo()
    elif command =="3":
        find_stones()
        kitchen()
    elif command =="9":
        checkstats()
        kitchen()
    else:
        kitchen()


##City
def city():
        print('''****************************************
    You arrived!!!!!
         ''')


## Events ***********************************************************
def find_stones():
    global ranged
    global ammo
    if ranged == 0:
        print('''********

You found 5 stones you can throw at an enemy.
(+1 ranged) (+5 ammo) ''')
        ranged = 1
        ammo = 5

    elif ranged >=1 and ammo < 5:
        ammo = 5
        print('''********
You stuff a few stones in your bag for later.''')
    elif ranged >= 1 and ammo > 4:
        print('''
********
        You don't find any suitable stones.''')







## Battle//////////
def battle():
    print('''****************

You have been attacked by a wild pig chicken. What do you do?
''')

    print('''1. Run
2. Fight
3. Make friends with the pig chicken''')
    command = prompt()
    if command == "1":
        forest()
    elif command == "2":
        print('''
*********''')
        print("You have just been brutally raped by a horny pig chicken!! You suck!!")
        print('''

GAME OVER!!!!!''')
    elif command == "3":
        print('''
*********''')
        print("You have just been brutally raped by a horny pig chicken!! You suck!!")
        print('''


GAME OVER!!!!!''')



##Training//////////////
def fishconvo():
    print('''********

Fisherman: "The fish aren't biting today. Want me to teach you a few boxing moves?

1. Yes
2. No''')
    global melee
    command=prompt()
    if command == "1" and melee <2:
        melee = 2
        print('''********
Fisherman: "Now don't go beating up that nerdy crippled kid."
(+1 melee)
''')
        coast()
    elif command == "1" and melee >1:
        print('''********
Fisherman "Looks like I have nothing left to teach you."
        ''')
        coast()
    elif command == "2":
        print(''' ********
Fisherman: "Well, don't come crying to me if you get brutally raped by a horny pig chicken."
''')
        coast()
    else:
        coast()


def boatconvo():
    print('''********
Boat captain: "I can sail you to the city for a nominal fee."

1. Okay
2. No thanks
''')
    command = prompt()
    if command == "1":
        print('''********
The boatman sails you to the capital city.
(-2 gold)
''')
        global gold
        gold = gold -2
        city()
    elif command =="2":
        coast()


start()