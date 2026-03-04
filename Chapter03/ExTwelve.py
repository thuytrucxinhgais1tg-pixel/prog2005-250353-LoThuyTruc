m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

A = []
B = []
C = []

print("Enter matrix A:")
for i in range(m):
    row = list(map(int, input().split()))
    A.append(row)

print("Enter matrix B:")
for i in range(m):
    row = list(map(int, input().split()))
    B.append(row)

for i in range(m):
    row = []
    for j in range(n):
        row.append(A[i][j] + B[i][j])
    C.append(row)

print("Result matrix:")
for row in C:
    print(row)
