N = int(input())

for i in range(N):
    a = input()
    score = 0
    total = 0
    for j in a:
        if j == 'O':
            score += 1
        else:
            score = 0
        total += score
    print(total)
    
