#!/usr/bin/env python
# coding: utf-8

# # Python Practice 131-140

# ## Here are the Python programs for each of the objectives along with the associated algorithm, mathematical calculations, and string manipulations:

# ### 131. Calculate the Perimeter of a Torus

# In[10]:


import math

def perimeter_of_torus(major_radius, minor_radius):
    return 2 * math.pi * (major_radius + minor_radius)

major_radius, minor_radius = 5, 3
perimeter = perimeter_of_torus(major_radius, minor_radius)
print(f"The perimeter of the torus with major radius {major_radius} and minor radius {minor_radius} is {perimeter:.2f}.")


# ### 132. Print the Pattern of a Rhombus Star

# In[9]:


def print_rhombus_star_pattern(n):
    for i in range(n):
        print(" " * (n - i - 1) + "* " * (i + 1))
    for i in range(n - 2, -1, -1):
        print(" " * (n - i - 1) + "* " * (i + 1))

rows = 5
print_rhombus_star_pattern(rows)


# ### 133. Generate a Random Password with Custom Character Requirements

# In[8]:


import random
import string

def generate_random_password_custom_requirements(length, requires_uppercase=True, requires_lowercase=True, requires_digits=True, requires_special_chars=True):
    characters = ""
    if requires_uppercase:
        characters += string.ascii_uppercase
    if requires_lowercase:
        characters += string.ascii_lowercase
    if requires_digits:
        characters += string.digits
    if requires_special_chars:
        characters += string.punctuation
    random_password = ''.join(random.choice(characters) for _ in range(length))
    return random_password

password_length = 12
password_requires_uppercase = True
password_requires_lowercase = True
password_requires_digits = True
password_requires_special_chars = True
random_password = generate_random_password_custom_requirements(password_length, password_requires_uppercase, password_requires_lowercase, password_requires_digits, password_requires_special_chars)
print(f"Generated Random Password with custom requirements: {random_password}")


# ### 134. Convert Decimal to Base-N (N > 10)

# In[7]:


def decimal_to_base_n(num, base):
    if num == 0:
        return "0"
    base_n_str = ""
    while num > 0:
        remainder = num % base
        if remainder >= 10:
            base_n_str = chr(ord('A') + remainder - 10) + base_n_str
        else:
            base_n_str = str(remainder) + base_n_str
        num //= base
    return base_n_str

decimal_num = 42
base = 16
base_n_num = decimal_to_base_n(decimal_num, base)
print(f"The base-{base} representation of {decimal_num} is {base_n_num}.")


# ### 135. Check if a Number is a Cube Number

# In[6]:


def is_cube_number(num):
    cube_root = round(num ** (1/3))
    return cube_root ** 3 == num

number = 27
if is_cube_number(number):
    print(f"{number} is a cube number.")
else:
    print(f"{number} is not a cube number.")


# ### 136. Calculate the Volume of a Sphere

# In[5]:


import math

def volume_of_sphere(radius):
    return (4/3) * math.pi * radius ** 3

radius = 5
volume = volume_of_sphere(radius)
print(f"The volume of the sphere with radius {radius} is {volume:.2f}.")


# ### 137. Implement Trie Data Structure

# In[4]:


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

# Example usage of the Trie data structure
trie = Trie()
trie.insert("apple")
trie.insert("banana")
trie.insert("orange")

search_word = "apple"
if trie.search(search_word):
    print(f"{search_word} is present in the Trie.")
else:
    print(f"{search_word} is not present in the Trie.")


# ### 138. Find the Lychrel Numbers in a Range

# In[3]:


def is_palindrome(num):
    return str(num) == str(num)[::-1]

def reverse_add(num):
    return num + int(str(num)[::-1])

def is_lychrel_number(num, max_iterations=50):
    for _ in range(max_iterations):
        num = reverse_add(num)
        if is_palindrome(num):
            return False
    return True

def find_lychrel_numbers(start, end):
    lychrel_numbers = [num for num in range(start, end+1) if is_lychrel_number(num)]
    return lychrel_numbers

start_range, end_range = 1, 1000
lychrel_numbers_list = find_lychrel_numbers(start_range, end_range)
print(f"Lychrel numbers in the range {start_range} to {end_range}: {lychrel_numbers_list}")


# ### 139. Calculate the Perimeter of a Regular Tetrahedron

# In[2]:


import math

def perimeter_of_regular_tetrahedron(edge_length):
    return 3 * edge_length

edge_length = 5
perimeter = perimeter_of_regular_tetrahedron(edge_length)
print(f"The perimeter of the regular tetrahedron with edge length {edge_length} is {perimeter:.2f}.")


# ### 140. Print the Pattern of a Hollow Rhombus Star

# In[1]:


def print_hollow_rhombus_star_pattern(n):
    for i in range(n):
        print(" " * (n - i - 1) + "* " * n)
    for i in range(1, n):
        print(" " * i + "* " * (n - i))

rows = 5
print_hollow_rhombus_star_pattern(rows)


# In[ ]:




