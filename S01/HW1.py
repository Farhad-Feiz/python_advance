# 1) input a low boundary
# 2) input high boundary
# 3) random => [a , b]
# 4) loop => condition => guess_count = 5 times => feedback

import random

try:
    a = int(input("Please Enter a low value : "))
    b = int(input("Please enter a high value : "))
except:
    print("Please enter a valid number")

r = random.randint(a, b)

guess_count = 5
while guess_count > 0:

    try:
        new_guess = input(f"you have {guess_count} chances*** Please enter a new number : \n ")
        new_guess = int(new_guess)
        if new_guess == r:
                print("Your number is correct")
                break
        elif new_guess < r: 
            print("Your number is less ")
        else:
            print("Your number is greater ")
        guess_count-=1
    except:
        print("Please enter a valid number")

    