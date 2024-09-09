import math

frequencies = [5, 14, 23, 6, 2]
x = [7.5, 12.5, 17.5, 22.5, 27.5]

def calculate_mean():
    sum_of_mean = 0
    for i in range(len(frequencies)):
        sum_of_mean += frequencies[i] * x[i]
    mean = sum_of_mean / (sum(frequencies))
    return mean

mean = calculate_mean()
print('Sum of frequencies', sum(frequencies))
print('Mean', mean)

def standard_deviation_sum_of_square():
    sum_of_square = 0
    for i in range(len(frequencies)):
        sum_of_square += frequencies[i] * (x[i] * x[i])

    print('Sum of square', sum_of_square)
    return sum_of_square
    
def standard_deviation_mean_of_square():
    sum_of_square = standard_deviation_sum_of_square()
    mean_of_square = sum_of_square / sum(frequencies)
    print('Mean of square', mean_of_square)
    return mean_of_square

def standard_deviation_square_of_mean():
    square_of_mean = mean * mean 
    print('Square of mean', square_of_mean)
    return square_of_mean

def variance():
    mean_of_square = standard_deviation_mean_of_square()
    square_of_mean = standard_deviation_square_of_mean()
    return mean_of_square - square_of_mean

def standard_deviation():
    mean_of_square = standard_deviation_mean_of_square()
    square_of_mean = standard_deviation_square_of_mean()
    return math.sqrt((mean_of_square - square_of_mean))

# Calculate mean
# Standard deviation mean of square
#     -> standard deviation sum of square
# Standard deviation square of mean
# Square root of the difference between mean of square & square of mean

def main():
    print('Variance', variance())
    print('Standard deviation', standard_deviation())
