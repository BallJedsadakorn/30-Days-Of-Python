# 1. Create an empty tuple
empty_tuple = ()
print(empty_tuple)  # ()

# 2. Tuple of sisters and brothers
sisters = ('Emma', 'Sophia')
brothers = ('Liam', 'Noah', 'Ethan')

# 3. Join brothers and sisters -> siblings
siblings = sisters + brothers
print(siblings)  # ('Emma', 'Sophia', 'Liam', 'Noah', 'Ethan')

# 4. How many siblings?
print(len(siblings))  # 5

# 5. Add father and mother to siblings -> family_members
# Tuples are immutable, so "modifying" means creating a new tuple
family_members = siblings + ('Robert', 'Maria')
print(family_members)  # ('Emma', 'Sophia', 'Liam', 'Noah', 'Ethan', 'Robert', 'Maria')

# 1. Unpack siblings and parents from family_members
# family_members = 5 siblings + father + mother = 7 items
sister1, sister2, brother1, brother2, brother3, father, mother = family_members
print(sister1, father, mother)  # Emma Robert Maria

# 2. Create fruits, vegetables, animal_products; join into food_stuff_tp
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('tomato', 'potato', 'cabbage', 'onion', 'carrot')
animal_products = ('milk', 'meat', 'cheese', 'yoghurt')

food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)
# ('banana', 'orange', 'mango', 'lemon', 'tomato', 'potato', 'cabbage', 
#  'onion', 'carrot', 'milk', 'meat', 'cheese', 'yoghurt')

# 3. Change food_stuff_tp tuple to food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)
print(type(food_stuff_lt))  # <class 'list'>

# 4. Slice out the middle item(s)
# len(food_stuff_tp) = 13 (odd), so there's a single middle item at index 6
length = len(food_stuff_tp)
mid_index = length // 2

if length % 2 == 0:
    # even length -> two middle items
    middle = food_stuff_tp[mid_index - 1: mid_index + 1]
else:
    # odd length -> one middle item
    middle = food_stuff_tp[mid_index]

print(middle)  # 'cabbage'  (index 6 of 13 items)

# 5. First three and last three items from food_stuff_lt
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print(first_three)  # ['banana', 'orange', 'mango']
print(last_three)   # ['meat', 'cheese', 'yoghurt']

# 6. Delete food_stuff_tp completely
del food_stuff_tp
# food_stuff_tp no longer exists — referencing it now raises NameError

# 7. Check membership in nordic_countries
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

print('Estonia' in nordic_countries)  # False
print('Iceland' in nordic_countries)  # True