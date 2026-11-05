'''-1이 입력될 때까지 정수를 계속 입력받아 합계를 출력하는 프로그램을 작성하시오.'''
total = 0

while True:
    n = int(input())
    if n == -1:
        break
    total += n

print(total)
