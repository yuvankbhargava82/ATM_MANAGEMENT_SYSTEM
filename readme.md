# 🏦 ATM Management System

A console-based ATM (Automated Teller Machine) simulation system built with Python that provides essential banking operations with robust security features. 


## 🎯 Overview
I built this as a way to simulate how ATMs actually work.It provides a secure and user-friendly interface for basic banking transactions including balance inquiry, cash withdrawal, deposits, and PIN management.

## ✨ Features

### 🔐 Authentication & Security
- **Username Validation**: Checks if you're a real user before letting you in
- **PIN Protection**: 4-digit PIN authentication system
- **Account Lockout**: Automatic card lock after 3 failed PIN attempts
- **PIN Change**:  You can change your PIN whenever you want, with confirmation

### 💰 Banking Operations
- **Balance Statement**: Check current account balance
- **Cash Withdrawal**: 
  - Withdraw money from your account
  - System makes sure the amount is a multiple of 10 (like real ATMs)
  - Checks for sufficient balance,Won't let you withdraw more than you have
- **Deposits (Lodgement)**:
  - Deposit cash directly
  - Deposit via cheque
  - Amount validation (multiple of 10)
-  **All transactions are validated**: No weird transactions going through

### 🎨 User Interface
- Simple menu-driven console
- Easy to navigate
- Error messages that actually tell you what went wrong
- Formatted output that's easy to read

## 🖥️ System Requirements

- **Python**: Needs version 3.x or higher
- **Operating System**: Works on Windows, Mac, or Linux
- **Memory**: Minimal (Less than 50 MB)
- **Storage**: Takes up less than 1 MB

## 📦 Getting Started

### Step 1: Make Sure Python is Installed

```
python --version
```

### Step 3: Run the Application

```
python atm_system.py
```

## 🚀 How to Use It

### Login

1. **Start the program** and enter your username
   - Test usernames: `user1`, `user2`, `user3`

2. **Enter your PIN**:
   - user1: `1234`
   - user2: `2222`
   - user3: `3333`


### Main Menu Options

Once logged in, you can select from the following operations:

| Options | What You Press | What Happens |
|--------|---------|-------------|
| **Check Balance** | `S` | Shows your account balance |
| **Withdraw** | `W` | Withdraw cash from account |
| **Deposit** | `L` | Put cash or cheques in |
| **Change PIN** | `P` | Update your 4-digit PIN |
| **Exit** | `E` | Exit the ATM system |


### Example Session

```
Enter User Name: user1
------------------
Please Enter your PIN: 1234
------------------
-------------------------
LOGIN SUCCESSFUL
-------------------------

User1 Welcome to the ATM
----------ATM SYSTEM-----------
-------------------------------
SELECT FROM FOLLOWING OPTIONS: 
Statement__(S) 
Withdraw___(W) 
Lodgement__(L)  
Change PIN_(P)  
Exit_______(E) 
: s
-------------------------------
---------------------------------------------
User1 You have 100000 RUPEES in your Account.
---------------------------------------------
```

## 🏗️ System Architecture(How It Works)

### Data Structure(Where the Data Lives)

```python
users = ["user1", "user2", "user3"]        # User accounts
pins = ["1234", "2222", "3333"]            # Their Corresponding PINs
amounts = [100000, 200000, 300000]         # Account balances (in Rupees)
```

### Flow of the Program

```
Start Here
    ↓
Enter Username
    ↓ (If wrong, try again)
Enter PIN
    ↓ (3 tries max, then locked out)
Login Works
    ↓
Pick an Option
    ├─ Check Balance
    ├─ Withdraw Cash
    ├─ Deposit Money
    ├─ Change PIN
    └─ Exit
    ↓
Either Exit or Loop Back
```


## 🔒 Security Features

### PIN Protection
- Maximum 3 PIN attempts before account and card get blocked
- PIN must be exactly 4 digits
- New PIN must be different from your old PIN
- PIN confirmation required for changes

### Input Validation
- Usernames work regardless of uppercase or lowercase
- Numeric PIN verification
- Withdrawal and deposit amounts have to be multiples of 10 (realistic for real ATMs)
- Balance sufficiency checks(You can't withdraw more than you have)

### Error Handling
- Clear error messages for invalid inputs
- Tells you exactly what you did wrong
- User-friendly feedback for all operations
- Graceful handling of incorrect data types
- Won't crash if you enter something unexpected

## 🔮 Future Enhancements

### Planned Features
- [ ] **Database Integration**: Store user data in SQLite/MySQL
- [ ] **Transaction History**: Keep track of everything you do with dates and times
- [ ] **Multiple Account Types**: Savings, Current, Fixed Deposit
- [ ] **Mini Statement**: Last 5-10 transactions
- [ ] **Transfer Money**: Transfer funds to other users
- [ ] **Encryption**: Hash PINs using bcrypt/hashlib
- [ ] **GUI Interface**: Make it look like a real ATM with buttons and a screen using Tkinter or PyQt-based interface
- [ ] **Receipt Generation**: Print transaction receipts
- [ ] **Multi-language Support**: Hindi, English, Regional languages
- [ ] **OTP Verification**: Two-factor authentication
- [ ] **Daily Withdrawal Limit**: Can't withdraw more than X per day
- [ ] **Account Management**: Add or remove accounts without editing code

### Technical Improvements
- Object-Oriented Programming (OOP) refactoring
- Rewrite using classes instead of just functions
- Load user data from a config file
- Add logging to track what's happening
- Write proper tests
- Clean up the input checking


## 📝 Code Structure

```
atm-management-system/
│
├── atm_system.py          # The actual program
├── README.md              # This file
└── requirements.txt       # Python packages needed (if any)
```

## 🐛 Known Issues

- Data gets erased when you close the program (it's all in memory)
- No transaction history records
- Limited to 3 pre-configured users mentionedd in the code
- No floating-point currency support(Can't handle money with cents (like 100.50))

## 👨‍💻 Made By
**Yuvank Bhargava**
- GitHub: [@yuvankbhargava82](https://github.com/yuvankbhargava82)
- Email: yuvankbhargava2729@gmail.com

## 🙏 Acknowledgments
- Inspired by real-world ATM systems
- Built as part of B.Tech CSE curriculum


**⭐ Star this repository if you find it helpful! ⭐**

