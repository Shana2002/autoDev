import sqlite3
import random
import faker

# Initialize Faker for generating random data
fake = faker.Faker()

# Connect to SQLite database
conn = sqlite3.connect('user_details.db')
cursor = conn.cursor()

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
for _ in range(150):
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
conn.close()

print("Database 'user_details.db' with 150 user records created successfully.")
