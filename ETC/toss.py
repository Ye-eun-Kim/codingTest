import heapq as h

string = input()
l = len(string)

q = []

for i in range(l-3):
    sub = string[i:i+3]
    if sub[0] == sub[1] and sub[1] == sub[2]:
        h.heappush(q, -int(sub))

if not q:
    answer = -1
else:
    answer = -h.heappop(q)
    if answer == 0:
        answer = '000'

print(answer)
