# x가 연결 리스트의 몇 번 원소인지 알려주기(=인덱스를 알려줌)
def index(x):
    curr = __head  # 더미 헤드
    for index in range(__numItems):
        curr = curr.next
        if curr.item == x:
            return index
    return -12345  # x가 없을 때