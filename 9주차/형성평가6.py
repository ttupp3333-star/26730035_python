'''0이 입력될 때까지 정수를 계속 입력받아 짝수의 개수를 출력하는 프로그램을 작성하시오.''
'''
count = 0

while True:
    n = int(input())
    if n == 0:
        break
    if n % 2 == 0:
        count += 1

print(count)'
