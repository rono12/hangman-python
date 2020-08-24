

HANGMAN_ASCII_ART = """
    _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_  \\
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |
                       |___/
"""

HANGMAN_PHOTOS = {
    1:
    """
x-------x
""",
    2:
    """
x-------x
|
|
|
|
|
""",
    3:
    """
x-------x
|       |
|       0
|
|
|
""",
    4:
    """
x-------x
|       |
|       0
|       |
|
|
""",
    5:
    """
x-------x
|       |
|       0
|      /|\\
|
|
""",
    6:
    """
x-------x
|       |
|       0
|      /|\\
|      /
|
""",
    7:
    """
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |
    """
}


def main():
    tries = 1
    old_letters_guessed = []
    print(HANGMAN_ASCII_ART)
    user_path = input(
        '\nPlease insert the path for words. \n"words.txt" is the path \n insert here:')
    user_index = input(
        '\nPlease choose a number (any number).\n the number you chose is:\n')
    while not user_index.isnumeric():
        user_index = input('You did not chose a number, try again:\n')
    if user_index.isnumeric():
        user_index = int(user_index)
    secret_word = choose_word(user_path, user_index)
    print('\nThis is the starting situation of the Hangman, try not to fail :)')
    print(HANGMAN_PHOTOS[1])
    while tries < 7:
        if try_update_letter_guessed(secret_word, old_letters_guessed, tries) == True:
            return HANGMAN_PHOTOS[tries]
        if HANGMAN_PHOTOS[tries] == HANGMAN_PHOTOS[7]:
            print(
                'I am sorry but the hangman has completed before you finisehd the word :(\nthe word was ' + secret_word + '.\n')
            user_input = input('Would you like to play again?\ny/n').lower()
            if user_input == 'y':
                main()
            elif user_input == 'n':
                print('Great game, have a nice day :)')
                return
        if check_win(secret_word, old_letters_guessed) == True:
            user_input = input('Would you like to play again?\ny/n').lower()
            if user_input == 'y':
                main()
            elif user_input == 'n':
                print('\nGreat game, have a nice day :)')
                return
        tries = tries + 1
    if tries == 7:
        print('You have used all your tries.\nthe word was ' +
              secret_word + '\nYou lost :(\n')
    user_input = input('Would you like to play again?\ny/n').lower()
    if user_input == 'y':
        main()
    elif user_input == 'n':
        print('Great game, have a nice day :)')
        return


def check_valid_input(guess_a_letter, old_letters_guessed):
    """this function checks if the letter input is valid or not

    Args:
        guess_a_letter ([str]): [the letter the user guesses]
        old_letters_guessed ([list]): [the letters the user has guessed]

    Returns:
        [bool]: [returns boolean condition for the function that updates the letter]
    """
    if(len(guess_a_letter) == 1) and (guess_a_letter not in old_letters_guessed) and (guess_a_letter.isalpha()):
        return True
    elif (len(guess_a_letter) >= 2) or (guess_a_letter in old_letters_guessed) or (not guess_a_letter.isalpha()):
        return False


def try_update_letter_guessed(secret_word, old_letters_guessed, tries):
    """this function gets the valid letter and checks if it has guessed
        already or not.
        also shows the user the letters he has guessed already

    Args:
        guessed_letter ([str]): [the letter the user has guessed]
        old_letters_guessed ([list]): [list of str's letters the user guessed]
    """
    guess_a_letter = input('What is the letter you think of?').lower()
    if guess_a_letter in secret_word:
        if check_valid_input(guess_a_letter, old_letters_guessed) == True:
            old_letters_guessed.append(guess_a_letter)
            print('\nYou are right, the letter is in the word\n')
            show_hidden_word(secret_word, old_letters_guessed)
            return True, secret_word
    elif (guess_a_letter not in secret_word) or (check_valid_input(guess_a_letter, old_letters_guessed) == False):
        old_letters_guessed.append(guess_a_letter)
        joined = '->'.join(old_letters_guessed)
        HANGMAN_PHOTOS[tries] = HANGMAN_PHOTOS[tries + 1]
        print(f"""\nX
{joined}
Letter is incorrect\n
\n
{HANGMAN_PHOTOS[tries]}""")
        return HANGMAN_PHOTOS[tries]


def show_hidden_word(secret_word, old_letters_guessed):
    """this function shows the hidden word according to the letters 
    that the user guesses

    Args:
        secret_word ([str]): [the word the user needs to guess]
        old_letters_guessed ([list]): [the letters the user has guessed]

    Returns:
        [str]: [returns str of the word with underscores and correct letters]
    """
    new_list = []
    underscore = '_ '
    for letter in secret_word:
        if letter in old_letters_guessed:
            new_list.append(letter)
        else:
            new_list.append(underscore)
    str_join = ' '
    secret_word = str_join.join(new_list)
    print(secret_word)
    return secret_word


def check_win(secret_word, old_letters_guessed):
    """this function iterates over the list and checks if the user has 
       guessed all the letters and prints the word with the letters the user guessed
       and underscores if not.
       also return False or True

    Args:
        user_word ([str]): [the word the user has requested]
        old_letters_guessed ([list]): [list of the letters the user guessed]
    """
    new_list = []
    underscore = '_ '
    for letter in secret_word:
        if letter in old_letters_guessed:
            new_list.append(letter)
        else:
            new_list.append(underscore)
        str_join = ' '
        new_list_str = str_join.join(new_list)
    if not underscore in new_list:
        print('\nYou are correct!\n You won the game, CONGRATS!!\n')
        return True
    else:
        print('\nnot yet, keep guessing the word\n you on the right way\n')


def choose_word(file_path, index):
    """this function gets from the path the secret word that goung through 
    the whole game.

    Args:
        file_path ([str]): [this is the path to the words]
        index ([int]): [the index indicates to the position of the word]

    Returns:
        [type]: [description]
    """
    with open(file_path, 'r') as r:
        my_list = list(r.read().split(' '))
        new_index = index % len(my_list)
    secret_word = my_list[new_index]
    return secret_word


if __name__ == "__main__":
    main()
