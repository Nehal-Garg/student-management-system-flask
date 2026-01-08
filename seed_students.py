import sqlite3

data = [
    ("Rahul Sharma", "A101", "CSE", 3),
    ("Neha Gupta", "A102", "AIML", 3),
    ("Amit Verma", "A103", "ECE", 2),
    ("Priya Singh", "A104", "IT", 4)
]

conn = sqlite3.connect("students.db")
conn.executemany(
    "INSERT INTO students (name, roll_no, department, year) VALUES (?,?,?,?)",
    data
)
conn.commit()
conn.close()

print("Sample students added")
