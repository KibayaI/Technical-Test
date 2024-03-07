"""Write a program that accepts a string as input, capitalizes the first letter of each word int he string,
    and then returns the result string."""

normal = input("Enter your string: ")

capitalized = normal.capitalize()
lisp = []

for i in range(len(capitalized)):
    if capitalized[i-1].isspace():
        lisp.append(capitalized[i].capitalize())
    else:
        lisp.append(capitalized[i])


print(''.join(lisp))
