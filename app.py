import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QWidget, QCheckBox, QTextBrowser

from start_parser import start_parser



# Подкласс QMainWindow для настройки главного окна приложения
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Парсинг протоколов ФБУЗ")

        self.label = QLabel()
        self.label.setFixedSize(QSize(600, 30))
        self.label.setText('Путь к папке с PDF:')
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.input = QLineEdit()
        self.input.setFixedSize(QSize(600, 30))
        self.input.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.check_arch = QCheckBox()
        self.check_arch.setText('Архивирование файлов')

        self.check_log = QCheckBox()
        self.check_log.setText('Логирование результата')

        self.check_json = QCheckBox()
        self.check_json.setText('Сохранение JSON файлов')
        
        self.button = QPushButton("Начать!")
        self.button.setFixedSize(QSize(100, 50))
        self.button.setCheckable(True)
        self.button.clicked.connect(self.the_button_was_clicked)
        
        #self.console = QTextBrowser()
        #self.console.setFixedSize(QSize(600, 200))
        #self.console.setAlignment(Qt.AlignmentFlag.AlignLeft)

        layout = QVBoxLayout()
        layout.setContentsMargins(50,50,50,50)
        layout.setSpacing(20)

        layout_btn = QHBoxLayout()

        layout.addWidget(self.label)
        layout.addWidget(self.input)
        layout.addWidget(self.check_arch)
        layout.addWidget(self.check_log)
        layout.addWidget(self.check_json)
        layout_btn.addWidget(self.button)
        layout.addLayout(layout_btn)
        #layout.addWidget(self.console)
        layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        container = QWidget()
        container.setLayout(layout)
        container.setFixedSize(QSize(800, 400))
        #container.setStyleSheet('border-style: solid; border-width: 1px; border-color: black;')
        
        # Устанавливаем центральный виджет Window.
        self.setFixedSize(QSize(800, 400))
        self.setCentralWidget(container)

    def the_button_was_clicked(self):
        path = self.input.text()
        if len(path) > 0:
            is_arch = self.check_arch.isChecked()
            is_log = self.check_log.isChecked()
            is_json = self.check_json.isChecked()
            start_parser(path, is_arch, is_log, is_json)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()