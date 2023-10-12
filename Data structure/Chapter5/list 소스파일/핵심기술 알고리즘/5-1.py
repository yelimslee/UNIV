# 연결 리스트에 원소 삽입하기 (더미 헤드 X)
if i == 0:
    newNode.item = x
    newNode.next = __head
    __head = newNode
    __numItems += 1
else:
    newNode.item = x
    newNode.next = prev.next
    prev.next = newNode
    __numItems += 1