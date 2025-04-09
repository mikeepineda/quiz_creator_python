# Create a program that ask user for a question, it will also ask for 4 possible answer (a,b,c,d) and the correct answer. 
# Write the collected data to a text file. Ask another question until the user chose to exit.

# start
# create loop: ask user input for questions, multiple choices, and the correct answer
# store the input to a new file
# ask user if they want add another question
# if no, stop the loop 
# end

print("\n=== Create a New Quiz Question ===")
question = input("Input your question here: ")

options = {}
options['a'] = input("Input option a: ")
options['b'] = input("Input option b: ")
options['c'] = input("Input option c: ")
options['d'] = input("Input option d: ")
