# Write a program that takes an integer as input and returs true if the input is a power of two.

number = int(input("Enter a number: "))


def power2(number):
    if number / 2 == 1:
        return True
    else:
        if number % 2 == 0:
            number = power2(number / 2)
            return number
        else:
            return False


print(power2(number))
