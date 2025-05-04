# Create the Quiz program that read the output file of the Quiz Creator. The user will answer the randomly selected question and check if the answer is correct.
# Hint: 
# Use your creativity.
# Feel free to use any library

# import both libraries json, random, PyQt5 for GUI
# create widget to organize quiz and GUI
# create GUI with progress bar, timer, questions, multiple choice
# shuffle ques using lib random
# use check_answer to check if user answer is right/wrong
# create popups for results every ques
# define main 


import sys
import json
import random 
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout,
    QMessageBox, QFileDialog, QProgressBar
)
from PyQt5.QtCore import Qt, QTimer, QPropertyAnimation, QRect

