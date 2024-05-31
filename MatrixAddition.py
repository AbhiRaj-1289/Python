print("Input first matrix:")
matrix1 = []
for i in range(3):
    row = list(map(int, input().split()))
    matrix1.append(row)

print("Input second matrix:")
matrix2 = []
for i in range(3):
    row = list(map(int, input().split()))
    matrix2.append(row)

result = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for i in range(3):
    for j in range(3):
        result[i][j] = matrix1[i][j] + matrix2[i][j]


print("Resultant matrix after addition:")
for row in result:
    print(row)
