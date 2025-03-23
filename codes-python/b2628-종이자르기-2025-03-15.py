#import sys
#input = sys.stdin.readline

width, height = map(int,input().split())
wl = [0,width]
hl = [0,height]
max_width=0 
max_height=0 

# 설정 시작
for _ in range(int(input())):
    wh,gridnum = map(int,input().split())
    if wh==0: # 가로 라인 설정
        hl.append(gridnum)
    else: # 세로 라인 설정
        wl.append(gridnum)
# 설정 끝 계산 시작
wl.sort()
hl.sort()
# 가로 최장 라인 구함
max_width = max([ wl[i+1]-wl[i] for i in range(len(wl)-1) ])
# 세로 최장 라인 구함
max_height = max([ hl[i+1]-hl[i] for i in range(len(hl)-1) ])
print(max_width*max_height)
