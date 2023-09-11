# 키와 값을 쌍으로 가지고 있는 튜플 리스트을 dict 생성하자
person = [('민들래', 30), ('개나리', 35), ('진달래',25)]
mydict = dict(person)
print(type(mydict))

age = mydict['개나리']
print(age)

score = dict(a=80, b=90, c=85)
print(type(score))
print(score['b'])

# 추가, 삭제 , 수정 , 읽기
# [] => 리스트, ()=> 튜플, {}=> 딕셔너리
person2 = {'민들래':30, '개나리':35, '진달래':25}
print(person2)

person2['진달래'] = 47   # 수정
print(person2)

person2['할미꽃'] = 15  # 추가
print(person2)

del person2['개나리']  # 삭제
print(person2)

# 만약에 없는 키를  get(key)사용하면 오류가 아니라 None이 출력
print(person2.get('장미꽃'))
# print(person2['장미꽃'])  # 오류 출력










