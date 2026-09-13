print("This is a calculator")

while True:

    type_of_number = input("What is the type of calculus do you want? \nInt / Float ?: ").title()

    if type_of_number == "Float":

        x = float(input("What's the x? "))
        y = float(input("What's the y? "))

        print(f"Your result is {round(x / y, 2):,}") 

        # print(f"Your result is {z:.2f}") 


    elif type_of_number == "Int":

        x = int(input("What's the x? "))
        y = int(input("What's the y? "))

        print(f"Your result is {(x + y):,}")

    else:

        print("You have to choose Int / Float !")


# Or z = int(x) + int(y)

'''
z = x + y
print(x + y)
'''

