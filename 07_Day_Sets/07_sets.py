it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

# 1. Length of the set
print(len(it_companies))  # 7

# 2. Add 'Twitter'
it_companies.add('Twitter')
print(it_companies)  # 8 items now, order not guaranteed (sets are unordered)

# 3. Insert multiple companies at once — use update()
it_companies.update(['Tesla', 'Netflix', 'Spotify'])
print(it_companies)  # 11 items now

# 4. Remove one company
it_companies.discard('IBM')  # or .remove('IBM')
print(it_companies)

# 5. remove vs discard
# Both delete an item from a set.
# - remove(x): raises a KeyError if x is not in the set
# - discard(x): does nothing (no error) if x is not in the set
# discard is "safer" when you're not sure the item exists.
it_companies.remove('Oracle')   # works fine, Oracle exists
# it_companies.remove('Yahoo')  # would raise KeyError
it_companies.discard('Yahoo')   # no error, silently does nothing

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# 1. Join A and B (union)
print(A.union(B))
# {19, 20, 22, 24, 25, 26, 27, 28}

# 2. A intersection B
print(A.intersection(B))
# {19, 20, 22, 24, 25, 26}

# 3. Is A a subset of B?
print(A.issubset(B))  # True — every element of A is in B

# 4. Are A and B disjoint sets?
print(A.isdisjoint(B))  # False — they share elements

# 5. Join A with B and B with A
print(A.union(B))  # same result
print(B.union(A))  # union is commutative — identical output
# {19, 20, 22, 24, 25, 26, 27, 28}

# 6. Symmetric difference between A and B
print(A.symmetric_difference(B))
# {27, 28} — elements in exactly one of the sets (not both)

# 7. Delete the sets completely
del A
del B
# A and B no longer exist — referencing them raises NameError

age = [22, 19, 24, 25, 26, 24, 25, 24]

# 1. Convert ages to a set, compare lengths
age_set = set(age)
print(len(age))      # 8 — list keeps duplicates
print(len(age_set))  # 5 — set removes duplicates: {19, 22, 24, 25, 26}
# The list is bigger (or equal) because sets can't hold duplicate values.

# 2. string, list, tuple, set — differences

# 3. Unique words in the sentence
sentence = "I am a teacher and I love to inspire and teach people"
unique_words = set(sentence.split())
print(unique_words)
print(len(unique_words))  # 10