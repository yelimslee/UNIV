# 연결 리스트의 i번 원소 알려주기(=원소를 알려줌)
def get(i):
    if i >= 0 and i < numItems:
        return __getNode(i).item
    else:
        print("error in get(", i, ")")