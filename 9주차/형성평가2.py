'''두 정수 a, b를 한 줄로 입력받아 a부터 b까지의 합을 출력하는 프로그램을 작성하시오.

단, a는 b보다 작거나 같다.'''
a, b = map(int, input().split())

total = 0
for i in range(a, b + 1):
    total += i

print(total)
