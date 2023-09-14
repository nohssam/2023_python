import pandas as pd

e_list = [[100,"이도", "CEO"],
          [110,"마루치", "IT_PROG"],
          [121,"홍길동", "IT_PROG"],
          [227,"둘리", "IT_PROG"],
          [247,"공실이", "MANAGE"],
          ]
s_name = ["empno", "name", "job_id"]

df = pd.DataFrame(e_list,columns=s_name)
print(df)
print('-' * 30)

# empno 가 200이상인 사람의 정보
# print(df[df.empno >= 120])
print(df.query('empno>=200'))
print('-' * 30)

# empno 가 200이상이면서 job_id가 'IT_PROG' 인 사람
#print(df[(df.empno >= 200) & (df.job_id == 'IT_PROG')])
print(df.query('empno>=200 and job_id == "IT_PROG"'))
print('-' * 30)

# 행과 열 삭제하기 : (drop)
# 원본이 삭제되는 것은 아니다.
# 보통행을 삭제할때는 index 번호를 가지고 삭제한다.
# 첫번째 행과 세번째 행을 삭제하자
# print(df.drop([0,2]))
res =  df.drop([0,2])
print(res)
print(type(res))
print('-' * 30)
print(df)
print('-' * 30)

# 특정 컬럼 삭제
res2 = df.drop(columns='empno')
print(res2)









