string = '0123456789'

#matrix = [[str(j) for j in range(10)] for i in range(10)]
matrix = [[j for j in string] for i in string]

for row in matrix:
    print(row)
