import matplotlib.pyplot as plt

plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False

fig = plt.figure()
ax = fig.add_subplot(1,1,1)


ax.set_xlim([0.,10.])  # x 축에 대해서   0-10 까지
ax.set_ylim([0., 2.5])  # y 축에 대해서  0.0 ~ 2.5 까지
ax.set_title("Chart 연습", size=15)
ax.set_xlabel('x-axis', size=12)
ax.set_ylabel('y-axis', size=12)

plt.show()