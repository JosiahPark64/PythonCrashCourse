class User:
    """create a user object"""

    def __init__(self, first_name, last_name):
        self.fn = first_name
        self.ln = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(f"first name: {self.fn} \nlast name: {self.ln}")

    def greet_user(self):
        print(f"hello, {self.fn} {self.ln}")

    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

# class Admin(User):
#     """initilaize admin user"""

#     def __init__(self, first_name, last_name, privileges):
#         super().__init__(first_name, last_name)
#         self.privileges = Privileges(privileges)

# class Privileges():
#     def __init__(self, privileges):
#         self.privileges = privileges
    
#     def show_privileges(self):
#         for privilege in self.privileges:
#             print(privilege)

# kev = User('kevin', 'dupuis')
# kev.describe_user()
# kev.greet_user()

# admin = Admin('first','last', ['can add users', 'can delete users'])
# admin.greet_user()
# admin.privileges.show_privileges()