import mysql.connector
from tabulate import tabulate

# rentalcar.py
config = {
    'host': 'cis2368summer.cidyiu02y2ba.us-east-1.rds.amazonaws.com', #hostname address
    'port': 3306,  # default MySQL port
    'user': 'admin', # username
    # password for the user
    'password': 'Rental#car1234',
    'database': 'cis2368summerdb',
}

def connect_db():
    return mysql.connector.connect(**config)

def add_rental_car(): # Function to add a rental car record
    name = input("Enter passenger name: ")
    origin = input("Enter origin city: ")
    destination = input("Enter destination city: ")
    make = input("Enter car make: ")
    model = input("Enter car model: ")
    price = float(input("Enter total price: "))

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO rentcar (passengername, origincity, destinationcity, make, model, totalprice)
        VALUES (%s, %s, %s, %s, %s, %s) 
    """, (name, origin, destination, make, model, price))
    conn.commit()
    print("Rental car info added.\n")
    cursor.close()
    conn.close()

def output_all_rentals():  # Function to output all rental car records
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM rentcar")  # Fetch all records from the rentcar table
    records = cursor.fetchall()  # Fetch all records
    if not records: #
        print("No records found.")
    else:
        headers = [i[0] for i in cursor.description]
        print("\nAll rental car records:")
        # Print the records in a tabular format using tabulate
        print(tabulate(records, headers=headers, tablefmt='grid'))
        print()
    cursor.close()
    conn.close()

def main():  # Main function to run the menu
    while True:
        print("""
==================Menu==================
    [a] Add a rental car
    [o] Output all rental car info
    [q] Quit
========================================
        """)
        choice = input("Choose an option: ").lower()
        if choice == 'a': # If user chooses to add a rental car
            add_rental_car()
        elif choice == 'o': # If user chooses to output all rental car info
            output_all_rentals()
        elif choice == 'q': # If user chooses to quit
            print("Exiting...")
            break
        else: # If user enters an invalid option
            print("Invalid option. Try again.\n")

if __name__ == "__main__":
    main()
# This code is a simple rental car management system that allows users to add rental car records and output all records.
# It connects to a MySQL database and performs the necessary operations.