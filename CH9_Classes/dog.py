class Dog:
    """A simple attmept to model a dog"""

    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting")

    def roll_over(self):
        print(f"{self.name} rolled over")

my_dog = Dog("Willie", 6)

my_dog.sit()
my_dog.roll_over()
print(my_dog.age)