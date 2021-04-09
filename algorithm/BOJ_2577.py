data = [int(input()) for i in range(3)]
value = 1
result = []
count = [0 for i in range(0, 10)]

for i in data:
    value *= i

value = str(value)

for j in range(0, 10):
    result.append(str(j))
for j in value:
    for k in result:
        if j == k:
            count[result.index(j)] += 1

for m in count:
    print(m)



            

    
                  
