import random

def main():
    print("\nWelcome to Giraffe!")
    print("You have stolen a giraffe to make your way across the Great Salt Lake.")
    print("Chaerin, giraffe owner, want her giraffe back and is chasing you down!")
    print("Use the giraffe's long legs to cross the lake and run away from Chaerin!\n")

    # variables
    done=False
    miles_traveled = 0
    hungry = 0
    giraffe_tiredness = 0
    Chaerin_traveled = -20
    apple = 3


    # Questions

    while not done:
        print("""A. Give an apple to your giraffe.
B. Ahead moderate speed.
C. Ahead full speed.
D. Stop and rest.
E. Status check.
Q. Quit.""")



        user_choice = input("What is your choice?")

        if user_choice.upper() == "Q":
            print("You have quit the game.")
            break

        elif user_choice.upper() == "E":
            print("\nYou have traveled " + str(miles_traveled) + " miles.")
            print("You have " + str(apple) + " apples left.")
            print("Chaerin is " + str(miles_traveled - Chaerin_traveled) + " miles behind you.\n")

        elif user_choice.upper() == "D":
            giraffe_tiredness=giraffe_tiredness-1
            print("\nYou have stopped for the night to rest. ")
            print("Your giraffe rested and happy!")
            Chaerin_traveled=Chaerin_traveled+random.randrange(7, 14)
            print("But, be careful! Chaerin is " + str(miles_traveled - Chaerin_traveled) + " miles behind you.\n")

        elif user_choice.upper() == "C":
            giraffe_tiredness = giraffe_tiredness + 1
            hungry=hungry+1
            print("\nYour giraffe is really good at swimming, dude!. ")
            miles_traveled = miles_traveled + random.randrange(10, 20)
            giraffe_tiredness = giraffe_tiredness + random.randrange(1, 3)
            Chaerin_traveled = Chaerin_traveled + random.randrange(7, 14)
            print("Chaerin is " + str(miles_traveled - Chaerin_traveled) + " miles behind you.\n")

        elif user_choice.upper() == "B":
            hungry = hungry + 1
            print("\nYour giraffe slows down... ")
            miles_traveled = miles_traveled + random.randrange(5, 12)
            giraffe_tiredness = giraffe_tiredness + 1
            Chaerin_traveled = Chaerin_traveled + random.randrange(7, 14)
            print("Chaerin is " + str(miles_traveled - Chaerin_traveled) + " miles behind you.\n")

        elif user_choice.upper() == "A":
            if apple > 0:
                hungry=0
                apple=apple-1
                print ("\nHere is an apple for you ;)\n")
            else:
                print("\nNo more apples :/\n")

        if hungry > 4:
            print("\nYour giraffe are hungry!\n")
        if hungry > 6:
           print("Your giraffe is dead of hungry\n")
           done=True
           break
        if giraffe_tiredness > 5:
            print("\nYour giraffe couldn't cross the Great Salt Lake")
            print("Game Over")
            done=True
            break







main()

