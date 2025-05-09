import csv
import pickle


class User:
    def __init__(self, first_name, last_name, password, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value > 0 and isinstance(value, int):
            self._balance = value
            return
        print("wrong balance value")


class Bank:
    def __init__(self, data):
        self.users = {}
        self.main_user = None
        self.main_user_card_number = None
        self.data_base = data

    def log_in(self, card_number, password):
        if card_number in self.users:
            if self.users[card_number].password == password:
                self.main_user = self.users[card_number]
                self.main_user_card_number = card_number
                return True
        return False

    def add_user(self, card_number, user):
        self.users[card_number] = user

    def check_balance(self):

        return self.users[self.main_user_card_number].balance

    def get_cash(self, amount):
        if self.users[self.main_user_card_number].balance >= amount:
            self.data_base = Database.csv_load()
            self.users = Database.pickle_load()
            self.users[self.main_user_card_number].balance -= amount
            self.data_base.append([self.main_user_card_number, self.users[self.main_user_card_number].first_name,
                                   self.users[self.main_user_card_number].last_name,
                                   self.users[self.main_user_card_number].password,
                                   self.users[self.main_user_card_number].balance, amount, 'get_cash_process'])
            Database.csv_save(self.data_base)
            Database.pickle_save(self)
            return True
        return False

    def change_password(self, password):
        self.data_base = Database.pickle_load()
        self.users[self.main_user_card_number].password = password
        Database.pickle_save(self)

    def transfer_money(self, card_number, money):
        if card_number in self.users:
            if self.users[self.main_user_card_number].balance >= money:
                self.data_base = Database.csv_load()
                self.users = Database.pickle_load()
                self.users[card_number].balance += money
                self.users[self.main_user_card_number].balance -= money
                self.data_base.append([self.main_user_card_number, self.users[self.main_user_card_number].first_name,
                                       self.users[self.main_user_card_number].last_name,
                                       self.users[self.main_user_card_number].password,
                                       self.users[self.main_user_card_number].balance, money, card_number])
                Database.csv_save(self.data_base)
                Database.pickle_save(self)
                return None
            print("not enough money")
            return 'not enough money'
        print(f"no user with {card_number}")
        return 'no user'


class CardReader:
    @staticmethod
    def read_card():
        # some process to read card and return card number for ATM
        # by default we return user1 card number
        scanned_card_number = "6037777777777777"
        return scanned_card_number


class Database:
    @staticmethod
    def csv_load():
        try:
            with open('users_transactions.csv', 'r', newline='') as csvfile:
                csv_data = csv.reader(csvfile)
                data_base = []
                for row in csv_data:
                    data_base.append(row)
                return data_base

        except FileNotFoundError:
            data_base = [
                ['card_number', 'first_name', 'last_name', 'password', 'balance', 'transfer_amount', 'transfer_card']]
            return data_base

    @staticmethod
    def csv_save(data_base):
        with open('users_transactions.csv', 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            for row in data_base:
                csv_writer.writerow(row)

    @staticmethod
    def pickle_load():

        try:
            with open('bank_users', 'rb') as f:
                return pickle.load(f)

        except:
            bank = Bank(CardReader.read_card())
            user1 = User('ali', 'jafari', "1234", 10000000)
            user2 = User('jafari', 'ali', "4321", 1000000)
            bank.add_user("6037777777777777", user1)
            bank.add_user("6037888888888888", user2)
            return bank.users

    @staticmethod
    def pickle_save(bank):
        with open('bank_users', 'wb') as f:
            pickle.dump(bank.users, f)


data_base = Database.csv_load()
bank = Bank(CardReader.read_card())
bank.users = Database.pickle_load()

Database.csv_save(data_base)

Database.pickle_save(bank)
