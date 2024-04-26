print("Welcome to GC Fruit Market! What is your name? ")
my_name = input("")
print("Welcome " + my_name + ". Which Fruit would you like to buy?")
fruit_options = ["Apple $2", "Grape $1", "Orange $3"]
print(f"1) {fruit_options[0]}")
print(f"2) {fruit_options[1]}")
print(f"3) {fruit_options[2]}")
fruit_type = input()
apple_cost = 2
grape_cost = 1
orange_cost = 3
apple_quantity = 0
grape_quantity = 0
orange_quantity = 0
if fruit_type == "apple":
    apple_quantity += 1
    print(f"You bought 1 apple at ${apple_cost}.")
elif fruit_type == "grape":
    grape_quantity += 1
    print(f"You bought 1 grape at ${grape_cost}.")
elif fruit_type == "orange":
    orange_quantity += 1
    print(f"You bought 1 orange at ${orange_cost}.")
else:
    print(f"Sorry. {fruit_type} is an invalid option")
while True:
    more_fruit = input("Would you like to buy another piece of fruit? y/n ")
    if more_fruit == "y":
        print("Welcome " + my_name + ". Which Fruit would you like to buy?")
        fruit_options = ["Apple $2", "Grape $1", "Orange $3"]
        print(f"1) {fruit_options[0]}")
        print(f"2) {fruit_options[1]}")
        print(f"3) {fruit_options[2]}")
        fruit_type = input()
        if fruit_type == "apple":
            apple_quantity += 1
            print(f"You bought 1 apple at ${apple_cost}.")
        elif fruit_type == "grape":
            grape_quantity += 1
            print(f"You bought 1 grape at ${grape_cost}.")
        elif fruit_type == "orange":
            orange_quantity += 1
            print(f"You bought 1 orange at ${orange_cost}.")
        else:
            print(f"Sorry. {fruit_type} is an invalid option")
    elif more_fruit == "n":
        break

subtotal = (apple_quantity * apple_cost) + (grape_quantity * grape_cost) + (orange_quantity * orange_cost)
tax = subtotal * .05
total = subtotal + tax

print(f"Order for {my_name}")
print(f"{apple_quantity} apple(s) at ${apple_cost} apiece")
print(f"{grape_quantity} grape(s) at ${grape_cost} apiece")
print(f"{orange_quantity} orange(s) at ${orange_cost} apiece")
print(f"Sub Total: ${subtotal}")
print(f"5% Tax: ${tax}")
print(f"Total: ${total}")
