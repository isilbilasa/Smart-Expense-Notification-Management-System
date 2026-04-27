from datetime import datetime


class Expense:
    def __init__(self, amount, category, date=None):
        self.amount = float(amount)
        self.category = str(category).strip().title()
        self.date = date if date else datetime.now().strftime("%Y-%m-%d")

    def __str__(self):
        return f"[{self.date}] {self.category}: {self.amount:.2f} TL"


class Budget:
    def __init__(self, limit=5000):
        self.limit = float(limit)
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def total_expense(self):
        return sum(exp.amount for exp in self.expenses)

    def average_expense(self):
        if not self.expenses:
            return 0
        return self.total_expense() / len(self.expenses)

    def max_expense(self):
        if not self.expenses:
            return None
        return max(self.expenses, key=lambda exp: exp.amount)

    def min_expense(self):
        if not self.expenses:
            return None
        return min(self.expenses, key=lambda exp: exp.amount)

    def expense_count(self):
        return len(self.expenses)

    def category_set(self):
        return set(exp.category for exp in self.expenses)

    def is_limit_exceeded(self):
        return self.total_expense() > self.limit