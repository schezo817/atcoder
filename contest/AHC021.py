import math
from heapq import heappush, heappop

nmk = [int(i) for i in input().split()]
nList = [[0]*2 for i in range(nmk[0])]
mList = [[0]*3 for i in range(nmk[1])]
kList = [[0]*2 for i in range(nmk[2])]
for i in range(nmk[0]):
    nList[i] = [int(i) for i in input().split()]
for i in range(nmk[1]):
    mList[i] = [int(i) for i in input().split()]
for i in range(nmk[2]):
    kList[i] = [int(i) for i in input().split()]

plist = [0]*nmk[0]
blist = [0]*nmk[1]

# ある人に対して一番近い放送局を見つける
# その放送局から電波を出す

#問題点 :使ってない放送局へのバンドを消してない

for i in range(nmk[2]):
    # kList[i][0] : x座標　kList[i][１] : y座標
    lengths = 5001
    bestbroad = 0
    flag = True
    for j in range(nmk[0]):
        templen = math.sqrt((nList[j][0] - kList[i][0])
                            ** 2 + (nList[j][1] - kList[i][1]) ** 2)
        # すでに帯域内か
        if(plist[j] >= templen):
            flag = False
            break
        if(lengths > templen):
            lengths = templen
            bestbroad = j
    if(flag and plist[bestbroad] < lengths):
        if(lengths.is_integer()):
            lengths = (int)(lengths)
        else:
            lengths = (int)(lengths+1)
        plist[bestbroad] = lengths

# プリム法で最小全域木を構築
graph = [[] for _ in range(nmk[0]+1)]
for i in range(nmk[1]):
    graph[mList[i][0]].append((mList[i][1], mList[i][2], i))
    graph[mList[i][1]].append((mList[i][0], mList[i][2], i))
marked = [False for _ in range(nmk[0]+1)]
marked_cnt = 0
marked[0] = True
marked[1] = True
marked_cnt += 1
q = []
connectNode = []
for j, c, s in graph[1]:
    heappush(q, (c, j, s))
while marked_cnt < nmk[0]:
    c, i, s = heappop(q)
    if marked[i]:
        continue
    marked[i] = True
    marked_cnt += 1
    if(mList[s][0] == i):
        connectNode.append([mList[s][0], mList[s][1], c, s])
    if(mList[s][1] == i):
        connectNode.append([mList[s][1], mList[s][0], c, s])
    for j, c, s in graph[i]:
        if marked[j]:
            continue
        heappush(q, (c, j, s))

for i in range(nmk[0]):
    if(plist[i] != 0):
        positon = i + 1
        count = 0
        while(i != 1 and count < 100):
            for j in range(len(connectNode)):
                if(positon == connectNode[j][0]):
                    positon = connectNode[j][1]
                    blist[connectNode[j][3]] = 1
                    break
            count += 1

for i in range(nmk[0]):
    print((str)(plist[i]), end=" ")
print()
for i in range(nmk[1]):
    print((str)(blist[i]), end=" ")
