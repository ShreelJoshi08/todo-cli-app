from db import get_connection

def create_table():
    conn = get_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            roll_no TEXT UNIQUE NOT NULL,
            branch TEXT NOT NULL,
            year INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def add_student(name, roll_no, branch, year):
    conn = get_connection()
    conn.execute("INSERT INTO students (name, roll_no, branch, year) VALUES (?, ?, ?, ?)", 
                 (name, roll_no, branch, year))
    conn.commit()
    conn.close()

def get_all_students():
    conn = get_connection()
    cursor = conn.execute("SELECT * FROM students")
    for row in cursor:
        print(row)
    conn.close()

def update_student(id, name, roll_no, branch, year):
    conn = get_connection()
    conn.execute("UPDATE students SET name=?, roll_no=?, branch=?, year=? WHERE id=?", 
                 (name, roll_no, branch, year, id))
    conn.commit()
    conn.close()

def delete_student(id):
    conn = get_connection()
    conn.execute("DELETE FROM students WHERE id=?", (id,))
    conn.commit()
    conn.close()
