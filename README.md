🏦 VanshBank — Banking System

A simple console-based banking system built with Python.

This project was created to practice Object-Oriented Programming (OOP), JSON file handling, functions, loops, and basic data persistence in Python.

✨ Features

- ➕ Create a new bank account
- 👤 View all existing accounts
- 💰 Deposit money
- 💸 Withdraw money
- 💵 Check account balance
- 💾 Automatically save account data to a JSON file
- 🔄 Load previously saved accounts when the program starts

🛠️ Technologies Used

- Python
- OOP (Object-Oriented Programming)
- JSON
- OS Module
- File Handling

📂 How It Works

When the program starts, it checks whether "accounts.json" exists.

- If the file exists → previously saved accounts are loaded.
- If it doesn't exist → a new account database is created when the first account is added.

Account information is stored in JSON format.

Example:

[
    {
        "name": "Vansh",
        "account_no": 101,
        "balance": 5000
    }
]

🚀 How to Run

Make sure Python is installed on your system.

Clone the repository:

git clone YOUR_GITHUB_REPOSITORY_URL

Go into the project directory:

cd VanshBank

Run the program:

python main.py

📋 Available Options

1. Add Account
2. See Accounts
3. Withdraw The Money
4. Deposit The Money
5. Exit

1️⃣ Add Account

Enter:

- Your name
- Account number
- Initial balance

The account will be saved automatically.

2️⃣ See Accounts

Displays all accounts currently stored in the system along with their balance.

3️⃣ Withdraw Money

Enter your account number and the amount you want to withdraw.

The system checks whether sufficient balance is available before completing the transaction.

4️⃣ Deposit Money

Enter your account number and the amount you want to deposit.

The balance is updated and saved automatically.

5️⃣ Exit

Closes the banking system.

🧠 What I Learned From This Project

While building VanshBank, I practiced:

- Creating classes and objects
- Using "__init__()" and "self"
- Encapsulation using private attributes
- Creating methods
- Working with lists of objects
- Searching objects inside a list
- Reading and writing JSON files
- Using the "os" module
- Saving persistent data
- Using functions to avoid repeated code
- Handling basic banking operations

⚠️ Current Limitations

This is a learning project, not a real banking application.

It currently does not include:

- User authentication / PIN
- Transaction history
- Account deletion
- Advanced input validation
- Encryption
- Database system
- Multi-user security

These may be added in future versions.

🔧 Future Improvements

Possible improvements:

- 🔐 Add PIN/password authentication
- 📜 Add transaction history
- 🗑️ Add account deletion
- 🔎 Add better account searching
- 🛡️ Improve input validation and error handling
- 🗄️ Replace JSON storage with SQLite/database
- 🧾 Generate transaction records
- 🏦 Add more banking features

📸 Feedback / Suggestions

If you use this project and find a bug, have a suggestion, or notice something that could be improved, feel free to contact me on Instagram:

Instagram: https://www.instagram.com/er.vanshbankar?stkn=MWtrc2N2OG00YXBxbg==

👨‍💻 Author

VANSH BANKAR

Built while learning Python and Object-Oriented Programming.

---

⭐ If you find this project useful for learning, feel free to star the repository!

This project is part of my journey to improve my Python programming and software development skills.
