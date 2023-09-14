from pandas  import DataFrame

m_dict = [{'id':1010, 'name':'마루치', 'Java':89, 'Python':78, 'Flask':90},
          {'id':1230, 'name':'아라치', 'Java':96, 'Python':80, 'Flask':92},
          {'id':1902, 'name':'을불', 'Java':90, 'Python':74, 'Flask':90},
          {'id':2002, 'name':'창조리', 'Java':98, 'Python':88, 'Flask':94}]
df = DataFrame(m_dict)
print(df)
print()

print("--- 총점을 의미하는  total 컬럼 추가 ")
df['total'] = df['Java'] + df['Python'] + df['Flask']
print(df)
print()

print("--- 평균을 의미하는 avg 컬럼 추가 ")
df['avg'] = df['total'] /3
print(df)
print()

print("--- 평균을 이용해서 학점을 의미하는 grade 컬럼 추가 ")
grade =[]

for i in df['avg']:
    if i >= 90:
        grade.append("A")
    elif i >= 80:
        grade.append("B")
    elif i >= 70:
        grade.append("C")
    else:
        grade.append("F")

df['grade'] = grade
print(df)









