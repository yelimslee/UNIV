#19
def asterisk(i):
    if i > 1:
        asterisk(i/2)
        asterisk(i/2)
    print("*", end='')

asterisk(5)  # ***************(15)


#21
def mystery3(n):
    if n == 1:
        return 1
    else:
        return mystery3(n-1) + 2*n-1
    
print(mystery3(3))  # 9

# 이 알고리즘의 반환값에 대한 순환 관계식을 만들고 풀어라. 
# => F(n) = F(n-1)+2n-1, F(1) = 1
# 이것은 무슨 알고리즘인가? => n²을 구하는 알고리즘

