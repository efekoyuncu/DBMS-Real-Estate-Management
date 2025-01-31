from pymongo import MongoClient, errors
from bson import ObjectId
from faker import Faker

def connectDB():
    uri = "mongodb+srv://efekoyuncu:eFe2012.@cluster0.s3vsylf.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri)
    try:
        db = client['my_database_name']
        db.command('ping')  # Check the MongoDB connection
        print("Successfully connected to MongoDB!")
        return db
    except errors.ConnectionFailure as e:
        print(f"Could not connect to MongoDB: {e}")
        return None

def createCollection(db, collection_name):
    if collection_name not in db.list_collection_names():
        db.create_collection(collection_name)
        print(f"Collection '{collection_name}' created successfully.")
    else:
        print(f"Collection '{collection_name}' already exists.")

def read_all_data(db, collection_name):
    collection = db[collection_name]
    documents = collection.find()
    for doc in documents:
        print(doc)

def insert_into_collection(db, collection_name, data):
    collection = db[collection_name]
    result = collection.insert_one(data)
    print("The data was successfully inserted!")
    print(f"Inserted document ID: {result.inserted_id}")

def delete_record_by_id(db, collection_name, record_id):
    collection = db[collection_name]
    result = collection.delete_one({'_id': ObjectId(record_id)})
    if result.deleted_count:
        print("The record was successfully deleted!")
    else:
        print("No matching record found to delete.")

def update_record_by_id(db, collection_name, record_id, update_data):
    collection = db[collection_name]
    result = collection.update_one({'_id': ObjectId(record_id)}, {'$set': update_data})
    if result.modified_count:
        print("The record was successfully updated!")
    else:
        print("No matching record found to update.")

def read_data_with_filter(db, collection_name, filter_query):
    collection = db[collection_name]
    documents = collection.find(filter_query)
    for doc in documents:
        print(doc)

def main_menu(db):
    user_id = input("Welcome to Review Portal!\nPlease enter your user id:\n ")

    while True:

        print("\nPlease pick the option that you want to proceed.")
        print("1- Create a collection.")
        print("2- Read all data in a collection.")
        print("3- Read some part of the data while filtering.")
        print("4- Insert data.")
        print("5- Delete data.")
        print("6- Update data.")
        print("7- Exit.")
        choice = input("Please select an option: ")

        if choice == '1':
            collection_name = input("Enter the name of the collection to create: ")
            createCollection(db, collection_name)
        elif choice == '2':
            collection_name = input("Enter the name of the collection to read from: ")
            read_all_data(db, collection_name)
        elif choice == '3':
            collection_name = input("Enter the name of the collection to filter data from: ")
            query_field = input("Enter the field name to filter by: ")
            query_value = input("Enter the value to filter by: ")
            filter_query = {query_field: query_value}
            read_data_with_filter(db, collection_name, filter_query)
        elif choice == '4':
            print("Please select the collection you want to insert data into:")
            print("1- Agent Reviews")
            print("2- Property Inquiries")
            selected_option = input("Selected option: ")

            if selected_option == '1':
                collection_name = "AgentReviews"
                print("Please enter the review details:")
                review_data = {
                    "agent_id": input("Agent ID: "),
                    "user_id": user_id,  # Using the user_id entered at the start
                    "review_message": input("Review Message: "),
                    "given_star": int(input("Given Star (1-5): "))
                }
                insert_into_collection(db, collection_name, review_data)

            elif selected_option == '2':
                collection_name = "PropertyInquiries"
                print("Please enter the inquiry details:")
                inquiry_data = {
                    "property_id": input("Property ID: "),
                    "user_id": user_id,  # Using the user_id entered at the start
                    "inquiry_message": input("Inquiry Message: "),
                    "date": input("Date (YYYY-MM-DD): ")
                }
                insert_into_collection(db, collection_name, inquiry_data)
            else:
                print("Invalid selection.")
        elif choice == '5':
            collection_name = input("Enter the name of the collection to delete from: ")
            record_id = input("Enter the ID of the record to delete: ")
            delete_record_by_id(db, collection_name, record_id)
        elif choice == '6':
            collection_name = input("Enter the name of the collection to update: ")
            record_id = input("Enter the ID of the record to update: ")
            update_field = input("Enter the field name to update: ")
            update_value = input("Enter the new value for the field: ")
            update_record_by_id(db, collection_name, record_id, {update_field: update_value})
        elif choice == '7':
            print("Exiting the system.")
            break
        else:
            print("Invalid option selected. Please try again.")

        continue_choice = input("\nWould you like to perform another action? (yes/no): ")
        if continue_choice.lower() != 'yes':
            print("Exiting Real Estate Management System.")
            break

if __name__ == "__main__":
    db = connectDB()
    if db is not None:
        main_menu(db)
