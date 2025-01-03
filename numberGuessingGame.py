from random import randint
def check_guess(Guess_count):
    user_guess = input(f"Tries left {Guess_count}  Guess: ")
    try:
        if Guess_count == 1:
            print("Gameover")
            return
            
        elif int(user_guess) < number_to_guess:
            print("The number is higher")
            guess = check_guess(Guess_count-1)
        elif int(user_guess) > number_to_guess:
            print("The number is lower")
            guess = check_guess(Guess_count-1)
        else:
             int(user_guess) == number_to_guess
             print("You guessed it")
             return
        
    except ValueError as e:
        print("Please use a valid number")
        guess = check_guess()



print("Guess the number in the range from 1 t 10.")
number_to_guess = randint(1,10)
check_user_guess = check_guess(5)

