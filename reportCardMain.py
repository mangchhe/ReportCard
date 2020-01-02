import matplotlib as mpl
import matplotlib.pylab as plt
import matplotlib.font_manager

#mpl.rc('font', family='Hancom Gothic')
#mpl.rc('axes', unicode_minus=False)

font1 = {'family' : 'Hancom Gothic', 'size' : 14, 'color' : 'blue'}
font2 = {'family' : 'Hancom Gothic', 'size' : 14, 'color' : 'blue'}
font3 = {'family' : 'Hancom Gothic', 'size' : 12, 'color' : 'blue'}

plt.rcParams['font.family'] = 'Hancom Gothic'   # 폰트 설정
plt.rcParams['font.size'] = 8                   # 크기 설정

fig = plt.figure(figsize=(10,6)) # https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.figure.html

plt.grid() # 그리드 라인 생성 https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.grid.html

plt.title('성적표', fontdict=font1, pad=20)
plt.xlabel('학기', fontdict=font2, labelpad=10)
#plt.ylabel('성적', fontdict=font3)

zum = [1.2,2.1,2.7,3.2,3.7,4.0,4.3]
plt.plot(zum, ls=":", marker="o", mec="b", mfc="b")
value = list(range(0,len(zum),1))
valueKo = []
for i in range(0,len(zum)+1,1):    # 평균 값 차트 그리기
    if(i%2 == 0):   # 1학기
        valueKo.append(str(i//2+1) + '학년 ' + '1학기')
    elif(i%2 == 1): # 2학기
        valueKo.append(str(i//2+1) + '학년 ' + '2학기')

plt.xticks(value,valueKo)
#plt.yticks([0.0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5])

#plt.xlim(0,9)
plt.ylim(0.0,5.0)

for i, v in enumerate(value):
    str_val = '%.2f' % zum[i]
    plt.text(v, zum[i], str_val, fontsize=10, color='#ff0000',
                horizontalalignment='center', verticalalignment='bottom')

plt.show()