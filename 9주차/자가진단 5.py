'''입력받은 정수를 2로 계속 나누어
1이 될 때까지 출력하는 프로그램을 작성하시오.'''

a = int(input())

while a > 1:
    print(a)
    a //= 2

print(1)  
