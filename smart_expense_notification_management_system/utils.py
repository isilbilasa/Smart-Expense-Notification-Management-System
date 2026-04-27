import random
from datetime import datetime

from models import Expense
from notifications import EmailNotification, SMSNotification

notification_history = []


def get_user_expenses():
    expenses_list = []
    print("--- Expense Entry System (Enter 0 to finish) ---")

    while True:
        try:
            amount = float(input("Amount: "))
            if amount == 0:
                break

            category = input("Category: ").strip()
            if not category:
                print("Error: Category cannot be empty!")
                continue

            new_expense = Expense(amount, category)
            expenses_list.append(new_expense)

        except ValueError:
            print("Error: Please enter a valid number for amount!")
            continue

    return expenses_list


def generate_random_notification(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    full_message = f"{message} | Created at: {timestamp}"
    notification_class = random.choice([EmailNotification, SMSNotification])
    return notification_class(full_message)

def register_notifications(*notifications):
    results = []
    for notification in notifications:
        results.append(notification.send())
    return results