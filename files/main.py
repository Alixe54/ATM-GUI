from PyQt6.QtGui import QFont, QDoubleValidator, QIntValidator, QIcon
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout,
                             QMessageBox, QHBoxLayout,
                             QRadioButton, QButtonGroup, QSizePolicy)
from PyQt6.QtCore import Qt
import sys
from ATM_back_end import *
from language_dictionary import *

class WellcomeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600, 400)
        self.init_ui()
    def init_ui(self):
        self.setWindowTitle("ali's ATM")
        horizontal_layout = QHBoxLayout()
        vertical_layout = QVBoxLayout()
        english_label = QLabel("Choose language")
        persian_label = QLabel("زبان خود را انتخاب کنید")
        english_btn = QPushButton("English")
        english_btn.clicked.connect(self.window_change)
        persian_btn = QPushButton("فارسی")
        persian_btn.clicked.connect(self.window_change)
        fixing_widgets = [english_label, persian_label, english_btn, persian_btn]
        for widget in fixing_widgets:
            widget.setFixedHeight(40)
        english_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        persian_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        horizontal_layout.addWidget(english_btn)
        horizontal_layout.addWidget(english_label)
        horizontal_layout.addWidget(persian_label)
        horizontal_layout.addWidget(persian_btn)
        vertical_layout.addLayout(horizontal_layout)
        exit_btn = QPushButton("Exit خروج")
        exit_btn.setFixedHeight(40)
        exit_btn.clicked.connect(self.exit)
        exit_btn.setShortcut('Esc')
        vertical_layout.addWidget(exit_btn)
        self.setLayout(vertical_layout)


    def window_change(self):
        text = self.sender().text()
        match text:
            case 'English':
                main_language = english
            case 'فارسی':
                main_language = persian
        self.window = SingIntWindow(main_language)
        self.window.show()
        self.close()


    def exit(self):
        self.close()
class SingIntWindow(QWidget):
    password_dict = {'123456789'}

    def __init__(self, main_language):
        super().__init__()
        self.main_language = main_language
        self.resize(600, 400)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("ali's ATM")
        vertical_layout = QVBoxLayout()
        password_label = QLabel(self.main_language['enter pass'])
        password_label.setFixedHeight(20)
        password_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.password_line_edit = QLineEdit()
        self.password_line_edit.setFixedHeight(40)
        self.password_line_edit.setValidator(QIntValidator(0, 9999))
        self.password_line_edit.setEchoMode(QLineEdit.EchoMode.Password)
        password_submit = QPushButton(self.main_language['submit'])
        password_submit.setFixedHeight(40)
        password_submit.setShortcut('return')
        password_submit.clicked.connect(self.sign_in)

        vertical_layout.addWidget(password_label)
        vertical_layout.addWidget(self.password_line_edit)
        vertical_layout.addWidget(password_submit)
        self.setLayout(vertical_layout)

    def sign_in(self):
        card_reader = CardReader()
        card_number = card_reader.read_card()
        if bank.log_in(card_number, self.password_line_edit.text()):
            self.window = SelectionWindow(self.main_language)
            self.window.show()
            self.close()
            return
        QMessageBox.warning(self, 'error', self.main_language['wrong pass'])


