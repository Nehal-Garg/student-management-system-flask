from database import get_connection

def get_all_students():
    conn = get_connection()
    data = conn.execute("SELECT * FROM students").fetchall()
    conn.close()
    return data

def add_student(name, roll, dept, year):
    conn = get_connection()
    conn.execute(
        "INSERT INTO students VALUES (NULL,?,?,?,?)",
        (name, roll, dept, year)
    )
    conn.commit()
    conn.close()

def get_student(id):
    conn = get_connection()
    student = conn.execute(
        "SELECT * FROM students WHERE id=?", (id,)
    ).fetchone()
    conn.close()
    return student

def update_student(id, name, roll, dept, year):
    conn = get_connection()
    conn.execute(
        "UPDATE students SET name=?, roll_no=?, department=?, year=? WHERE id=?",
        (name, roll, dept, year, id)
    )
    conn.commit()
    conn.close()

def delete_student(id):
    conn = get_connection()
    conn.execute("DELETE FROM students WHERE id=?", (id,))
    conn.commit()
    conn.close()

def search_students(q):
    conn = get_connection()
    data = conn.execute(
        "SELECT * FROM students WHERE name LIKE ? OR roll_no LIKE ?",
        (f"%{q}%", f"%{q}%")
    ).fetchall()
    conn.close()
    return data
def get_stats():
    conn = get_connection()

    total = conn.execute(
        "SELECT COUNT(*) FROM students"
    ).fetchone()[0]

    departments = conn.execute(
        "SELECT COUNT(DISTINCT department) FROM students"
    ).fetchone()[0]

    final_year = conn.execute(
        "SELECT COUNT(*) FROM students WHERE year = 4"
    ).fetchone()[0]

    conn.close()
    return total, departments, final_year
