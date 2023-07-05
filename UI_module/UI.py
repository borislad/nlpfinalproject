import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from word_verification.word_verification import word_verification_test

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Word Verification")

        # Set the window size and position it in the center of the screen
        window_width = 1000
        window_height = 500
        screen_width = QApplication.desktop().screenGeometry().width()
        screen_height = QApplication.desktop().screenGeometry().height()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.setGeometry(x, y, window_width, window_height)

        # Create the button to start the verification process
        button_width = 300
        button_height = 80
        start_button = QPushButton("Start Improving Your English", self)
        start_button.setGeometry((window_width - button_width) // 2, (window_height - button_height) // 2,
                                 button_width, button_height)
        start_button.clicked.connect(self.start_verification)

    def start_verification(self):
        # Call the word_verification_test function
        word_verification_test()

def Lunch_UI():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())