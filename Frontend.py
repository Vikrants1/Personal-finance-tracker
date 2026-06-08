import requests

BASE_URL = "http://127.0.0.1:5000"


def show_transactions():

    response = requests.get(f"{BASE_URL}/transactions")

    data = response.json()

    print("\nTransactions\n")

    income = 0
    expense = 0

    for item in data:

        print(
            f"{item['_id']} | "
            f"{item['title']} | "
            f"₹{item['amount']} | "
            f"{item['type']}"
        )

        if item["type"] == "income":
            income += item["amount"]
        else:
            expense += item["amount"]

    print("\n------------------")
    print(f"Income  : ₹{income}")
    print(f"Expense : ₹{expense}")
    print(f"Balance : ₹{income - expense}")
    print("------------------\n")


def add_transaction():

    title = input("Enter title: ")
    amount = int(input("Enter amount: "))
    ttype = input("Type (income/expense): ")

    data = {
        "title": title,
        "amount": amount,
        "type": ttype
    }

    requests.post(
        f"{BASE_URL}/transactions",
        json=data
    )

    print("Transaction Added\n")


def delete_transaction():

    id = input("Enter Transaction ID: ")

    requests.delete(
        f"{BASE_URL}/transactions/{id}"
    )

    print("Transaction Deleted\n")


while True:

    print("==== FinTrack AI ====")
    print("1. View Transactions")
    print("2. Add Transaction")
    print("3. Delete Transaction")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        show_transactions()

    elif choice == "2":
        add_transaction()

    elif choice == "3":
        delete_transaction()

    elif choice == "4":
        break

    else:
        print("Invalid Choice\n")
