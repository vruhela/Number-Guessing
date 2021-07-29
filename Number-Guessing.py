number=50
attempts=0

while True:
    attempts+=1
    guess=int(input("Guess the number: "))
    if guess<number:
        print("Your guess was too low!!")
    elif guess>number:
        print("Your guess was too high!!")
    else:
        print("Congratulations, you guessed the number right. It was",'number')