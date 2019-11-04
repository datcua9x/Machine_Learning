base = [1, 1, 1, 1, 1, 1]  # x0
size = [30, 43, 25, 51, 40, 20]  # x1
floors = [3, 4, 2, 4, 3, 1]  # x2
rooms = [6, 8, 3, 9, 5, 2]  # x3
price = [2.5, 3.4, 1.8, 4.5, 3.2, 1.6]  # y
theta = [0, 0, 0, 0]


def cal_theta(theta0, theta1, theta2, theta3, x, y, learning_rate=0.001):
    sigma = 0
    for i in range(len(y)):
        for j in range(theta):
            sigma += (1 / len(y)) * ((theta0 + theta[i] * x[j][i] + theta2 * x[j][i] + theta3 * x[j][i] - y[i]) * x0[i])
            new_theta0 = theta0 - learning_rate * sigma
    return new_theta0
