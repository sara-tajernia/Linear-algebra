import matplotlib.pyplot as plt
import numpy as np
from matplotlib import image

def noise_canceling(pic):
    R = pic[:, :, 0]
    G = pic[:, :, 1]
    B = pic[:, :, 2]

    U_R, S_R, V_R = np.linalg.svd(R)
    U_G, S_G, V_G = np.linalg.svd(G)
    U_B, S_B, V_B = np.linalg.svd(B)

    R_R = np.full((U_R.shape[1], V_R.shape[0]), 0, dtype='float64')
    R_G = np.full((U_G.shape[1], V_G.shape[0]), 0, dtype='float64')
    R_B = np.full((U_B.shape[1], V_B.shape[0]), 0, dtype='float64')

    for i in range(20):
        for j in range(20):
            if i==j:
                R_R[i][j] = S_R[i]
                R_G[i][j] = S_G[i]
                R_B[i][j] = S_B[i]

    matrix_R = U_R.dot(R_R).dot(V_R)
    matrix_G = U_G.dot(R_G).dot(V_G)
    matrix_B = U_B.dot(R_B).dot(V_B)

    cleaned_matrix = np.full((matrix_R.shape[0], matrix_R.shape[1], 3), 255, dtype='uint8')
    cleaned_matrix[:, :, 0] = matrix_R
    cleaned_matrix[:, :, 1] = matrix_G
    cleaned_matrix[:, :, 2] = matrix_B
    plt.imshow(cleaned_matrix)
    plt.imsave('pa th.jpeg', cleaned_matrix)
    plt.show()

if __name__ == '__main__':
    input = image.imread(input('Enter the path: '))
    noise_canceling(input)