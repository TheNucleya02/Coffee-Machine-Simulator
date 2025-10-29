# ☕ Coffee Machine Simulator - Flask Web Application

A full-stack web application that simulates a coffee machine using **Python Flask backend** with Object-Oriented Programming principles. This project demonstrates real-world backend development, RESTful API design, and clean software architecture.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

**Live Demo:** [Add your deployment link here]

## ✨ Features

### Core Functionality
- 🍵 **Multiple Drink Options** - Latte, Espresso, Cappuccino
- 📊 **Real-time Resource Tracking** - Monitor water, milk, and coffee levels
- 💰 **Payment Processing** - Handle transactions with change calculation
- 📈 **Sales Analytics** - Track profits and transaction history
- ⚡ **Power Management** - Turn machine on/off with state preservation
- 🔄 **Resource Refilling** - Quick refill functionality for maintenance
- 📱 **Responsive Design** - Works on desktop and mobile devices

### Technical Features
- RESTful API architecture
- Session-based state management
- JSON data exchange
- Error handling with proper HTTP status codes
- Clean separation of concerns (Backend/Frontend)
- Dynamic UI updates without page refresh

---

## 🛠️ Technology Stack

### Backend
- **Python 3.8+** - Core programming language
- **Flask 3.0.0** - Web framework for API development
- **Flask Sessions** - State management

### Frontend
- **HTML5** - Structure
- **JavaScript (ES6+)** - Dynamic interactions
- **Tailwind CSS** - Styling framework
- **Fetch API** - Backend communication

### Development Tools
- Git - Version control
- Virtual Environment - Dependency isolation

---

## 🏗️ Architecture

### System Design

```
┌─────────────────────────────────────────────────────────────┐
│                         Frontend (HTML/JS)                   │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │  Menu    │  │ Resources│  │ Payment  │  │ Analytics│   │
│  │ Display  │  │  Monitor │  │   Form   │  │ Dashboard│   │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘   │
│       │             │              │             │          │
│       └─────────────┴──────────────┴─────────────┘          │
│                          │                                   │
│                  Fetch API (AJAX)                           │
└──────────────────────────┼──────────────────────────────────┘
                           │
┌──────────────────────────┼──────────────────────────────────┐
│                    Flask Backend (Python)                    │
│  ┌────────────────────────────────────────────────────────┐ │
│  │              Flask Routes (app.py)                     │ │
│  │  /api/menu  /api/order  /api/resources  /api/refill   │ │
│  └─────┬──────────────┬───────────────┬──────────────┬────┘ │
│        │              │               │              │       │
│  ┌─────▼─────┐  ┌────▼─────┐  ┌─────▼──────┐  ┌────▼────┐ │
│  │   Menu    │  │  Coffee  │  │   Money    │  │ Session │ │
│  │   Class   │  │  Maker   │  │  Machine   │  │ Manager │ │
│  │           │  │  Class   │  │   Class    │  │         │ │
│  └───────────┘  └──────────┘  └────────────┘  └─────────┘ │
└─────────────────────────────────────────────────────────────┘
```

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git (optional)

### Step-by-Step Setup

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/coffee-machine-flask.git
cd coffee-machine-flask
```

2. **Create virtual environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Create project structure**
```bash
mkdir templates
# Place index.html in templates/ folder
```

5. **Run the application**
```bash
python app.py
```

6. **Access the application**
```
Open browser: http://localhost:5000
```

### Quick Start (Alternative)
```bash
pip install Flask
python app.py
```

---

## 🚀 Usage

### Running the Application

1. **Start the server**
```bash
python app.py
```

2. **Navigate to the web interface**
```
http://localhost:5000
```

### Using the Coffee Machine

1. **Turn on the machine** - Click the "Turn ON" button (if off)
2. **Select a drink** - Click on Latte, Espresso, or Cappuccino
3. **Enter payment** - Type amount equal to or greater than the drink cost
4. **Confirm payment** - Click "Pay Now"
5. **Receive your coffee** - Resources update automatically
6. **Monitor resources** - Check water, milk, and coffee levels
7. **Refill when needed** - Click "Refill Resources"
8. **View analytics** - Click "View Report" for detailed statistics

---

## 📚 API Documentation

### Base URL
```
http://localhost:5000/api
```

### Endpoints

#### 1. Get Menu
```http
GET /api/menu
```
**Response:**
```json
{
  "drinks": [
    {
      "name": "latte",
      "cost": 2.5,
      "ingredients": {"water": 200, "milk": 150, "coffee": 24}
    }
  ]
}
```

#### 2. Get Resources
```http
GET /api/resources
```
**Response:**
```json
{
  "resources": {"water": 300, "milk": 200, "coffee": 100},
  "profit": 15.50,
  "is_on": true,
  "transactions": [...]
}
```

#### 3. Place Order
```http
POST /api/order
Content-Type: application/json

{
  "drink_name": "latte",
  "payment": 3.0,
  "time": "10:30:45"
}
```
**Success Response:**
```json
{
  "success": true,
  "message": "Here is your latte ☕! Enjoy!",
  "change": 0.50,
  "resources": {...},
  "profit": 18.00
}
```

**Error Response:**
```json
{
  "success": false,
  "message": "Sorry, not enough water"
}
```

#### 4. Refill Resources
```http
POST /api/refill
```
**Response:**
```json
{
  "success": true,
  "message": "Resources refilled! ✨",
  "resources": {"water": 300, "milk": 200, "coffee": 100}
}
```

#### 5. Toggle Power
```http
POST /api/power
```
**Response:**
```json
{
  "success": true,
  "is_on": false,
  "message": "Machine turned OFF"
}
```

#### 6. Get Report
```http
GET /api/report
```
**Response:**
```json
{
  "water": 250,
  "milk": 150,
  "coffee": 76,
  "profit": 5.00,
  "total_orders": 2
}
```

---

## 📁 Project Structure

```
coffee-machine-flask/
│
├── app.py                      # Main Flask application & API routes
├── coffee_maker.py             # CoffeeMaker class (resource management)
├── menu.py                     # Menu & MenuItem classes
├── money_machine.py            # MoneyMachine class (payment processing)
│
├── templates/
│   └── index.html              # Frontend HTML interface
│
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
├── .gitignore                  # Git ignore file
└── LICENSE                     # MIT License

```

### File Descriptions

- **app.py** - Flask server with all API endpoints and session management
- **coffee_maker.py** - Handles resource checking and coffee preparation
- **menu.py** - Manages menu items and drink definitions
- **money_machine.py** - Processes payments and tracks profit
- **templates/index.html** - Single-page application frontend

---

## 🚀 Deployment

### Render
1. Connect GitHub repository
2. Select "Web Service"
3. Build: `pip install -r requirements.txt`
4. Start: `gunicorn app:app`
   
---

## 🔗 Useful Links

- [Flask Documentation](https://flask.palletsprojects.com/)
- [REST API Best Practices](https://restfulapi.net/)
- [Python OOP Guide](https://realpython.com/python3-object-oriented-programming/)
- [Tailwind CSS Docs](https://tailwindcss.com/)

---

**Made with ☕ Python and Flask**
