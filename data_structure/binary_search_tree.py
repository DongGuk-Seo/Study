# 이진트리 구현 [5, 11, 12, 14, 15, 18, 19, 21, 23, 25, 27, 28, 30, 32, 37]

# 1. 노드 클래스 만들기
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

# 2. 이진 탐색 트리에 데이터 넣기
class NodeMgmt: 
    def __init__(self,head): # root node
        self.head = head
    
    def insert(self, value): # node 입력 모듈
        self.current_node = self.head
        while True:
            if value < self.current_node.value:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break
    
    def search(self, value): # 이진 탐색 트리 탐색 모듈
        self.current_node = self.head
        while self.current_node:
            if self.current_node.value == value:
                return True
            elif value < self.current_node.value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right
        return False

# 데이터 입력
head = Node(1)
BST = NodeMgmt(head)
BST.insert(2)
BST.insert(3)
BST.insert(0)
BST.insert(4)
BST.insert(8)

print(BST.search(-1))