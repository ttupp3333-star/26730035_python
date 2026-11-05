'''정수 n을 입력받아 1부터 n까지의 수 중 3의 배수를 모두 출력하는 프로그램을 작성하시오.

'''
n = int(input())

for i in range(1, n + 1):
    if i % 3 == 0:
        print(i)
