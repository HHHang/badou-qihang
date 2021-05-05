import numpy as np
def calc_dot(x,y):
    return np.dot(x,y)
def calc_abs(x):
    a = np.square(x)
    b = np.sum(a)
    return np.sqrt(b)

A = np.array([1,2,3,4])
B = np.array([1,2,3,4])
COS = (calc_dot(A,B))/((calc_abs(A))*(calc_abs(B)))
print(COS)