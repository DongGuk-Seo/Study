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

# 이진 탐색 트리 삭제
# Leaf Node 삭제 - 삭제할 Node의 Parent Node가 삭제할 Node를 가리키지 않도록 한다.
# Child Node 삭제(Child Node가 단일 branch) - 삭제할 Node의 Parent Node가 삭제할 Node의 Child Node를 가리키도록 한다.
# Child Node가 두 개인 Node 삭제
## 1. 삭제할 Node 오른쪽 자식 중 가장 작은 값을 삭제할 Node의 Parent Node가 가리키도록 한다.
## - 삭제할 Node의 오른쪽 자식 선택
## - 오른쪽 자식의 가장 왼쪽에 있는 Node를 선택
## - 해당 Node를 삭제할 Node의 Parent Node의 왼쪽 branch가 가리키게 함
## - 해당 Node의 왼쪽 branch가 삭제할 Node의 왼쪽 Child Node를 가리키게 함
## - 해당 Node의 오른쪽 branch가 삭제할 Node의 오른쪽 Child Node를 가리키게 함
## - 만약 해당 Node가 오른쪽 Child Node를 가지고 있었을 경우, 해당 Node의 본래 Parent Node의 왼쪽 branch가 해당 오른쪽 Child Node를 가리키게 함


## 2.삭제할 Node의 왼쪽 자식 중 가장 큰 값을 삭제할 Node의 Parent Node가 가리키도록 한다.

# 데이터 입력
head = Node(1)
BST = NodeMgmt(head)
BST.insert(2)
BST.insert(3)
BST.insert(0)
BST.insert(4)
BST.insert(8) 