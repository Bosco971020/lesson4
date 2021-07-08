x=int(input('請問你要幾層的交叉星星塔?"只能輸入奇數"'))
if x%2==0:
    print('奇數only!')
elif x==1:
    print('你輸入的數字太小了!')
elif x>=55:
    print('你輸入的數字太大了!')
else:
    for i in range(1,x-1,2):
        print(' '*i+'*' + ' ' * (x*2 - i*2-1) + '*')
    for i in [x]:
        print(' '*i+'*')
    for i in range(1,x,2):
        print(' '*(x-i-1)+'*' + ' ' * (x*2 - (x-i)*2+1) + '*')
    


