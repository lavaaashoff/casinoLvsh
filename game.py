from random import choice
import sqlite3

#database connection
db = sqlite3.connect("casino.db")
cursor = db.cursor()


class Game:

    def __init__(self, balance):
        self.balance = balance
        self.symbols = {"777" : 10,
                        "$$$" : 5,
                        "###" : 3}
    #the main method that starts the game
    def start(self):

        #table creation
        cursor.execute("""CREATE TABLE IF NOT EXISTS results(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        balance INT,
                        bet INT,
                        symbols TEXT,
                        res TEXT
                    )""")
        db.commit()

        print("Your balance:", self.balance)
        while True: #a loop that goes on throughout the game
            answer = input("Play again? (Yes, No) ")
            if answer.lower() == "yes":
                self.bet_result()
            elif answer.lower() == "no":
                break
            else:
                continue
        self.base()
    
    def generate(self): #dropped symbol generation
        gensymbols = ["7", "#", "$"]
        res = []
        for _ in range(3):
            res.append(choice(gensymbols))
        return "".join(res)
    
    def valid_bet(self, bet): #checking the possibility of a bet
        if str(bet).isnumeric() and 0 < int(bet) < self.balance:
            return True
        return False
    
    def bet_result(self): #receiving a bet, choosing the result of a bet
        bet = input("Enter your bet: ")
        if self.valid_bet(bet):
            bet = int(bet)
            res = self.generate()
            wl = "loss"
            if res not in self.symbols: #check for loss
                self.balance -= bet      
                print(res)      
                print(f"Unfortunately you lost :( Now your balance {self.balance}")
            elif res in self.symbols: #check for victory
                self.balance += bet * self.symbols[res]
                print(res)
                print(f"you won x{self.symbols[res]}! Now your balance {self.balance}")
                wl = "win"    
            cursor.execute("""INSERT INTO results(balance, bet, symbols, res)
                       VALUES('%d', '%d', '%s', '%s')""" % (self.balance, bet, res, wl ))
            db.commit()
        else:
            print("Invalid bet.")

    def base(self): #outputting the database if necessary and deleting
        if input("Show database? (Yes, No) ").lower() == "yes":
            for value in cursor.execute("SELECT * FROM results"):
                print(value)
        cursor.execute("DROP TABLE results")
        db.commit()
        close = input("Press Enter...")
    