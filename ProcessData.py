from ExcelData import ExcelData

class ProcessData:  # 엑셀 값 받아와 가공하는 클래스

    def __init__(self):
        self.excelData = ExcelData()

    def getAvg(self, semester): # 평균값 반환

        gradeRank = []
        selectGrade = semester

        tempGradeName = self.excelData.getCourseName()[selectGrade]
        valueKo = []
        tempCourseRank = self.excelData.getCourseRank()[selectGrade]
        valueKo2 = []

        for i in self.excelData.getRank()[selectGrade]: # 한 학기에 존재하는 강의 개수만큼 반복
            valueKo.append(tempGradeName[0])
            del tempGradeName[0]
            valueKo2.append(tempCourseRank[0])
            del tempCourseRank[0]

            if i == 'A+':               # 각 학점 점수로 변환
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
                del valueKo2[-1]
                pass
            else:
                pass

        sum = 0
        sumCount = 0
        gradeRankNum = len(gradeRank)
        for i in range(len(valueKo2)):  # 총 이수 학점 계산
            sumCount += valueKo2[i]

        for i in range(gradeRankNum):   # 평균 학점 계산
            sum += gradeRank.pop() * valueKo2.pop()

        return round(sum/sumCount,2)    # 평균 학점 반환