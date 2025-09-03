############# Hangman Program

import random as rnd

words = ("Faze Clan",
         "Natus Vincere",
         "Virtus Pro",
         "Spirit",
         "Furia",
         "Mouz Esports",
         "Falcons",
         "Vitality",
         "Fnatic",
         "Gamerlegion",
         "Cloud9",
         "BCG Esports",
         "Liquid",
         "ENCE",
         "BIG",
         "3DMAX")


hangman_art = {
    0: ("   ",
        "   ",
        "   "),
    1: (" o ",
        "   ",
        "   "),
    2: (" o ",
        " | ",
        "   "),
    3: (" o ",
        "/| ",
        "   "),
    4: (" o ",
        "/|\\ ",
        "   "),
    5: (" o ",
        "/|\\ ",
        "/   "),
    6: (" o ",
        "/|\\ ",
        "/  \\ ")
}


def display_man(wrong_guesses):
    print("****************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("****************")


def display_hint(hint):
    print(" ".join(hint))


def main():
    answer = rnd.choice(words).lower()
    hint = [" " if c == " " else "_" for c in answer]
    wrong_guesses = 0
    guessed_letters = set()

    print("Welcome to Hangman! ")
    print("Guess the Esports Team!")

    while True:
        display_man(wrong_guesses)
        display_hint(hint)

        guess = input("Guess a letter: ").lower()


        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for index, letter in enumerate(answer):
                if letter == guess:
                    hint[index] = guess
            print(f" Good guess: {guess}")
        else:
            wrong_guesses += 1
            print(f" Wrong guess: {guess}")


        if "_" not in hint:
            print("\n Congratulations! You guessed it:")
            print("Answer:", answer.title())
            break


        if wrong_guesses == 6:
            display_man(wrong_guesses)
            print("\n Game Over! The correct answer was:", answer.title())
            break


if __name__ == '__main__':
    main()
