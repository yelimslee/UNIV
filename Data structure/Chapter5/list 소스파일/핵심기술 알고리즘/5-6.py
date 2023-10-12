# 연결 리스트의 i번 노드 알려주기
def __getNode(i):
    curr = __head
    for index in range(i+1):
        curr = curr.next
    return curr