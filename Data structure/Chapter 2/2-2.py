# 피보나치 수열(재귀 버전) => 시간이 오래 걸림

import time
import datetime

def fib(n):
    if n==0 or n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)


for i in range(30,51,2):
    print("fib(%d) : "%i, end="")
    start=time.time()
    result=fib(i)
    end=time.time()
    sec=end-start
    #print("%d 경과시간: %.5f 초"%(result,sec))
    print("%d 경과시간: %s 초"%(result,datetime.timedelta(seconds=sec)))
      
