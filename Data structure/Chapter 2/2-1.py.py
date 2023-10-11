# 공차가 3인 등차수열

def seq(n): 
    if n==1:
        return 1
    else:
        return seq(n-1)+3



print(seq(100))
