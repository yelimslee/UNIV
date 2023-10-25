# 자료구조란?
# 데이터를 저장, 조직, 관리하는 방법.
# 문제 해결에 사용할 부품.
# 생각하는 방법을 훈련하는 도구

# 추상 데이터 타입(ADT) : 어떤 데이터 타입이 어떤 작업으로 이루어지는지만 표현

# 재귀: 내 안에 나를 찾는 것, 성격은 같고 크기만 작은 나를 찾아 
#큰 나와 작은 내가 연결된 관계를 드러내는 것
# 재귀 알고리즘 = 자기호출 알고리즘

# 피보나치, 팩토리억, 하노이탑, 선택정렬 => 재귀/ 바재귀
# 재귀는 잘못 쓰면 치명적


# 공차가 3인 등차수열
from http.client import NETWORK_AUTHENTICATION_REQUIRED
from operator import truediv
from re import X


def seq(n):
    if n==1:
        return 1
    else:
        return seq(n-1)+3
    
# 피보나치 수열(재귀)
def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n+1)
    
# 피보나치 (비재귀)
def fib(n):
    if n==0 or n==1:
        return 1
    else:
        f0 = 1
        f1 = 1
        for i in range(2, n+1):
            t = f1
            f1 = f0+f1
            f0 = t
        return f1
    
def fib(n):
    if n==0 or n==1:
        return 1
    else:
        arr = []
        arr.append(1)
        arr.append(1)
        for i in range(2, n+1):
            arr.append(arr[i-1] + arr[i-2])
            return arr[n]
        
# 하노이탑  / 최종 b로 옮김  / T(n) = 2ⁿ-1
def hanoi(n, a, b, c):
    if n > 0:
        hanoi(n-1, a, c, b)
        print()
        hanoi(n-1, c, b, a)

def hanoi2(n, scr, dest):
    if n > 0:
        mid = 6-scr-dest
        hanoi2(n-1, scr, mid)
        print()
        hanoi2(n-1, mid, dest)

# 선택정렬 (재귀)  / 제일 큰 수를 찾아 맨마지막 인덱스와 바꾸고, n-1재귀
def theLargest(A, last):
    largest = 0
    for i in range(last+1):
        if A[i] > A[largest]:
            largest = A[i]
    return largest

def selectionSort(A, n):
    if n > 1:
        last = n-1
        k = theLargest(A, last)
        A[k], A[last] = A[last], A[k]
        selectionSort(A, last)

# 선택정렬 (비재귀)  / for문 뒤에서 순회, 제일 큰 수를 찾아  바꿈
def selectionSort(A, n):
    for last in range(n-1, 0, -1):
        k = theLargest(A, last)
        A[k], A[last] = A[last], A[k]

# 재귀 필수조건  1) 경계조건  2) 재귀호출  3) 닮은꼴 작은 문제 관계





# 알고리즘 수행시간 
# for문 쓸때 +1, 재귀할 떄 +1

# 점근적 복잡도: 입력의 크기가 충분이 클때의 복잡도
# 기껏해야 => O()
# 적어도 => Ω()
# 항상 => Θ()




# 리스트- 배열리스트, 연결리스트, 비교
# 내장리스트의 한계: 하부가 배열로 구현됨
# 배열의 단점: 연속된 공간에 저장되므로 삽입이나 삭제시 시프트 작업이 필요하다
#             미리 크기를 정해야 하므로 오버플로우시 배열을 새로 배정받아 내용을 복사해야 한다.

# 더미헤드를 사용하는 장단점
# 장점: 맨 앞 삽입의 경우, 중간 삽입과 같은 방법으로 가능. 로직의 일관성
# 단점: 메모리 추가 사용, 없어도 가능


# 연결리스트 클래스 구조(더미헤드)
from listNode import ListNode

