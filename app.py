from flask import Flask, render_template, request, jsonify, session
from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine
import os
import secrets

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', secrets.token_hex(16))

# Initialize machines (stored in session for each user)
def get_machines():
    if 'initialized' not in session:
        session['initialized'] = True
        session['resources'] = {"water": 300, "milk": 200, "coffee": 100}
        session['profit'] = 0.0
        session['is_on'] = True
        session['transactions'] = []
    
    coffee_maker = CoffeeMaker()
    coffee_maker.resources = session['resources']
    
    money_machine = MoneyMachine()
    money_machine.profit = session['profit']
    
    return coffee_maker, money_machine

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/api/menu', methods=['GET'])
def get_menu():
    """Get all available drinks"""
    menu = Menu()
    drinks = []
    for item in menu.menu:
        drinks.append({
            'name': item.name,
            'cost': item.cost,
            'ingredients': item.ingredients
        })
    return jsonify({'drinks': drinks})

@app.route('/api/resources', methods=['GET'])
def get_resources():
    """Get current resource levels"""
    coffee_maker, money_machine = get_machines()
    return jsonify({
        'resources': coffee_maker.resources,
        'profit': money_machine.profit,
        'is_on': session.get('is_on', True),
        'transactions': session.get('transactions', [])
    })

@app.route('/api/order', methods=['POST'])
def make_order():
    """Process a coffee order"""
    data = request.get_json()
    drink_name = data.get('drink_name')
    payment = float(data.get('payment', 0))
    
    if not session.get('is_on', True):
        return jsonify({'success': False, 'message': 'Machine is OFF'}), 400
    
    coffee_maker, money_machine = get_machines()
    menu = Menu()
    
    # Find the drink
    drink = menu.find_drink(drink_name)
    if drink is None:
        return jsonify({'success': False, 'message': 'Drink not available'}), 404
    
    # Check resources
    resource_check = coffee_maker.is_resource_sufficient(drink)
    if not resource_check['sufficient']:
        return jsonify({
            'success': False, 
            'message': f"Sorry, not enough {resource_check['missing']}"
        }), 400
    
    # Process payment
    payment_result = money_machine.make_payment(drink.cost, payment)
    
    if payment_result['success']:
        # Make the coffee
        coffee_maker.make_coffee(drink)
        
        # Update session
        session['resources'] = coffee_maker.resources
        session['profit'] = money_machine.profit
        
        # Add transaction
        transactions = session.get('transactions', [])
        transactions.insert(0, {
            'drink': drink.name,
            'cost': drink.cost,
            'time': data.get('time', '')
        })
        session['transactions'] = transactions[:10]  # Keep last 10
        
        session.modified = True
        
        return jsonify({
            'success': True,
            'message': f"Here is your {drink.name} ☕! Enjoy!",
            'change': payment_result['change'],
            'resources': coffee_maker.resources,
            'profit': money_machine.profit
        })
    else:
        return jsonify({
            'success': False,
            'message': 'Insufficient payment. Money refunded.'
        }), 400

@app.route('/api/refill', methods=['POST'])
def refill_resources():
    """Refill all resources to maximum"""
    if not session.get('is_on', True):
        return jsonify({'success': False, 'message': 'Machine is OFF'}), 400
    
    session['resources'] = {"water": 300, "milk": 200, "coffee": 100}
    session.modified = True
    
    return jsonify({
        'success': True,
        'message': 'Resources refilled! ✨',
        'resources': session['resources']
    })

@app.route('/api/power', methods=['POST'])
def toggle_power():
    """Toggle machine power on/off"""
    current_state = session.get('is_on', True)
    session['is_on'] = not current_state
    session.modified = True
    
    return jsonify({
        'success': True,
        'is_on': session['is_on'],
        'message': f"Machine turned {'ON' if session['is_on'] else 'OFF'}"
    })

@app.route('/api/report', methods=['GET'])
def get_report():
    """Get detailed machine report"""
    coffee_maker, money_machine = get_machines()
    
    return jsonify({
        'water': coffee_maker.resources['water'],
        'milk': coffee_maker.resources['milk'],
        'coffee': coffee_maker.resources['coffee'],
        'profit': money_machine.profit,
        'total_orders': len(session.get('transactions', []))
    })

if __name__ == '__main__':
    # Get port from environment variable or use 5000 as default
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
