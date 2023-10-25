# 억지 기법
def multiply(A, B, C):
    n = len(A)
    for i in range(n):
        for j in range(n):
            C[i][j] = 0
            for k in range(n):
                C[i][j] += A[i][k]*B[k][j]

# O(n³)


# 쉬트라쎈 (거의 O(n³))
import numpy as np 		# numpy모듈을 np란 이름으로 사용함
def strassen(A, B): 		# A, B : numpy모듈의 array 객체
    n = len(A)
    if n == 1:         	# 1x1 행렬
        return A * B 		# 실수의 곱셈

    n2 = n//2
    A11, A12, A21, A22 = A[:n2, :n2], A[:n2, n2:], A[n2:, :n2], A[n2:, n2:] 
    B11, B12, B21, B22 = B[:n2, :n2], B[:n2, n2:], B[n2:, :n2], B[n2:, n2:] 

    M1 = strassen(A11+A22, B11+B22)   
    M2 = strassen(A21+A22, B11)         
    M3 = strassen(A11, B12-B22)         
    M4 = strassen(A22, B21-B11)         
    M5 = strassen(A11+A12, B22)         
    M6 = strassen(A21-A11, B11+B12)   
    M7 = strassen(A12-A22, B21+B22)   # M1~M7을 위해 각각 곱셈--> 총 7번 
  
    C11 = M1 + M4 - M5 + M7   
    C12 = M3 + M5            
    C21 = M2 + M4             
    C22 = M1 + M3 - M2 + M6   		# 덧셈/뺄셈 연산(+,-)은 총 18번 
  
    C = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))  
  
    return C 