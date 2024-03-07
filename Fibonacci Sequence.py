# Write a program to generate the Fibonacci sequence up to 100.

def fibo_seq(limit):
    if limit <= 1:
        return limit
    else:
        return fibo_seq(limit - 1) + fibo_seq(limit - 2)


i = True
target = 0

while i:
    if fibo_seq(target) <= 100:
        print(fibo_seq(target))
        target += 1
    else:
        i = False
