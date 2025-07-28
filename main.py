import random
l=[1,2,3]
comp=random.choice(l)
dic={
    "snake":1,
    "water":2,
    "gun":3
}
revdict={
    1:"snake",
    2:"water",
    3:"gun"
}
youstr=input("enter amongst snake,water and gun:")
you=dic[youstr]
print(f"you chose {youstr}")
print(f"computer chose {revdict[comp]}")
if(comp==you):
    print("DRAW")
else:
    if(comp==1 and you==2):
        print("YOU LOOSE")
    elif(comp==1 and you==3):
        print("YOU WIN")
    elif(comp==2 and you==1):
        print("YOU WIN")
    elif(comp==2 and you==3):
        print("YOU LOOSE")
    elif(comp==3 and you==1):
        print("YOU LOOSE")
    elif(comp==3 and you==2):
        print("YOU WIN")
    else:
        print("Something went wrong")
        print("Play again")

input("Press enter to exit the game")