from random import choice
from numpy import unique

balance = 500
def valid_bet(bet):
    if 0 < bet <= balance and str(bet).isnumeric():
        return True
    return False


def generate():
    symbols = ["7", "#", "$", "&"]
    res = []
    for _ in range(3):
        res.append(choice(symbols))
    return res




def bet_result(local_balance):
    bet = (int(input("Введите вашу ставку: ")))
    if valid_bet(bet):
        res = generate()
        if len(unique(res)) == 1 and res[0] == "7":
            local_balance += bet * 10
            print("Вы выиграли x10! Теперь ваш баланс", local_balance)
            print(*res)
        elif len(unique(res)) == 1 and res[0] == "#":
            local_balance += bet * 5
            print("Вы выиграли x5! Теперь ваш баланс", local_balance)
            print(*res)
        elif len(unique(res)) == 1 and res[0] == "$":
            local_balance += bet * 3
            print("Вы выиграли x3! Теперь ваш баланс", local_balance)
            print(*res)
        elif len(unique(res)) == 1 and res[0] == "&":
            local_balance += bet * 2
            print("Вы выиграли x2! Теперь ваш баланс", local_balance)
            print(*res)
        else:
            local_balance -= bet
            print("К сожалению вы проиграли :( Теперь ваш баланс", local_balance)
            print(*res)
    else:
        print("Вы ввели недопустимую ставку")
    return local_balance



print("Ваш баланс", balance)

while True:
    answer = input("Играем ещё? (Да Нет) ")
    if answer.lower() == "да":
        balance = bet_result(balance)
    elif answer.lower() == "нет":
        break
    else:
        continue
