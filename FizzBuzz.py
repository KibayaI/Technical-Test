"""Write a program that prints the numbers from 1 to 100. For multiples of 3, print"Fizz";
    for multiples of 5, print "Buzz";
    and for numbers that are multiples of both 3 and 5, print "FizzBuzz"."""

for number in range(101):
    if number % 3 == 0 and number % 5 != 0:
        print("Fizz")
    elif number % 5 == 0 and number % 3 != 0:
        print("Buzz")
    elif number % 5 == 0 and number % 3 == 0:
        print("FizzBuzz")
    else:
        print(number)

