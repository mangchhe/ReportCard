from openpyxl import load_workbook

class ExcelData:

    def __init__(self):

        self.grade = 0          # 총 이수 학기
        self.count = 0          # 현재 이수 학기 위치
        self.is_check = 0       # 학점 함수 중복 사용 제한
        self.is_check2 = 0      # 강의 이름 함수 중복 사용 제한
        self.is_check3 = 0      # 강의 학점 함수 중복 사용 제한
        self.gradeRank = []     # 학점 리스트
        self.gradeName = []     # 강의 이름 리스트
        self.courseRank = []    # 강의 학점 리스트

        try:
            self.wb = load_workbook('collectionOfGrade.xlsx', data_only=True)   # 학점 리스트 엑셀 열기
        except FileNotFoundError as err:
            print('맞지 않는 파일 이름')

        try:
            self.ws = self.wb['성적표']
        except KeyError as err:
            print('존재하지 않는 시트')

        for i in range(1,5,1):  # 총 이수 학기 계산
            for j in range(1,3,1):
                for row in self.ws.rows:
                    if row[0].value == str(i) + '학년 ' + str(j) + '학기':
                        self.grade+=1
                        break

        for i in range(self.grade): # 총 이수 학기 만큼 리스트 배열 생성
            line = []
            line2 = []
            line3 = []
            self.gradeRank.append(line)
            self.gradeName.append(line2)
            self.courseRank.append(line3)

    def getRank(self):  # 학점 get 함수
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

    def getCourseName(self):    # 강의 이름 get 함수
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

    def getCourseRank(self):    # 강의 학점 get 함수
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

    def getGradeCount(self):    # 이수 강의 갯수 get 함수

        return self.grade