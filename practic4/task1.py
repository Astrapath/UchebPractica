import sqlite3


class Student:
    def __init__(self, firstname, lastname, surname, group, grade):
        self.firstname = firstname
        self.lastname = lastname
        self.surname = surname
        self.group = group
        self.grade = grade

    def avrgrade(self):
        return sum(self.grade) / len(self.grade)


def initdb():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            firstname TEXT,
            lastname TEXT,
            surname TEXT,
            groupname TEXT,
            grade TEXT
        )
    ''')
    conn.commit()
    conn.close()


def add(student):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    gradestr = ','.join(str(grade) for grade in student.grade)
    cursor.execute('''
        INSERT INTO students (firstname, lastname, surname, groupname, grade)
        VALUES (?, ?, ?, ?, ?)
    ''', (student.firstname, student.lastname, student.surname, student.group, gradestr))
    conn.commit()
    conn.close()


def viewall():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students')
    return cursor.fetchall()


def viewone(studid):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students WHERE id = ?', (studid,))
    student = cursor.fetchone()
    conn.close()
    if student:
        gradestr = student[5].split(',')
        grades = []
        for grade in gradestr:
            grades.append(int(grade))
        avrgrade = sum(grades) / len(grades)
        return student + (avrgrade,)
    return None


def edit(studid, update):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    gradestr = ','.join(str(grade) for grade in update.grade)
    cursor.execute('''
        UPDATE students
        SET firstname = ?, lastname = ?, surname = ?, groupname = ?, grade = ?
        WHERE id = ?
    ''', (update.firstname, update.lastname, update.surname, update.group, gradestr, studid))
    conn.commit()
    conn.close()


def delete(studid):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM students WHERE id = ?', (studid,))
    conn.commit()
    conn.close()


initdb()
student1 = Student("Кирилл", "Пхалагов", "Игоревич", "634", [5, 5, 5, 5])
add(student1)

students = viewall()
print("Все студенты:", students)

details = viewone(1)
print("Детали студента:", details)

updated = Student("Олег", "Раковицэ", "непомню", "634", [4, 4, 4, 4])
edit(1, updated)

delete(1)
