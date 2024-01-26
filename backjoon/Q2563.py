T = int(input())
lst = [list(map(int, input().split())) for _ in range(T)]


paper = []
for i in range(100):
    a = []
    for j in range(100):
        a.append(0)
    paper.append(a)
        

for k in lst:
    dis_left = int(k[0])
    dis_bottom = int(k[1])
    for l in range(10):
        paper[dis_left + l][dis_bottom] = 1
        for m in range(10):
            paper[dis_left + l][dis_bottom + m] = 1

count = 0
for bottom in range(100):
    for height in range(100):
        if paper[bottom][height] == 1:
            count += 1
result = count

print(result)

