# Create a program that ask user for a question, it will also ask for 4 possible answer (a,b,c,d) and the correct answer. 
# Write the collected data to a text file. Ask another question until the user chose to exit.

# start
# create loop: ask user input for questions, multiple choices, and the correct answer
# store the input to a new file
# ask user if they want add another question
# if no, stop the loop 
# end

import json

def get_question_data():
    print("\n=== Create a New Quiz Question ===")
    question = input("Input your question here: ")

    options = {}
    options['a'] = input("Input option a: ")
    options['b'] = input("Input option b: ")
    options['c'] = input("Input option c: ")
    options['d'] = input("Input option d: ")

    correct = ""
    while correct not in ['a', 'b', 'c', 'd']:
        correct = input("What letter is the correct answer (a/b/c/d) ?:  ").lower()
        if correct not in ['a', 'b', 'c', 'd']:
            print("Invalid. Kindly enter a, b, c, or d")
    
    return {
        "question": question
        "options": option
        "answer": correct
    }

def load_existing_questions(filename):
    if os.path.exist(filename):     #check if the file exist in the current folder
        with open(filename, "r") as file:  # open the file in read mode using "r"
            return json.load(file)
    return []