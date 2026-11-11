print("Bank Balance App")

name = input("Customer Name: ")
balance = int(input("Starting Balance: "))

deposit = int(input("Deposit Amount: "))
balance = balance + deposit
print("After Deposit Balance:", balance)

withdraw = int(input("Withdraw Amount: "))
balance = balance - withdraw
print("After Withdraw Balance:", balance)

print("----- FINAL -----")
print(name)
print("Balance:", balance)

if balance >= 1000:
    print("Status: Safe")
else:
    print("Status: Low Balance")
