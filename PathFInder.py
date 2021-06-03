import sys 
from io import StringIO
sys.stdin = StringIO('''5 8
1 0 1 1 1 1 1 1
1 0 0 0 0 1 0 1
1 1 1 1 1 1 1 9
0 0 1 0 0 0 0 1
0 0 1 1 1 1 1 1''')
input = sys.stdin.readline

def test(i, j, cond):
    global explored
    global matrix

    if cond:
        if matrix[i][j] != 0 and (i, j) not in explored: # explored.count((i, j)) < 4:
            if maze(matrix, i, j, n, m):
                return True
            else:
                explored.remove((i, j))  
        return False
        
    else:
        return False

def maze(matrix, i, j, n, m):
    global explored
    
    if matrix[i][j] == 9:
        global goal
        goal = [i, j]
        return True
    explored += [(i, j)]
    # print("i - j", i, j)
    
    
    t1 = test(i, j + 1, j + 1 < m)     
    t2 = test(i, j - 1, j - 1 >= 0)
    t3 = test(i + 1, j, i + 1 < n)
    
    t4 = test(i - 1, j, i - 1 >= 0)
    

#     print(t1 or t2 or t3 or t4, i, j)
    if t1 or t2 or t3 or t4:
        return True
    return False

explored = []
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
goal = []
f = maze(matrix, 0, 0, n, m)
print(f, end='\n\n')

if f:
    path = [[0 for _ in range(m)] for _ in range(n)]
    for node in explored:
        path[node[0]][node[1]] = '+'
    path[goal[0]][goal[1]] = '#'

    for i in range(n):
        for j in range(m):
            sym = path[i][j]
            if sym != 0:
                print(sym,end=" ")
            else:
                print(" ",end=" ")
        print()
