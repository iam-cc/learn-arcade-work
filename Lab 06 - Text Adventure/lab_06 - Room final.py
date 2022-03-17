def start():
    print('''
****************************************
*                                      *
*  Welcome to Chaerin's Text Adventure!*
*                                      *
****************************************
''')

    balcony()


def prompt():
    x = input("Type a command: ")
    return x




# ROOMS*******************************************************************************8

# Balcony

def balcony():
    print("****************************************")
    print('''

You are on the balcony in your house. The wind is strong and cold.
    ''')
    print('''Options:
1. Go inside the house
2. Stay on the balcony

''')

    command = prompt()
    if command == "1":
        north_hall()
    elif command == "2":
        print("********")
        print ("You are still on the balcony. It's getting colder.")
        balcony()
    else:
        balcony()


# north_hall
def north_hall():
    print("****************************************")
    print ('''
You are in your north hall. You can walk around your house.
    ''')

    print('''Options:
1. Go back to the balcony
2. Enter the bedroom on your right
3. Enter the kitchen on your left
4. Walk forward
''')
    command = prompt()
    if command == "1":
        balcony()
    elif command == "2":
        bedroom()
    elif command == "3":
        kitchen()
    elif command == "4":
        south_hall()
    else:
        north_hall()

# south_hall
def south_hall():
    print("****************************************")
    print ('''
You are in your south hall. You can walk around your house.
    ''')

    print('''Options:
1. Go back to the north hall
2. Enter the bathroom on your right
3. Enter the dinning room on your left
''')
    command = prompt()
    if command == "1":
        north_hall()
    elif command == "2":
        bathroom()
    elif command == "3":
        dinning()
    else:
        south_hall()

# Dinning room
def dinning():
    print('''****************************************
You are in the dinning room. Nothing in the dinning room.
    ''')
    print('''Options:
    1. Stay in the dinning room
    2. Go back to the south hall
''')

    command = prompt()
    if command == "1":
        dinning()
    elif command == "2":
        south_hall()
    else:
        south_hall()

# Bathroom
def bathroom():
    print('''****************************************
You are in the bathroom. There is warm water in the bathtub.
    ''')
    print('''Options:
    1. Take a bath
    2. Go back to the south hall
''')

    command = prompt()
    if command == "1":
        bath()
    elif command == "2":
        south_hall()
    else:
        south_hall()

# kitchen
def kitchen():
    print('''****************************************
You are in the kitchen. It smells like pancakes.
    ''')
    print('''Options:
    1. Eat pancakes 
    2. Go back to the north hall
''')

    command = prompt()
    if command == "1":
        pancakes()
    elif command == "2":
        north_hall()
    else:
        kitchen()

# Bedroom
def bedroom():
    print('''****************************************

You are in the bedroom. It's dark.
''')
    print('''Options:
    1. Turn on the light 
    2. Go back to the north hall
''')

    command = prompt()
    if command == "1":
        light_on()
    elif command == "2":
        north_hall()
    else:
        bedroom()


# EVENTS *****************************************************************************************
# turn on the light
def light_on():
    print('''****************************************

You turn on the light. There are some clothes to prevent freezing.
    ''')
    print('''Options:
    1. Put on clothes 
    2. Go back to the north hall without clothes
''')

    command = prompt()
    if command == "1":
        clothes()
    elif command == "2":
        north_hall()
    else:
        light_on()


#clothes
def clothes():
    print('''****************************************

You put on clothes. Your body is getting warm.
    ''')
    print('''Options:
    1. Wear some other clothes
    2. Go back to the north hall without clothes
''')

    command = prompt()
    if command == "1":
        clothes()
    elif command == "2":
        north_hall()
    else:
        clothes()


# pancakes
def pancakes():
    print('''****************************************

You eat pancakes. You are getting full.
    ''')
    print('''Options:
    1. Eat more pancakes 
    2. Go back to the north hall
''')

    command = prompt()
    if command == "1":
        pancakes()
    elif command == "2":
        north_hall()
    else:
        pancakes()

# bath
def bath():
    print('''****************************************

You take a bath. It makes you feel better.
    ''')
    print('''Options:
    1. Go back to the south hall
''')

    command = prompt()
    if command == "1":
        south_hall()
    else:
        bath()




start()