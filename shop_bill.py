print("Shop Bill Calculator")

customer = input("Customer Name: ")
item1 = input("Item 1 Name: ")
price1 = int(input("Item 1 Price: "))
qty1 = int(input("Item 1 Quantity: "))

item2 = input("Item 2 Name: ")
price2 = int(input("Item 2 Price: "))
qty2 = int(input("Item 2 Quantity: "))

total1 = price1 * qty1
total2 = price2 * qty2
total = total1 + total2

print("----- BILL -----")
print(customer)
print(item1, "-", total1)
print(item2, "-", total2)
print("Total Bill:", total)

if total >= 1000:
    print("Discount: 100")
    print("Pay:", total - 100)
else:
    print("Pay:", total)
