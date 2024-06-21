import random

if __name__ == "__main__":

    guess = -1

    answer = random.randint(0, 5) # 0, 1, 2, 3, 4, 5
    # print(answer)

    while(guess != answer):
        guess = input("Guess the number: ")
        guess = int(guess)

        if(guess < answer):
            print("Too low!")
        elif(guess > answer):
            print("Too high!")
        else:
            print("You guessed correctly!")

