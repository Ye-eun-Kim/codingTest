n = list(map(int, input()))

if 0 in n and sum(n) % 3 == 0:
    n.sort(reverse=True)
    print(''.join(str(num) for num in n))
else:
    print(-1)


# n.sort(reverse=True)
#
# m = int("".join(n))
#
# if m % 30 == 0:
#     print(m)
#     exit()
#
# # 30의 배수라면 무조건 마지막 숫자가 0이어야 함
# if n[-1] != '0':
#     print(-1)
#     exit()
#
# tot = sum(list(map(int, n)))
# if tot % 3 == 0:
#     print(m)
# else:
#     print(-1)

