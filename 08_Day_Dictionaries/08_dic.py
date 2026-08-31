# 1. Create an empty dictionary called dog
dog = {}
print(dog)  # {}

# 2. Add name, color, breed, legs, age to the dog dictionary
dog = {
    'name': 'Rex',
    'color': 'brown',
    'breed': 'Labrador',
    'legs': 4,
    'age': 3
}
print(dog)

# 3. Create a student dictionary with the given keys
student = {
    'first_name': 'Ball',
    'last_name': 'Boonlerd',
    'gender': 'Male',
    'age': 24,
    'marital_status': 'Single',
    'skills': ['Python', 'SQL', 'Airflow'],
    'country': 'Thailand',
    'city': 'Bangkok',
    'address': '123 Sukhumvit Rd'
}
print(student)

# 4. Get the length of the student dictionary
print(len(student))  # 9

# 5. Get the value of skills, check its data type
print(student['skills'])        # ['Python', 'SQL', 'Airflow']
print(type(student['skills']))  # <class 'list'>

# 6. Modify the skills values by adding one or two skills
student['skills'].append('PySpark')
student['skills'].extend(['PostgreSQL', 'GCS'])
print(student['skills'])
# ['Python', 'SQL', 'Airflow', 'PySpark', 'PostgreSQL', 'GCS']

# 7. Get the dictionary keys as a list
student_keys = list(student.keys())
print(student_keys)
# ['first_name', 'last_name', 'gender', 'age', 'marital_status',
#  'skills', 'country', 'city', 'address']

# 8. Get the dictionary values as a list
student_values = list(student.values())
print(student_values)

# 9. Change the dictionary to a list of tuples using items()
student_items = list(student.items())
print(student_items)
# [('first_name', 'Ball'), ('last_name', 'Boonlerd'), ('gender', 'Male'), ...]

# 10. Delete one of the items in the dictionary
del student['marital_status']
print(student)  # marital_status key/value is gone

# 11. Delete one of the dictionaries
del dog
# dog no longer exists — referencing it now raises NameError