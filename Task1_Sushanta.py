
## create an accounts.txt file 
with open('accounts.txt', mode='w') as accounts:
    accounts.write('100 Jones 24.98\n')
    accounts.write('200 Doe 345.67\n')
    accounts.write('300 Williams 0.00\n')
    accounts.write('400 Stone -42.16\n')
    accounts.write('500 Rich 224.62\n')

# Open the file 'accounts.txt' in read mode
with open('accounts.txt', mode='r') as accounts:
    # Print the header of the table
    print(f'{"Account":<10}{"Name":<10}{"Balance":>10}')
    # Iterate over each line (record) in the file
    for record in accounts:
        # Split the line into account, name, and balance
        account, name, balance = record.split()
        # Print each record in a formatted manner
        print(f'{account:<10}{name:<10}{balance:>10}')

# Open the file 'accounts.txt' in read mode
accounts = open('accounts.txt', 'r')

# Open a temporary file 'temp_file.txt' in write mode
temp_file = open('temp_file.txt', 'w')

# Use a context manager to ensure both files are closed at the end
with accounts, temp_file:
    # Iterate over each line (record) in the accounts file
    for record in accounts:
        # Split the line into account, name, and balance
        account, name, balance = record.split()
        # Check if the account number is not '300'
        if account != '300':
            # If it's not '300', write the record as is to the temp file
            temp_file.write(record)
        else:
            # If it is '300', change the name to 'Williams' and write to the temp file
            new_record = ' '.join([account, 'Williams', balance])
            temp_file.write(new_record + '\n')

# Import the json module
import json

# Define a dictionary with account information
accounts_dict = {
    'accounts': [
        {'account': 100, 'name': 'Jones', 'balance': 24.98},
        {'account': 200, 'name': 'Doe', 'balance': 345.67}
    ]
}

# Open the file 'accounts.json' in write mode
with open('accounts.json', 'w') as accounts:
    # Use the json module's dump function to serialize the dictionary 'accounts_dict' into the file
    json.dump(accounts_dict, accounts)

# Save a dictionary into a pickle file.
import pickle

favorite_color = { "lion": "yellow", "kitty": "red" }

pickle.dump( favorite_color, open( "save.p", "wb" ) )

# dividebyzero.py
'''Simple exception handling example.'''

# Start an infinite loop
while True:
    # Try to execute the following code block
    try:
        # Ask the user for the numerator and convert it to an integer
        number1 = int(input('Enter numerator: '))
        # Ask the user for the denominator and convert it to an integer
        number2 = int(input('Enter denominator: '))
        # Divide the numerator by the denominator
        result = number1 / number2
    # If a ValueError occurs (non-numeric value entered), print an error message
    except ValueError: 
        print('You must enter two integers\n')
    # If a ZeroDivisionError occurs (denominator was 0), print an error message
    except ZeroDivisionError: 
        print('Attempted to divide by zero\n')
    # If no exceptions occur, print the result and break the loop
    else: 
        print(f'{number1:.3f} / {number2:.3f} = {result:.3f}')
        break # terminate the loop

try:
    # This is the code that will be executed
    print('try suite with no exceptions raised')
    # Raise an exception
    raise Exception('This is a custom exception')
except Exception as e:
    # This code will be executed because an exception is raised in the try block
    print(f'An exception occurred: {e}')
else:
    # This code will not be executed because an exception was raised in the try block
    print('else executes because no exceptions in the try suite')
finally:
    # This code will always be executed, regardless of whether an exception was raised or not
    print('finally always executes')

# Import the csv module
import csv

# Open the accounts.csv file in write mode
with open('accounts.csv', mode='w', newline='') as accounts:
    # Create a writer object
    writer = csv.writer(accounts)
    # Write rows to the CSV file
    writer.writerow([100, 'Jones', 24.98])
    writer.writerow([200, 'Doe', 345.67])
    writer.writerow([300, 'White', 0.00])
    writer.writerow([400, 'Stone', -42.16])
    writer.writerow([500, 'Rich', 224.62])

#  read the CSV data from the file
with open('accounts.csv', 'r', newline='') as accounts:
    # Print the header
    print(f'{"Account":<10}{"Name":<10}{"Balance":>10}')
    # Create a reader object
    reader = csv.reader(accounts)
    # Iterate over each record in the CSV file
    for record in reader:
        # Unpack the record
        account, name, balance = record
        # Print the record
        print(f'{account:<10}{name:<10}{balance:>10}')

# Import the pandas module
import pandas as pd

# Read the CSV file from the URL and store it in a DataFrame
titanic = pd.read_csv('TitanicSurvival.csv')

# Set the precision for floating-point values
pd.set_option('precision', 2)

# Display the first five rows of the DataFrame
print(titanic.head())

# Display the last five rows of the DataFrame
print(titanic.tail())
