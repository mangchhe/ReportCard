from openpyxl import load_workbook

try:
    wb = load_workbook('collectionOfGrade.xlsx', data_only=True)
except FileNotFoundError as err:
    print('맞지 않는 파일 이름')

try:
    ws = wb['성적표']
except KeyError as err:
    print('존재하지 않는 시트')

grade = 0

for i in range(1,5,1):
    for j in range(1,3,1):
        for row in ws.rows:
            if row[0].value == str(i) + '학년 ' + str(j) + '학기':
                grade+=1
                break

gradeRank = []
gradeCredit = []

for i in range(grade):
    line = []
    line2 = []
    gradeRank.append(line)
    gradeCredit.append(line2)

count = 0

for i in range(1,5,1):
    for j in range(1,3,1):
        for row in ws.rows:
            if row[0].value == str(i) + '학년 ' + str(j) + '학기':
                gradeRank[count].append(row[4].value)
                gradeCredit[count].append(row[2].value)
        count += 1

for i in range(grade):
    print(gradeRank[i])
    print(gradeCredit[i])
