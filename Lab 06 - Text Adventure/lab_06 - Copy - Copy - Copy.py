class player:
    def __int__(self):
        self.name = ""
        self.hp = 0
        self.mp = 0
        self.status_effects = []
myPlayer = player()

#### title screen ####
def title_screen_selections():
    option = input(">")
    if option.lower() == ("play"):
        start_game() #placeholder until written
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ['play','help','quit']:
        print("Please enter a valid command.")
        option = input(">")
        if option.lower() ==("play"):
            start_game() #placeholder until written
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit()
def title_screen():
    os.system("clear")
    print("#########################")
    print("# Welcome to the Text RPG! #")
    print("#########################")
    print("      - Play -       ")
    print("      - Help -       ")
    print("      - Quit -       ")
    print(" Copyright 2022 chaerin.me ")