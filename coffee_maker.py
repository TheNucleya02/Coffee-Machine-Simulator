class CoffeeMaker:
    """Models the machine that makes the coffee"""
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """Returns a dictionary of all resources."""
        return {
            "water": self.resources['water'],
            "milk": self.resources['milk'],
            "coffee": self.resources['coffee']
        }

    def is_resource_sufficient(self, drink):
        """Returns dict with 'sufficient' boolean and 'missing' item if insufficient."""
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                return {"sufficient": False, "missing": item}
        return {"sufficient": True}

    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
