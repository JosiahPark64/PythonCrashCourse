prompt = "Input each guest's age one at a time: "
prompt += "\n(Input 'quit' when you have entered everyone's age.)"
price = 0

active = True
while active:
    age = input(prompt)
    if age == "quit":
        active = False
    else:    
        age = int(age)
        if age < 3:
            price += 0
        elif age >= 3 and age <= 12:
            price += 10
        else:
            price += 15
    print(f"Your total cost is {price}")