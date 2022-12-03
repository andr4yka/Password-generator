import random
import string
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QComboBox, QGridLayout, QMessageBox


class PasswordGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.password_length_label = QLabel("Длина пароля: ")
        self.password_length_input = QLineEdit()
        self.password_length_input.setMaxLength(3)
        self.password_length_input.setFixedWidth(50)

        self.password_difficulty_label = QLabel("Уровень сложности пароля: ")
        self.password_difficulty_combo = QComboBox()
        self.password_difficulty_combo.addItems(["Лёгкий (только маленькие буквы и цифры)", "Сложный (маленькие буквы, спецсимволы и цифры)", "Ультра сложный (всё подряд)"])

        self.generate_button = QPushButton("Генерировать пароль")
        self.generate_button.clicked.connect(self.generate_password)

        self.password_label = QLabel("Пароль: ")
        self.password_input = QLineEdit()
        self.password_input.setReadOnly(True)

        self.grid = QGridLayout()
        self.grid.setSpacing(10)

        self.grid.addWidget(self.password_length_label, 1, 0)
        self.grid.addWidget(self.password_length_input, 1, 1)
        self.grid.addWidget(self.password_difficulty_label, 2, 0)
        self.grid.addWidget(self.password_difficulty_combo, 2, 1)
        self.grid.addWidget(self.generate_button, 3, 0)
        self.grid.addWidget(self.password_label, 4, 0)
        self.grid.addWidget(self.password_input, 4, 1)

        self.setLayout(self.grid)
        self.setWindowTitle("Генератор паролей")
        self.show()

    def generate_password(self):
        password_length = self.password_length_input.text()
        password_difficulty = self.password_difficulty_combo.currentText()


        if not password_length.isdigit():
            QMessageBox.about(self, "Ошибочка!", "Длина пароля должна быть числом, дурень!")
        elif int(password_length) < 6:
            QMessageBox.about(self, "Ошибочка!", "Длина пароля должна быть больше 5 символов.")
        if int(password_length) >= 400:
            QMessageBox.about(self, "Во дурак...", "Пожалей свои нервы, ты же всё равно не станешь использовать такой пароль!")
        elif int(password_length) >= 300:
            QMessageBox.about(self, "Всё, крышу снесло...", "Я не дам тебе такой длинный пароль, дурень! Ты что, собираешься его вручную вводить? Пожалей себя, вспомни что ты такое, и введи меньше 100 символов!")
        elif int(password_length) > 200:
            QMessageBox.about(self, "Во дурак...", "У тебя крыша поехала? Нахрена тебе пароль длиннее 200 символов?")
        elif int(password_length) == 200:
            QMessageBox.about(self, "Во дурак...", "У тебя крыша поехала? Нахрена тебе пароль в 200 символов?")
        elif int(password_length) == 100:
            QMessageBox.about(self, "Пользуйся мной нормально, пожалуйста", "Зачем тебе пароль в 100 символов?")
        elif int(password_length) >= 100:
            QMessageBox.about(self, "Пользуйся мной нормально, пожалуйста", "Зачем тебе пароль длиннее 100 символов?")

        else:
            if password_difficulty == "Лёгкий (только маленькие буквы и цифры)":
                password_characters = string.ascii_lowercase + string.digits
            elif password_difficulty == "Сложный (маленькие буквы, спецсимволы и цифры)":
                password_characters = string.ascii_lowercase + string.digits + string.punctuation
            else:
                password_characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

            password = "".join(random.choice(password_characters) for i in range(int(password_length)))
            self.password_input.setText(password)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PasswordGenerator()
    sys.exit(app.exec_())
