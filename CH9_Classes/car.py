class Car:
    """representing a car"""
    
    def __init__(self, make, model, year):
        """initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """return a neatly formatted name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name
    
    def read_odometer(self):
        """print a statement showing the cars mileage"""
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self, mileage):
        """
        set odometer reading to the given value
        reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you cant roll back an odometer")

    def increment_odometer(self, miles):
        """add the given amount to the odometer reading"""
        self.odometer_reading += miles

# class Battery:
#     """a simple attempt to model a battery for an EV"""

#     def __init__(self, battery_size=40):
#         """initialize battery attributes"""
#         self.battery_size = battery_size
    
#     def describe_battery(self):
#         """print a statement describing the battery size"""
#         print(f"this car has a {self.battery_size}-kWh battery")

#     def get_range(self):
#         """print a statement about hte range this battery provides"""
#         if self.battery_size == 40:
#             range = 150
#         elif self.battery_size == 65:
#             range = 225

#         print(f"this car can go about {range} miles on a full charge")

#     def describe_battery(self):
#         """print a statement describing battery size"""
#         print(f"this car has a {self.battery_size}-kWh battery")

#     def upgrade_battery(self):
#         """check battery size and set capacity to 65 if it isnt already"""
#         if self.battery_size != 65:
#             self.battery_size = 65

# class ElectricCar(Car):
#     """represents aspects of a car, specific to electric vehicles"""

#     def __init__(self, make, model, year):
#         """
#         initialize attributes of the parent class
#         then initialize attributes specific to EV
#         """
#         super().__init__(make,model,year)
#         self.battery = Battery()