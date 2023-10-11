# 하노이 탑

import time
# a에서 b로 옮김
def hanoi(n,a,b,c):
    if n>0:
        hanoi(n-1, a, c, b)
        print("%d : %d->%d"%(n,a,b))
        hanoi(n-1,c,b,a)

def hanoi2(n,src,dest):
    if n>0:
        mid=6-src-dest
        hanoi2(n-1, src, mid)
        print("%d : %d->%d"%(n,src,dest))
        hanoi2(n-1,mid,dest)

hanoi(10,1,2,3)
hanoi2(10,1,2)
