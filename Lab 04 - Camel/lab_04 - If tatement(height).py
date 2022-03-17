# x= 163

user_input = input("Hey, guess my height. You have two chances. But no hint sorry:")
user_input2 = input("And now give me another number.")
x = int(user_input)
y = int(user_input2)


# simple if statement
if 164>x>162 or 162<y<164 :
    print("You are right there. Correct!. It's 163!")

elif x>163 and y>163:
    print("Thank you! but, nope. DOWN")

elif x<163 and y<163:
    print("Nope. I am taller than you thought")

else:
    print("nope, dang. I am 163")




