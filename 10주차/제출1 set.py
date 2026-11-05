#len() 개수반환
fruits={"apple","banana","grape"}
size =len(fruits)
print(size)

# in 포함되는지
string = input()
fruits={"apple","banana","grape"}
if string in fruits:
    print(string,"있습니다.")
else:
    print(string,"없습니다.")
# 출력 (순서가 없다)
fruits={"apple","banana","grape"}
print(fruits)

#출력(출력시 정렬해서 출력할 수는 있다)
fruits={"apple","banana","grape"}
for x in sorted(fruits, reverse = True):
    print(x, end="")

# add() 요소추가
fruits={"apple","banana","grape"}
fruits.add("kiwi")
print(fruits)
fruits.discard("o")
print(fruits)
fruits.clear()
print(fruits)
