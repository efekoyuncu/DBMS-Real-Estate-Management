# 🏡 Real Estate Management System

This project is a **Real Estate Management System** that integrates **Python** with **MongoDB** and **MySQL** for efficient property and agent management.

## 🔥 Features
✅ **MongoDB Integration**: Handles property listings, agent reviews, and inquiries  
✅ **MySQL Integration**: Populates real estate database with fake data  
✅ **User-Friendly CLI**: Perform CRUD operations via interactive menu  
✅ **Data Filtering & Searching**: Retrieve and filter property and agent details  
✅ **Secure Database Connection Handling**  

---

## 📂 **Project Structure**
```
📦 DBMS_RealEstateProject
 ┣ 📜 connect.py              # MongoDB connection script
 ┣ 📜 main.py                 # MySQL database population script
 ┣ 📜 main2.py                # MongoDB CRUD operations with user interaction
 ┣ 📜 CS 306- Phase IV.pdf    # Project documentation
 ┣ 📜 README.md               # Project documentation (this file)
 ┣ 📜 .gitignore              # Ignore unnecessary files
```

---

## 🚀 **Getting Started**
### **1️⃣ Install Dependencies**
Ensure you have Python installed and install required packages:
```sh
pip install pymongo pymysql faker
```

---

### **2️⃣ Clone the Repository**
```sh
git clone https://github.com/efekoyuncu/DBMS_RealEstateProject.git
cd DBMS_RealEstateProject
```

---

### **3️⃣ Run the Application**
#### **▶️ Start MongoDB-Based System**
```sh
python main2.py
```

#### **▶️ Populate MySQL Database with Fake Data**
```sh
python main.py
```

---

## 📊 **Database Design & Functionality**
### **MongoDB Collections**
- **AgentReviews**: Stores real estate agent reviews with user ratings  
- **PropertyInquiries**: Tracks user inquiries for listed properties  

### **MySQL Tables**
- **RealEstateAgent**: Stores agent details (name, email, specialization, etc.)  
- **Client**: Tracks client info including budget and preferences  
- **Property**: Houses real estate property details  
- **Transaction**: Records all property sales and rental transactions  

---

## 🔧 **Usage Example**
#### **📌 Connecting to MongoDB**
```python
from connect import connectDB
db = connectDB()
```

#### **📌 Inserting a New Property Inquiry**
```python
insert_into_collection(db, "PropertyInquiries", {
    "property_id": "123",
    "user_id": "456",
    "inquiry_message": "Is this still available?",
    "date": "2024-01-31"
})
```

---

## 📎 **Notes**
- Ensure **MongoDB Atlas or Local MongoDB** is running before starting the application.
- Update MySQL connection details (`main.py`) before running the data population script.
- For better performance, avoid inserting a large dataset in MySQL if not required.

---

👨‍💻 Developed by **Efe Koyuncu**  
📍 **Sabancı University - CS306**  

---

 
