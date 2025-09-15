from admin import Admin

test = Admin('first', 'last', ['is evil', 4, {3, 4, 5}])
test.privileges.show_privileges()