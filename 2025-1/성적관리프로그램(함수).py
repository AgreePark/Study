stdID = []   # 학번
name = []    # 이름
Eng = []     # 영어
CLang = []   # C언어
Py = []      # 파이썬
sum = []     # 총점
average = [] # 평균
grade = []   # 학점
rank = [1, 1, 1, 1, 1]  # 등수

# 입력 함수
def input_info(i): 
    stdID.append(input("학번 >> "))
    name.append(input("이름 >> "))
    Eng.append(int(input("영어 성적 >> ")))
    CLang.append(int(input("C언어 성적 >> ")))
    Py.append(int(input("파이썬 성적 >> ")))

# 총점/평균 계산 함수
def sum_aver_calculate(i):
    sum.append(Eng[i] + CLang[i] + Py[i])
    average.append(sum[i] / 3)

# 학점 계산 함수    
def grade_calculate(i):
    if average[i] > 95 : grade.append('A+')
    elif average[i] > 90 : grade.append('A0')
    elif average[i] > 85 : grade.append('B+')
    elif average[i] > 80 : grade.append('B0')
    elif average[i] > 75 : grade.append('C+')
    elif average[i] > 70 : grade.append('C0')
    elif average[i] > 65 : grade.append('D+')
    elif average[i] > 60 : grade.append('D0')
    else: grade.append('F')

# 등수 계산 함수
def rank_calculate():
    for i in range (0, 5):
        for j in range (0, 5):
            if average[i] < average[j] : rank[i] += 1

# 출력 함수
def output_info():
    for i in range (0, 5):
        print("=============================================================================")
        print("학번          이름       영어   C-언어   파이썬     총점   평균   학점   등수")
        print(stdID[i], "  ", name[i], "    ", Eng[i], "    ", CLang[i], "     ", Py[i], "     ", sum[i], "  ", average[i], " ", grade[i], "    ", rank[i])
        print("=============================================================================")

for i in range (0, 5):
    input_info(i)
    sum_aver_calculate(i)
    grade_calculate(i)
    
rank_calculate()
output_info()
