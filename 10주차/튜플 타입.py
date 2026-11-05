#b,c,d =1,2,3
#print(type(b),type(c),type(d))

#turple
#a =1,2,3
#print(type(a))

#list
a= 1,2,3 # <-- turple
a = list(a)
print(type(a))

#set(고유한 값을 가진다, 순서가 없다)
a= set({1,2,3,1,2,3,1,2,3})
print(a)

b= [1,2,3,1,2,3,1,2,3]
a= set(b)
print(*a)
