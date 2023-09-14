from pandas  import DataFrame

df = DataFrame([
    {'name':'홍길동', 'b_day':'1987-10-09'},
    {'name':'일지매', 'b_day':'1993-04-22'},
    {'name':'장길산', 'b_day':'2001-09-09'},
    {'name':'임꺽정', 'b_day':'1996-11-11'},
])
print(df)
print('-'*50)

def clip_year(col):
    return col.split('-')[0]

# b-day가 clip_year 함수에 적용되어서 df에 추가 한다.
df['year'] = df['b_day'].apply(clip_year)
print(df)
print('-'*50)

def get_age(year, c_year):
    return c_year - int(year)

df['age'] = df['year'].apply(get_age, c_year=2023)
print(df)
print('-'*50)











