'''
Data Structure - stack
'''

class Stack :
    def __init__(self):
        self.arr = []
    def push (self, x):
        self.arr.append(x)
    def pop (self):
        try:
            return self.arr.pop()
        except IndexError :
            raise IndexError("Stack is empty")
    def top(self):
        try:
            return self.arr[-1]
        except IndexError:
            raise IndexError("Stack is empty")

    def __len__(self):
        return len(self.arr)

    def isEmpty(self):
        return len(self) == 0

import sys

words = list(sys.stdin.readline().strip())

def check(words):
    S = Stack()

    for i in words:
        if i in ['(', '[']:
            S.push(i)
        else :
            if S.isEmpty():
                return False
            elif i == ')' and S.top() == '(':
                S.pop()
            elif i == ']' and S.top() == '[':
                S.pop()

    if S.isEmpty():
        return True
    else:
        return False

def Solution(words):
    S = Stack()
    res = 0
    tmp = 1
    prev = ''

    if not check(words):
        return 0

    else:
        for i in words:
            if i == '(' :
                S.push(i)
                tmp *= 2
                prev = i
            elif i == '[':
                S.push(i)
                tmp *= 3
                prev = i

            elif i == ')' :
                if prev == '(':
                    res += tmp
                S.pop()
                tmp //= 2
                prev = i
            else:
                if prev == '[' :
                    res += tmp
                S.pop()
                tmp //= 3
                prev = i

    return res

print(Solution(words))









