# Problem Set 2, hangman.py
# Name: Dylan Walker 
# Collaborators: None
# Time spent: 6:00
# Late Days Used: 1

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    '''
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    secret_sorted = sorted(list(secret_word))
    letters_sorted = sorted(letters_guessed)
    word = []
    for secret_count in range(len(secret_sorted)):
        for letters_count in range(len(letters_sorted)):
            if letters_sorted[letters_count] == secret_sorted[secret_count]:
                word.append(letters_sorted[letters_count])
    if secret_sorted == sorted(word):
        return True
    else:
        return False

def get_word_progress(secret_word, letters_guessed):
    '''
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and underscore (_) that represents
        which letters in secret_word have not been guessed so far
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    word_progress = list(secret_word)
    word1 = []
    yesno = 0
    for count2 in range(len(word_progress)):
        for count1 in range(len(letters_guessed)):
            if letters_guessed[count1] == word_progress[count2]:
                word1.append(word_progress[count2])
                yesno = 0
                break
            elif letters_guessed[count1] != word_progress[count2]:
                yesno = 1
        if yesno == 1:
            word1.append('_')
    if len(word1) == 0:
        for count3 in range(len(secret_word)):
            word1.append('_')
    word_progress_complete = ''.join(word1)
    return word_progress_complete

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    for count3 in range(len(letters_guessed)):
        for count4 in range(len(alphabet)):
            if letters_guessed[count3] == alphabet[count4]:
                alphabet[count4] = ''
    alphabet_complete = ''.join(alphabet)
    return alphabet_complete

def help(secret_word, h):
    secret_list2 = list(secret_word)
    letters = h
    choose_from_list = []
    for count1 in range(len(secret_word)):
        for count2 in range(len(letters)):
            if secret_list2[count1] == letters[count2]:
                choose_from_list.append(secret_list2[count1])
    choose_from = ''.join(choose_from_list)
    '''if len(choose_from) == 0:
        new = random.randint(0, len(choose_from))
        revealed_letter = choose_from[new]
        print
        return revealed_letter
    else:'''
    new = random.randint(0, len(choose_from)-1)
    revealed_letter = choose_from[new]
    return revealed_letter

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter or help character '?'

    * If the user inputs an incorrect letter, then the user loses ONE guess

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol ?, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print ("Welcome to Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    guesses = 10
    letters_guessed = []
    while guesses >= 1:
        print ("------------")
        print ("You currently have", guesses, "guesses left.")
        if has_player_won(secret_word, letters_guessed) == True:
            print ("Congratulations, you won!")
            print ("Your total score for this game is: ", 4 * guesses + 3 * len(secret_word))
            break
        print ("Available letters:", get_available_letters(letters_guessed))
        guess = str(input("Please guess a letter: "))
        guess.lower()
        if guess == "?":
            if guesses <= 3:
                print ("Oops! Not enough guesses left:", get_word_progress(secret_word, letters_guessed))
            else:
                revealed = help(secret_word, get_available_letters(letters_guessed))
                print ("Letter revealed:", revealed)
                letters_guessed.append(revealed)
                print (get_word_progress(secret_word, letters_guessed))
                guesses -= 3
        elif len(guess) > 1:
            print ("Oops! That is not a valid letter. Please input a letter from the alphabet:", get_word_progress(secret_word, letters_guessed))
        elif guess.isalpha() == False:
            print ("Oops! That is not a valid letter. Please input a letter from the alphabet:", get_word_progress(secret_word, letters_guessed))
        elif list(get_available_letters(letters_guessed)).count(guess) == 0:
            print (guess.count(get_available_letters(letters_guessed)))
            print ("Oops! You already guessed that letter:", get_word_progress(secret_word, letters_guessed))
        elif list(secret_word).count(guess) == 0:
            letters_guessed.append(guess)
            print("Oops! That letter is not in my word:", get_word_progress(secret_word, letters_guessed))
            guesses -= 1
        else:
            letters_guessed.append(guess)
            print ("Good guess:", get_word_progress(secret_word, letters_guessed))    
    if guesses == 0:
        print ("------------")
        print ("Sorry, you ran out of guesses. The word was", secret_word,".")
        
# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following two lines.
    secret_word = choose_word(wordlist)
    hangman(secret_word)

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.
    pass
