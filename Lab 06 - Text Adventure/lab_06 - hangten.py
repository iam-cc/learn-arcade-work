# Data setup
rooms = {"Great Hall" : {"name" : "Great Hall", "South": "Bedroom", "North" : "Dungeon", "West": "Library", "East": "Kitchen" },
         "Bedroom" : {'name': 'Bedroom', 'East': 'Cellar', 'North': 'Great Hall'},
         'Cellar': {'name': 'Cellar', 'West': 'Bedroom'},
         'Library': {'name': 'Library', 'East': 'Great Hall'},
         'Kitchen': {'name': 'Kitchen', 'West': 'Great Hall', 'North': 'Dining Room'},
         'Dining Room': {'name': 'Dining Room', 'South': 'Kitchen'},
         'Dungeon': {'name': 'Dungeon', 'South': 'Great Hall', 'East': 'Gallery'},
         'Gallery': {'name': 'Gallery', 'West': 'Dungeon'},}
directions = ["North", "South", "East", "West"]
current_room = rooms ["Great Hall"]

# game loop
while True:
    # display current location
    print()
    print("You are in the {}.".format(current_room["name"]))

    # get user input
    command = input("\nWhat direction do you want to go?"). strip()
    # movement
    if command in directions:
        if command in current_room:
            current_room = rooms[current_room[command]]
        else:
            # bad movement
            print("You can't go that way.")
    # Exit game
    elif command.lower() in ("q", "quit"):
        break
    # bad command
    else:
        print("I don't understand that command.")

class Room:
    name: str
    north: "Room"
    east: "Room"
    south: "Room"
    west: "Room"

    def __int__(self, name, north=None, east=None, south=None, west=None):
        self.name = name
        self.north = north
        self.east = east
        self.west = west
        self.south = south

        if north:
            north.south = self
        if east:
            east.west = self
        if south:
            south.north = self
        if west:
            west.east = self
    def go_to(self, direction):
        if direction in ["north", "east", "south", "west"] :
            return getattr(self, direction)
        else:
            return None
    #def __str__(self):
        #retrun self.name

class House:
    current_room: Room
    rooms: list[Room]  # at the moment is not used but could be in the future?

    def __init__(self, current_room: Room, rooms: list[Room]):
        self.current_room = current_room
        self.rooms = rooms

    def go_to(self, direction):
        if next_room := self.current_room.go_to(direction):
            self.current_room = next_room
        return next_room

if __name__ == '__main__':
    while game_loop():
        pass
