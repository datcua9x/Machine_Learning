import numpy as np

base = [1, 1, 1, 1, 1, 1]  # x0
size = [30, 43, 25, 51, 40, 20]  # x1
floors = [3, 4, 2, 4, 3, 1]  # x2
rooms = [6, 8, 3, 9, 5, 2]  # x3
price = [2.5, 3.4, 1.8, 4.5, 3.2, 1.6]  # y


# set the value of matrix X(m,n+1) as A and the out put matrix as B
A = np.array([base, size, floors, rooms])
B = np.array([price])
# Change the matrix A(1x6) into 6 x 1 and B(4x6) into 6x4
X = A.transpose()
Y = B.transpose()
# Z = inverse of (X transpose * X)
# G = X transpose * Y
Z = np.linalg.inv(X.transpose().dot(X))
G = X.transpose().dot(Y)
# calculate the theta
theta = Z.dot(G)
print(theta)


def cost_function(ans, x1, x2, x3, y):
    sigma = 0
    for i in range(len(x1)):
        sigma += (ans[0] + ans[1] * x1[i] + ans[2] * x2[i] + ans[3] * x3[i] - y[i]) ** 2
    return sigma / (2 * len(x1))


print("the value of cost function is", cost_function(theta, size, floors, rooms, price))
