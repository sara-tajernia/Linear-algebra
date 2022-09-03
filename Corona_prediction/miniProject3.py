import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

def linear_Regression(open, last_ten):
    date = np.zeros(len(open))
    one = np.ones(len(open))
    for i in range(len(open)):
        date[i] = i + 1
    A = np.hstack((one.reshape(-1, 1), date.reshape(-1, 1)))
    transpose_A = A.transpose()
    Atranspose_A = transpose_A.dot(A)
    Atranspose_B = transpose_A.dot(open)
    betas = np.linalg.solve(Atranspose_A, Atranspose_B)
    beta0, beta1 = betas[0], betas[1]
    print('"Linear Regression"')
    for i in range(len(last_ten)):
        calculated_value = (len(open) + i) * beta1 + beta0
        print('calculated value:', calculated_value)
        print('actual value:', last_ten[i])
        print('error:', calculated_value - last_ten[i], '\n')


def none_linear_Regression(all_list, open, last_ten):
    date = np.zeros(len(open))
    date2 = np.zeros(len(open))
    one = np.ones(len(open))
    for i in range(len(open)):
        date[i] = i + 1
        date2[i] = pow(i+1, 2)
    A = np.hstack((one.reshape(-1, 1), date.reshape(-1, 1), date2.reshape(-1, 1)))
    transpose_A = A.transpose()
    Atranspose_A = transpose_A.dot(A)
    Atranspose_B = transpose_A.dot(open)
    betas = np.linalg.solve(Atranspose_A, Atranspose_B)
    beta0, beta1, beta2 = betas[0], betas[1], betas[2]
    calculated_all_value = np.zeros(len(all_list))
    for i in range(len(all_list)):
        calculated_all_value[i] = pow(i+1, 2) * beta2 + (i+1) * beta1 + beta0
    print('\n********************************\n'
             '********************************\n\n\n"None Linear Regression"')
    for i in range(len(last_ten)):
        calculated_value = pow(len(open)+i, 2)*beta2 + (len(open) + i) * beta1 + beta0
        print('calculated value:', calculated_value)
        print('actual value:', last_ten[i])
        print('error:', calculated_value - last_ten[i], '\n')

    plt.plot(calculated_all_value, color= 'black', label= 'calculated polynomial')
    plt.scatter(range(len(all_list)), all_list, color='cornflowerblue', label= 'actual value')
    plt.legend(loc= 'upper left')
    plt.show()


if __name__ == '__main__':
    df = pd.read_csv(input('Enter the path: '))
    all_list = df['Open'].to_list()
    open = df.head(-10)['Open'].to_list()
    last_ten = df.tail(10)['Open'].to_list()
    linear_Regression(open, last_ten)
    none_linear_Regression(all_list, open, last_ten)