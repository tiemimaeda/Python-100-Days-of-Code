import random
import hangman_art
import hangman_word

print(hangman_art.logo)

lives = 6

chosen_word = random.choice(hangman_word.word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for posistion in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    user_guess = input("Guess a letter: ").lower()

    display = ""

    if user_guess in correct_letters:
        print(f"You've already guessed {user_guess}")

    for letter in chosen_word:
        if letter == user_guess:
            display += letter
            correct_letters.append(user_guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if user_guess not in chosen_word:
        lives -= 1
        print(f"You guessed {user_guess}, that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True
            print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(hangman_art.stages[lives])