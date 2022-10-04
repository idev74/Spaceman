import random

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.

    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.

    Parameters:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns:
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    word = ''
    word_is_guessed = False
    for i in range(len(secret_word)):
        if secret_word[i] in letters_guessed:
            word += secret_word[i]
            if word == secret_word:
                word_is_guessed = True
    return word_is_guessed

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.

    Parameters: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet

    output_line = ''
    for i in range(len(secret_word)): 
        if secret_word[i] in letters_guessed : 
            output_line += f'{secret_word[i]} ' 
        else: output_line += '_ ' 
    return output_line

def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word

    Parameters:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word

    Returns:
        bool: True if the guess is in the secret_word, False otherwise

    '''
    #TODO: check if the letter guess is in the secret word
    if guess in secret_word:
        return True
    else:
        return False


def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.

    Parameters:
      secret_word (string): the secret word to guess.

    '''
    #TODO: show the player information about the game according to the project spec

    print(f'Get ready to blast off! Welcome to spaceman. \nYour job is to guess the secret word with:\n{len(secret_word)} letters')
    #TODO: Ask the player to guess one letter per round and check that it is only one letter
    game = True
    letters_guessed = []
    incorrect_guesses = []
    tries = 0;
    while game is True:
        get_guessed_word(secret_word, letters_guessed)
        guess = input('Enter a letter: ')
        if len(guess) != 1:
            print('Please guess one letter.')
            game = True
        if is_guess_in_word(guess, secret_word) is True:
            letters_guessed.append(guess)
            print('That letter is in the secret word!')
        else:
            print('Unfortunately, that letter is not in the word.')
            incorrect_guesses.append(guess)
            tries += 1
        print(get_guessed_word(secret_word, letters_guessed))
        print(f'You have failed {tries} times')
        print(f'You have incorrectly guessed: {incorrect_guesses}')
        print(f'You have correctly guessed: {letters_guessed}')
        if is_word_guessed(secret_word, letters_guessed) is True or tries == 7:
            if tries == 7:
                print(f'Sorry! You did not guess the word. The word was {secret_word}.')
                game = False
            else:
                print('Congrats, you guessed it!')
                game = False


#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)
