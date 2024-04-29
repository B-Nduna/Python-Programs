import random

def guess_the_number():
    print("Welcome to Guess the Number!")
    print("I have picked a number between 1 and 100. Try to guess it!")
    
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            guess = int(input("\nEnter your guess: "))
            attempts += 1
            
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue
            
            if guess < secret_number:
                print("Too low! Try guessing higher.")
            elif guess > secret_number:
                print("Too high! Try guessing lower.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    guess_the_number()
