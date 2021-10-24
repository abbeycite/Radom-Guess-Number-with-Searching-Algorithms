import random
def guess_random_number(tries, start, stop):
    random_number = random.randint(start,stop)
    while tries != 0:
        print("The number of tries remaining is:", tries)
        guess_number = int(input(f"Input a guess number between {start} and {stop}:"))
        if random_number == guess_number:
            print("Your guessed number is:", guess_number)
            print("The random number you compared with was:", random_number)
            print("You guessed correctly, Success!!!")
            return
        elif guess_number < random_number:
            print("Guess higher!")
        elif guess_number > random_number:
            print("Guess lower!")
        tries -=1
    print("Your guesses do not match")

def guess_random_num_linear(tries, start, stop):
    random_number = random.randint(start,stop)
    print("The number of tries remaining is:", tries)
    print(f"The random number you compared with was: {random_number}")
    for x in range(start, stop+ 1):
        if x == random_number:
            print(f"The guessed number by the computer is:: {x}")
            print("The numbers matches, success!!!")
            return
        elif x == 0:
            print(f"The guessed number by the computer is:: {x}")
            print("The computer made a wrong guess, failed!!!")
            return
        else:
            print(f"The computer has guessed: {x}")
            print("Your guesses do not match")
        tries -=1

def guess_random_num_binary(tries, start, stop):
    y = random.randint(start,stop)
    #print("The number of tries remaining is:", tries)
    print(f"The random number you compared with was: {y}")
    low = start
    high = stop

    l = list(range(stop))

    while low <= high:
        mid = (start + stop)//2
        if y == l[len(l)//2]:
            print(f"The search for {y} is correct and completed")
            return
        elif l[mid]> y:
            print(f"Please guess a lower number {l[mid]}")
            high = mid - 1
        else:
            return mid
            low = mid +1
    print(f"The search for the {y} was unsuccessful, failed!!!")



    
        



"""test driver code for task1 """
#guess_random_number(5, 0, 10)
"""test driver code for task2 """
#guess_random_num_linear(5, 0, 10)
"""test driver code for task3 """
guess_random_num_binary(5, 0, 10) 
