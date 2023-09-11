print("첫번째 수를 입력하세요 : ")
s1 = input()

print("두번째 수를 입력하세요 : ")
s2 = input()

result = int(s1) +  int(s2)

print("{0} * {1} = {2}".format(s1, s2, result))
print("{1} * {0} = {2}".format(s1, s2, result))