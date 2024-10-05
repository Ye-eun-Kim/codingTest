N = int(input())
result = 0

# 이 문제 주의해야 할 게, 나도 모르게 자꾸 n=4에 맞춰서 코딩함...
def dfs(row):
    global result
    for col in range(N): # 리스트에 어떤 숫자를 넣을지 고민하는 과정
        rows[row:] = [-1] * (N-row)
        if col in rows: # 이미 쓴 숫자면 불가능
            continue
        if row > 0:
            flag = False
            for i in range(0, row):
                if abs(rows[i]-col) == abs(row-i):  # 처음에 이걸 잘못 세워서 틀림
                    flag = True
                    if col == N - 1:  # 모든 숫자를 넣어봐도 각이 안 서면 이 경우 자체 패스
                        return
                    break
            if flag:
                continue
        rows[row] = col # 문제 없는 경우에는 해당 숫자 넣기
        if row == N-1: # 마지막 row였다면 result를 증가시키기 위해 return하여 이전 함수 호출로 계속 돌아가기
            result += 1
            return
        dfs(row+1)


rows = [-1] * N
dfs(0)

print(result)

