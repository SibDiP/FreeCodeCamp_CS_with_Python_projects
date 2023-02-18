class Category:

    def __init__(self, category_name: str):
        self.name = category_name
        self.ledger = []
        self.total_amount = 0
        self.money_balance = 0
        self.terminal_output = ''
        
    def deposit(self, amount: int, description: str = '') -> object:
        self.ledger.append({'amount': amount, 'description': description})
        self.money_balance += amount

    def withdraw(self, amount: int, description: str = '') -> bool:
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            self.money_balance -= amount
            return True
        return False

    def transfer(self, amount: int, category: object) -> bool:
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        return False

    def get_balance(self):
        return self.money_balance

    def check_funds(self, amount: int) -> bool:
        if amount > self.money_balance:
            return False
        return True

    # Check-style output
    def __str__(self):
        DESCRIPTION_LENGTH = 23
        AMOUNT_LENGTH = 7
        CHECK_WIDTH = 30

        self.terminal_output += self.name.center(CHECK_WIDTH, '*')

        for ledger_index, ledger_value in enumerate(self.ledger):
            description_part = self.ledger[ledger_index]['description'][:DESCRIPTION_LENGTH].ljust(DESCRIPTION_LENGTH)
            transaction_amount = self.ledger[ledger_index]['amount']
            transaction_amount_part = f"{transaction_amount:.2f}" # ex: 26 => 26.00 | 26.34523 => 26.35
            transaction_full_row = f"\n{description_part}{transaction_amount_part.rjust(AMOUNT_LENGTH)}"

            self.terminal_output += transaction_full_row
            self.total_amount += transaction_amount

        self.terminal_output += f"\nTotal: {self.total_amount}"

        return self.terminal_output

def create_spend_chart(categories: list) -> list:
    SEPARATOR_LINE_LEN_PER_CATEGORY = 3
    SEPARATOR_LINE_LEN_LEDGE = 1

    spent_money_by_categories_list = spent_money_by_categories(categories)
    total_withdraw_amount = total_withdraw(spent_money_by_categories_list)
    share_of_categories_in_total_withdrawal_dict = share_of_categories_in_total_withdrawal(spent_money_by_categories_list,
                                                                                     total_withdraw_amount)
    separator_length = (len(share_of_categories_in_total_withdrawal_dict) * SEPARATOR_LINE_LEN_PER_CATEGORY
                        + SEPARATOR_LINE_LEN_LEDGE)

    spend_chart_output = (f'Percentage spent by category\n'
                          f'{form_a_spent_chart(share_of_categories_in_total_withdrawal_dict)} \n    '
                          f'{"-" * separator_length}'
                          f'{vertical_names(categories)}')

    return spend_chart_output

def spent_money_by_categories(categories: list) -> dict:
    spend_sum_by_categories = {}

    # Find a sum of all withdraws in category
    for category in categories:
        spend_sum_by_categories[category.name] = 0

        for ledger_index, ledger_value in enumerate(category.ledger):
            transaction_amount = category.ledger[ledger_index]['amount']

            if transaction_amount < 0:
                spend_sum_by_categories[category.name] += transaction_amount

    return spend_sum_by_categories

def total_withdraw(spent_list: list) -> int:
    total_withdraw_count = 0

    for category, amount in spent_list.items():
        total_withdraw_count += amount

    return total_withdraw_count

def share_of_categories_in_total_withdrawal(spent_list: list, total_withdraw_amount: int) -> dict:
    withdrawal_shares = {}

    for category, amount in spent_list.items():
        withdrawal_shares[category] = amount / total_withdraw_amount * 100

    return withdrawal_shares

def form_a_spent_chart(share_of_categories_in_total_withdraw: dict) -> str:
    TWO_DIGIT_LEN = 2
    spend_chart_output_temp = ''

    for percentage_bar in range(100, -1, -10):  # 100 as 100%, -1 as lowest gap, -10 as step
        spend_chart_output_temp += f' \n{str(percentage_bar).rjust(3)}|'

        for category, share in share_of_categories_in_total_withdraw.items():

            # Round down to the nearest 10 (as it ask in task)
            rounded_to_decimal_share = round(share)

            if len(str(rounded_to_decimal_share)) < TWO_DIGIT_LEN:
                rounded_to_decimal_share = 0
            else:
                rounded_to_decimal_share = int(f'{rounded_to_decimal_share}')

            if rounded_to_decimal_share - percentage_bar >= 0:
                spend_chart_output_temp += ' o '
            else:
                spend_chart_output_temp += '   '

    return spend_chart_output_temp.lstrip()

def vertical_names(categories: list) -> str:
    spend_chart_output_temp = ''
    max_category_name_length = 0

    for category in categories:
        if len(category.name) > max_category_name_length:
            max_category_name_length = len(category.name)

    for letter_index in range(max_category_name_length):
        spend_chart_output_temp += ' \n    '

        for category in categories:
            try:
                spend_chart_output_temp += f' {category.name[letter_index]} '
            except IndexError:
                spend_chart_output_temp += '   '

    return spend_chart_output_temp[1:] + ' '