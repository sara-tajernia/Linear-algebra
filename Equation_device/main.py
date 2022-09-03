import numpy as np
import math
np.set_printoptions(2, suppress=True)
def make_num_valid(matrix, row, column):  #function for round numbers if they are to small
    num = matrix[row][column]
    if math.ceil(num) - num <0.00000000001:
        matrix[row, column] = math.ceil(num)
    elif num - math.floor(num) <0.00000000001:
        matrix[row, column] = math.floor(num)

print ('Coefficient matrix:\nEnter number of rows and columns respectively:')
rows, columns = list(map(int, input('> ').split()))  #getting rows and columns throw input
matrix = np.zeros((rows, columns))

for i in range(rows):  #get each rows of matrix
    print("Enter row",(i+1), ":")
    matrix[i] = input('> ').split()

print('Enter constant values:')
matrix_value = np.array([int(i) for i in input('> ').split()])
matrix = np.hstack((matrix, matrix_value.reshape(-1, 1)))  #put the values in the end of matrix by numpy library
columns +=1
print('Given matrix:\n',matrix)

np.set_printoptions(2, suppress=True)
pivot = 0
pivot_columns = []
for j in range (columns):
    for i in range (pivot, rows):
        if matrix[i][j] != 0:  #find the pivot columns
            matrix[[i, pivot]] = matrix[[pivot, i]]  #change the pivot row
            for k in range(i+1, rows):
                if matrix[k][j] != 0:
                    multi = -matrix[k][j] / matrix[pivot][j]
                    for p in range(0, columns):
                        matrix[k][p] = (matrix[pivot][p] * multi) + matrix[k][p]  #change the lower element of pivot to 0

            for k in range(0, pivot):
                if matrix[k][j] != 0:
                    multi = -matrix[k][j] / matrix[pivot][j]
                    for p in range(0, columns):
                        matrix[k][p] = (matrix[pivot][p] * multi) + matrix[k][p] #change the upper element of pivot to 0

            save = matrix[pivot][j]
            if matrix[i][j] != 1:  #change the pivot to 1 by dividing or multipling
                save = matrix[pivot][j]
                for q in range(columns):
                    matrix[pivot][q] /= save

            pivot +=1
            pivot_columns.append(j)
            break

for j in range(columns-1): #print the answer
    check = 0
    for i in range(len(pivot_columns)):
        if pivot_columns[i] == j:  #find the pivot columns
            check += 1
            print('\nx{}'.format((j+1)), ':', end=' ')
            for l in range(rows):
                make_num_valid(matrix,l,j)
                if matrix[l][j] !=0:
                    make_num_valid(matrix,l,columns-1)
                    if matrix[l][columns - 1] != 0:
                        print('{:.2f}'.format(matrix[l][columns - 1]), end='')  #add the -1 element of pivot row to answer
                    for k in range(j + 1, columns - 1):
                        make_num_valid(matrix, l, k)
                        if matrix[l][k] != 0:
                            print('+({:.2f}.x{})'.format(-matrix[l][k], k + 1), end='')  #add multiply of each element in the pivot row
            break                                                                           #to x[row+1]
    if check == 0:  #rows with no pivot are free
        print('\nx{}'.format(j+1), ': is free')
# print('\n', matrix)