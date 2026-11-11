import sqlite3

print("Student Marks - SQL Project")

# SQL Database create pannurom
con = sqlite3.connect("student.db")
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS marks (name TEXT, mark INTEGER)")

name = input("Student Name: ")
mark = int(input("Mark: "))

cur.execute("INSERT INTO marks VALUES (?, ?)", (name, mark))
con.commit()

print("Saved in SQL Database!")

print("----- All Students -----")
cur.execute("SELECT * FROM marks")
for row in cur.fetchall():
    print(row)

con.close()