class SelectionWindow(QWidget):
    def __init__(self, main_language):
        super().__init__()
        self.main_language = main_language
        self.resize(600, 400)
        self.init_ui()


    def init_ui(self):
        self.setWindowTitle("ali's ATM")
        horizontal_layout1 = QHBoxLayout()
        get_cash_btn = QPushButton(self.main_language['get cash'])
        get_cash_btn.setFixedHeight(50)
        get_cash_btn.clicked.connect(self.window_change)
        change_password_btn = QPushButton(self.main_language['change pass'])
        change_password_btn.setFixedHeight(50)
        change_password_btn.clicked.connect(self.window_change)
        horizontal_layout1.addWidget(get_cash_btn)
        horizontal_layout1.addWidget(change_password_btn)
        horizontal_layout2 = QHBoxLayout()
        money_transfer_btn = QPushButton(self.main_language['money trans'])
        money_transfer_btn.setFixedHeight(50)
        money_transfer_btn.clicked.connect(self.window_change)
        account_balance_btn = QPushButton(self.main_language['account balance'])
        account_balance_btn.setFixedHeight(50)
        account_balance_btn.clicked.connect(self.window_change)
        horizontal_layout2.addWidget(money_transfer_btn)
        horizontal_layout2.addWidget(account_balance_btn)
        vertical_layout = QVBoxLayout()
        vertical_layout.addLayout(horizontal_layout1)
        vertical_layout.addLayout(horizontal_layout2)
        self.setLayout(vertical_layout)

    def window_change(self):
        text = self.sender().text()

        if text == self.main_language['get cash']:
            self.window = GetCashWindow(self.main_language)
        elif text == self.main_language['change pass']:
            self.window = ChangePasswordWindow(self.main_language)
        elif text == self.main_language['money trans']:
            self.window = MoneyTransferWindow(self.main_language)
        elif text == self.main_language['account balance']:
            self.window = CheckBalanceWindow(self.main_language)

        self.window.show()
        self.close()


class GetCashWindow(QWidget):
    def __init__(self, main_language):
        super().__init__()
        self.main_language = main_language
        self.resize(600, 400)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("ali's ATM")
        horizontal_layout1 = QHBoxLayout()
        _500_btn = QPushButton("500/000")
        _500_btn.setFixedHeight(50)
        _500_btn.clicked.connect(self.get_cash_process)
        _1500_btn = QPushButton("1/500/000")
        _1500_btn.setFixedHeight(50)
        _1500_btn.clicked.connect(self.get_cash_process)
        horizontal_layout1.addWidget(_500_btn)
        horizontal_layout1.addWidget(_1500_btn)
        horizontal_layout2 = QHBoxLayout()
        _1000_btn = QPushButton("1/000/000")
        _1000_btn.setFixedHeight(50)
        _1000_btn.clicked.connect(self.get_cash_process)
        _2000_btn = QPushButton("2/000/000")
        _2000_btn.setFixedHeight(50)
        _2000_btn.clicked.connect(self.get_cash_process)
        horizontal_layout2.addWidget(_1000_btn)
        horizontal_layout2.addWidget(_2000_btn)
        vertical_layout = QVBoxLayout()
        vertical_layout.addLayout(horizontal_layout1)
        vertical_layout.addLayout(horizontal_layout2)
        self.setLayout(vertical_layout)

    def get_cash_process(self):
        amount = self.sender().text()
        amount = int("".join(amount.split("/")))
        if bank.get_cash(amount):
            self.window = MissionCompletedWindow(self.main_language)
            self.window.show()
            self.close()
            return
        QMessageBox.warning(self, 'error', f'{self.main_language['not enough money']} {bank.check_balance()}')


class ChangePasswordWindow(QWidget):
    def __init__(self, main_language):
        super().__init__()
        self.main_language = main_language
        self.resize(600, 400)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("ali's ATM")
        vertical_layout = QVBoxLayout()
        new_password_label = QLabel(self.main_language['enter new pass'])
        new_password_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        new_password_label.setFixedHeight(50)
        self.new_password_line_edit = QLineEdit()
        self.new_password_line_edit.setFixedHeight(50)
        vertical_layout.addWidget(new_password_label)
        vertical_layout.addWidget(self.new_password_line_edit)
        submit_btn = QPushButton(self.main_language['submit'])
        submit_btn.setShortcut('return')
        submit_btn.setFixedHeight(50)
        submit_btn.clicked.connect(self.change_password)
        vertical_layout.addWidget(submit_btn)
        self.setLayout(vertical_layout)

    def change_password(self):
        new_password = self.new_password_line_edit.text()
        if new_password.isdigit() and len(new_password) == 4:
            bank.change_password(new_password)
            self.window = MissionCompletedWindow(self.main_language)
            self.window.show()
            self.close()
            return
        QMessageBox.warning(self, 'error', f'{self.main_language['wrong pass input']}')


