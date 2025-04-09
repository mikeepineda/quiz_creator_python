# Create a program that ask user for a question, it will also ask for 4 possible answer (a,b,c,d) and the correct answer. 
# Write the collected data to a text file. Ask another question until the user chose to exit.

# start
# create loop: ask user input for questions, multiple choices, and the correct answer
# store the input to a new file
# ask user if they want add another question
# if no, stop the loop 
# end

import json
import os

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
        "options": options
        "answer": correct
    }

def load_existing_questions(filename):
    if os.path.exist(filename):     #check if the file exist in the current folder
        with open(filename, "r") as file:  # open the file in read mode using "r"
            return json.load(file)
    return []

def save_questions(filename, questions):
    with open(filename, "w") as file:   #open the file while overwriting
        json.dump(questions, file, indent=4)

def main(): 
    filename = "quiz_data.json"     #set the name of json file"
    quiz_data = load_existing_questions(filename) 

    while True: 
        question_data = get_question_data() 
        quiz_data.append(question_data)       #add/append the question to the quiz_data
        save_questions(filename, quiz_data)     #save the question to quiz_data.json file
        print("Your question was saved!")

        cont = input("\nDo you want to add another question? (yes/no): ").lower()
        if cont != "yes":
            break
    
    print("\nAll questions are saved to", filename)

if __name__ == "__main__":
    main()