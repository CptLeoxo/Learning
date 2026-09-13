# To run this script, type "python3 hello.py" in your terminal.

# docs.python org/3/library/functions.html
# print(*objects, sep='', end='\n', file=sys.stdout, flush=False)



name = input("What's your name?\n")  # Prompt the user for their name

print(f"Hello, {name}!")

surname = input("What's your surname?\n")  # Prompt the user for their surname
print("Nice to meet you", surname)

age = input("How old are you?\n")  # Prompt the user for their age
print("You are " + age)
