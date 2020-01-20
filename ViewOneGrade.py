from ExcelData import ExcelData
import matplotlib.pylab as plt

class ViewOneGrade:

    def __init__(self):
        self.excelData = ExcelData()

        self.gradeRank = []
        self.valueKo = []
        self.selectGrade = 0
        self.count = 0

    def getGradeGraph(self, gradeNum):

        del self.gradeRank[:]
        del self.valueKo[:]

        self.selectGrade = gradeNum

        tempGradeName = self.excelData.getCourseName()[self.selectGrade]

        for i in self.excelData.getRank()[self.selectGrade]:
            self.valueKo.append(tempGradeName[self.count])
            self.count += 1

            if i=='A+':
                self.gradeRank.append(4.5)
            elif i=='A0':
                self.gradeRank.append(4.0)
            elif i=='B+':
                self.gradeRank.append(3.5)
            elif i=='B0':
                self.gradeRank.append(3.0)
            elif i=='C+':
                self.gradeRank.append(2.5)
            elif i=='C0':
                self.gradeRank.append(2.0)
            elif i=='D+':
                self.gradeRank.append(1.5)
            elif i=='D0':
                self.gradeRank.append(1.0)
            elif i=='F':
                self.gradeRank.append(0.0)
            elif i=='P':
                del self.valueKo[-1]
                pass
            else:
                pass

        self.count = 0

        font1 = {'family' : 'Hancom Gothic', 'size' : 14, 'color' : 'blue'}
        font2 = {'family' : 'Hancom Gothic', 'size' : 14, 'color' : 'blue'}
        font3 = {'family' : 'Hancom Gothic', 'size' : 12, 'color' : 'blue'}

        plt.rcParams['font.family'] = 'Hancom Gothic'   # 폰트 설정
        plt.rcParams['font.size'] = 8                   # 크기 설정

        fig = plt.figure(figsize=(10,6)) # https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.figure.html

        #plt.grid() # 그리드 라인 생성 https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.grid.html

        plt.title('성적표', fontdict=font1, pad=20)
        plt.xlabel('강의명', fontdict=font2, labelpad=10)

        y = self.gradeRank
        x = range(len(y))

        plt.bar(x,y,width=0.7, color="blue")

        value = list(range(0,len(self.valueKo),1))

        plt.xticks(value,self.valueKo)
        plt.ylim(0.0,5.0)

        for i, v in enumerate(x):
            str_val = '%.2f' % y[i]
            plt.text(v, y[i], str_val, fontsize=10, color='#ff0000',
                        horizontalalignment='center', verticalalignment='bottom')

        plt.show()
