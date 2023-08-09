#!/usr/bin/env python
# coding: utf-8

# # Python Practice 151-160

# ## Here are the Python programs for each of the objectives along with the associated algorithm, mathematical calculations, and string manipulations:

# ### 151. Check if a Number is a Triangular Number

# In[11]:


def is_triangular_number(num):
    n = 1
    while num > 0:
        num -= n
        n += 1
    return num == 0

number = 45
if is_triangular_number(number):
    print(f"{number} is a triangular number.")
else:
    print(f"{number} is not a triangular number.")


# ### 152. Calculate the Volume of a Torus

# In[10]:


import math

def volume_of_torus(major_radius, minor_radius):
    return (math.pi ** 2) * minor_radius ** 2 * major_radius

major_radius, minor_radius = 5, 3
volume = volume_of_torus(major_radius, minor_radius)
print(f"The volume of the torus with major radius {major_radius} and minor radius {minor_radius} is {volume:.2f}.")


# ### 153. Implement Hash Table Data Structure

# In[9]:


class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [[] for _ in range(self.size)]

    def _hash_function(self, key):
        return sum(ord(char) for char in key) % self.size

    def put(self, key, value):
        index = self._hash_function(key)
        for item in self.table[index]:
            if item[0] == key:
                item[1] = value
                return
        self.table[index].append((key, value))

    def get(self, key):
        index = self._hash_function(key)
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
        return None

# Example usage of the Hash Table data structure
hash_table = HashTable()
hash_table.put("apple", 50)
hash_table.put("banana", 20)
hash_table.put("orange", 30)

print("Value of 'apple':", hash_table.get("apple"))
print("Value of 'grape':", hash_table.get("grape"))


# ### 154. Find the Fascinating Numbers in a Range

# In[8]:


def is_fascinating_number(num):
    num_str = str(num) + str(2 * num) + str(3 * num)
    return set(num_str) == set("123456789")

def find_fascinating_numbers(start, end):
    fascinating_numbers = [num for num in range(start, end+1) if is_fascinating_number(num)]
    return fascinating_numbers

start_range, end_range = 100, 999
fascinating_numbers_list = find_fascinating_numbers(start_range, end_range)
print(f"Fascinating numbers in the range {start_range} to {end_range}: {fascinating_numbers_list}")


# ### 155. Calculate the Perimeter of a Regular Dodecahedron

# In[7]:


def perimeter_of_regular_dodecahedron(edge_length):
    return 12 * edge_length

edge_length = 5
perimeter = perimeter_of_regular_dodecahedron(edge_length)
print(f"The perimeter of the regular dodecahedron with edge length {edge_length} is {perimeter:.2f}.")


# ### 156. Print the Pattern of a Hollow Pascal's Triangle

# In[6]:


def print_hollow_pascals_triangle(n):
    for i in range(n):
        for j in range(i+1):
            if j == 0 or j == i or i == n-1:
                print(1, end=" ")
            else:
                print(" ", end=" ")
        print()

rows = 5
print_hollow_pascals_triangle(rows)


# ### 157. Generate a Random Password with Levenshtein Distance Constraint

# In[5]:


import random
import string
import Levenshtein

def generate_random_password_levenshtein_constraint(length, constraint_string, max_distance):
    characters = string.ascii_letters + string.digits + string.punctuation
    random_password = ''.join(random.choice(characters) for _ in range(length))
    while Levenshtein.distance(random_password, constraint_string) > max_distance:
        random_password = ''.join(random.choice(characters) for _ in range(length))
    return random_password

password_length = 8
constraint_string = "password"
max_distance = 2
random_password = generate_random_password_levenshtein_constraint(password_length, constraint_string, max_distance)
print(f"Generated Random Password with Levenshtein distance constraint: {random_password}")


# ### 158. Convert Decimal to Balanced Ternary

# In[4]:


def decimal_to_balanced_ternary(num):
    digits = "012"
    balanced_ternary = ""
    while num != 0:
        remainder = num % 3
        if remainder == 2:
            num += 1
            balanced_ternary = "T" + balanced_ternary
        else:
            balanced_ternary = digits[remainder] + balanced_ternary
        num //= 3
    return balanced_ternary

decimal_num = 42
balanced_ternary_num = decimal_to_balanced_ternary(decimal_num)
print(f"The balanced ternary representation of {decimal_num} is {balanced_ternary_num}.")


# ### 159. Check if a Number is a Powerful Number

# In[3]:


def is_powerful_number(num):
    def prime_factors(n):
        factors = set()
        while n % 2 == 0:
            factors.add(2)
            n //= 2
        for i in range(3, int(n**0.5) + 1, 2):
            while n % i == 0:
                factors.add(i)
                n //= i
        if n > 2:
            factors.add(n)
        return factors

    factors = prime_factors(num)
    return all(num % (factor ** 2) == 0 for factor in factors)

number = 64
if is_powerful_number(number):
    print(f"{number} is a powerful number.")
else:
    print(f"{number} is not a powerful number.")


# ### 160. Calculate the Volume of a Tetrahedron

# In[2]:


def volume_of_tetrahedron(edge_length):
    return (edge_length ** 3) / (6 * (2 ** 0.5))

edge_length = 5
volume = volume_of_tetrahedron(edge_length)
print(f"The volume of the tetrahedron with edge length {edge_length} is {volume:.2f}.")


# In[ ]:




