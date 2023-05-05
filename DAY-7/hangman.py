import random
import hangman_words
import hangman_arts

end_of_game = False

# we get a random word form a list
chosen_word = random.choice(hangman_words.word_list)
# get a length of chosen_word
word_length = len(chosen_word)

# Set 'lives' to equal 6.
lives = 6
# printing the logo
print(hangman_arts.logo)

# Create blanks and add "_" at all position
display = []
for _ in range(word_length):
    display += "_"
# start the game
# end_of_game=false,so it indicates true
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    # checking you again you type the same letter or not
    if guess in display:
        print(f"you already guess the letter '{guess}'")

    if guess not in display:
        print(f"you guessed a particular letter '{guess}' that is not in word ,you lose a life")

    # Check guessed letter
    for position in range(word_length):
        if chosen_word[position] == guess:
            display[position] = guess

    # Then reduce 'lives' by 1.
    # If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        lives = lives - 1
        if lives == 0:
            end_of_game = True
            print("You lose the game.")

    # Join all the elements in the list and turn it into a String.
    # print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_arts.stages[lives])
#     answer
print(f' the solution is {chosen_word}.')
