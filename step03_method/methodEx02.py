def show1(a,b,c,d):
    print(a,b,c,d)

def show2(k, e, m):
    avg = (k+e+m)/3
    print('평균 : %.2f' %avg)
    if avg>=60:
        return '합격'
    else:
        return '불합격'

def show3(avg):
    avg = int(avg/10)
    return{
        10:'A',
        9:'A',
        8:'B',
        7:'C'
    }.get(avg, 'F')

show1(10,'A', 100.4, True)

res = show2(90,80,60)
print('결과 : ', res)

res2 = show3(1557.69)
print(res2)

