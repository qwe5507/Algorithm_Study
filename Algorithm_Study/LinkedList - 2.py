class Node:

    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None

    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None

        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr

    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos == 1:
            newNode.next = self.head
            self.head = newNode

        else:
            if pos == self.nodeCount + 1:
                prev = self.tail
            else:
                prev = self.getAt(pos - 1)
            newNode.next = prev.next
            prev.next = newNode

        if pos == self.nodeCount + 1:
            self.tail = newNode

        self.nodeCount += 1
        return True

    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError
        ## 원소가 하나일떄
        # if self.nodeCount == 1:
        #     temp = self.head
        #     self.head = None
        #     self.tail = None

        ## node가 맨앞일때
        if pos == 1:
            temp = self.head
            self.head = self.head.next
            ## 원소가 하나일떄
            if self.nodeCount == 1:
                self.head = None
                self.tail = None

        ## node가 맨 끝일때
        # elif pos == self.nodeCount:
        #     temp = self.tail
        #     pre = self.getAt(pos-1)
        #     pre.next = None
        #     self.tail = pre

        ##나머지 경우
        else:
            ## node가 맨 끝일때
            prev = self.getAt(pos - 1)
            temp = self.getAt(pos)
            prev.next = temp.next
            if pos == self.nodeCount:
                temp = self.tail
                prev.next = None
                self.tail = prev
        self.nodeCount -= 1
        return temp.data

    def traverse(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result


def solution(x):
    return 0