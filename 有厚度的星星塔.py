x=int(input('請問你要多厚的星星塔?'))

for i in range(x+1):
    print('*'*i)
for i in range(x):
    print('*'*((x-1)-i))
    