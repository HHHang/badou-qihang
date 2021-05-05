import numpy as np


def mini_batch(x, epsilon, gamma, beta):
    # epsilon为一很小正数
    miu = np.mean(x)
    # print('miu=',miu)
    sigma2 = np.var(x)
    # print("sigma2 = ",sigma2)
    x_hat = (x - miu) / (sigma2 + epsilon)
    return gamma * x_hat + beta


x = np.array([1, 2, 3, 4, 5])
print(mini_batch(x, 0, 1, 0))