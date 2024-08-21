# 모르겠음ㅠㅠㅠㅠㅠㅠㅠ

test_cases = int(input())

for _ in range(test_cases):
    n = int(input())
    coins = list(map(int, input().split()))
    money = int(input())

    result = [0] * (money + 1)
    # 조건 처리를 위해...
    result[0] = 1

    for i in range(coins[0], money + 1):
        temp = 0
        cnt = 0
        for coin in coins:
            if i-coin >= 0:
                if result[i-coin] != 0:
                    temp = max(temp, result[i - coin])
                    cnt += 1
        result[i] = temp + cnt - 1

    print(result[money])
