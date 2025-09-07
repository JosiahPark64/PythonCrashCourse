sandwich_orders = ['tuna','pastrami','BLT', 'pastrami', 'hotdog', 'pastrami']
finished_sandwiches = []

print("WE ARE OUT OF PASTRAMI DO NOT ORDER IT")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

print("current order queue:")
print(sandwich_orders)

while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    print(f"I made your {sandwich}")
    finished_sandwiches.append(sandwich)

print("Here are teh sandwiches I made today:")
for sandwich in finished_sandwiches:
    print(f"\t{sandwich}")