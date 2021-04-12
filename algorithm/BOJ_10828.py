import sys

def push(data):
    stack_list.append(data)
 
def pop():
    if len(stack_list) == 0:
        return print(-1)
    else:
        data = stack_list[-1]
        del stack_list[-1]
        return print(data)

def size():
    stack_size = len(stack_list)
    return print(stack_size)

def empty():
    if len(stack_list) == 0:
        return print(1)
    else:
        return print(0) 

def top():
    if len(stack_list) == 0:
        return print(-1)
    else:
        return print(stack_list[-1])

m = int(sys.stdin.readline().rstrip())
stack_list = []

for _ in range(m):
    n = sys.stdin.readline().rstrip().split()
    if n[0] == "push":
        push(n[1])
    elif n[0] == "top":
        top()
    elif n[0] == "empty":
        empty()
    elif n[0] == "pop":
        pop()
    else: 
        size()


