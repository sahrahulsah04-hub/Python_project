import random
num = random.randint(1,100)

tries = 0 
while True:
    guessed = int(input("guess the number between 1 - 100 : "))
    tries +=1
    if guessed == num:
        print(f"congratulations  you found the numberin {tries} tries")
        break
    elif guessed > num:
        print("sorry you need to go lower\n")

    elif guessed < num:
        print("sorry you need to go to a little upper")
 
    

           