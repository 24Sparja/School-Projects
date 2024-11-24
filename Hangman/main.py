## James Sparks
## November 24, 2024
## Project 2 - Hangman Game
import random
import os
def clear_console():
    os.system('cls')
def get_word():
    word_list = []
    with open('hangman_words.txt', 'r') as hangman_words:
        for line in hangman_words:
            new_word = hangman_words.readline()
            fixed_word = new_word.replace('\n', '')
            word_list.append(fixed_word)
    list_len = len(word_list)
    rand_num = random.randrange(0,list_len)
    chosen_word = word_list[rand_num]
    return(chosen_word)
        
def HM():   
    playing = True
    print('Welcome to Hangman.')
    print()
    print('A word will be chosen at random, guess the letters in the word until you finish the word.')
    print('The game will end if you guess 10 incorrect letters.')
    print()
    start_playing = input('Begin? (y/n): ')
    while start_playing != 'y' and start_playing != 'n':
        start_playing = input('y or n: ') 
    if start_playing == 'n':
        print('Thank you for not playing.')
        return
    print()
    while playing:
        
    #Set Starting values for variables
        hangWord = get_word()
        split_word = []
        for letter in hangWord:
            split_word.append(letter)
        guesses_left = 10

        used_letters = []
        hidden_word = []
        for letter in range(len(split_word)):
            hidden_word.append('-')

        while (hidden_word != split_word) and (guesses_left != 0):
    #Show current stats
            print(f'Tries left: {guesses_left}')
            print(f'Word: ' ,end='')
            for letter in hidden_word:
                print(letter, end='')
            print()
            used_letters.sort()
            if len(used_letters) != 0:
                if len(used_letters) == 1:
                    print(f'\nGuessed letter: {used_letters[0]}')

                else:
                    print('\nGuessed letters: ', end='')
                    for letter in used_letters:
                        print(letter, end='')
                    print()

            print()        
            player_guess = input('Guess a letter: ')     
  
            try: #trigger ValueError to know guess contains a letter

                while True:                    
                    if (player_guess not in used_letters) and (len(player_guess) == 1) and (player_guess.isalnum() == True):
                        int(player_guess)
                        print('A letter: ', end='')
                    elif player_guess in used_letters:
                        print('Already guessed, guess a new letter: ', end='')
                    elif len(player_guess) > 1:
                        print('A single letter: ', end='')
                    elif player_guess.isalnum() == False:
                        print('A letter: ', end='')
                    player_guess = input()

            except ValueError:
                used_letters.append(player_guess)
            pos_letter = int(-1) #to start increment at index 0
            player_guess_in_word = 0

    #compare current guessed letter to the real word
            for letter in split_word:
                pos_letter += 1
                if letter == player_guess:
                    hidden_word[pos_letter] = player_guess
                    player_guess_in_word += 1
            if player_guess_in_word == 1:
                print(f'There is 1 \'{player_guess}\' in the word.\n')
            elif player_guess_in_word > 1:
                print(f'There are {player_guess_in_word} \'{player_guess}\'s in the word.\n')
            else:
                print(f'There are no {player_guess}\'s in the word.\n')
                guesses_left -= 1

    #End the game when word is finished or too many incorrect guesses
        if guesses_left == 0:
            print(f'Out of tries, the word was {hangWord}.')
            print()
            keep_playing = input('Would you like to try again? (y/n): ')
        else: 
            print(f'Tries left: {guesses_left}')
            print(f'Word: {hangWord}')
            print()
            keep_playing = input('You guessed the word, would you like to play again? (y/n): ')
        while keep_playing != 'y' and keep_playing != 'n':
            keep_playing = input('y or n: ') 
        if keep_playing == 'n':
            playing = False
        print()
    print('Thank you for playing.')

## Place function call to automatically run your code when accessing your script file.
clear_console()
HM()