responses = {}
#set a flag indicating the poll is active
polling_active = True
while polling_active == True:
    name = input("\nWhat is your name?")
    response = input("What mountain would you like to climb?")

    #store the response in a dictionary
    responses[name] = response

    repeat = input("would you like to let another person respond? (yes/no)")
    if repeat == 'no':
        polling_active = False

#polling is complete, show responses
print('\n---- Poll results ----')
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response}.")