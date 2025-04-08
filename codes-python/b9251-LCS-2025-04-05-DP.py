import sys
# import pprint

def dp_count():
    for i in range(1,len(s2)+1):
        for j in range(1,len(s1)+1):
            if s2[i-1] == s1[j-1]: # 인덱스 0인 행/열 때문에 문자 위치가 한 칸씩 밀렸으므로.
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[-1][-1]

def restore_seq():
    lcs = str()
    i, j = len(s2), len(s1) # i,j는 끝에서부터 시작, 또한, 위 dp_count()와 i→s2, j→s1 매칭 필요
    while i > 0 and j > 0:
        if s2[i-1] == s1[j-1]: # 현재 보는 글자가 서로 같다?
            lcs = s2[i-1]+lcs 
            i -= 1              # ↖로 한 칸 이동
            j -= 1
        else:                  # 다르다?
            if dp[i-1][j] > dp[i][j-1]: # 한 칸 ← 또는 ↑를 비교하여,
                i -= 1                   # 해당 셀의 숫자가 더 큰 놈으로 이동.
            else:
                j -= 1

    return lcs


# 입력 & 세팅
s1 = sys.stdin.readline().strip()
s2 = sys.stdin.readline().strip()
dp = [[0]*(len(s1)+1) for _ in range(len(s2)+1)] # row, col이 거꾸로 되어 있는 것 확인!
# pprint.pprint(dp) # row는 0ACAYKP, col은 0CAPCAK

# 처리 & 출력
print(dp_count())
print(restore_seq())


""" https://www.acmicpc.net/source/92244580

str1 = [0] + list(input())
str2 = [0] + list(input())
len_1 = len(str1)
len_2 = len(str2)

array = [['' for _ in range(len_1)] for _ in range(len_2)]

for i in range(1, len_2) :
    for j in range(1, len_1) :
        if str1[j] == str2[i] :
            array[i][j] = array[i-1][j-1] + str1[j]
        else :
            if len(array[i][j-1]) > len(array[i-1][j]) :
                array[i][j] = array[i][j-1]
            else : 
                array[i][j] = array[i-1][j]
answer = len(array[-1][-1])
print(answer)

if answer != 0 :
    print(array[-1][-1])

"""