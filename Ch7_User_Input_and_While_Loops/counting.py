current_number = 0

#using continue instead of break or flag
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)