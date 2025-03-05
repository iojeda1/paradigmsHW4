# Isabel Ojeda
# HW4 Q2

import random

class Wordle: 
    def __init__(self):
        # get random word
        with open("words.txt", "r") as file:
            lines = file.readlines()
            self.words = [l.rstrip('\n').lower() for l in lines]
        
        self. word = random.choice(self.words)
        self.tries = 0
        self.good_letters = []
        self.bad_letters = []
        self.correct_letters = [""] * 5

        # write random word in answer file 
        with open("answer.txt", "w") as file2:
            file2.write(self.word)

game = Wordle() # game object
# get user input 
while (game.tries < 6): 
    guess = input("Enter a 5 letter word: ").strip().lower()
    if (len(guess) != 5):
        print("The word needs to be 5 letters. Try again. ")
        continue
    if (guess not in game.words):
        print("Invalid word. Try again.")
        continue 
    
    game.tries += 1
    # guessed correct word
    if (guess == game.word):
        print(f"Congratulations, you correctly identified the word after {game.tries} attempts")
        break
    # implement good, bad, and correct words 
    for i in guess:
        if (i in game.word):
            if (i not in game.good_letters): # no repeats
                game.good_letters.append(i) 
        elif (i not in game.bad_letters): 
                game.bad_letters.append(i)
    for j in range(5):
        if guess[j] == game.word[j]:
            game.correct_letters[j] = guess[j]

    print(f"Good letters: {game.good_letters}")
    print(f"Bad letters: {game.bad_letters}")
    print(f"Correct letters: {game.correct_letters}")

else: 
    print(f"The answer is {game.word}. You did not correctly guess it within 6 tries.")