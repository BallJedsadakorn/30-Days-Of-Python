# 1. Age check for driving
age = int(input("Enter your age: "))

if age >= 18:
    print("You are old enough to learn to drive.")
else:
    years_needed = 18 - age
    print(f"You need {years_needed} more years to learn to drive.")
    
# 2. Compare my_age and your_age
my_age = 30
your_age = int(input("Enter your age: "))

if your_age > my_age:
    diff = your_age - my_age
    if diff == 1:
        print(f"You are {diff} year older than me.")
    else:
        print(f"You are {diff} years older than me.")
elif your_age < my_age:
    diff = my_age - your_age
    if diff == 1:
        print(f"You are {diff} year younger than me.")
    else:
        print(f"You are {diff} years younger than me.")
else:
    print("We are the same age.")
    
# 3. Compare two numbers
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))

if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")
    
# 1. Grade calculator
score = int(input("Enter your score: "))

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"Your grade is {grade}")

# 2. Season from month
month = input("Enter month: ").capitalize()

autumn = ['September', 'October', 'November']
winter = ['December', 'January', 'February']
spring = ['March', 'April', 'May']
summer = ['June', 'July', 'August']

if month in autumn:
    print("The season is Autumn.")
elif month in winter:
    print("The season is Winter.")
elif month in spring:
    print("The season is Spring.")
elif month in summer:
    print("The season is Summer.")
else:
    print("Not a valid month.")
    
# 3. Add fruit if not already in the list
fruits = ['banana', 'orange', 'mango', 'lemon']

new_fruit = input("Enter a fruit: ")

if new_fruit in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(new_fruit)
    print(fruits)
    

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# 1. Middle skill in skills list, if 'skills' key exists
if 'skills' in person:
    skills = person['skills']
    length = len(skills)
    mid_index = length // 2

    if length % 2 == 0:
        middle_skill = skills[mid_index - 1: mid_index + 1]
    else:
        middle_skill = skills[mid_index]

    print(f"Middle skill: {middle_skill}")
    # skills has 5 items -> odd -> single middle item at index 2 -> 'Node'

# 2. Check if 'skills' key exists, then check for 'Python'
if 'skills' in person:
    if 'Python' in person['skills']:
        print('He knows Python')
    else:
        print('He does not know Python')

# 3. Determine developer title based on skills
skills = person['skills']

if 'JavaScript' in skills and 'React' in skills and 'Node' not in skills and 'MongoDB' not in skills and 'Python' not in skills:
    print('He is a front end developer')
elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
    print('He is a backend developer')
elif 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
    print('He is a fullstack developer')
else:
    print('unknown title')
# Since skills contains React, Node, and MongoDB (among others),
# this matches the "fullstack developer" condition -> prints that.

# 4. Married + lives in Finland
if person.get('is_married') and person.get('country') == 'Finland':
    full_name = f"{person['first_name']} {person['last_name']}"
    print(f"{full_name} lives in {person['country']}. He is married.")