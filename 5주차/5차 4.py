'''정수 N개를 입력받아 리스트에 저장한 후 모든 값의 평균을 출력하는 프로그램 작성
(정수부분만 출력한다)'''

N= int(input())
lst =[]

for i in range(N):
    temp = int(input())
    lst.append(temp)

print(int(sum(lst)/N))


'''
다른예시

total = 0
for i in lst:
     total += i


print(int(sum(lst)/len(lst))'''
