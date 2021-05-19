import sys 
from io import StringIO
sys.stdin = StringIO('''5 7
1 0 1 0 1 0 1
1 0 1 0 0 0 9
1 1 1 0 1 0 1
0 0 1 1 0 1 1
0 0 0 1 1 1 0''')
input = sys.stdin.readline

def maze(matrix, i, j, n, m):
    global explored
    explored += [(i, j)]
    
    if matrix[i][j] == 9:
        return True
    if j + 1 < m:
        if matrix[i][j + 1] != 0 and (i, j + 1) not in explored:
            if maze(matrix, i, j + 1, n, m):
                return True
    if j - 1 >= 0:
        if matrix[i][j - 1] != 0 and (i, j - 1) not in explored:
            if maze(matrix, i, j - 1, n, m):
                return True
    if i + 1 < n:
        if matrix[i + 1][j] != 0 and (i + 1, j) not in explored:
            if maze(matrix, i + 1, j, n, m):
                return True
    if i - 1>= 0:
        if matrix[i - 1][j] != 0 and (i - 1, j) not in explored:
            if maze(matrix, i - 1, j, n, m):
                return True
    return False

explored = []
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

f = maze(matrix, 0, 0, n, m)
print(f, end='\n\n')

if f:
    path = [[0 for _ in range(m)] for _ in range(n)]
    for node in explored:
        path[node[0]][node[1]] = '+'
    path[node[0]][node[1]] = '#'

    for i in range(n):
        for j in range(m):
            sym = path[i][j]
            if sym != 0:
                print(sym,end=" ")
            else:
                print(" ",end=" ")
        print()
