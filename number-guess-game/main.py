
import random


class NumberGuessingGame:

    LEVELS = {
        "1": ("EASY", 50, 10),
        "2": ("MEDIUM", 100, 8),
        "3": ("HARD", 200, 5)
    }

    def __init__(self):
        self.look()
        print("\tNUMBER GUESSING GAME")
        self.look()

    def look(self, a="=", b=40):
        print(a * b)

    def menu(self):
        while True:
            self.look("*", 10)
            print("MENU")
            self.look("*", 10)

            print("1. EASY LEVEL")
            print("2. MEDIUM LEVEL")
            print("3. HARD LEVEL")
            print("0. EXIT")

            level = input("ENTER YOUR LEVEL: ")

            if level == "0":
                return None

            if level in self.LEVELS:
                return self.LEVELS[level]

            print("INVALID CHOICE! TRY AGAIN.")

    def get_guess(self, upper_range):
        while True:
            try:
                guess = int(input("ENTER YOUR GUESS: "))

                if 1 <= guess <= upper_range:
                    return guess

                print(f"ENTER NUMBER BETWEEN 1 AND {upper_range}")

            except ValueError:
                print("PLEASE ENTER A VALID INTEGER!")

    def play_game(self, level, upper_range, attempts):

        secret_number = random.randint(1, upper_range)

        print(f"\nLEVEL: {level}")
        print(f"GUESS NUMBER BETWEEN 1 AND {upper_range}")
        print(f"YOU HAVE {attempts} ATTEMPTS")

        for attempt in range(1, attempts + 1):

            print(f"\nATTEMPT {attempt}/{attempts}")

            guess = self.get_guess(upper_range)

            if guess == secret_number:
                print("\nCONGRATULATIONS! YOU WON!")
                print("YOU GUESSED THE CORRECT NUMBER.")
                return

            elif guess < secret_number:
                print("TOO LOW! TRY A HIGHER NUMBER.")

            else:
                print("TOO HIGH! TRY A LOWER NUMBER.")

            print("ATTEMPTS LEFT:", attempts - attempt)

        print("\nGAME OVER!")
        print("THE CORRECT NUMBER WAS:", secret_number)

    def start(self):

        while True:

            selected_level = self.menu()

            if selected_level is None:
                print("THANK YOU FOR PLAYING!")
                break

            level, upper_range, attempts = selected_level

            self.play_game(level, upper_range, attempts)

            self.look()

            play_again = input("DO YOU WANT TO PLAY AGAIN? (Y/N): ").lower()

            if play_again != "y":
                print("THANK YOU FOR PLAYING!")
                break


game = NumberGuessingGame()
game.start()
