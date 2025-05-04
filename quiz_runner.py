# Create the Quiz program that read the output file of the Quiz Creator. The user will answer the randomly selected question and check if the answer is correct.
# Hint: 
# Use your creativity.
# Feel free to use any library


# import both libraries json, random, PyQt5 for GUI
import sys
import json
import random 
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout,
    QMessageBox, QFileDialog, QProgressBar
)
from PyQt5.QtCore import Qt, QTimer, QPropertyAnimation, QRect

# create widget to organize quiz and GUI
class QuizApp(QWidget): 
    def __init__(self, questions):
        super().__init__    #initialize
        self.questions = random.sample(questions, len(questions))
        self.current_q = 0
        self.score = 0
        self.time_per_question = 15 #seconds
        self.timer = QTimer()
        self.remaining_time = self.time_per_question  #track how much time left
    
    def init_ui(self):  # create GUI with progress bar, timer, questions, multiple choice
        self.setWindowTitle("Quiz Runner")
        self.setGeometry(100, 100, 600, 400)

        self.layout = QVBoxLayout()

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setMaximum(len(self.questions))
        self.progress_bar.setValue(0)
        self.layout.addWidget(self.progress_bar)

        self.timer_label = QLabel('', self)
        self.timer_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.timer_label)

        self.question_label = QLabel('', self)
        self.question_label.setWordWrap(True)
        self.question_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.question_label)

def load_question(self):
    if self.current_q < len(self.questions):
        self.remaining_time = self.time_per_question
        self.timer.start(1000)
        
        q = self.questions[self.current_q]
        self.question_label.setTest(f"Q{self.current_q + 1}: {q['question']}")
# shuffle ques using lib random
# use check_answer to check if user answer is right/wrong
# create popups for results every ques
# define main 