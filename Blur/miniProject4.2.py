import matplotlib.pyplot as plt
import numpy as np
from matplotlib import image
import math

def get_main_function():
    x = np.linspace(0, math.pi * 3 / 2, 30)
    y = np.linspace(0, math.pi * 3 / 2, 30)
    X, Y = np.meshgrid(x, y)
    return np.sin(X * Y)

def make_function_noisy(z):
    max_noise = 0.1
    t = 2 * np.random.rand(30 * 30) * max_noise - max_noise
    t = t.reshape(30, 30)
    return np.add(z, t)

def get_function():
    return make_function_noisy(get_main_function())

def show_my_matrix(Z):
    x = np.linspace(0, math.pi * 3 / 2, 30)
    y = np.linspace(0, math.pi * 3 / 2, 30)
    X, Y = np.meshgrid(x, y)
    ax = plt.axes(projection='3d')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='black')
    ax.set_title('surface')
    ax.view_init(70, 45)
    plt.show()

def show_main():
    Z = get_main_function()
    show_my_matrix(Z)

def show_noisy():
    Z = get_function()
    show_my_matrix(Z)

def noise_canceling():
    R = get_function()
    U_R, S_R, V_R = np.linalg.svd(R)
    R_R = np.full((U_R.shape[1], V_R.shape[0]), 0, dtype='float64')

    for i in range(8):
        for j in range(8):
            if i == j:
                R_R[i][j] = S_R[i]

    matrix_R = U_R.dot(R_R).dot(V_R)
    show_my_matrix(matrix_R)

if __name__ == '__main__':
    noise_canceling()