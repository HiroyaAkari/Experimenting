import random

def main():
    target = random.randint(1, 100)
    tries = 0

    print("I'm thinking of a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        tries += 1

        if guess < target:
            print("Higher!")
        elif guess > target:
            print("Lower!")
        else:
            print(f"Correct! You got it in {tries} {'try' if tries == 1 else 'tries'}.")
            break

if __name__ == "__main__":
    main()