# 기타 작업들
def isEmpty():  # 리스트가 비었는지 알려주기
    return __numItems == 0

def size():  # 리스트의 총 원소 수 알려주기
    return __numItems

def clear():  # 리스트 깨끗이 청소하기
    newNode.next = None  # 더미 헤드 노드
    __head = newNode
    __numItems = 0