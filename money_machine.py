class MoneyMachine:
    """Models the payment processing machine"""
    CURRENCY = "$"

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Returns the current profit"""
        return {"profit": self.profit}

    def make_payment(self, cost, amount):
        """Returns dict with 'success' boolean and 'change' amount."""
        self.money_received = amount
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            self.profit += cost
            self.money_received = 0
            return {"success": True, "change": change}
        else:
            self.money_received = 0
            return {"success": False, "change": 0}