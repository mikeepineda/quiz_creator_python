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
        super().__init__()
        self.questions = random.sample(questions, len(questions)) # shuffle ques using lib random

        self.current_q = 0
        self.score = 0
        self.time_per_question = 15  # seconds
        self.timer = QTimer()
        self.remaining_time = self.time_per_question

        self.init_ui()
        self.load_question()

    def init_ui(self): # create GUI with progress bar, timer, questions, multiple choice
        self.setWindowTitle('Quiz App')
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

        self.option_buttons = []
        for i in range(4):
            btn = QPushButton('', self)
            btn.clicked.connect(self.check_answer)
            self.layout.addWidget(btn)
            self.option_buttons.append(btn)

        self.setLayout(self.layout)

        self.timer.timeout.connect(self.update_timer)

    def load_question(self):
        if self.current_q < len(self.questions):
            self.remaining_time = self.time_per_question
            self.timer.start(1000)
            self.update_timer_label()

            q = self.questions[self.current_q]
            self.question_label.setText(f"Q{self.current_q + 1}: {q['question']}")

            # Simple fade-in animation
            anim = QPropertyAnimation(self.question_label, b"geometry")
            anim.setDuration(500)
            anim.setStartValue(QRect(0, 0, 600, 0))
            anim.setEndValue(QRect(0, 0, 600, 100))
            anim.start()

            options = list(q['options'].items())
            self.correct_answer = q['answer']

            for i, (key, value) in enumerate(options):
                self.option_buttons[i].setText(f"{key}. {value}")
                self.option_buttons[i].setProperty('answer_key', key)
                self.option_buttons[i].setEnabled(True)

            self.progress_bar.setValue(self.current_q)
        else:
            self.show_score()

    def update_timer(self):
        self.remaining_time -= 1
        self.update_timer_label()
        if self.remaining_time <= 0:
            self.timer.stop()
            QMessageBox.information(self, "Time's Up", "⏰ Time's up for this question!")
            self.current_q += 1
            self.load_question()

    def update_timer_label(self):
        self.timer_label.setText(f"Time left: {self.remaining_time} seconds")

    def check_answer(self):     # use check_answer to check if user answer is right/wrong
        self.timer.stop()
        sender = self.sender()
        selected = sender.property('answer_key')

        correct_text = self.questions[self.current_q]['options'][self.correct_answer]

        if selected == self.correct_answer:
            QMessageBox.information(self, "Result", "✅ Correct!")          # create popups for results every ques
            self.score += 1
        else:
            QMessageBox.information(
                self, "Result",
                f"❌ Incorrect.\nCorrect answer: {self.correct_answer}. {correct_text}"     # create popups for results every ques
            )

        self.current_q += 1
        self.load_question()

    def show_score(self):
        QMessageBox.information(
            self, "Final Score",
            f"🎉 You scored {self.score} out of {len(self.questions)}"      # create popups for results every ques
        )
        self.close()

def load_quiz_file():
    file_dialog = QFileDialog()
    file_path, _ = file_dialog.getOpenFileName(
        None, "Select Quiz File", "", "JSON Files (*.json)"
    )
    if file_path:
        with open(file_path, 'r') as f:
            return json.load(f)
    return None

def main():     # define main 
    app = QApplication(sys.argv)
    questions = load_quiz_file()
    if questions:
        quiz = QuizApp(questions)
        quiz.show()
        sys.exit(app.exec_())
    else:
        QMessageBox.critical(None, "Error", "Failed to load quiz file.")
        sys.exit()

if __name__ == "__main__":
    main()
