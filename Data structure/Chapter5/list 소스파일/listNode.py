# 노드 객체를 만드는 클래스

class ListNode:
	def __init__(self, newItem, nextNode:'ListNode'):
		self.item = newItem
		self.next = nextNode
		