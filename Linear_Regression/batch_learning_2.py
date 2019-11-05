base = [1, 1, 1, 1, 1, 1]  # x0
size = [30, 43, 25, 51, 40, 20]  # x1
floors = [3, 4, 2, 4, 3, 1]  # x2
rooms = [6, 8, 3, 9, 5, 2]  # x3
price = [2.5, 3.4, 1.8, 4.5, 3.2, 1.6]  # y
theta = [0] * 4


# x = [base, size, floors, rooms]  # x[1][2] = 25
# y = price


def cal_derrivative(x, y, theta,price):
    derrivative = 0
    for j in range(len(base)):
        for i in range(len(theta)):
            derrivative += (theta[i] * x[i][j] - y[j]) * x[price][i]
    return derrivative / len(base)


print(cal_derrivative([base, size, floors, rooms], price, theta))
