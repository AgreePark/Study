import sqlite3

##################

  # 프로그램명: 성적 관리 프로그램

  # 작성자: 소프트웨어학부 2024042026 박인정

  # 작성일: 2025.06.07

  # 프로그램 설명: 학생들의 성적을 입력받아 총점, 평균, 학점, 등수를 계산하고 관리하는 프로그램 / 데이터베이스 (SQLite 활용)

###################


class Student:
    def __init__(self, stdID, name, Eng, CLang, Py):
        self.stdID = stdID
        self.name = name
        self.Eng = Eng
        self.CLang = CLang
        self.Py = Py
        self.sum = self.Eng + self.CLang + self.Py
        self.average = self.sum / 3
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        if self.average > 95: return 'A+'
        elif self.average > 90: return 'A0'
        elif self.average > 85: return 'B+'
        elif self.average > 80: return 'B0'
        elif self.average > 75: return 'C+'
        elif self.average > 70: return 'C0'
        elif self.average > 65: return 'D+'
        elif self.average > 60: return 'D0'
        else: return 'F'

    def display(self):
        print("=============================================================================")
        print("학번          이름       영어   C-언어   파이썬     총점   평균   학점")
        print(f"{self.stdID}   {self.name}       {self.Eng}      {self.CLang}        {self.Py}      {self.sum}    {self.average:.2f}     {self.grade}")
        print("=============================================================================")

class StudentDB:
    def __init__(self):
        self.conn = sqlite3.connect("students.db")
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            stdID TEXT PRIMARY KEY,
            name TEXT,
            Eng INTEGER,
            CLang INTEGER,
            Py INTEGER,
            sum INTEGER,
            average REAL,
            grade TEXT
        )
        """)
        self.conn.commit()

    def insert_student(self, student):
        self.cursor.execute("""
        INSERT INTO students (stdID, name, Eng, CLang, Py, sum, average, grade)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (student.stdID, student.name, student.Eng, student.CLang, student.Py,
              student.sum, student.average, student.grade))
        self.conn.commit()

    def delete_student(self, stdID):
        self.cursor.execute("DELETE FROM students WHERE stdID = ?", (stdID,))
        self.conn.commit()

    def fetch_all_students(self):
        self.cursor.execute("SELECT * FROM students ORDER BY average DESC")
        return self.cursor.fetchall()

    def search_student(self, keyword):
        self.cursor.execute("SELECT * FROM students WHERE stdID = ? OR name = ?", (keyword, keyword))
        return self.cursor.fetchall()

    def count_upto80(self):
        self.cursor.execute("SELECT COUNT(*) FROM students WHERE average >= 80")
        return self.cursor.fetchone()[0]

    def close(self):
        self.conn.close()

class StudentManager:
    def __init__(self):
        self.db = StudentDB()

    def input_info(self):
        stdID = input("학번 >> ")
        name = input("이름 >> ")
        Eng = int(input("영어 성적 >> "))
        CLang = int(input("C언어 성적 >> "))
        Py = int(input("파이썬 성적 >> "))
        student = Student(stdID, name, Eng, CLang, Py)
        self.db.insert_student(student)

    def output_info(self):
        rows = self.db.fetch_all_students()
        for row in rows:
            s = Student(*row[:5])
            s.sum, s.average, s.grade = row[5], row[6], row[7]
            s.display()

    def insert_info(self):
        self.input_info()
        self.output_info()

    def delete_info(self):
        stdID = input("삭제할 학생의 학번을 입력하세요 >> ")
        self.db.delete_student(stdID)
        self.output_info()

    def search_info(self):
        keyword = input("찾고 싶은 학생의 학번 또는 이름 >> ")
        result = self.db.search_student(keyword)
        if result:
            for row in result:
                s = Student(*row[:5])
                s.sum, s.average, s.grade = row[5], row[6], row[7]
                s.display()
        else:
            print("해당하는 학생을 찾을 수 없습니다")

    def count_upto80(self):
        count = self.db.count_upto80()
        print(f"평균 80점이 넘는 학생은 총 {count}명 입니다")

    def run(self):
        for _ in range(5):
            self.input_info()
        self.output_info()

        while True:
            WhatToDo = input("다음으로 할 것은? (삽입/삭제/탐색/카운트/종료) >> ")
            if WhatToDo == "삽입":
                self.insert_info()
            elif WhatToDo == "삭제":
                self.delete_info()
            elif WhatToDo == "탐색":
                self.search_info()
            elif WhatToDo == "카운트":
                self.count_upto80()
            elif WhatToDo == "종료":
                self.db.close()
                print("프로그램을 종료합니다.")
                break
            else:
                print("알 수 없는 명령입니다.")

if __name__ == "__main__":
    manager = StudentManager()
    manager.run()
