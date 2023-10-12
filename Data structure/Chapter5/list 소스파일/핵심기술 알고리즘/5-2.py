# 연결 리스트에 원소 삽입하기 (더미 헤드를 두는 대표 버전)
newNode.item = x
newNode.next = prev.next
prev.next = newNode
__numItems += 1