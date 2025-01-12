import mysql.connector
from mysql.connector import Error
from datetime import datetime

def init_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ankit@1234"
        )
        cursor = connection.cursor()

        cursor.execute("CREATE DATABASE IF NOT EXISTS banking_system")

        cursor.close()
        connection.close()

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ankit@1234",
            database="banking_system"
        )
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Customers (
            CustomerID INT AUTO_INCREMENT PRIMARY KEY,
            FirstName VARCHAR(255) NOT NULL,
            LastName VARCHAR(255) NOT NULL,
            DateOfBirth DATE,
            Address TEXT,
            Phone VARCHAR(15),
            Email VARCHAR(255) UNIQUE,
            CreatedDate DATE
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Accounts (
            AccountID INT AUTO_INCREMENT PRIMARY KEY,
            AccountNumber VARCHAR(20) UNIQUE,
            CustomerID INT,
            AccountType ENUM('Savings', 'Current', 'Fixed Deposit'),
            Balance DECIMAL(15, 2),
            CreatedDate DATE,
            FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Transactions (
            TransactionID INT AUTO_INCREMENT PRIMARY KEY,
            AccountID INT,
            TransactionType ENUM('Credit', 'Debit'),
            Amount DECIMAL(15, 2),
            TransactionDate DATETIME,
            Description TEXT,
            FOREIGN KEY (AccountID) REFERENCES Accounts(AccountID)
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Loans (
            LoanID INT AUTO_INCREMENT PRIMARY KEY,
            CustomerID INT,
            LoanType ENUM('Home', 'Car', 'Education', 'Personal'),
            Amount DECIMAL(15, 2),
            InterestRate DECIMAL(5, 2),
            StartDate DATE,
            EndDate DATE,
            Status ENUM('Active', 'Closed'),
            FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS LoanPayments (
            PaymentID INT AUTO_INCREMENT PRIMARY KEY,
            LoanID INT,
            PaymentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            Amount DECIMAL(15, 2),
            PaymentMethod ENUM('Cash', 'Cheque', 'Online Transfer'),
            FOREIGN KEY (LoanID) REFERENCES Loans(LoanID)
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Employees (
            EmployeeID INT AUTO_INCREMENT PRIMARY KEY,
            FirstName VARCHAR(50),
            LastName VARCHAR(50),
            Position VARCHAR(50),
            Branch VARCHAR(100),
            Email VARCHAR(100) UNIQUE,
            Phone VARCHAR(15),
            HiredDate DATE
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Branches (
            BranchID INT AUTO_INCREMENT PRIMARY KEY,
            BranchName VARCHAR(100),
            Address VARCHAR(255),
            Phone VARCHAR(15),
            ManagerID INT,
            FOREIGN KEY (ManagerID) REFERENCES Employees(EmployeeID)
        )
        """)

        conn.commit()
        cursor.close()
        conn.close()

        print("Database and tables initialized successfully.")

    except Error as e:
        print(f"Error: {e}")


def add_customer():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ankit@1234",
            database="banking_system"
        )
        cursor = conn.cursor()

        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        dob = input("Enter Date of Birth (YYYY-MM-DD): ")
        address = input("Enter Address: ")
        phone = input("Enter Phone: ")
        email = input("Enter Email: ")

        cursor.execute("""
        INSERT INTO Customers (FirstName, LastName, DateOfBirth, Address, Phone, Email, CreatedDate)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (first_name, last_name, dob, address, phone, email, datetime.today().date()))

        conn.commit()
        cursor.close()
        conn.close()
        print("Customer added successfully.")

    except Error as e:
        print(f"Error: {e}")


def view_customers():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ankit@1234",
            database="banking_system"
        )
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM Customers")
        rows = cursor.fetchall()
        print("CustomerID | FirstName | LastName | DateOfBirth | Address | Phone | Email | CreatedDate")
        for row in rows:
            print(" | ".join(str(x) for x in row))

        cursor.close()
        conn.close()

    except Error as e:
        print(f"Error: {e}")


def add_account():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ankit@1234",
            database="banking_system"
        )
        cursor = conn.cursor()

        customer_id = int(input("Enter Customer ID: "))
        account_number = input("Enter Account Number: ")
        account_type = input("Enter Account Type (Savings/Current/Fixed Deposit): ")
        balance = float(input("Enter Initial Balance: "))

        cursor.execute("""
        INSERT INTO Accounts (AccountNumber, CustomerID, AccountType, Balance, CreatedDate)
        VALUES (%s, %s, %s, %s, %s)
        """, (account_number, customer_id, account_type, balance, datetime.today().date()))

        conn.commit()
        cursor.close()
        conn.close()
        print("Account added successfully.")

    except Error as e:
        print(f"Error: {e}")


def view_accounts():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ankit@1234",
            database="banking_system"
        )
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM Accounts")
        rows = cursor.fetchall()
        print("AccountID | AccountNumber | CustomerID | AccountType | Balance | CreatedDate")
        for row in rows:
            print(" | ".join(str(x) for x in row))

        cursor.close()
        conn.close()

    except Error as e:
        print(f"Error: {e}")


def add_loan():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ankit@1234",
            database="banking_system"
        )
        cursor = conn.cursor()

        customer_id = int(input("Enter Customer ID: "))
        loan_type = input("Enter Loan Type (Home/Car/Education/Personal): ")
        amount = float(input("Enter Loan Amount: "))
        interest_rate = float(input("Enter Interest Rate: "))
        start_date = input("Enter Start Date (YYYY-MM-DD): ")
        end_date = input("Enter End Date (YYYY-MM-DD): ")
        status = input("Enter Loan Status (Active/Closed): ")

        cursor.execute("""
        INSERT INTO Loans (CustomerID, LoanType, Amount, InterestRate, StartDate, EndDate, Status)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (customer_id, loan_type, amount, interest_rate, start_date, end_date, status))

        conn.commit()
        cursor.close()
        conn.close()
        print("Loan added successfully.")

    except Error as e:
        print(f"Error: {e}")


def view_loans():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ankit@1234",
            database="banking_system"
        )
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM Loans")
        rows = cursor.fetchall()
        print("LoanID | CustomerID | LoanType | Amount | InterestRate | StartDate | EndDate | Status")
        for row in rows:
            print(" | ".join(str(x) for x in row))

        cursor.close()
        conn.close()

    except Error as e:
        print(f"Error: {e}")


def add_loan_payment():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ankit@1234",
            database="banking_system"
        )
        cursor = conn.cursor()

        loan_id = int(input("Enter Loan ID: "))
        amount = float(input("Enter Payment Amount: "))
        payment_method = input("Enter Payment Method (Cash/Cheque/Online Transfer): ")

        cursor.execute("""
        INSERT INTO LoanPayments (LoanID, Amount, PaymentMethod)
        VALUES (%s, %s, %s)
        """, (loan_id, amount, payment_method))

        conn.commit()
        cursor.close()
        conn.close()
        print("Loan payment added successfully.")

    except Error as e:
        print(f"Error: {e}")


def view_loan_payments():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ankit@1234",
            database="banking_system"
        )
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM LoanPayments")
        rows = cursor.fetchall()
        print("PaymentID | LoanID | PaymentDate | Amount | PaymentMethod")
        for row in rows:
            print(" | ".join(str(x) for x in row))

        cursor.close()
        conn.close()

    except Error as e:
        print(f"Error: {e}")


def random_query():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ankit@1234",
            database="banking_system"
        )
        cursor = conn.cursor()

        print("Enter your custom SQL query (e.g., SELECT, INSERT, UPDATE, DELETE, etc.):")
        query = input()
        
        cursor.execute(query)

        if query.strip().lower().startswith('select'):
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        else:
            conn.commit()
            print("Query executed successfully.")

        cursor.close()
        conn.close()

    except Error as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    init_db()

    while True:
        print("\nBanking System Menu")
        print("1. Add Customer")
        print("2. View Customers")
        print("3. Add Account")
        print("4. View Accounts")
        print("5. Add Loan")
        print("6. View Loans")
        print("7. Add Loan Payment")
        print("8. View Loan Payments")
        print("9. Execute Custom Query")
        print("10. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_customer()
        elif choice == 2:
            view_customers()
        elif choice == 3:
            add_account()
        elif choice == 4:
            view_accounts()
        elif choice == 5:
            add_loan()
        elif choice == 6:
            view_loans()
        elif choice == 7:
            add_loan_payment()
        elif choice == 8:
            view_loan_payments()
        elif choice == 9:
            random_query()
        elif choice == 10:
            break
        else:
            print("Invalid choice. Please try again.")
