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
        self.rank = 1

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
        print("학번          이름       영어   C-언어   파이썬     총점   평균   학점   등수")
        print(f"{self.stdID}   {self.name}       {self.Eng}      {self.CLang}        {self.Py}      {self.sum}    {self.average:.2f}     {self.grade}    {self.rank}")
        print("=============================================================================")

class StudentManager:
    def __init__(self):
        self.students = []
        self.HowManyStd = 5

    def input_info(self):
        stdID = input("학번 >> ")
        name = input("이름 >> ")
        Eng = int(input("영어 성적 >> "))
        CLang = int(input("C언어 성적 >> "))
        Py = int(input("파이썬 성적 >> "))
        student = Student(stdID, name, Eng, CLang, Py)
        self.students.append(student)

    def rank_calculate(self):
        for s in self.students:
            s.rank = 1
        for i in self.students:
            for j in self.students:
                if i.average < j.average:
                    i.rank += 1

    def output_info(self):
        for s in self.students:
            s.display()

    def insert_info(self):
        self.input_info()
        self.HowManyStd += 1
        self.rank_calculate()
        self.output_info()

    def delete_info(self):
        WhoStd = int(input("몇번 학생을 지우시겠습니까? (위에서부터 1번째) >> ")) - 1
        if 0 <= WhoStd < len(self.students):
            del self.students[WhoStd]
            self.HowManyStd -= 1
            self.rank_calculate()
            self.output_info()
        else:
            print("해당 학생 번호가 없습니다.")

    def search_info(self):
        IDdic = {}
        namedic = {}
        for i, s in enumerate(self.students):
            IDdic[s.stdID] = i
            namedic[s.name] = i
        WhoStd = input("찾고싶은 학생의 학번 또는 이름 >> ")
        cantSearch = 0
        try:
            self.students[IDdic[WhoStd]].display()
        except:
            cantSearch += 1
        try:
            self.students[namedic[WhoStd]].display()
        except:
            cantSearch += 1
        if cantSearch == 2:
            print("해당하는 학생을 찾을 수 없습니다")

    def sort_info(self):
        # rank를 기준으로 정렬
        self.students.sort(key=lambda x: x.rank)
        self.output_info()

    def count_upto80(self):
        count = 0
        for s in self.students:
            if s.average >= 80:
                count += 1
        print("평균 80점이 넘는 학생은 총 ", count, "명 입니다")

    def run(self):
        for _ in range(self.HowManyStd):
            self.input_info()
        self.rank_calculate()
        self.output_info()

        while True:
            WhatToDo = input("다음으로 할 것은? (삽입/삭제/탐색/정렬/카운트) >> ")
            if WhatToDo == "삽입":
                self.insert_info()
            elif WhatToDo == "삭제":
                self.delete_info()
            elif WhatToDo == "탐색":
                self.search_info()
            elif WhatToDo == "정렬":
                self.sort_info()
            elif WhatToDo == "카운트":
                self.count_upto80()
            else:
                print("해당 기능을 찾을 수 없습니다. 프로그램을 종료합니다.")
                break


manager = StudentManager()
manager.run()
