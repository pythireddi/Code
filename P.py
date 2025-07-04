import random

def guess_game():
    number = random.randint(1, 10)
    tries = 3
    print("🎯 Guess the number between 1 and 10. You have 3 tries!")

    while tries > 0:
        guess = input("Enter your guess: ")

        if not guess.isdigit():
            print("❌ Please enter a valid number.")
            continue

        guess = int(guess)
        if guess == number:
            print("✅ Correct! You guessed it! 🎉")
            break
        else:
            tries -= 1
            hint = "Too low!" if guess < number else "Too high!"
            print(f"❌ {hint} Tries left: {tries}")

    else:
        print(f"💥 Game Over! The number was {number}.")

if __name__ == "__main__":
    guess_game()
