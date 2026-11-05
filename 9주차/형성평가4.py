'''정수 n을 입력받아 n의 약수를 모두 출력하는 프로그램을 작성하시오.

'''
n = int(input())

for i in range(1, n + 1):
    if n % i == 0:
        print(i)
