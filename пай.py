import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit, QMessageBox


class MaeKasino(QWidget):
    def __init__(self):
        super().__init__()
        self.balance = 52
        self.initUI()

    def initUI(self):
        self.setWindowTitle('КАЗЕК')
        self.balance_label = QLabel(f'Баланс<: {self.balance}', self)
        self.bet_input = QLineEdit(self)
        self.bet_input.setPlaceholderText('На чо ставим')
        self.rn = QPushButton('ПИНК', self)
        self.bn = QPushButton('ПЕРПЛ', self)
        self.rn.clicked.connect(lambda: self.make_bet('ПИНг'))
        self.bn.clicked.connect(lambda: self.make_bet('ПёПРЛ'))
        layout = QVBoxLayout()
        layout.addWidget(self.balance_label)
        layout.addWidget(self.bet_input)
        layout.addWidget(self.rn)
        layout.addWidget(self.bn)
        self.setLayout(layout)

    def make_bet(self, color):
        try:
            bet = int(self.bet_input.text())
            if bet <= 0:
                raise "ОшИбКа"

            if bet > self.balance:
                raise ValueError("Недостаточно средств у вас")


            game_color = random.choice(['ПИНг', 'ПёПРЛ'])
            if color == game_color:
                self.balance += bet
                QMessageBox.information(self, 'Результат', f'Ты выиграл бро! Цвет был {game_color}.')
            else:
                self.balance -= bet
                QMessageBox.warning(self, 'Результат', f'Ти проиграл(;! Цвет был {game_color}.')

            self.balance_label.setText(f'Баланс<: {self.balance}')
            self.bet_input.clear()

            if self.balance <= 0:
                QMessageBox.critical(self, 'Игра окончена', 'Поздравляю вы банкрот!')
                self.balance = 52
                self.balance_label.setText(f'Баланс<: {self.balance}')

        except ValueError as e:
            QMessageBox.warning(self, 'Ошибка', str(e))


def main():
    app = QApplication(sys.argv)
    z = MaeKasino()
    z.resize(300, 200)
    z.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()