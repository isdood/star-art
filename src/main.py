import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QHBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from src.tools.animation_tool import AnimationTool

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.animation_tool = AnimationTool()

    def initUI(self):
        self.setWindowTitle('Star Art Studio')
        self.setWindowIcon(QIcon('icon.png'))
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        label = QLabel('Welcome to Star Art Studio!', self)
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        animation_layout = QHBoxLayout()
        add_frame_button = QPushButton('Add Frame', self)
        add_frame_button.clicked.connect(self.add_frame)
        animation_layout.addWidget(add_frame_button)

        remove_frame_button = QPushButton('Remove Frame', self)
        remove_frame_button.clicked.connect(self.remove_frame)
        animation_layout.addWidget(remove_frame_button)

        play_animation_button = QPushButton('Play Animation', self)
        play_animation_button.clicked.connect(self.play_animation)
        animation_layout.addWidget(play_animation_button)

        layout.addLayout(animation_layout)

        self.show()

    def add_frame(self):
        # Placeholder for adding a frame
        pass

    def remove_frame(self):
        # Placeholder for removing a frame
        pass

    def play_animation(self):
        self.animation_tool.play_animation()

def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
