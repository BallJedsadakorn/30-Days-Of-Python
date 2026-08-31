# 1. Filter only negative numbers and zero using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
non_positive = [n for n in numbers if n <= 0]
print(non_positive)
# [-4, -3, -2, -1, 0]

# 2. Flatten list of lists to one dimensional list
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flat_list = [item for sublist in list_of_lists for item in sublist]
print(flat_list)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 3. Build the list of tuples (n, n^0, n^1, n^2, n^3, n^4, n^5)
result = [(n, n**0, n**1, n**2, n**3, n**4, n**5) for n in range(11)]
print(result)
# [(0, 1, 0, 0, 0, 0, 0),
#  (1, 1, 1, 1, 1, 1, 1),
#  (2, 1, 2, 4, 8, 16, 32),
#  (3, 1, 3, 9, 27, 81, 243),
#  (4, 1, 4, 16, 64, 256, 1024),
#  (5, 1, 5, 25, 125, 625, 3125),
#  (6, 1, 6, 36, 216, 1296, 7776),
#  (7, 1, 7, 49, 343, 2401, 16807),
#  (8, 1, 8, 64, 512, 4096, 32768),
#  (9, 1, 9, 81, 729, 6561, 59049),
#  (10, 1, 10, 100, 1000, 10000, 100000)]

# 4. Flatten and transform the countries list
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

flattened = [
    [country.upper(), country[:3].upper(), city.upper()]
    for [(country, city)] in countries
]
print(flattened)
# [['FINLAND', 'FIN', 'HELSINKI'],
#  ['SWEDEN', 'SWE', 'STOCKHOLM'],
#  ['NORWAY', 'NOR', 'OSLO']]

# 5. Convert to a list of dictionaries
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

country_dicts = [
    {'country': country.upper(), 'city': city.upper()}
    for [(country, city)] in countries
]
print(country_dicts)
# [{'country': 'FINLAND', 'city': 'HELSINKI'},
#  {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
#  {'country': 'NORWAY', 'city': 'OSLO'}]

# 6. Concatenate first and last names
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

full_names = [f'{first} {last}' for [(first, last)] in names]
print(full_names)
# ['Asabeneh Yetayeh', 'David Smith', 'Donald Trump', 'Bill Gates']

# 7. Lambda functions for slope and y-intercept of a linear function
# Given two points (x1, y1) and (x2, y2):
#   slope m = (y2 - y1) / (x2 - x1)
#   y-intercept b = y1 - m * x1

slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
y_intercept = lambda x1, y1, x2, y2: y1 - slope(x1, y1, x2, y2) * x1

# Example: line through (2, 3) and (4, 7)
m = slope(2, 3, 4, 7)
b = y_intercept(2, 3, 4, 7)
print(f'slope = {m}, y-intercept = {b}')
# slope = 2.0, y-intercept = -1.0
# i.e. the line is y = 2x - 1