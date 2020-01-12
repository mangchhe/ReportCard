from ExcelData import ExcelData

def getAvg(semester):

    excelData = ExcelData()

    gradeRank = []
    selectGrade = semester

    tempGradeName = excelData.getCourseName()[selectGrade]

    valueKo = []

    for i in excelData.getRank()[selectGrade]:
        valueKo.append(tempGradeName[0])
        del tempGradeName[0]

        if i == 'A+':
            gradeRank.append(4.5)
        elif i == 'A0':
            gradeRank.append(4.0)
        elif i == 'B+':
            gradeRank.append(3.5)
        elif i == 'B0':
            gradeRank.append(3.0)
        elif i == 'C+':
            gradeRank.append(2.5)
        elif i == 'C0':
            gradeRank.append(2.0)
        elif i == 'D+':
            gradeRank.append(1.5)
        elif i == 'D0':
            gradeRank.append(1.0)
        elif i == 'F':
            gradeRank.append(0.0)
        elif i == 'P':
            del valueKo[-1]
            pass
        else:
            pass

    sum = 0
    gradeRankNum = len(gradeRank)
    for i in range(gradeRankNum):
        sum += gradeRank.pop()

    return round(sum/gradeRankNum,2)

for i in range(0,6,1):
    print(getAvg(i))

