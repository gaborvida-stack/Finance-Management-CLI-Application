try:
    import sqlite3
    import pandas as pd
    import matplotlib.pyplot as plt
except ImportError as err:
    print("error occured: {}".format(err))


conn = sqlite3.connect("finance_data.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY,
        amount REAL,
        type TEXT
    )
""")
conn.commit()

def new_transaction():
    amount = float(input("Amount: "))
    transaction_type = input("Income or expend (I/E): ")

    if transaction_type.lower() == "i":
        transaction_type = "income"
    else:
        transaction_type = "expend"

    cursor.execute("""
        INSERT INTO transactions (amount, type) VALUES (?, ?)
    """, (amount, transaction_type))
    conn.commit()

def summary(plot=False):
    try:
        df = pd.read_sql_query("SELECT * FROM transactions", conn)
        print("\n{}".format(df))

        income = df[df["type"] == "income"]["amount"].sum()
        expend = df[df["type"] == "expend"]["amount"].sum()

        print("\nIncome: {}$".format(income))
        print("Expend: {}$".format(expend))
        print("Balance: {}$".format(income - expend))

        if plot:
            labels = ["Income", "Expenses"]
            amounts = [income, expend]

            plt.figure(figsize=(8, 6))
            plt.bar(labels, amounts, color=["green", "red"])
            plt.xlabel("Type")
            plt.ylabel("Amount")
            plt.title("Total Income vs. Expenses")
            plt.show()

            plt.figure(figsize=(8, 6))
            plt.pie(amounts, labels=labels, colors=["green", "red"], autopct="%1.1f%%", startangle=140)
            plt.title("Income vs. Expenses Distribution")
            plt.show()

    except pd.errors.EmptyDataError:
        print("Nothing here!")

def clear_hist():
    cursor.execute("DELETE FROM transactions")
    conn.commit()

def main():
    while True:
        print("\n1. Add new transaction")
        print("2. See summary")
        print("3. See summary in a plot")
        print("4. Clear history")
        print("5. Exit")
        print("-----------------------------")

        try:
            choice = int(input("Your Choice: "))

            if choice == 1:
                new_transaction()

            elif choice == 2:
                summary()

            elif choice == 3:
                summary(True)

            elif choice == 4:
                clear_hist()

            elif choice == 5:
                break
            
            else:
                print("Enter 1, 2, 3, 4, or 5!")

        except ValueError as err:
            print("Enter an integer as input cause: {}".format(err))

if __name__ == "__main__":
    main()
    
conn.close()