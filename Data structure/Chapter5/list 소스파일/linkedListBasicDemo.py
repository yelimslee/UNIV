# 클래스 LinkedListBasic 사용 예
from linkedListBasic import *

list = LinkedListBasic()
list.append(30); list.insert(0, 20)  # [20,30]
a = LinkedListBasic()
a.append(4); a.append(3); a.append(3); a.append(2); a.append(1)  # [4,3,3,2,1]
list.extend(a)  # [20,30,4,3,3,2,1]
list.reverse()  # [1,2,3,3,4,30,20]
list.pop(0)  # [2,3,3,4,30,20]
print("count(3):", list.count(3))
print("get(2):", list.get(2))
list.printList()

# 코드 5-16