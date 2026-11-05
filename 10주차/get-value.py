capitals ={"one":1,"two":2,"three":3}
print(num["one"]) #key를 사용해서 value출력
#print(num["four"]) #key error

#get() 매서드는 특정 키에 해당하는 값을 가져올 때 사용
#존재하지 않는 키를 조회해도 오류가 발생하지 않는다.

print(num.get["four", "해당 키가 없습니다."])

#get 개수를 카운트 할때 사용 --기말고사  무조건 나옴--
fruits = ["apple", "banana","apple","melon","banana","apple"]
count = {}#set을 만들려면  b = set()

for fruit in fruits:
    count[fruit] = count.get(fruit,0)+1

print(count)

'''
count=[10,20,30,40]
#print(count[3])'''

#항목 key,value출력 (items())
for key,value in count.items():
    print(key,":",value)

#딕셔너리에서 key만 출력 (key())
print(count.keys())

#딕셔너리에서 value만 출력  (values())

print(count.values())
