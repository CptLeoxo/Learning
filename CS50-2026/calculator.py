print("This is a calculator")

def main():

    type_of_number = input("What is the type of calculus do you want? \nInt / Float ?: ").title()

    if type_of_number not in ["Int", "Float"]:

        print(calculator(type_of_number))
        return

    x = input("What's the x? ")
    y = input("What's the y? ")

    print(calculator(type_of_number, x, y))

def calculator(type_of_number, x=0, y=0):

    if type_of_number == "Float":
        try:
            x = float(x)
            y = float(y)

            return f"Your result is {round(x + y, 2):,}"
        except ValueError:
            return f"Error: Please enter only numbers."
        # print(f"Your result is {z:.2f}") 

    elif type_of_number == "Int":
        try:
            x = int(x)
            y = int(y)

            return f"Your result is {(x + y):,}"
        except ValueError:
            return f"Error: Please enter only numbers."

    else:

        return "You have to choose Int / Float !"

# Or z = int(x) + int(y)

'''
z = x + y
print(x + y)
'''
# Запускаем скрипт только при прямом вызове
if __name__ == "__main__":
    main()