import sqlite3
import tkinter as tk

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS UserAccounts(
                user_id INTERGER PRIMARY KEY,
                email TEXT,
                username TEXT,
                password TEXT,
                phone_number TEXT
                )
''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Incomes(
                income_id INTEGER PRIMARY KEY,
                name TEXT,
                amount REAL,
                user_id INTEGER,
                FOREIGN KEY (user_id) REFERENCES UserAccounts(user_id)
                )
''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Expenses(
                expense_id INTEGER PRIMARY KEY,
                name TEXT,
                amount REAL,
                user_id INTEGER,
                FOREIGN KEY (user_id) REFERENCES UserAccounts(user_id)
                )
''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Balance(
                balance_id INTEGER PRIMARY KEY,
                user_id INTEGER,
                FOREIGN KEY (user_id) REFERENCES UserAccounts(user_id)
                )
''')

conn.commit()
def insert_income():
    name = income_name.get()
    amount = float(income_amount.get())
    user_id = 1  # For simplicity, assuming a single user with userid 1
    cursor.execute('INSERT INTO Incomes (name, amount, user_id) VALUES (?, ?, ?)', (name, amount, user_id))
    conn.commit()
    update_balance_label()

# Create a function to insert an expense
def insert_expense():
    name = expense_name.get()
    amount = float(expense_amount.get())
    user_id = 1  # For simplicity, assuming a single user with userid 1
    cursor.execute('INSERT INTO Expenses (name, amount, user_id) VALUES (?, ?, ?)', (name, amount, user_id))
    conn.commit()
    update_balance_label()

# Create a function to update the balance label
def update_balance_label():
    user_id = 1  # For simplicity, assuming a single user with userid 1
    cursor.execute('SELECT SUM(amount) FROM Incomes WHERE user_id = ?', (user_id,))
    total_income = cursor.fetchone()[0] or 0
    cursor.execute('SELECT SUM(amount) FROM Expenses WHERE user_id = ?', (user_id,))
    total_expense = cursor.fetchone()[0] or 0
    balance = total_income - total_expense
    balance_label.config(text=f'Balance: ${balance:.2f}')

# Create the main application window
root = tk.Tk()
root.title("Financial Management App")

# Create and configure Tkinter widgets for adding income
income_frame = tk.Frame(root)
income_frame.pack(padx=10, pady=10, anchor="w")

income_label = tk.Label(income_frame, text="Add Income:")
income_label.grid(row=0, column=0)

income_name_label = tk.Label(income_frame, text="Name:")
income_name_label.grid(row=1, column=0)

income_name = tk.Entry(income_frame)
income_name.grid(row=1, column=1)

income_amount_label = tk.Label(income_frame, text="Amount:")
income_amount_label.grid(row=1, column=2)

income_amount = tk.Entry(income_frame)
income_amount.grid(row=1, column=3)

income_button = tk.Button(income_frame, text="Add", command=insert_income)
income_button.grid(row=1, column=4)

# Create and configure Tkinter widgets for adding expense
expense_frame = tk.Frame(root)
expense_frame.pack(padx=10, pady=10, anchor="w")

expense_label = tk.Label(expense_frame, text="Add Expense:")
expense_label.grid(row=0, column=0)

expense_name_label = tk.Label(expense_frame, text="Name:")
expense_name_label.grid(row=1, column=0)

expense_name = tk.Entry(expense_frame)
expense_name.grid(row=1, column=1)

expense_amount_label = tk.Label(expense_frame, text="Amount:")
expense_amount_label.grid(row=1, column=2)

expense_amount = tk.Entry(expense_frame)
expense_amount.grid(row=1, column=3)

expense_button = tk.Button(expense_frame, text="Add", command=insert_expense)
expense_button.grid(row=1, column=4)

# Create and configure Tkinter label for displaying balance
balance_label = tk.Label(root, text="Balance: $0.00")
balance_label.pack(padx=10, pady=10)

# Update balance label initially
update_balance_label()

# Start the Tkinter main loop
root.mainloop()

# Close the database connection when the application is closed
conn.close()
