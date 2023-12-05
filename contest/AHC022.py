import time

inputlist = []
for i in range(30):
    inputlist.append([int(j) for j in input().split()])
time_sta = time.perf_counter()
anslist = []
counter = 0

while(counter < 9900):
    for _ in range(30):
        for i in range(29):
            for j in range(i+1):
                if(inputlist[i][j] == 0):
                    if(inputlist[i+1][j] < inputlist[i+1][j+1]):
                        if(inputlist[i][j] > inputlist[i+1][j]):
                            inputlist[i][j], inputlist[i +
                                                       1][j] = inputlist[i+1][j], inputlist[i][j]
                            anslist.append([i, j, i+1, j])
                            counter += 1
                        if(inputlist[i][j] > inputlist[i+1][j+1]):
                            inputlist[i][j], inputlist[i+1][j +
                                                            1] = inputlist[i+1][j+1], inputlist[i][j]
                            anslist.append([i, j, i+1, j+1])
                            counter += 1
                    else:
                        if(inputlist[i][j] > inputlist[i+1][j+1]):
                            inputlist[i][j], inputlist[i+1][j +
                                                            1] = inputlist[i+1][j+1], inputlist[i][j]
                            anslist.append([i, j, i+1, j+1])
                            counter += 1
                        if(inputlist[i][j] > inputlist[i+1][j]):
                            inputlist[i][j], inputlist[i +
                                                       1][j] = inputlist[i+1][j], inputlist[i][j]
                            anslist.append([i, j, i+1, j])
                            counter += 1

    tempcount1 = 0
    tempcount2 = 0
    tempcount3 = 0
    while(tempcount1 < 10):
        for i in range(9):
            for j in range(i+1):
                if(inputlist[i+1][j] < inputlist[i+1][j+1]):
                    if(inputlist[i][j] > inputlist[i+1][j]):
                        inputlist[i][j], inputlist[i +
                                                   1][j] = inputlist[i+1][j], inputlist[i][j]
                        anslist.append([i, j, i+1, j])
                        counter += 1
                    if(inputlist[i][j] > inputlist[i+1][j+1]):
                        inputlist[i][j], inputlist[i+1][j +
                                                        1] = inputlist[i+1][j+1], inputlist[i][j]
                        anslist.append([i, j, i+1, j+1])
                        counter += 1
                else:
                    if(inputlist[i][j] > inputlist[i+1][j+1]):
                        inputlist[i][j], inputlist[i+1][j +
                                                        1] = inputlist[i+1][j+1], inputlist[i][j]
                        anslist.append([i, j, i+1, j+1])
                        counter += 1
                    if(inputlist[i][j] > inputlist[i+1][j]):
                        inputlist[i][j], inputlist[i +
                                                   1][j] = inputlist[i+1][j], inputlist[i][j]
                        anslist.append([i, j, i+1, j])
                        counter += 1
        tempcount1 += 1
    while(tempcount2 < 10):
        for i in range(10, 19):
            for j in range(i+1):
                if(inputlist[i+1][j] < inputlist[i+1][j+1]):
                    if(inputlist[i][j] > inputlist[i+1][j]):
                        inputlist[i][j], inputlist[i +
                                                   1][j] = inputlist[i+1][j], inputlist[i][j]
                        anslist.append([i, j, i+1, j])
                        counter += 1
                    if(inputlist[i][j] > inputlist[i+1][j+1]):
                        inputlist[i][j], inputlist[i+1][j +
                                                        1] = inputlist[i+1][j+1], inputlist[i][j]
                        anslist.append([i, j, i+1, j+1])
                        counter += 1
                else:
                    if(inputlist[i][j] > inputlist[i+1][j+1]):
                        inputlist[i][j], inputlist[i+1][j +
                                                        1] = inputlist[i+1][j+1], inputlist[i][j]
                        anslist.append([i, j, i+1, j+1])
                        counter += 1
                    if(inputlist[i][j] > inputlist[i+1][j]):
                        inputlist[i][j], inputlist[i +
                                                   1][j] = inputlist[i+1][j], inputlist[i][j]
                        anslist.append([i, j, i+1, j])
                        counter += 1
        tempcount2 += 1
    while(tempcount3 < 10):
        for i in range(20, 29):
            for j in range(i+1):
                if(inputlist[i+1][j] < inputlist[i+1][j+1]):
                    if(inputlist[i][j] > inputlist[i+1][j]):
                        inputlist[i][j], inputlist[i +
                                                   1][j] = inputlist[i+1][j], inputlist[i][j]
                        anslist.append([i, j, i+1, j])
                        counter += 1
                    if(inputlist[i][j] > inputlist[i+1][j+1]):
                        inputlist[i][j], inputlist[i+1][j +
                                                        1] = inputlist[i+1][j+1], inputlist[i][j]
                        anslist.append([i, j, i+1, j+1])
                        counter += 1
                else:
                    if(inputlist[i][j] > inputlist[i+1][j+1]):
                        inputlist[i][j], inputlist[i+1][j +
                                                        1] = inputlist[i+1][j+1], inputlist[i][j]
                        anslist.append([i, j, i+1, j+1])
                        counter += 1
                    if(inputlist[i][j] > inputlist[i+1][j]):
                        inputlist[i][j], inputlist[i +
                                                   1][j] = inputlist[i+1][j], inputlist[i][j]
                        anslist.append([i, j, i+1, j])
                        counter += 1
        tempcount3 += 1
    for i in range(29):
        for j in range(i+1):
            if(inputlist[i+1][j] < inputlist[i+1][j+1]):
                if(inputlist[i][j] > inputlist[i+1][j]):
                    inputlist[i][j], inputlist[i +
                                               1][j] = inputlist[i+1][j], inputlist[i][j]
                    anslist.append([i, j, i+1, j])
                    counter += 1
                if(inputlist[i][j] > inputlist[i+1][j+1]):
                    inputlist[i][j], inputlist[i+1][j +
                                                    1] = inputlist[i+1][j+1], inputlist[i][j]
                    anslist.append([i, j, i+1, j+1])
                    counter += 1
            else:
                if(inputlist[i][j] > inputlist[i+1][j+1]):
                    inputlist[i][j], inputlist[i+1][j +
                                                    1] = inputlist[i+1][j+1], inputlist[i][j]
                    anslist.append([i, j, i+1, j+1])
                    counter += 1
                if(inputlist[i][j] > inputlist[i+1][j]):
                    inputlist[i][j], inputlist[i +
                                               1][j] = inputlist[i+1][j], inputlist[i][j]
                    anslist.append([i, j, i+1, j])
                    counter += 1
    time_end = time.perf_counter()
    if(time_end - time_sta > 0.9):
        break

count = len(anslist)
print(count)
for i in range(count):
    print((str)(anslist[i][0])+" "+(str)(anslist[i][1]) +
          " "+(str)(anslist[i][2])+" "+(str)(anslist[i][3]))
