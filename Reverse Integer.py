# Write a program that takes an integer as input and returns an integer with reversed digit ordering.

integer = int(input("Enter a number: "))

strInteger = str(integer)

if strInteger[0] == "-":
    reversed = strInteger[::-1]
    reversed = "-" + reversed[:-1]
else:
    reversed = strInteger[::-1]

print(int(reversed))
