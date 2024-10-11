from itertools import permutations
N, M = map(int, input().split())
# for p in list(pm(range(1, N+1), M)):
#     for i in p:
#         print(i, end=" ")
#     print()

for p in list(permutations(list(map(str, range(1, N+1))), M)):
    print(' '.join(p))

# join 함수는 구분자를 앞에 넣고, 인자로는 리스트를 받는다!