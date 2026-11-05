'''1부터 입력받은 수까지의 홀수의 합을 출력하는 프로그램을 작성하시오'''

a= int(input())
s=0
for i in range(1,a+1):
    if i%2==1:
        s += i
print(s)
