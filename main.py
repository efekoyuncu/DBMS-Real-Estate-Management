from faker import Faker
import random
import pymysql

fake = Faker()

conn = pymysql.connect(
    host='localhost',  # Update with your details
    user='root',
    password='Nurdan4980',
    db='REMS',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with conn.cursor() as cur:
        # Populate RealEstateAgent table
        for _ in range(1000000):  # One million records
            first_name = fake.first_name()
            last_name = fake.last_name()
            email = fake.email()
            contact_number = fake.phone_number()[:20]  # Truncate to 20 characters
            specialization = fake.random_element(elements=('Residential', 'Commercial'))
            license_number = fake.bothify(text='???-#####')

            cur.execute("INSERT INTO RealEstateAgent (FirstName, LastName, Email, ContactNumber, Specialization, LicenseNumber) VALUES (%s, %s, %s, %s, %s, %s)",
                        (first_name, last_name, email, contact_number, specialization, license_number))

        # Populate Client table
        for _ in range(1000000):  # One million records
            first_name = fake.first_name()
            last_name = fake.last_name()
            email = fake.email()
            contact_number = fake.phone_number()
            budget = random.uniform(100000.0, 1000000.0)
            preferences = fake.text(max_nb_chars=200)

            cur.execute("INSERT INTO Client (FirstName, LastName, Email, ContactNumber, Budget, PropertyPreferences) VALUES (%s, %s, %s, %s, %s, %s)",
                        (first_name, last_name, email, contact_number, budget, preferences))

        # Populate Property table
        for _ in range(1000000):  # One million records
            property_type = fake.random_element(elements=('House', 'Apartment', 'Condo'))
            address = fake.address()
            area = random.uniform(500.0, 3000.0)
            bedrooms = random.randint(1, 5)
            bathrooms = random.randint(1, 3)
            price = random.uniform(100000.0, 500000.0)
            status = fake.random_element(elements=('Available', 'Under Contract', 'Sold'))

            cur.execute("INSERT INTO Property (PropertyType, Address, Area, Bedrooms, Bathrooms, Price, AvailabilityStatus) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                        (property_type, address, area, bedrooms, bathrooms, price, status))

        # Populate Transaction table
        for _ in range(1000000):  # One million records
            property_id = random.randint(1, 1000000)
            client_id = random.randint(1, 1000000)
            agent_id = random.randint(1, 1000000)
            transaction_date = fake.date_between(start_date='-2y', end_date='today')
            transaction_type = fake.random_element(elements=('Sale', 'Rent'))
            price = random.uniform(100000.0, 500000.0)

            cur.execute("INSERT INTO Transaction (PropertyID, ClientID, AgentID, TransactionDate, TransactionType, Price) VALUES (%s, %s, %s, %s, %s, %s)",
                        (property_id, client_id, agent_id, transaction_date, transaction_type, price))

        conn.commit()
finally:
    conn.close()
