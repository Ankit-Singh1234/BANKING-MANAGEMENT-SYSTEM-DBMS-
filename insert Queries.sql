-- Insert customers
INSERT INTO banking_system.customers (FirstName, LastName, DateOfBirth, Address, Phone, Email, CreatedDate) VALUES
('Rahul', 'Sharma', '1990-05-12', '123 MG Road, Delhi', '9876543210', 'rahul.sharma@example.com', '2024-12-12'),
('Amit', 'Verma', '1985-09-22', '456 BBD Chowk, Lucknow', '9876543211', 'amit.verma@example.com', '2024-12-12'),
('Ravi', 'Kumar', '1992-02-10', '789 Gariahat, Kolkata', '9876543212', 'ravi.kumar@example.com', '2024-12-12'),
('Vikash', 'Singh', '1987-07-15', '12, Park Street, Chennai', '9876543213', 'vikash.singh@example.com', '2024-12-12'),
('Suresh', 'Patel', '1994-11-30', '43, Sadar Bazaar, Ahmedabad', '9876543214', 'suresh.patel@example.com', '2024-12-12'),
('Ajay', 'Reddy', '1991-04-25', '101, Brigade Road, Bangalore', '9876543215', 'ajay.reddy@example.com', '2024-12-12'),
('Sandeep', 'Gupta', '1989-03-18', '56, Rajpath, Patna', '9876543216', 'sandeep.gupta@example.com', '2024-12-12'),
('Prakash', 'Yadav', '1993-12-05', '36, MG Road, Pune', '9876543217', 'prakash.yadav@example.com', '2024-12-12'),
('Manoj', 'Joshi', '1988-01-10', '78, Old Mumbai, Mumbai', '9876543218', 'manoj.joshi@example.com', '2024-12-12'),
('Nitin', 'Kumar', '1995-08-20', '9, Surat Road, Jaipur', '9876543219', 'nitin.kumar@example.com', '2024-12-12');

-- Insert accounts
INSERT INTO banking_system.Accounts (AccountNumber, CustomerID, AccountType, Balance, CreatedDate) VALUES
('ACC001', 1, 'Savings', 10000.50, '2024-12-12'),
('ACC002', 2, 'Current', 20000.75, '2024-12-12'),
('ACC003', 3, 'Fixed Deposit', 50000.00, '2024-12-12'),
('ACC004', 4, 'Savings', 15000.25, '2024-12-12'),
('ACC005', 5, 'Current', 8000.00, '2024-12-12'),
('ACC006', 6, 'Fixed Deposit', 20000.00, '2024-12-12'),
('ACC007', 7, 'Savings', 12000.30, '2024-12-12'),
('ACC008', 8, 'Current', 10000.80, '2024-12-12'),
('ACC009', 9, 'Savings', 35000.60, '2024-12-12'),
('ACC010', 10, 'Fixed Deposit', 25000.40, '2024-12-12');

-- Insert loans
INSERT INTO banking_system.Loans (CustomerID, LoanType, Amount, InterestRate, StartDate, EndDate, Status) VALUES
(1, 'Home', 500000.00, 6.50, '2023-01-15', '2033-01-15', 'Active'),
(2, 'Car', 200000.00, 7.00, '2023-05-20', '2028-05-20', 'Active'),
(3, 'Education', 150000.00, 8.00, '2023-07-01', '2028-07-01', 'Closed'),
(4, 'Personal', 100000.00, 9.00, '2023-02-25', '2026-02-25', 'Active'),
(5, 'Home', 600000.00, 6.75, '2022-11-10', '2032-11-10', 'Active'),
(6, 'Car', 250000.00, 7.25, '2023-03-05', '2028-03-05', 'Closed'),
(7, 'Personal', 50000.00, 8.50, '2023-06-10', '2026-06-10', 'Active'),
(8, 'Education', 100000.00, 7.50, '2023-04-20', '2028-04-20', 'Closed'),
(9, 'Home', 400000.00, 6.25, '2022-09-15', '2032-09-15', 'Active'),
(10, 'Personal', 80000.00, 8.75, '2023-08-30', '2026-08-30', 'Closed');

-- Insert loan payments
INSERT INTO banking_system.LoanPayments (LoanID, Amount, PaymentMethod) VALUES
(1, 5000.00, 'Online Transfer'),
(2, 10000.00, 'Cheque'),
(3, 5000.00, 'Cash'),
(4, 2000.00, 'Cheque'),
(5, 6000.00, 'Online Transfer'),
(6, 15000.00, 'Cash'),
(7, 2000.00, 'Cheque'),
(8, 1000.00, 'Online Transfer'),
(9, 7000.00, 'Cash'),
(10, 3000.00, 'Online Transfer');

-- Insert employees
INSERT INTO banking_system.Employees (FirstName, LastName, Position, Branch, Email, Phone, HiredDate) VALUES
('Anil', 'Kumar', 'Manager', 'Delhi Branch', 'anil.kumar@bank.com', '9999999990', '2018-06-25'),
('Pankaj', 'Singh', 'Manager', 'Lucknow Branch', 'pankaj.singh@bank.com', '9999999991', '2019-07-15'),
('Kishore', 'Patel', 'Clerk', 'Kolkata Branch', 'kishore.patel@bank.com', '9999999992', '2020-08-05'),
('Ravi', 'Sharma', 'Assistant Manager', 'Chennai Branch', 'ravi.sharma@bank.com', '9999999993', '2021-05-10'),
('Vikram', 'Joshi', 'Manager', 'Ahmedabad Branch', 'vikram.joshi@bank.com', '9999999994', '2017-09-22'),
('Rajeev', 'Reddy', 'Assistant Manager', 'Bangalore Branch', 'rajeeve.reddy@bank.com', '9999999995', '2022-01-15'),
('Sandeep', 'Rathore', 'Clerk', 'Patna Branch', 'sandeep.rathore@bank.com', '9999999996', '2023-04-12'),
('Manoj', 'Gupta', 'Manager', 'Pune Branch', 'manoj.gupta@bank.com', '9999999997', '2016-03-08'),
('Nikhil', 'Yadav', 'Clerk', 'Jaipur Branch', 'nikhil.yadav@bank.com', '9999999998', '2020-10-20'),
('Arvind', 'Chauhan', 'Assistant Manager', 'Mumbai Branch', 'arvind.chauhan@bank.com', '9999999999', '2021-11-18');

-- Insert branches
INSERT INTO banking_system.Branches (BranchName, Address, Phone, ManagerID) VALUES
('Delhi Branch', '123 Connaught Place, New Delhi', '011-23456789', 1),
('Lucknow Branch', '456 Hazratganj, Lucknow', '0522-2345678', 2),
('Kolkata Branch', '789 Park Street, Kolkata', '033-23456789', 3),
('Chennai Branch', '101 T. Nagar, Chennai', '044-23456789', 4),
('Ahmedabad Branch', '123 SG Road, Ahmedabad', '079-23456789', 5),
('Bangalore Branch', '100 MG Road, Bangalore', '080-23456789', 6),
('Patna Branch', '12 Boring Road, Patna', '0612-2345678', 7),
('Pune Branch', '45 FC Road, Pune', '020-23456789', 8),
('Jaipur Branch', '78 MI Road, Jaipur', '0141-2345678', 9),
('Mumbai Branch', '101 Nariman Point, Mumbai', '022-23456789', 10);
