a = int(input())

score = list(map(int, input().strip().split()))

max_score = max(score)

score = [num/max_score * 100 for num in score]
print(sum(score)/len(score))

