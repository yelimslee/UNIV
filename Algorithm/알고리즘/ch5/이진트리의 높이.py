# 이진트리를 위한 노드 클래스
class TNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def calc_height(root):
    if root is None:  # 기본연산
        return 0
    hLeft = calc_height(root.left)
    hRight = calc_height(root.right)
    return max(hLeft, hRight) + 1  # 기본연산

# 입력의 크기: n
# T(n) = T(nleft) + T(nright) +1, T(0) = 0
# O(n)

d = TNode('D', None, None)
e = TNode('E', None, None)
b = TNode('B', d, e)
f = TNode('F', None, None)
c = TNode('C', f, None)
root = TNode('A', b, c)		# 루트 노드
print(" 트리의 높이 =", calc_height(root))




# 주어진 이진트리에서 모든 노드의 수를 계산하는 알고리즘을 분할 정복 기법으로 설계하라
class TNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

    def count_node(n):
        if n is None:
            return 0
        else:
            return 1 + count_node(n.left) + count_node(n.right)
        

# 주어진 이진트리에서 단말 노드의 수를 계산하는 알고리즘을 분할 정복 기법으로 설계하라.
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

    def isLeaf(self):  # 단말노드인지 확인
        return self.left == None and self.right == None
    
    def count_leaf(n):
        if n is None:
            return 0
        elif n.isLeaf():  # 단말노드
            return 1
        else: return count_leaf(n.leaf) + count_leaf(n.right)  # 중간노드이면 왼쪽단말노드 + 오른쪽 단말노드