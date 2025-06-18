# Rental Car Management System

This is a command-line rental car manager written in Python for **CIS 2368 - Homework 1 (Summer 2025)**. It connects to a MySQL database hosted on AWS and allows users to:

* Add rental car records
* View all rental car records

---

## 📁 Project Structure

```
.
├── rentalcar.py         # Main script
├── README.md            # Project documentation (this file)
```

---

## ⚙️ Setup Instructions

### 1. Clone the GitHub Classroom Repository

Accept the assignment and clone your private repository:

```bash
git clone https://github.com/your-username/homework-1-yourGitHubID.git
cd homework-1-yourGitHubID
```

### 2. Install Dependencies

```bash
pip install mysql-connector-python tabulate
```

### 3. Create the MySQL Table (on AWS)

Run this in your MySQL client:

```sql
USE cis2368summerdb;

CREATE TABLE rentalcar (
    id INT AUTO_INCREMENT PRIMARY KEY,
    passengername VARCHAR(100),
    origincity VARCHAR(100),
    destinationcity VARCHAR(100),
    make VARCHAR(50),
    model VARCHAR(50),
    totalprice DECIMAL(10,2)
);
```

---

## 🚀 Running the Program

```bash
python rentalcar.py
```

### Menu Options

```
[a] Add a rental car
[o] Output all rental car info
[q] Quit
```

---

## 🔐 Database Configuration

The database connection is configured in `rentalcar.py`:

```python
config = {
    'host': 'cis2368summer.cidyiu02y2ba.us-east-1.rds.amazonaws.com',
    'user': 'admin',
    'password': 'Rental#car1234',
    'database': 'cis2368summerdb'
}
```

**⚠️ Warning:** Never use personal or reused passwords. Use only this temporary homework-safe credential.

---

## ✅ GitHub Submission Checklist

* [x] Code compiles and runs
* [x] Minimum 3 meaningful commits
* [x] Code pushed to GitHub Classroom repo (no manual uploads)
* [x] Canvas submission with GitHub repo link

---

## 📌 Author

Shourya Sai Macha — CIS 2368 Summer 2025
