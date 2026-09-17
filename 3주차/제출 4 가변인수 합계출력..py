'''a=[1,2,3] -리스트는 수정가능
b=(1,2,3)- 튜플은 안의 값을 변경,수정 못함'''


def add(a,b=10,*numbers): #가변인수가 제일 마지막에 위치!! *numbers가 무조건 a,b=10뒤에!
    sum =0
    for i in numbers: 
        sum= sum+i
    return sum
'''print(type(numbers)) #가변인수 값은 튜플이다.'''
print(add(10,20,30,40,50))
