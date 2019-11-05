import random

base = [1, 1, 1, 1, 1, 1]  # x0
size = [30, 43, 25, 51, 40, 20]  # x1
floors = [3, 4, 2, 4, 3, 1]  # x2
rooms = [6, 8, 3, 9, 5, 2]  # x3
price = [2.5, 3.4, 1.8, 4.5, 3.2, 1.6]  # y


# functuon to generate a random number
def random_value(base):
    j = random.randrange(1, len(base), 1)
    return j


# store the random value in the temp value
temp = random_value(base)


# calculate theta 0
def cal_theta0(theta0, theta1, theta2, theta3, x0, x1, x2, x3, y, learning_rate=0.001):
    sigma = 0
    # choose a random value to calculate the theta
    # temp stand for the address of value
    sigma += ((theta0 + theta1 * x1[temp] + theta2 * x2[temp] + theta3 * x3[temp] - y[temp]) * x0[temp])
    new_theta0 = theta0 - learning_rate * sigma
    return new_theta0


# calculate theta 1
def cal_theta1(theta0, theta1, theta2, theta3, x0, x1, x2, x3, y, learning_rate=0.001):
    sigma = 0
    # choose a random value to calculate the theta
    # temp stand for the address of value
    sigma += ((theta0 + theta1 * x1[temp] + theta2 * x2[temp] + theta3 * x3[temp] - y[temp]) * x1[temp])
    new_theta1 = theta1 - learning_rate * sigma
    return new_theta1


# calculate theta 2
def cal_theta2(theta0, theta1, theta2, theta3, x0, x1, x2, x3, y, learning_rate=0.001):
    sigma = 0
    # choose a random value to calculate the theta
    # temp stand for the address of value
    sigma += ((theta0 + theta1 * x1[temp] + theta2 * x2[temp] + theta3 * x3[temp] - y[temp]) * x2[temp])
    new_theta2 = theta2 - learning_rate * sigma
    return new_theta2


# calculate theta 3
def cal_theta3(theta0, theta1, theta2, theta3, x0, x1, x2, x3, y, learning_rate=0.001):
    sigma = 0
    # choose a random value to calculate the theta
    # temp stand for the address of value
    sigma += ((theta0 + theta1 * x1[temp] + theta2 * x2[temp] + theta3 * x3[temp] - y[temp]) * x3[temp])
    new_theta3 = theta3 - learning_rate * sigma
    return new_theta3


def cost_function(theta0, theta1, theta2, theta3, x0, x1, x2, x3, y):
    sigma = 0
    # choose a random value to calculate cost function
    # temp stand for the address of value
    sigma += (theta0 + theta1 * x1[temp] + theta2 * x2[temp] + theta3 * x3[temp] - y[temp]) ** 2
    return sigma / 2


# set the first value for theta
theta1 = 0
theta2 = 0
theta3 = 0
theta0 = 0
# store the value of theta in temporary variable to save the value of that iteration
temp0 = theta0
temp1 = theta1
temp2 = theta2
temp3 = theta3
# set the value of min equal the cost value of first theta
min = cost_function(theta0, theta1, theta2, theta3, base, size, floors, rooms, price)
best_theta0 = theta0
best_theta1 = theta1
best_theta2 = theta2
best_theta3 = theta3
# enter n for the number of iterations that you wanted
n = input("enter number of iterations =")
for i in range(int(n)):
    # calculate the theta after n iteration(input n from the keyboard)
    temp = random_value(base)  # generate a random value and stored in base value
    theta0 = cal_theta0(theta0, theta1, theta2, theta3, base, size, floors, rooms, price)
    theta1 = cal_theta1(temp0, theta1, theta2, theta3, base, size, floors, rooms, price)
    theta2 = cal_theta2(temp0, temp1, theta2, theta3, base, size, floors, rooms, price)
    theta3 = cal_theta3(temp0, temp1, temp2, theta3, base, size, floors, rooms, price)
    temp0 = theta0
    temp1 = theta1
    temp2 = theta2
    temp3 = theta3
    # find the min value of cost function and save the it in to best_theta
    if abs(cost_function(theta0, theta1, theta2, theta3, base, size, floors, rooms, price)) < abs(min):
        min = cost_function(theta0, theta1, theta2, theta3, base, size, floors, rooms, price)
        best_theta0 = theta0
        best_theta1 = theta1
        best_theta2 = theta2
        best_theta3 = theta3

print("theta 0 to get the min cost value is:", best_theta0)
print("theta 1 to get the min cost value is:", best_theta1)
print("theta 2 to get the min cost value is:", best_theta2)
print("theta 3 to get the min cost value is:", best_theta3)
print("best cost function is ", min)
