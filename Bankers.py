#Coded by Darkz143
def bankers_algorithm(need, maxm, allot, avail):
    n = len(need)
    m = len(avail)
    f = [0]*n  
    ans = [0]*n
    ind = 0
    while ind < n:
        for i in range(n):
            if f[i] == 0:
                flag = 0
                for j in range(m):
                    if need[i][j] > avail[j]:
                        flag = 1
                        break
                if flag == 0:
                    ans[ind] = i
                    ind += 1
                    for y in range(m):
                        avail[y] -= allot[i][y] 
                    f[i] = 1
                else:
                    ind += 1 
    flag = 1
    for i in range(n):
        if f[i] == 0:
            flag = 0
            print("The given sequence is not safe")
            break
    if flag == 1:
        print("Following is the SAFE Sequence")
        for i in range(n - 1):
            print(" P", ans[i], " ->", sep="", end="")
        print(" P", ans[n - 1], sep="")

need = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]
maxm = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]
allot = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]
avail = [3, 3, 2]
bankers_algorithm(need, maxm, allot, avail)