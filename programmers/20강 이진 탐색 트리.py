## 프로그래머스 자료구조와 알고리즘 20강 이진 탐색 트리의 원소 삽입 연산 구현

class Node:

    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None

## 방법 1 재귀적으로 insert 구현
    def insert(self, key, data):
        if key < self.key:
            if self.left:
                self.left.insert(key, data)
            else :
                self.left = Node(key, data)
        elif key > self.key:
            if self.right:
                self.right.insert(key, data)
            else :
                self.right = Node(key, data)
        else:
            raise KeyError("중복된 키 허용 안함")
## 왼쪽, 오른쪽 서브트리가 존재하지 않을때 조건으로 insert 구현
    # def insert(self, key, data):
    #     if key < self.key:
    #         if self.left is None:
    #             self.left = Node(key, data)
    #             return
    #         self = self.left
    #         self.insert(key, data)
    #     elif key > self.key:
    #         if self.right is None:
    #             self.right = Node(key, data)
    #             return
    #         self = self.right
    #         self.insert(key, data)
    #     else:
    #         raise KeyError("...")

    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self)
        if self.right:
            traversal += self.right.inorder()
        return traversal

    def min(self):
        if self.left:
            return self.left.min()
        else:
            return self
    def max(self):
        if self.right:
            return self.right.max()
        else:
            return self

# 트리에서 key 조회, parent는 삭제 연산 시 필요해 구한다, 자세한건 다음 강의 에서
    def lookup(self, key, parent = None):
        if key < self.key:
            if self.left:
                return self.left.lookup(key, self)
            else:
                return None, None
        elif key > self.key:
            if self.right:
                return self.right.lookup(key, self)
            else:
                return None, None
        else:
            return self, parent


class BinSearchTree:

    def __init__(self):
        self.root = None


    def insert(self, key, data):
        if self.root:
            self.root.insert(key, data)
        else:
            self.root = Node(key, data)


    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []
    def min(self):
        if self.root:
            return self.root.min()
        else:
            return None
    def max(self):
        if self.root:
            return self.root.max()
        else:
            return None
    def lookup(self, key):
        if self.root:
            return self.root.lookup(key)
        else:
            return None, None

def solution(x):
    return 0