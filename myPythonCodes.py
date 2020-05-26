
"""Program to print what year you will turn 100 """

from datetime import datetime #to get second, minute, hour, day,month,  year. included from datetime to get the attribute "now"

print("Welcome!! I can reveal the year you will turn 100")
name = input("What is your name?: ")
age = int(input("How old are you?: "))
year = datetime.now().year

age_100 = 100 - age 
year = year + age_100

print("Hello " +name+ ", you are turning 100 in year", year)

print()

#**********************************************************************************

"""Program to print if number is even or odd """

print("Hello, I can determine if your number is odd, even, or multiple of 4")

num = int(input("Enter any number of your choice: "))
if num % 2 == 0:
    print(num, "is an even number")
    if num % 4 == 0:
        print(num, "is also a multiple of 4")
else:
    print(num, "is an odd number")

    
#**********************************************************************************
print()
""" Program to print numbers less than 5 in a list"""
print("Hello, I will print numbers less than 5 in your list")

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
    if i < 5:
        print(i)

#user can enter their own one digit list
print()

num = list(input("Enter your numbers not separated by comma: "))
list1 = []
for i in num:
    a = int(i)
    list1.append(a)
print("Here are the numbers you enetered: ",list1)

print()
print("Here are the numbers less than 5 in your list:")


for i in list1:
    if i < 5:
        print(i, end = " ")

#******************************************************************************
print()
"""Program to print divisors """

print("Hello, I am a program to print the divisors of any number you enter")
num = int(input("enter your number: "))
num2 = num + 1
for i in range(1, num2):
    if num % i == 0:
        print(i)


#or

num = int(input("enter your number: "))
divisors =[]
num2 = num + 1
for i in range(1, num2):
    if num % i == 0:
        divisors.append(i)
print(divisors)


#********************************************************************************
print()
"""Program using try/except"""
print("Hello, I'm a program to ensure you use the right input")
while True:
    try:
        age = int(input("Enter you age: "))
        if age >= 18:
            print("You are eligible for admission!")
        else:
            print("You are not eligible for admission")
        break
            
    except ValueError:
        print("Please enter your age as a whole number")


        
#***********************************************************************************

print()
"""Program to print common numbers in multiple lists"""
print("Hello, I will print out the common numbers in two lists without duplicates")
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = []
for i in a:
    if i in b:
        if i not in c:
            c.append(i)
print(c)


#using random
    
import random
a = range(1, random.randint(1,30))

b = range(1, random.randint(1,40))
c = []
for i in a:
    if i in b:
        if i not in c:
            c.append(i)
print(a)
print(b)
print(c)

#**********************************************************************************

age_range = 12
age = int(input("how old are you?: "))


if age >= age_range:
    hw = input("have you done your homework?: ")
    hw = hw.casefold()
    
    if hw == "yes":
        print("Awesome! You can now play fortnite")
    else:
        print("You have to complete your homework before you can play fortnite")
else:
    print("You are not allowed to play fortnite yet")


#*************************************************************************************
    # factorial is 1.2.3...n, -ve no fact, 0 is 1
# 4.3.2

num = int(input("Enter you number to get the factorial: "))

i = 1
result = 1


if num == 0:
    print("factorial is 1")
elif num < 0:
    print("no factorial for -ve numbers")
else:
    for i in range(i, num+1):
        result = result * i
    print(result)




# using while

while i <= num:
    result = result * i
    i += 1

print(result)

#*******************************************************************************

print("Welcome to Rock, Paper, Scissors Game")
print()
print("Here are the Rules:")
print("Rock crushes Scissors")
print()
print("Paper covers Rock")
print()
print("Scissors cuts Paper")
print()

import random

list1 = ["Rock", "Paper", "Scissors"]



scores_computer = 0

scores_human = 0

num_of_rounds = 1

while num_of_rounds <= 6:
    game = list1[random.randint(0,2)]
    pick = input("Enter your pick! Rock, Paper, Scissors: ")

    if pick == game:
        print("you both chose", game, "it is a tie!")
    elif pick == "Rock" and game == "Scissors":
        print("Rock crushes Scissors, you win")
        num_of_rounds += 1
        scores_human += 1
    elif pick == "Rock" and game == "Paper":
        print("Paper covers Rock, computer wins")
        num_of_rounds += 1
        scores_computer += 1

    
    elif pick == "Scissors" and game == "Rock":
        print("Rock crushes Scissors, computer wins")
        num_of_rounds += 1
        scores_computer += 1

    elif pick == "Scissors" and game == "Paper":
        print("Scissors cuts Paper, you win")
        num_of_rounds += 1
        scores_human += 1
        
    elif pick == "Paper" and game == "Rock":
        print("Paper covers Rock, you win")
        num_of_rounds += 1
        scores_human += 1
    elif pick == "Paper" and game == "Scissors":
        print("Scissors cuts Paper, computer wins")
        num_of_rounds += 1
        scores_computer += 1
    else:
        print("invalid pick")
if scores_human > scores_computer:
    print("after", num_of_rounds-1, "rounds, you won", scores_human, "-", scores_computer)
elif scores_human < scores_computer:
    print("after", num_of_rounds-1, "rounds, computer won", scores_computer, "-", scores_human)
else:
    print("after", num_of_rounds-1, "rounds, it was a tie", scores_computer, "-", scores_human)


#*******************************************************************************

"""List Comprehension"""
list1= [1,2,3,4,5,6,7,8,9,10]
list2 = []
for i in list1:
    list2.append(i**2)
print(list2)


list2 = [i**3 for i in list1 if i % 2 == 1]
