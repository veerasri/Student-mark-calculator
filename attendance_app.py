print("Student Attendance App")

name = input("Student Name: ")
total_days = int(input("Total Days: "))
present_days = int(input("Present Days: "))

absent_days = total_days - present_days
percentage = (present_days / total_days) * 100

print("----- REPORT -----")
print(name)
print("Present:", present_days)
print("Absent:", absent_days)
print("Attendance %:", percentage)

if percentage >= 75:
    print("Status: Eligible for Exam")
else:
    print("Status: Not Eligible")
