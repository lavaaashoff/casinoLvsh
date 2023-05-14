from random import choice
import sqlite3

#подключение базы данных
db = sqlite3.connect("casino.db")
cursor = db.cursor()


class Game:

    def __init__(self, balance):
        self.balance = balance
        self.symbols = {"777" : 10,
                        "$$$" : 5,
                        "###" : 3}
    #основной метод, запускающий игру
    def start(self):

        #создание таблицы
        cursor.execute("""CREATE TABLE IF NOT EXISTS results(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        balance INT,
                        bet INT,
                        symbols TEXT,
                        res TEXT
                    )""")
        db.commit()

        print("Ваш баланс:", self.balance)
        while True: #цикл которые идёт все время игры
            answer = input("Играем ещё? (Да, Нет) ")
            if answer.lower() == "да":
                self.bet_result()
            elif answer.lower() == "нет":
                break
            else:
                continue
        self.base()
    
    def generate(self): #создание списка из символов
        gensymbols = ["7", "#", "$"]
        res = []
        for _ in range(3):
            res.append(choice(gensymbols))
        return "".join(res)
    
    def valid_bet(self, bet): #проверка ставки на валидность
        if str(bet).isnumeric() and 0 < int(bet) < self.balance:
            return True
        return False
    
    def bet_result(self): #получение ставки, выбор результата ставки
        bet = input("Введите вашу ставку: ")
        if self.valid_bet(bet):
            bet = int(bet)
            res = self.generate()
            wl = "lose"
            if res not in self.symbols: #проверка проигрыша
                self.balance -= bet      
                print(res)      
                print(f"К сожалению вы проиграли :( Теперь ваш баланс {self.balance}")
            elif res in self.symbols: #проверка выигрыша
                self.balance += bet * self.symbols[res]
                print(res)
                print(f"Вы выиграли x{self.symbols[res]}! Теперь ваш баланс {self.balance}")
                wl = "win"    
            cursor.execute("""INSERT INTO results(balance, bet, symbols, res)
                       VALUES('%d', '%d', '%s', '%s')""" % (self.balance, bet, res, wl ))
            db.commit()
        else:
            print("Недопустимая ставка.")

    def base(self): #вывод базы данных при надобности и удаление
        if input("Вывести базу данных? ").lower() == "да":
            for value in cursor.execute("SELECT * FROM results"):
                print(value)
        cursor.execute("DROP TABLE results")
        db.commit()
    