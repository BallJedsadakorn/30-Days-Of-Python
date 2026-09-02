# How to import numpy
import numpy as np

# # Creating python List
# python_list = [1,2,3,4,5]
# # Checking data types
# print('Type:', type (python_list)) # <class 'list'>
# #
# print(python_list) # [1, 2, 3, 4, 5]

# # Creating Numpy(Numerical Python) array from python list
# numpy_array_from_list = np.array(python_list)
# print(type (numpy_array_from_list))   # <class 'numpy.ndarray'>
# print(numpy_array_from_list) # array([1, 2, 3, 4, 5])

# # Python list
# python_list = [1,2,3,4,5]

# numpy_array_from_list2 = np.array(python_list, dtype=float)
# print(numpy_array_from_list2) # array([1., 2., 3., 4., 5.])

# numpy_bool_array = np.array([0, 1, -1, 0, 0], dtype=bool)
# print(numpy_bool_array) # array([False,  True,  True, False, False])

# two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]
# numpy_two_dimensional_list = np.array(two_dimensional_list)
# print(type (numpy_two_dimensional_list))
# print(numpy_two_dimensional_list)

# # We can always convert an array back to a python list using tolist().
# np_to_list = numpy_array_from_list.tolist()
# print(type (np_to_list))
# print('one dimensional array:', np_to_list)
# print('two dimensional array: ', numpy_two_dimensional_list.tolist())

# nums = np.array([1, 2, 3, 4, 5])
# print(nums)
# print('shape of nums: ', nums.shape)
# numpy_two_dimensional_list = np.array([[0,1,2],[3,4,5],[6,7,8]])
# print(numpy_two_dimensional_list)
# print('shape of numpy_two_dimensional_list: ', numpy_two_dimensional_list.shape)
# three_by_four_array = np.array([[0, 1, 2, 3],
#     [4,5,6,7],
#     [8,9,10,11]])
# print(three_by_four_array)
# print('shape of three_by_four_array: ', three_by_four_array.shape)

# int_lists = [-3, -2, -1, 0, 1, 2,3]
# int_array = np.array(int_lists)
# float_array = np.array(int_lists, dtype=float)

# print(int_array)
# print(int_array.dtype)
# print(float_array)
# print(float_array.dtype)

# numpy_array_from_list = np.array([1, 2, 3, 4, 5])
# two_dimensional_list = np.array([[0, 1, 2],
#                               [3, 4, 5],
#                               [6, 7, 8]])

# print('The size:', numpy_array_from_list.size) # 5
# print('The size:', two_dimensional_list.size)  # 9

# Mathematical Operation
# Addition
# numpy_array_from_list = np.array([1, 2, 3, 4, 5])
# print('original array: ', numpy_array_from_list)
# ten_plus_original = numpy_array_from_list  + 10
# print(ten_plus_original)
# Subtraction
# numpy_array_from_list = np.array([1, 2, 3, 4, 5])
# print('original array: ', numpy_array_from_list)
# ten_minus_original = numpy_array_from_list  - 10
# print(ten_minus_original)

# Modulus; Finding the remainder
# numpy_array_from_list = np.array([1, 2, 3, 4, 5])
# print('original array: ', numpy_array_from_list)
# ten_times_original = numpy_array_from_list % 3
# print(ten_times_original)

# np.random.normal(mu, sigma, size)
# normal_array = np.random.normal(79, 15, 80)
# normal_array

import matplotlib.pyplot as plt
import seaborn as sns
# sns.set()
# plt.hist(normal_array, color="grey", bins=50)

# from scipy import stats
# np_normal_dis = np.random.normal(5, 0.5, 1000) # mean, standard deviation, number of samples
# np_normal_dis
# ## min, max, mean, median, sd
# print('min: ', np.min(np_normal_dis))
# print('max: ', np.max(np_normal_dis))
# print('mean: ', np.mean(np_normal_dis))
# print('median: ', np.median(np_normal_dis))
# print('mode: ', stats.mode(np_normal_dis))
# print('sd: ', np.std(np_normal_dis))
# plt.hist(np_normal_dis, color="grey", bins=21)
# plt.show()

mu = 28
sigma = 15
samples = 100000

x = np.random.normal(mu, sigma, samples)
ax = sns.distplot(x);
ax.set(xlabel="x", ylabel='y')
plt.show()