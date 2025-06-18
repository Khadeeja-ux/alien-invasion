import random

MAX_LINES = 3
MAX_BIT = 100
MIN_BIT = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

def slot_machine_spin(rows , cols , symbols):
    all_symbols = []
    for symbol , symbol_count in symbols:
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range (cols):
        column = []
        current_symbol = all_symbols[:]
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbol.remove(value)
            column.append(value)

        columns.append(column)
    return columns

def print_slot_machine(columns):

def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("The amount must be greater than 0.")
        else:
            print("Enter a number, please.")
    return amount

def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines (1 - {MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Enter a number, please.")
    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet on each line?$ ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BIT <= amount <= MAX_BIT:
                break
            else:
                print(f"The amount must be between ({MIN_BIT} - {MAX_BIT}).")
        else:
            print("Enter a number, please.")
    return amount

def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"Tou do not have enough to bet . Your balance is ${balance}")
        else:
            break

    print(f"You are betting {bet} on each {lines} lines. The total bet: {total_bet}.")

main()
nm = ltrk
lktr = ""
ljkg = 1
