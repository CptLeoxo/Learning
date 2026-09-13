# Week two

'''
>  GT

>=  GT or EQ

<  LT

<=  LT or EQ

==  EQ

!=  NEQ



'''

def compare(x, y):
    try:
        x = float(x)
        y = float(y)

        if x < y:
            return "x is less then y"

        if x > y:
            return "x is greater then y"

        if x == y:
            return "x is equal to y"
    except ValueError:
        return "Error Value!"

def main():

    print("This is comperator.")
    x = input("What's x? ")
    y = input("What's y? ")
    print(compare(x, y))

if __name__ == "__main__":
    main()