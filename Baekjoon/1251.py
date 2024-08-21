word = input()
results = []

def reverse(word):
    new_word = ''
    for i in range(len(word)-1, -1, -1):
        new_word+=word[i]

    return new_word

# 시작 index를 0으로 잡아서 오류가 났었음.
for i in range(1, len(word)-1):
    for j in range(i+1, len(word)):
        fir = word[0:i]
        # reverse를 쓰지 않고 문자열 slicing을 이용하여 뒤집을 수 있음!
        # n_fir = fir[::-1]
        fir = reverse(fir)
        sec = word[i:j]
        # n_sec = sec[::-1]
        sec = reverse(sec)
        thi = word[j:]
        # n_thi = thi[::-1]
        thi = reverse(thi)
        # new_word = n_fir+n_sec+n_thi
        new_word = fir+sec+thi
        results.append(new_word)

results.sort()
print(results[0])