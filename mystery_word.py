
# This is the third version I wrote from the ground up and it's beginning to make a lot more sense, albeit slowly.

import random

quit = False
while not quit:
    user_input = input("Enter 'Y' if you want to play a crazy game,")
    if user_input == "Y":
        quit = True
        print("Let's do this!")
    else:
        print("You are wack.", user_input)


def open_text_file(file):
    """
    Opens file of words, makes a list and removes  unnecessary characters
    """
    text_file = open(file, 'r')
    open_file = text_file.readlines()
    open_file = [word.replace('\n', '').lower() for word in open_file]
    return open_file


def difficulty_level_list(word_list, level):
    """
    Takes words in txt file, grabs them in varying lengths
    """
    difficulty_level_word_list = []

    for word in word_list:
        if level == "easy":
            if len(word) == 3 or len(word) == 4:
                difficulty_level_word_list.append(word)
        if level == "medium":
            if len(word) == 5 or len(word) == 6:
                difficulty_level_word_list.append(word)
        if level == "hard":
            if len(word) > 7:
                difficulty_level_word_list.append(word)

    print(difficulty_level_word_list)


def user_level_choice():
    """
    Prompts user to type level of difficulty, passes choice into difficulty
    level list function.
    """

    user_input = input(
        "Choose easy medium or hard only use lower-case characters. ")

    difficulty_level_list(open_text_file("words.txt"), user_input)


user_level_choice()

# Currently stuck on writing a function that will return a random word from my difficulty level list. But I think
# I know where to go from here. But once again, I'm moving very slowly.
