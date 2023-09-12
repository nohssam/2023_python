import matplotlib.pyplot as plt

names = ["Python", "Java","Spring","Flask"] # x 축의 값
score = [155,301,125,98] # y 축의 값


# 한글 깨짐 처리
plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False
plt.rcParams["font.size"] = 15

plt.plot(names,score, color="#f00")
plt.title("2022년도 개발언어 순서")
plt.xlabel("Language")
plt.ylabel("Preference")
plt.show()