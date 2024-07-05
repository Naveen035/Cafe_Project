menu = {
    'Coffee': 80,
    'Tea': 50,
    'Black Coffee': 60,
    'Samosa (2 pcs)': 30,
    'Biscuit (2 pcs)': 20,
    'Green Tea': 30
}

print("Welcome to the Cafe!")
print("Coffee: ₹80\nTea: ₹50\nBlack Coffee: ₹60\nSamosa (2 pcs): ₹30\nBiscuit (2 pcs): ₹20\nGreen Tea: ₹30")

order_amount = 0

while True:
    item = input("Enter the name of the item you want to order: ")
    if item in menu:
        order_amount += menu[item]
        print(f"Your item {item} has been added to your order.")
    else:
        print(f"Sorry, {item} is not present in our menu. Please check the menu.")
    
    another_order = input("Do you want to order anything else? (Yes/No): ")
    if another_order.lower() != 'yes':
        break

print(f"The total order bill is ₹{order_amount}")
