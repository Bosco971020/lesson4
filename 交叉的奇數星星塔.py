x=int(input('請問你要幾層的交叉星星塔?'))


for i in range(1,x-1,2):
    print(' '*i+'*' + ' ' * (x*2 - i*2-1) + '*')
for i in [x]:
    print(' '*i+'*')
for i in range(1,x,2):
    print(' '*(x-i-1)+'*' + ' ' * (x*2 - (x-i)*2+1) + '*')
    


