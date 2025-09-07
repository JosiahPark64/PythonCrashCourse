#start with usres that need to be verified, and an empty list
# to hold confirmed users

unconfirmed_users = ['alice','brian', 'candace']
confirmed_users = []

#verify each user until there are no more unconfirmed users
# Move each verified user into the list of confirmed users
while unconfirmed_users:
    current_user = unconfirmed_users.pop(0)
    print(f"{current_user} has been confirmed.")
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for user in confirmed_users:
    print(user)