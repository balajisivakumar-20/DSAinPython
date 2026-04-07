n = 5

for i in range(5):
    row = ""
    for j in range(n-i):
        row = row + str(j+1)
    print(row)



for i in range(5):
    row = ""
    for j in range(n-i):
        row = row + str(j+1)
    print(row)


for i in range(n):
    row = ""
    for j in range(i+1):
        row = row + str(i+1)
    print(row)