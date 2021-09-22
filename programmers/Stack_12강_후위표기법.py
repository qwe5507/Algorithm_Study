# (12) 스택 - 중위 표기법 -> 후위표기법 변환
# 프로그래머스 12강
class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]


prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}


def solution(S):
    opStack = ArrayStack()
    answer = ''
    for s in S:
        if s in prec:
            if opStack.isEmpty():
                opStack.push(s)
            elif s == '(' or prec[opStack.peek()] < prec[s]:
                opStack.push(s)
            else:
                while not opStack.isEmpty() and prec[s] <= prec[opStack.peek()]:
                    answer += opStack.pop()
                opStack.push(s)

        else:
            if s == ')':
                while opStack.peek() != '(':
                    answer += opStack.pop()
                opStack.pop()
            else:
                answer += s
    else:
        while not opStack.isEmpty():
            answer += opStack.pop()

    return answer