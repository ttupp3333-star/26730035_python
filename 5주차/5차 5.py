'''map을 써봐'''



a= list(map(int,input().split()))

max_value= a[0]


print(max(a))

'''
for i in range(1,len(a)):
    if max_value <a[i]:
        max_value = a[i]
    print(max_value)
    '''
