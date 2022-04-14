# -----------------------------------------------
# Author: Nick V.
# All in one Convert & Sort Tool
# Version: 1.2
# creation date: 27.03.2022
# -----------------------------------------------
# 02.04.2022 Fixed \n Bug in the Convert Func
# -----------------------------------------------

# For checking "if path exists"
import os

# Setting the Checkpoint for my Menu on True
global file_location

check = True


# Main function and Menu
def main_menu():
    # Menu Loop
    while True:
        # Printing the Menu
        print("""(1) Converting Menu 
(2) Counting Menu
(3) Numerating Menu
(4) Split words
(0) Exit""")
        # Input field to insert Choice which Menu user wants
        choice_main_menu = input("Which function you wanna use?: ")

        if choice_main_menu == "1":
            # Calling Menu for converting sentences in List or smth else
            converting_menu()

        elif choice_main_menu == "2":
            # Calling Menu for counting Lists,Letters or words
            counting_menu()

        elif choice_main_menu == "3":
            # Calling Menu for Numerating
            enumerating_menu()

        elif choice_main_menu == "4":
            # Calling Function for separate Words with new seperator
            split_words()

        # Exiting on specific Input the Pgm
        # Option to exit the Pgm
        elif choice_main_menu == "0":
            break
        else:
            print("Wrong or not a valid Option inserted")


# Function to insert the Location of the File
def input_location():
    # Defining DATA global to access everywhere in the Pgm
    global file_location
    # Input to insert the Location of the File
    file_location = input("Insert the raw Location of your File: ")
    # Check with assert os path exists if data is in the Directory
    assert os.path.exists(file_location), "I did not find the file at, " + str(file_location)


# Menu to access the converting functions
def converting_menu():
    # Setting the Checkpoint on False to end the endless loop in the menu above
    check = False
    print("""(1) Read file No List
(2) Read File in a all in One List
(3) Read File in original List  
""")
    # Insert choice in the converting Menu
    choice_converting_menu = input("Which reading Option you wanna choose")

    if choice_converting_menu == "1":
        # Function for read file and give no list
        read_file_no_list()
    elif choice_converting_menu == "2":
        # Function for whole sentence in 1 list
        read_file_to_AiO_list()
    elif choice_converting_menu == "3":
        # Function for converting sentence in an original list
        read_file_to_list()


# Function for read file and give no list
def read_file_no_list():
    # Calling the Function for inserting a File Path
    input_location()
    # Way which doesn't need a file.close
    with open(file_location) as f:
        # Iterating through f
        for value in f:
            # Prints output of f
            print(value)


# Function for whole sentence in 1 list
def read_file_to_AiO_list():
    # Calling the Function for inserting a File Path
    input_location()

    # Way which doesn't need a file.close
    with open(file_location) as f:
        # Referencing a list to lines
        input_of_file = f.readlines()
        # For loop to del the \n from some Editors
        for line in range(len(input_of_file)):
            # del the \n from some Editors
            input_of_file[line] = input_of_file[line].replace('\n', '')
        # Result Output
        print(line)


# Function for converting sentence in an original list
def read_file_to_list():
    # Calling the Function for inserting a File Path
    input_location()
    # Way which doesn't need a file.close
    with open(file_location) as f:
        # Iterating through f
        for line in f:
            # Remove some things from line and reference it to strip_lines
            strip_lines = line.strip()
            # splits a string into a list and reference it to list
            splitted_list = strip_lines.split()
            print(splitted_list)


# Menu to access the counting functions
def counting_menu():
    # Setting the Checkpoint on False to end the endless loop in the menu above
    check = False
    print("""(1) Counting Letters
(2) Counting Words
(3) Count Lists""")

    # Insert choice in the counting Menu
    choice_counting_menu = input("Which reading Option you wanna choose")

    if choice_counting_menu == "1":
        # Function for count letter in File
        count_letter()
    elif choice_counting_menu == "2":
        # Function for count words in File
        count_words()
    elif choice_counting_menu == "3":
        # Function for count lists in file
        count_lists()
    else:
        print("Not a valid Option!")


def count_letter():
    # Calling the Function for inserting a File Path
    input_location()
    # Way which doesn't need a file.close
    with open(file_location) as f:
        number_of_characters = len(file_location)
        print(f"Number of Characters is: {number_of_characters} ")


def count_words():
    # Calling the Function for inserting a File Path
    input_location()
    # Way which doesn't need a file.close
    with open(file_location) as f:
        input_of_file= f.read()
        word_count = input_of_file.split()

        print('Total Words:', len(word_count))


def count_lists():
    # Calling the Function for inserting a File Path
    input_location()
    # Way which doesn't need a file.close
    with open(file_location) as f:
        list_count = len(f.readlines())

    print('The Textfile contains: ', list_count, 'lists.')


#  Menu for navigating through the enumerating menu
def enumerating_menu():
    # Setting the Checkpoint on False to end the endless loop in the menu above
    check = False
    print("""(1) Numerating Words
(2) Numerating Lists""")

    # Insert choice in the enumerating Menu
    choice_enumerating_menu = input("Which reading Option you wanna choose")

    if choice_enumerating_menu == "1":
        # Calling function to enumerate words
        enumerating_words()
    elif choice_enumerating_menu == "2":
        # Calling function to enumerate lists
        enumerate_list()
    else:
        print("Not a valid Option!")


#  Function for numerating single words in a file
def enumerating_words():
    # Calling the Function for inserting a File Path
    input_location()

    # Way which doesn't need a file.close
    with open(file_location, 'r+') as file:
        # Referencing file data with a file read command.
        input_of_file = file.read()
        # Referencing counter and set it to 1 to start at 1
        counter = 1

        # Referencing splits to the var splits to work with it
        splits = input_of_file.split()

        # For loop to iterate over words and enumerate them
        for split in splits:
            # Printing count + word
            print(counter, split)
            # Increment counter to let the loop count
            counter += 1


# Function for numerating whole Lists
def enumerate_list():
    # Calling the Function for inserting a File Path
    input_location()
    # Open the file as f
    with open(file_location) as f:
        # For loop to Numerate lists
        for count, value in enumerate(f, start=1):
            # Write values in File
            print(count, value.replace('\n', ""))


# Function for separate Words with actual and new seperator
def split_words():
    # Calling the Function for inserting a File Path
    input_location()
    # Reference to an input to insert the actual Seperator
    actual_delimiter = input("Enter the actual seperator")
    # Reference to an input to insert the new Seperator
    new_delimiter = input("Enter the new seperator")

    # Way which doesn't need a file.close
    with open(file_location, 'r+') as file:
        # Referencing file data with a file read command.
        input_of_file = file.read()

    # Replace the target string
    replaced_input = input_of_file.replace(actual_delimiter, new_delimiter)

    # Write the Data to File (w mode)
    with open(file_location, 'w') as file:
        # Command to write to a file
        file.write(replaced_input)


# Calling main and therefor the Program
if __name__ == '__main__':
    main_menu()
