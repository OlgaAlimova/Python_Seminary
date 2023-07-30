# Возьмите задачу о банкомате из семинара:
#  Программа банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег
# 2. Разбейте её на отдельные операции — функции. Дополнительно
# сохраняйте все операции поступления и снятия средств в список.

# Глобальная переменная для хранения суммы денег на счете
account_balance = 0
# Глобальная переменная для хранения списка всех операций поступления и снятия средств
transactions = []

# Функция для пополнения счета
def deposit(amount):
    global account_balance
    account_balance += amount
    transactions.append(f"Пополнение на сумму {amount} у.е.")
    print(f"Счет успешно пополнен. Текущая сумма: {account_balance} у.е.")

# Функция для снятия средств
def withdraw(amount):
    global account_balance
    global transactions
    if amount > account_balance:
        print("Недостаточно средств на счете.")
        return

    if account_balance > 5000000:
        tax = 0.1 * amount
        amount -= tax
        transactions.append(f"Снятие на сумму {amount} у.е. (включая налог на богатство {tax} у.е.)")
    else:
        transactions.append(f"Снятие на сумму {amount} у.е.")

    fee = max(30, min(600, 0.015 * amount))
    account_balance -= (amount + fee)
    transactions.append(f"Комиссия за снятие: {fee} у.е.")
    print(f"Средства успешно сняты. Текущая сумма: {account_balance} у.е.")

# Функция для вывода текущего баланса
def get_balance():
    print(f"Текущий баланс: {account_balance} у.е.")

# Функция для основного меню
def main_menu():
    global account_balance
    global transactions

    while True:
        print("\n*** Банкомат ***")
        print("1. Пополнить счет")
        print("2. Снять средства")
        print("3. Вывести текущий баланс")
        print("4. Выйти")

        choice = input("Введите номер пункта меню: ")

        if choice == "1":
            amount = int(input("Введите сумму для пополнения: "))
            if amount % 50 == 0:
                deposit(amount)
            else:
                print("Сумма пополнения должна быть кратной 50 у.е.")

        elif choice == "2":
            amount = int(input("Введите сумму для снятия: "))
            if amount % 50 == 0:
                withdraw(amount)
            else:
                print("Сумма снятия должна быть кратной 50 у.е.")

        elif choice == "3":
            get_balance()

        elif choice == "4":
            print("До свидания!")
            break

        else:
            print("Некорректный выбор. Повторите попытку.")

if __name__ == "__main__":
    main_menu()