class LinkedListBasic:
    def __init__(self):
        self.__head = ListNode('dummy', None)
        self.__numItems = 0

        #삽입
        def insert(self, i:int, newItem):
            if i >= 0 and i <= self.__numItems:
                prev = self.__getNode(i-1)
                newNode = ListNode(newItem, prev.next)
                prev.next = newNode
                self.__numItems += 1
            else:
                print("없음")

        def append(self, newItem):
            prev = self.__getNode(self.__numItems-1)
            newNode = ListNode(newItem, prev.next)
            prev.next = newNode
            self.__numItems += 1

        #삭제
        def pop(self, i:int):
            if (i>=0 and i<= self.__numItems-1):
                prev = self.__getNode(i-1)
                curr = prev.next
                prev.next = curr.next
                retItem = curr.item
                self.__numItems -= 1
            else:
                return None
            
        def remove(self, x):
            (prev, curr) = self.__findNode(x)
            if curr != None:
                prev.next = curr.next
                self.__numItems -= 1
                return x
            else:
                return None
            
        def get(self, i:int):
            if self.isEmpty():
                return None
            if (i>=0 and i<=self.__numItems-1):
                return self.__getNode(i).item
            else:
                return None
            
        def index(self, x) -> int:
            curr = self.__head.next
            for index in range(self.__numItems):
                if curr.item == x:
                    return index
                else:
                    curr = curr.next
            return -2
        
        def isEmpty(self) -> bool:
            return self.__numItems == 0
        
        def size(self) -> int:
            return self.__numItems
        
        def clear(self):
            self.__head = ListNode("dummy", None)
            self.__numItems = 0

        def count(self, x) -> int:
            cnt = 0
            curr = self.__head.next
            while curr != None:
                if curr.item == x:
                    cnt += 1
                    curr = curr.next
            return cnt
        
        def extend(self, a):
            for index in range(a.size()):
                self.append(a.get(index))

        def copy(self):
            a = LinkedListBasic()
            for index in range(self.__numItems):
                a.append(self.get(index))
            return a
        
        def revese(self):
            a = LinkedListBasic()
            for index in range(self.__numItems):
                a.inset(0, self.get(index))
            self.clear()
            for index in range(a.size()):
                self.append(a.get(index))

        def sort(self) -> None:
            a = []
            for index in range(self.__numItems):
                a.append(self.get(index))
                a.sort()
                self.clear()
                for index in range(len(a)):
                    self.append(a[index])

        def __findNode(self, x) -> (ListNode, ListNode):
            prev = self.__head
            curr = prev.next
            while curr != None:
                if curr.item == x:
                    return (prev, curr)
                else:
                    prev = curr, curr = curr.next
            return(None, None)
        
        def __getNode(self, i:int) -> ListNode:
            curr = self.__head
            for index in range(i+1):
                curr = curr.next
            return curr
        
        def print(self):
            curr - self.__head.next
            while curr != None:
                print(curr.item, end=' ')
                curr = curr.next
            print()



# 원소 x가 존재하는지 체크메소드
def contains(self, x) -> bool:
    return index(x) >= 0

# i부터 j까지 원소 출력메소드
def printInterval(self, i:int, j:int):
    t = self.head
    for index in range(j+1):
        t = t.next
        if (i <= index):
            print(element, end = '')
    print()

# 원소 수 확인메소드 (재귀/비재귀)
#비재귀
def numItems(self):
    t = self.__head.next
    cnt = 0
    while (t != None):
        cnt += 1
        t = t.next
    return cnt

#재귀
def numItems(self):
    return __nItem(self.__head.next)

def __nItem(self, t):
    if (t == None):
        return 0
    else:
        return __nItem(t.next) +1
    
# i번 노드부터 k개 삭제메소드
def pop(self, i:int, k:int):
    prev = self.__getNode(i-1)
    curr = prev
    for _ in range(k):
        if (curr.next == None):
            break
        curr = curr.next
        self.numItems -= 1
    prev.next = curr.next

# 두 노드가 같은 연결리스트에 속하는지 확인하는 메소드
def sameList(node1, node2):
    curr = node1
    while (curr != None):
        curr = curr.next
        if (curr == node2):
            return True
    curr = node2
    while (curr != None):
        curr = curr.next
        if (curr == node1):
            return True
        
# 맨마지막 x인덱스 찾는 메소드
NOT_FOUND = -12345
def lastIndexOf(self, x):
    curr = self.__head
    lastIndex = NOT_FOUND
    for i in range(self.__numItems):
        curr = curr.next
        if curr.item == x:
            lastIndex = i
    return lastIndex






# 스택의 예: 식당주방 접시, 키보드입력 백스페이스, 계산기

#리스트스택
class ListStack:
    def __init__(self):
        self.__stack = []

    def push(self, x):
        self.__stack.append(x)
    
    def pop(self):
        return self.__stack.pop()
    
    def top(self):
        if self.isEmpty():
            return None
        else:
            return self.__stack[-1]
        
    def isEmpty(self) -> bool:
        return not bool(self.__stack)
    
    def popALL(self):
        self.__stack.clear()

    def printStack(self):
        print("stack from top: ", end= ' ')
        for i in range(len(self.__stack)-1, -1, -1):
            print(self.__stack[i], end=' ')
        print()

