import random

base = [1, 1, 1, 1, 1, 1]  # x0
size = [30, 43, 25, 51, 40, 20]  # x1
floors = [3, 4, 2, 4, 3, 1]  # x2
rooms = [6, 8, 3, 9, 5, 2]  # x3
price = [2.5, 3.4, 1.8, 4.5, 3.2, 1.6]  # y


# functuon to generate a random list of element
def random_value(base):
    random_numbers = random.sample(range(1, len(base)), 3)  # 3 is number of value that you wanted to use
    return random_numbers

#store the random values in the a list
list = random_value(base)

# calculate theta 0
def cal_theta0(theta0, theta1, theta2, theta3, x0, x1, x2, x3, y, learning_rate=0.001):
    sigma = 0
    # choose random values to calculate the theta(stored in list)
    # i stand for the address of value
    for i in list:
        sigma += (1 / len(list)) * ((theta0 + theta1 * x1[i] + theta2 * x2[i] + theta3 * x3[i] - y[i]) * x0[i])
        new_theta0 = theta0 - learning_rate * sigma
    return new_theta0

# calculate theta 1
def cal_theta1(theta0, theta1, theta2, theta3, x0, x1, x2, x3, y, learning_rate=0.001):
    sigma = 0
    # choose random values to calculate the theta(stored in list)
    # i stand for the address of value
    for i in list:
        sigma += (1 / len(list)) * ((theta0 + theta1 * x1[i] + theta2 * x2[i] + theta3 * x3[i] - y[i]) * x1[i])
        new_theta1 = theta1 - learning_rate * sigma
    return new_theta1

# calculate theta 2
def cal_theta2(theta0, theta1, theta2, theta3, x0, x1, x2, x3, y, learning_rate=0.001):
    sigma = 0
    # choose random values to calculate the theta(stored in list)
    # i stand for the address of value
    for i in list:
        sigma += (1 / len(list)) * ((theta0 + theta1 * x1[i] + theta2 * x2[i] + theta3 * x3[i] - y[i]) * x2[i])
        new_theta2 = theta2 - learning_rate * sigma
    return new_theta2

# calculate theta 3
def cal_theta3(theta0, theta1, theta2, theta3, x0, x1, x2, x3, y, learning_rate=0.001):
    sigma = 0
    # choose random values to calculate the theta(stored in list)
    # i stand for the address of value
    for i in list:
        sigma += (1 / len(list)) * ((theta0 + theta1 * x1[i] + theta2 * x2[i] + theta3 * x3[i] - y[i]) * x3[i])
        new_theta3 = theta3 - learning_rate * sigma
    return new_theta3

#calculate cost function
def cost_function(theta0, theta1, theta2, theta3, x0, x1, x2, x3, y):
    sigma = 0
    # choose a random value to calculate the theta(stored in list)
    # i stand for the address of value
    for i in list:
        sigma += (theta0 + theta1 * x1[i] + theta2 * x2[i] + theta3 * x3[i] - y[i]) ** 2
    return sigma / (2 * len(list))

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

    list = random_value(base)
    print("the list is", list)
    temp = random_value(base)
    theta0 = cal_theta0(theta0, theta1, theta2, theta3, base, size, floors, rooms, price)
    theta1 = cal_theta1(temp0, theta1, theta2, theta3, base, size, floors, rooms, price)
    theta2 = cal_theta2(temp0, temp1, theta2, theta3, base, size, floors, rooms, price)
    theta3 = cal_theta3(temp0, temp1, temp2, theta3, base, size, floors, rooms, price)
    temp0 = theta0
    temp1 = theta1
    temp2 = theta2
    temp3 = theta3
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
