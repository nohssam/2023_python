import matplotlib.pyplot as plt

names = ["Python", "Java","Spring","Flask"] # x 축의 값
score = [155,301,125,98] # y 축의 값

# plt.plot(names,score, color="#f00")
plt.bar(names,score, color="skyblue")
plt.show()