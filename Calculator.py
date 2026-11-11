print("Student Mark Calculator")

name = input("Student Name: ")
tamil = int(input("Tamil Mark: "))
english = int(input("English Mark: "))
maths = int(input("Maths Mark: "))
science = int(input("Science Mark: "))
social = int(input("Social Mark: "))

total = tamil + english + maths + science + social
average = total / 5

print("Total Marks:", total)
print("Average:", average)

if average >= 90:
    print("Grade: A")
elif average >= 75:
    print("Grade: B")
elif average >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")
