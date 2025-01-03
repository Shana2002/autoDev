import sqlite3
import random
import faker
import os
# Initialize Faker for generating random data
fake = faker.Faker()

# Connect to SQLite database
conn = sqlite3.connect('database/user_details.db')
cursor = conn.cursor()

def createTable():
    # Create table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            username TEXT,
            password TEXT,
            address TEXT,
            email TEXT,
            mobile TEXT,
            address_line1 TEXT,
            address_line2 TEXT,
            country TEXT,
            postal_code TEXT,
            city TEXT
        )
    ''')

    # Generate and insert 150 user records
    for _ in range(1000):
        first_name = fake.first_name()
        last_name = fake.last_name()
        username = f"{first_name.lower()}.{last_name.lower()}{random.randint(10, 99)}"
        password = fake.password()
        address = fake.address().replace("\n", ", ")
        email = f"{first_name.lower()}.{last_name.lower()}@{fake.free_email_domain()}"
        mobile = fake.phone_number()
        address_line1 = fake.street_address()
        address_line2 = fake.secondary_address()
        country = fake.country()
        postal_code = fake.postcode()
        city = fake.city()

        cursor.execute('''
            INSERT INTO users (
                first_name, last_name, username, password, address, email, mobile,
                address_line1, address_line2, country, postal_code, city
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (first_name, last_name, username, password, address, email, mobile,
            address_line1, address_line2, country, postal_code, city))

    # Commit changes and close connection
    conn.commit()
    

    print("Database 'user_details.db' with 1000 user records created successfully.")

def createProductTable():
    # Create the products table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT,
            type TEXT,
            description TEXT,
            price REAL
        )
    ''')

    # Define some product types
    product_types = ['Electronics', 'Clothing', 'Furniture', 'Beauty', 'Toys', 'Food', 'Books', 'Sports']

    # Generate and insert 150 product records
    for _ in range(1000):
        product_name = fake.word().capitalize() + " " + fake.word().capitalize()
        type_ = random.choice(product_types)
        description = fake.text(max_nb_chars=100)
        price = round(random.uniform(10, 500), 2)

        cursor.execute('''
            INSERT INTO products (
                product_name, type, description, price
            ) VALUES (?, ?, ?, ?)
        ''', (product_name, type_, description, price))

    # Commit changes and close connection
    conn.commit()
    

    print("Database 'products.db' with 1000 product records created successfully.")

# table names

def get_table():
    tables_data = cursor.execute('SELECT name FROM sqlite_master WHERE type = "table"').fetchall()
    tables_name = {}
    for table in tables_data:
        if table[0] != "sqlite_sequence":
            column_data = cursor.execute(f"PRAGMA table_info({table[0]})").fetchall()
            colums = []
            for colum in column_data:
                colums.append(colum[1])
            tables_name[table[0]] = colums
    
    return tables_name
            
      
    # print(cursor.execute("PRAGMA table_info('users')").fetchall())



def reset_db():
    cursor.execute('drop table users')
    cursor.execute('drop table products')
    createTable()
    createProductTable()

