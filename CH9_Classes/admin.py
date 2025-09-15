from user import User
from privileges import Privileges

class Admin(User):
    """initilaize admin user"""

    def __init__(self, first_name, last_name, privileges):
        super().__init__(first_name, last_name)
        self.privileges = Privileges(privileges)