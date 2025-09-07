def make_pizza(size,*toppings):
    print(f"\nMaking a {size}-inch pizza with the follwing toppings:")
    for topping in toppings:
        print(f"- {topping}")