# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
# from word_verification_module.word_verification_module import word_verification_test
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("English Tutorial")
#
#         # Set the window size and position it in the center of the screen
#         window_width = 1000
#         window_height = 500
#         screen_width = QApplication.desktop().screenGeometry().width()
#         screen_height = QApplication.desktop().screenGeometry().height()
#         x = (screen_width - window_width) // 2
#         y = (screen_height - window_height) // 2
#         self.setGeometry(x, y, window_width, window_height)
#
#         # Create the button to start the verification process
#         button_width = 300
#         button_height = 80
#         start_button = QPushButton("Start Improving Your English", self)
#         start_button.setGeometry((window_width - button_width) // 2, (window_height - button_height) // 2,
#                                  button_width, button_height)
#         start_button.clicked.connect(self.start_verification)
#
#     def start_verification(self):
#         # Call the word_verification_test function
#         word_verification_test()
#
# def Lunch_UI():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())

import sys
import threading
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QStackedLayout
from PyQt5.QtCore import Qt, QMetaObject, pyqtSlot
from learning_process_moudle.learning_process import learning_steps


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("English Tutorial")
        self.button_clicked = False

        # Set the window size and position it in the center of the screen
        window_width = 1000
        window_height = 500
        screen_width = QApplication.desktop().screenGeometry().width()
        screen_height = QApplication.desktop().screenGeometry().height()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.setGeometry(x, y, window_width, window_height)

        # Create the stacked layout
        self.stacked_layout = QStackedLayout()

        # Create the first page widget
        self.create_first_page()

        # Set the stacked layout as the central layout
        central_widget = QWidget(self)
        central_widget.setLayout(self.stacked_layout)
        self.setCentralWidget(central_widget)

    def create_first_page(self):
        # Create the first page widget
        first_page_widget = QWidget()

        # Create the button to start the verification process
        button_width = 300
        button_height = 80
        start_button = QPushButton("Start Improving Your English", first_page_widget)
        start_button.setGeometry((self.width() - button_width) // 2, (self.height() - button_height) // 2,
                                 button_width, button_height)
        start_button.clicked.connect(self.start_verification)

        # Add the first page widget to the stacked layout
        self.stacked_layout.addWidget(first_page_widget)

    @pyqtSlot()
    def create_second_page_wrapper(self):
        # Call the create_second_page method
        self.create_second_page()

    def create_second_page(self):
        # Create the second page widget
        second_page_widget = QWidget()

        # Create the label for the second page
        label = QLabel("This is the second page", second_page_widget)
        label.setAlignment(Qt.AlignCenter)

        # Add the second page widget to the stacked layout
        self.stacked_layout.addWidget(second_page_widget)

        # Set the second page as the current widget in the stacked layout
        self.stacked_layout.setCurrentWidget(second_page_widget)

    def start_verification(self):
        if not self.button_clicked:
            self.button_clicked = True
            # Start a new thread to run word_verification_test
            Learning_proccess_thread = threading.Thread(target=self.Learning_proccess_thread)
            Learning_proccess_thread.start()
            self.button_clicked = False

            # Create the second page after the word verification is complete
            QMetaObject.invokeMethod(self, "create_second_page_wrapper", Qt.QueuedConnection)

    def Learning_proccess_thread(self):
        # Call the word_verification_test function
        learning_steps()

def Lunch_UI():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
