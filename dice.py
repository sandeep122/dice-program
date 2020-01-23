my_value=0
total=0
third_value=0
fourth_value=0
snake_bite=[10,33,24,18]
steps=[11,17,22]
won=40
import random
while total<=won and my_value<=won and third_value<=won:
    a=input("FOR THROWING DICE JUST WRITE 't' FOR 1ST USER:")
    if a=='t':
        choice=random.choice(range(1,7))
        print("first user dice value is:",choice)
        total=choice+total
        if total in steps:
            total=total+10
            print("CONGRATES U GET A STAIRS")
        if total in snake_bite:
            total=total-10
            print("snake is bite you")
        print("the current place of first user is",total)
    else:
        print("type write place")
    b=input("FOR THROWING DICE JUST WRITE 't' FOR 2ND USER:")
    if b=='t':
        my_num=random.choice(range(1,7))
        print("second user dice value is ",my_num)
        my_value=my_num+my_value
        if my_value in steps:
            my_value=my_value+10
            print("CONGRATES U GET A STAIRS")
        if my_value in snake_bite:
            my_value=10-my_value
            print("snake is bite you")
        print("the current value of second user is",my_value)
    else:
        print("type write word")
    c=input("FOR THROWING DICE JUST WRITE 't' FOR 3RD USER:")
    if c=='t':
        third_num=random.choice(range(1,7))
        print("third user number is",third_num)
        third_value=third_value+third_num
        if third_value in steps:
            third_value=third_value+10
            print("CONGRATES U GET A STAIRS")
        if third_num in snake_bite:
            third_num=10-third_num
            print("snake is bite you")
        print("the current value for third user is:",third_value)
    else:
        print("print write input")
    d=input("FOR THROWING DICE JUST WRITE 't' FOR 4th USER:")
    if d=='t':
        fourth_num=random.choice(range(1,7))
        print("the current value of third user is",fourth_num)
        fourth_value=fourth_value+fourth_num
        if fourth_value in steps:
            fourth_value=fourth_value+10
            print("CONGRATES U GET A STAIRS")
        if fourth_value in snake_bite:
            fourth_num=10-fourth_num
            print("snake is bite you")
        print("the current position of fourth user:",fourth_value)
    else:
        print("type write input")
if total>=won:
    print("first user is won")
elif(third_value>=won):
    print("third user is won")
elif(my_value>=won):
    print("second user is won")
elif(fourth_value>=won):
    print("fourth user is won")
