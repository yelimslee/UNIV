class TNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

# 전위 순회(VLR)
def preorder(n):
    if n is not None:  # 기본 연산
        print(n.data, end=' ')  # 기본 연산
        preorder(n.left)
        preorder(n.right)

# 중위 순회(LVR)
def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.data, end= ' ')   # 기본 연산
        inorder(n.right)

# 후위 순회(LRV)
def postorder(n):
    if n is not None:
        postorder(n.left)
        postorder(n.right)
        print(n.data, end= ' ')   # 기본 연산


# 출력문을 기본연산으로 하면 T(n) = n, => O(n)
# 공백 트리를 기본연산으로 하면 T(n) = n+x,  => O(n)


d = TNode('D', None, None)
e = TNode('E', None, None)
b = TNode('B', d, e)
f = TNode('F', None, None)
c = TNode('C', f, None)
root = TNode('A', b, c)		# 루트 노드


print('  Pre-Order : ', end='')
preorder(root)
print()
print('   In-Order : ', end='')
inorder(root)
print()
print(' Post-Order : ', end='')
postorder(root)
print()
