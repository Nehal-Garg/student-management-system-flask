import sqlite3
import hashlib

username = "admin"
password = "admin123"   # you can change later

hashed = hashlib.sha256(password.encode()).hexdigest()

conn = sqlite3.connect("students.db")
conn.execute(
    "INSERT INTO users (username, password) VALUES (?, ?)",
    (username, hashed)
)
conn.commit()
conn.close()

print("Admin user created")
