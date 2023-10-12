# 연결 리스트의 원소 삭제하기
if i == 0:
    __head.next = __head.next.next
    __numItmes -= 1
else:
    prev.next = prev.next.next
    __numItems -= 1