#연결리스트스택
from linkedListBasic import *

class LinkedStack:
    def __init__(self):
        self.__list = LinkedListBasic()

    def push(self, newItem):
        self.__list.insert(0, newItem)

    def pop(self):
        return self.__list.pop(0)
    
    def top(self):
        if self.isEmpty():
            return None
        else:
            return self.__list.get(0)
        
    def isEmpty(self) -> bool:
        return self.__list.isEmpty()
    
    def popAll(self):
        self.__list.clear()

    def printStack(self):
        print("stack from top:", end= ' ')
        for i in range(self.__list.size()):
            print(self.__list.get(i), end='')
        print()

# abcd$dcba 같이 되어있는지 검사
def checkString(string):
    i = 0
    for i in range(1, string.length):
        if (string[i] == '$'):
            break
        stack.push(string[i])
    for j in range(i+1, string.length):
        if (stack.isEmpty()): 
            return False
        if (stack[j] != stack.pop()): 
            return False
    if (stack.isEmpty()): 
        return True
    else: 
        return False
    
# a를 b로 복사하는 코드
def copyStack(self, stack):
    tmpStack = LinkedStack()
    while (not self.isEmpty()):
        tmpStack.push(self.pop())
    while (not tmpStack.isEmpty()):
        item = tmpStack.pop()
        self.push(item)
        stack.push(item)

# 괄호 확인
def parenBalance(s:String):
    stack = ListStack()
    for i in range(len(s)):
        if s[i] == '(' or '[' or '{':
            stack.push(s[i])
        elif s[i] == ')' or ']' or '}':
            if stack.isEmpty():
                return False
            if stack.pop() != s[i]:
                return False
    return stack.isEmpty()





# 큐의 예: 병원에서 번호표, 서비스센터의 콜, 유투브 버퍼링

# 선형 큐
# 선형 큐의 단점: 리스트의 맨 앞에서 항목을 삭제하면 그 항목들 이후의 모든 항목을 한칸씩 앞으로 이동해야 함
items = []

def isEmpty():
    return len(items) == 0

def enqueue(item):
    items.append(item)

def dequeue():
    if not isEmpty():
        return items.pop(0)

def peek():
    if not isEmpty():
        return items[-1]

def display():
    print(items)

# 원형 큐
# front는 항상 비워놔야함, rear
# 공백상태 : front == rear
# 포화상태 : front % M == (rear+1) % M
# 사이즈: (self.rear - self.front + MAX_QSIZE) % MAX_QSIZE
# 출력: if self.front < self.rear:
#           out = self.items[self.front+1:self.rear+1]

MAX_QSIZE = 10
class CircularQueue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.items = [None] * MAX_QSIZE

    def isEmpty(self): 
        return self.front == self.rear
    
    def isFull(self):
        return self.front == (self.rear+1) % MAX_QSIZE
    
    def clear(self):
        self.front = self.rear

    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear+1) % MAX_QSIZE
            self.items[self.rear] = item

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front+1) % MAX_QSIZE
            return self.items[self.front]
        
    def peek(self):
        if not self.isEmpty():
            return self.items[(self.front+1) % MAX_QSIZE]
        
    def size(self):
        return 
    
    def display(self):
        out = []
        if self.front < self.rear:
            out = self.items[self.front+1:self.rear+1]
        else:
            out = self.items[self.front+1:MAX_QSIZE] \
                + self.items[0:self.rear+1]
        print()


# 원형 덱
class CircularDeque(CircularQueue) :	          
    def __init__( self ) :		                  
        super().__init__()		                  

    def addRear( self, item ): self.enqueue(item )
    def deleteFront( self ): return self.dequeue()
    def getFront( self ): return self.peek()		
   
    def addFront( self, item ):			          
        if not self.isFull():
            self.items[self.front] = item        
            self.front = self.front - 1		      
            if self.front < 0 : self.front = MAX_QSIZE - 1

    def deleteRear( self ):			      
        if not self.isEmpty():
            item = self.items[self.rear];
            self.rear = self.rear - 1		
            if self.rear < 0 : self.rear = MAX_QSIZE - 1
            return item			     

    def getRear( self ):			 
        return self.items[self.rear]