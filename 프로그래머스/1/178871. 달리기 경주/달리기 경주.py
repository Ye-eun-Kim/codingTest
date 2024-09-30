def solution(players, callings):
    answer = {}
    for i in range(len(players)):
        answer[players[i]] = i
    for calling in callings:
        idx = answer[calling]
        players[idx-1], players[idx] = players[idx], players[idx-1]
        answer[calling] -= 1
        answer[players[idx]] += 1
    return players