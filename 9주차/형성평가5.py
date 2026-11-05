'''1부터 차례대로 곱하여 나가다가 곱한 결과가 입력받은 수 이상이 되는 최초의 값을 출력하는 프로그램을 작성하시오.'''
n = int(input())

product = 1
i = 1

while product < n:
    i += 1
    product *= i

print(product)