class CheckBalanceWindow(QWidget):
    def __init__(self, main_language):
        super().__init__()
        self.main_language = main_language
        self.resize(600, 400)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("ali's ATM")
        vertical_layout = QVBoxLayout()
        balance_label = QLabel(f"{self.main_language['balance']} {bank.check_balance()}")
        balance_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        confirm_btn = QPushButton(self.main_language['confirm'])
        confirm_btn.setShortcut('return')
        confirm_btn.setFixedHeight(50)
        confirm_btn.clicked.connect(self.back_to_completed)
        vertical_layout.addWidget(balance_label)
        vertical_layout.addWidget(confirm_btn)
        self.setLayout(vertical_layout)

    def back_to_completed(self):
        self.window = MissionCompletedWindow(self.main_language)
        self.window.show()
        self.close()

class MoneyTransferWindow(QWidget):
    def __init__(self, main_language):
        super().__init__()
        self.main_language = main_language
        self.resize(600, 400)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("ali's ATM")
        vertical_layout = QVBoxLayout()
        sender_label = QLabel(self.main_language['sender'])
        self.sender_line_edit = QLineEdit()
        self.sender_line_edit.setValidator(QIntValidator())
        receiver_label = QLabel(self.main_language['receiver'])
        self.receiver_line_edit = QLineEdit()
        confirm_btn = QPushButton(self.main_language['confirm'])
        confirm_btn.setShortcut('return')
        confirm_btn.clicked.connect(self.transfer)
        self.back_btn = QPushButton(self.main_language['back'])
        self.back_btn.setShortcut('Esc')
        self.back_btn.clicked.connect(self.back_to_completed)
        fixing_widgets = [sender_label, self.sender_line_edit, receiver_label, self.receiver_line_edit, confirm_btn, self.back_btn]
        for number, widget in enumerate(fixing_widgets):
            widget.setFixedHeight(30)
            if number not in [4, 5]:
                widget.setAlignment(Qt.AlignmentFlag.AlignCenter)
            vertical_layout.addWidget(widget)

        self.setLayout(vertical_layout)

    def transfer(self):
        amount = 0
        try:
            amount = int(self.sender_line_edit.text())
        except:
            QMessageBox.warning(self, 'error', f'{self.main_language["empty input"]}')
            return
        receiver = self.receiver_line_edit.text()
        status = bank.transfer_money(receiver, amount)
        if status == 'not enough money':
            QMessageBox.warning(self, 'error', f'{self.main_language['not enough money']} {bank.check_balance()}')
        elif status == 'no user':
            QMessageBox.warning(self, 'error', f'{self.main_language['user not found']}')
        else:
            QMessageBox.about(self, 'success', f'{self.main_language['successful transfer']}')
            self.back_to_completed()

    def back_to_completed(self):
        self.window = MissionCompletedWindow(self.main_language)
        if self.sender().text() == self.main_language['back']:
            self.window = SelectionWindow(self.main_language)
        self.window.show()
        self.close()

class MissionCompletedWindow(QWidget):
    def __init__(self, main_language):
        super().__init__()
        self.main_language = main_language
        self.resize(600, 400)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("ali's ATM")
        vertical_layout = QVBoxLayout()
        completed_label = QLabel(self.main_language['mission accomplish'])
        completed_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        vertical_layout.addWidget(completed_label)
        horizontal_layout = QHBoxLayout()
        good_bye_btn = QPushButton(self.main_language['good bye'])
        good_bye_btn.setShortcut('Esc')
        good_bye_btn.setFixedHeight(50)
        good_bye_btn.clicked.connect(self.go_to_main)
        new_mission_btn = QPushButton(self.main_language['new mission'])
        new_mission_btn.setShortcut('return')
        new_mission_btn.setFixedHeight(50)
        new_mission_btn.clicked.connect(self.new_mission)
        horizontal_layout.addWidget(good_bye_btn)
        horizontal_layout.addWidget(new_mission_btn)
        vertical_layout.addLayout(horizontal_layout)
        self.setLayout(vertical_layout)

    def go_to_main(self):
        self.window = WellcomeWindow()
        self.window.show()
        self.close()

    def new_mission(self):
        self.window = SelectionWindow(self.main_language)
        self.window.show()
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WellcomeWindow()
    # window = SelectionWindow()
    # window = GetCashWindow()
    # window = MissionCompletedWindow()
    window.show()
    sys.exit(app.exec())

