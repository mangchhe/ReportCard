from openpyxl import load_workbook

class ExcelData:

    def __init__(self):

        self.grade = 0
        self.count = 0
        self.gradeRank = []
        self.gradeCredit = []
        self.gradeName = []

        try:
            self.wb = load_workbook('collectionOfGrade.xlsx', data_only=True)
        except FileNotFoundError as err:
            print('맞지 않는 파일 이름')

        try:
            self.ws = self.wb['성적표']
        except KeyError as err:
            print('존재하지 않는 시트')

        for i in range(1,5,1):
            for j in range(1,3,1):
                for row in self.ws.rows:
                    if row[0].value == str(i) + '학년 ' + str(j) + '학기':
                        self.grade+=1
                        break

        for i in range(self.grade):
            line = []
            line2 = []
            line3 = []
            self.gradeRank.append(line)
            self.gradeCredit.append(line2)
            self.gradeName.append(line3)

    def getRank(self):
        self.count = 0
        for i in range(1,5,1):
            for j in range(1,3,1):
                for row in self.ws.rows:
                    if row[0].value == str(i) + '학년 ' + str(j) + '학기':
                        self.gradeRank[self.count].append(row[4].value)
                self.count += 1

        return self.gradeRank

    def getCredit(self):
        self.count = 0
        for i in range(1,5,1):
            for j in range(1,3,1):
                for row in self.ws.rows:
                    if row[0].value == str(i) + '학년 ' + str(j) + '학기':
                        self.gradeCredit[self.count].append(row[2].value)
                self.count += 1

        return self.gradeCredit

    def getCourseName(self):
        self.count = 0
        for i in range(1,5,1):
            for j in range(1,3,1):
                for row in self.ws.rows:
                    if row[0].value == str(i) + '학년 ' + str(j) + '학기':
                        self.gradeName[self.count].append(row[3].value)
                self.count += 1

        return self.gradeName

    def getGradeCount(self):

        return self.grade