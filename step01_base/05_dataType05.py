'''
  딕셔너리는 key와 values로 이루어짐
  key는 불변하는 값만 넣을 수 있다.
'''
d1 = {1:"Hello!!"}
print(d1)     # {1: 'Hello!!'}
print(d1[1])  #  Hello!!

# 추가
d1[2] = "홍길동"
d1[5] = "고길동"

print(d1)  # {1: 'Hello!!', 2: '홍길동', 5: '고길동'}

d1['둘리'] = 24
d1['마이콜'] = 38
print(d1) # {1: 'Hello!!', 2: '홍길동', 5: '고길동', '둘리': 24, '마이콜': 38}
# 키는 중복이 안됨 ( 같은 키의 다른 값이 들어오면  덮어쓴다.)
d1[1] = 'hi'
print(d1)

d1['num'] = [1,2,3]
print(d1)

# 키 를 이용해서 삭제 할 수 있다.
del d1['num']
print(d1)

# 키에 리스트는 사용할 수 없다. 튜플은 사용 가능하다.

d2 ={"name":"홍길동", "hp":"010-7979-7979", "age":24}
# keyList  만드는 함수 => keys()
res = d2.keys();
print(res) # dict_keys(['name', 'hp', 'age'])

for k in d2.keys():
    print(k)

# key를 리스트 변환할 수 있다.
res2 = list(d2.keys())
print(res2)

# value를 리스트로 변환
res3 = d2.values();
print(res3)

# key와 value 한쌍을 얻기 (items())
# 리터값은 dict_items 객체이다. 튜플로 구성 되어있다.
res4 = d2.items()
print(res4)

# key를 이용해서 값을 얻어오기(get)
k1 = d2.get('age')
print(k1)

k2 = d2['age']
print(k2)

# 없은 키을 넣으면
k3 = d2.get('gender')
print(k3) # None

# 없는 키를 넣으면 오류 발생
# k4 = d2['gender']
# print(k4)

# 딕셔너리에서 해당 키가 존재하는지 알아보기
res5 = 'age' in d2
print(res5)  # True

res6 = 'gender' in d2
print(res6) # False

# 삭제 ; clear() => 모두 삭제
# d2.clear()
# print(d2)

#del d2["age"]
#print(d2)

#res7 = d2.pop('name')
#print(d2)

# 항목의 갯수를 구함
res8 = len(d2)
print(res8)








