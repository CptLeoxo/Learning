# To run this script, type "python3 hello.py" in your terminal.

# docs.python org/3/library/functions.html
# print(*objects, sep='', end='\n', file=sys.stdout, flush=False)

# .capitalize() -> only capitalizing the first [0] one char

# name = input("What's your name?\n").strip().title()  # Prompt the user for their name with stripping from whitespaces and capitalizing name 

# Remove whitespace from str and capitalize user's name in one as a new line of code
# name = name.strip().capitalize()

# Or only capitalize as a new code name = name.capitalize() 

# first, last = name.split(" ")

# print(f"Hello, {first} {last}!")
# print("Your name is", name, sep="???")

# age = input("How old are you?\n")  # Prompt the user for their age
# print("You are " + age)

# hobby = input("What is your hobby?\n")  # Prompt the user for their hobby
# print("Your hobby is ", end="") # Print the hobby without a newline at the end
# print(hobby)

# print('So you\'re a "coder"')

# book = input("What is your favourite book?").title()
# print(f"Your favourite book is {book}")

def main():
    who = input("What is your name? Please?")
    hello(who)


def hello(to="world"):
    print(f"hello,", to)

# hello()

if __name__ == "__main__":
    main()