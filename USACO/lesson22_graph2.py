n = 10
data = [[0, 1], [0, 3], [1, 2],
        [3, 4], [3, 5], [4, 5],
        [4, 8], [6, 7], [8, 9]]

matrix = [[0 for _ in range(n)] for _ in range(n)]

for i, j in data:
    matrix[i][j] = 1
    matrix[j][i] = 1

path = []
start = 0
stop = 5

def find_path():
    pass

find_path()

print(len(path))
print(path)

