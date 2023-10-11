# 피보나치 수열 (비재귀 버전)

import time
import datetime

# 배열 사용
def fib(n):
    if n==0 or n==1:
        return 1
    else:
        arr=[]
        arr.append(1)
        arr.append(1)
        for i in range(2,n+1):
            arr.append(arr[i-1]+arr[i-2])
        return arr[n]

def fib2(n):
    if n==0 or n==1:
        return 1
    else:
        f0=1
        f1=1
        for i in range(2,n+1):
            t=f1
            f1=f1+f0
            f0=t
        return f1    


for i in range(30,51,1):
    print("fib(%d) : "%i, end="")
    start=time.time()
    result=fib2(i)
    end=time.time()
    sec=end-start
    #print("%d 경과시간: %.5f 초"%(result,sec))
    print("%d 경과시간: %s 초"%(result,datetime.timedelta(seconds=sec)))
      
