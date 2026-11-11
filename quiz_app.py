print("Simple Quiz App")

name = input("Your Name: ")
score = 0

print("Q1. Python yaru create pannanga?")
print("1. Guido van Rossum")
print("2. Elon Musk")
ans1 = int(input("Answer (1 or 2): "))
if ans1 == 1:
    print("Correct!")
    score = score + 1
else:
    print("Wrong!")

print("Q2. 2 + 2 = ?")
print("1. 3")
print("2. 4")
ans2 = int(input("Answer (1 or 2): "))
if ans2 == 2:
    print("Correct!")
    score = score + 1
else:
    print("Wrong!")

print("----- RESULT -----")
print(name)
print("Score:", score, "/ 2")

if score == 2:
    print("Status: Excellent!")
else:
    print("Status: Try Again!")
