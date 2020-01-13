from openpyxl import load_workbook

class ExcelData:

    def __init__(self):

        self.grade = 0
        self.count = 0
        self.is_check = 0
        self.is_check2 = 0
        self.is_check3 = 0
        self.gradeRank = []
        self.gradeName = []
        self.courseRank = []

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
            self.gradeName.append(line2)
            self.courseRank.append(line3)

    def getRank(self):
        if self.is_check == 0:
            self.count = 0
            if self.gradeRank is not -1:
                for i in range(1,5,1):
                    for j in range(1,3,1):
                        for row in self.ws.rows:
                            if row[0].value == str(i) + '학년 ' + str(j) + '학기':
                                self.gradeRank[self.count].append(row[4].value)
                        self.count += 1
            self.is_check = 1

        return self.gradeRank

    def getCourseName(self):
        if self.is_check2 == 0:
            self.count = 0
            for i in range(1,5,1):
                for j in range(1,3,1):
                    for row in self.ws.rows:
                        if row[0].value == str(i) + '학년 ' + str(j) + '학기':
                            self.gradeName[self.count].append(row[3].value)
                    self.count += 1
            self.is_check2 = 1
        return self.gradeName

    def getCourseRank(self):
        if self.is_check3 == 0:
            self.count = 0
            for i in range(1,5,1):
                for j in range(1,3,1):
                    for row in self.ws.rows:
                        if row[0].value == str(i) + '학년 ' + str(j) + '학기':
                            self.courseRank[self.count].append(row[2].value)
                    self.count += 1
        self.is_check3 = 1

        return self.courseRank

    def getGradeCount(self):

        return self.grade