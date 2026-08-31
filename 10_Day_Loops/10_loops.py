# 1. Numbers 0 to 10, for loop and while loop
from data import countries


for i in range(11):
    print(i)

i = 0
while i <= 10:
    print(i)
    i += 1
    
# 2. Numbers 10 to 0, for loop and while loop
for i in range(10, -1, -1):
    print(i)

i = 10
while i >= 0:
    print(i)
    i -= 1
    
# 3. Triangle of hashes (7 rows)
for i in range(1, 8):
    print('#' * i)
    
# 4. 8x8 grid of hashes, space-separated
for row in range(8):
    line = ''
    for col in range(8):
        line += '# '
    print(line.strip())
    
# 5. Multiplication table (n x n = n^2)
for i in range(11):
    print(f'{i} x {i} = {i * i}')
    
# 6. Iterate through the list and print items
techs = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for tech in techs:
    print(tech)
    
# 7. Even numbers 0 to 100
for i in range(0, 101, 2):
    print(i)
    
# 8. Odd numbers 0 to 100
for i in range(1, 101, 2):
    print(i)
    
# 1. Sum of all numbers 0 to 100
total = 0
for i in range(101):
    total += i
print(f'The sum of all numbers is {total}.')
# The sum of all numbers is 5050.

# 2. Sum of evens and odds separately
sum_evens = 0
sum_odds = 0

for i in range(101):
    if i % 2 == 0:
        sum_evens += i
    else:
        sum_odds += i

print(f'The sum of all evens is {sum_evens}. And the sum of all odds is {sum_odds}.')
# The sum of all evens is 2550. And the sum of all odds is 2500.

# 1. Countries containing the word 'land'
# (assumes: from countries import countries)
countries_with_land = []
for country in countries:
    if 'land' in country.lower():
        countries_with_land.append(country)

print(countries_with_land)
# Includes entries like 'Iceland', 'Ireland', 'New Zealand',
# 'Poland', 'Switzerland', 'Thailand', etc.

# 2. Reverse a fruit list using a loop (without reversed()/.reverse())
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []

for i in range(len(fruits) - 1, -1, -1):
    reversed_fruits.append(fruits[i])

print(reversed_fruits)
