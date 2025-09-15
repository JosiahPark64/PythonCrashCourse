class Restaurant:
    """modelling a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f'restaurant name is {self.name}')
        print(f'the restaurant serves {self.type} food')

    def open_restaurant(self):
        print(f'the restaurant is open')

    def serve_customers(self, customers):
        print(f"serving {customers} customers")
        self.number_served += customers
    
    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        print(f"serving {number} customers")
        self.number_served += number

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors:list):
        """initialize an icecream stand using attributes from restaurant"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
    
    def describe_flavors(self):
        """print a statement describing the flavors available"""
        print(self.flavors)
        
# mcdonalds = Restaurant('mcdonalds', 'fast food')
# print(mcdonalds.name)
# print(mcdonalds.type)
# mcdonalds.describe_restaurant()
# mcdonalds.open_restaurant()
# mcdonalds.set_number_served(10)
# mcdonalds.increment_number_served(3)
# print(mcdonalds.number_served)

# chinese_ice_cream = IceCreamStand("china cream", "ice cream stand", ["matcha", 'lime', 'wasabi'])
# chinese_ice_cream.describe_restaurant()
# chinese_ice_cream.describe_flavors()