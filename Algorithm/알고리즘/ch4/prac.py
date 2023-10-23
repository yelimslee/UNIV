# 5 다음은 삽입 정렬의 변형된 알고리즘이다.
# (1)이 알고리즘을 파이썬으로 구현하라
def insertion_sort2(A,n):
    for i in range(1, n):
        j = i-1
        while j >= 0 and A[j]>A[j+1]:
            A[j], A[j+1] = A[j+1], A[j]
            j = j-1

# (2)이 알고리즘의 효율은 어떨까? 알고리즘 4.3과 비교하여 설명하라
# 비효율적이다
# 항목들을 연속적으로 교환하기 때문에, 복사를 하고 마지막에 항목을 삽입하는 알고리즘보다 복사 횟수가 훨씬 많을 수 밖에 없다



# 6 셸 정렬(shell sort)은 삽입 정렬이 어느 정도 정렬된 배열에 대해서는 대단히 빠른 것에 착안한 정렬 방법이다. 
# 이 정렬 방법을 찾아보고 삽입 정렬과의 차이를 설명해 보라.
# 각 단계에서 간격(gap)을 줄이면서 정렬하고, 이것을 간격이 1이 될 때까지 여러 번 반복한다.
# 복잡도는 최악의 경우이지만 평균적인 경우으로 알려져 있다.

def sortGapInsertion(A, first, last, gap) :
    for i in range(first+gap, last+1, gap) :
        key = A[i]
        j = i - gap
        while j >= first and key<A[j] :	
            A[j + gap] = A[j]			
            j = j - gap
        A[j + gap] = key				

def shell_sort(A) : 					
    n = len(A)
    gap = n//2	#홀수가 좋음					
    while gap > 0 :
        if (gap % 2) == 0 : gap += 1	
        for i in range(gap) :
            sortGapInsertion(A, i, n - 1, gap)
        gap = gap//2					