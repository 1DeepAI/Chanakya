#!/usr/bin/env python
# coding: utf-8

# # Python Practice 111-120

# ##  

# ###  111. Check if a Number is a Magic Number

# In[10]:


def is_magic_number(num):
    num_str = str(num)
    sum_of_digits = sum(int(digit) for digit in num_str)
    return num == sum_of_digits

number = 19
if is_magic_number(number):
    print(f"{number} is a magic number.")
else:
    print(f"{number} is not a magic number.")


# ### 112. Calculate the Volume of a Cube

# In[9]:


def volume_of_cube(side_length):
    return side_length ** 3

side_length = 5
volume = volume_of_cube(side_length)
print(f"The volume of the cube with side length {side_length} is {volume}.")


# ### 113. Implement Binary Search Tree Data Structure

# In[8]:


class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if not node:
            return TreeNode(key)
        if key < node.key:
            node.left = self._insert_recursive(node.left, key)
        else:
            node.right = self._insert_recursive(node.right, key)
        return node

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if not node or node.key == key:
            return node
        if key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)

# Example usage of the Binary Search Tree data structure
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

search_key = 40
if bst.search(search_key):
    print(f"{search_key} is present in the Binary Search Tree.")
else:
    print(f"{search_key} is not present in the Binary Search Tree.")


# ### 114. Find the Harshad Numbers in a Range

# In[7]:


def is_harshad_number(num):
    return num % sum(int(digit) for digit in str(num)) == 0

def find_harshad_numbers(start, end):
    harshad_numbers = [num for num in range(start, end+1) if is_harshad_number(num)]
    return harshad_numbers

start_range, end_range = 1, 100
harshad_numbers_list = find_harshad_numbers(start_range, end_range)
print(f"Harshad numbers in the range {start_range} to {end_range}: {harshad_numbers_list}")


# ### 115. Calculate the Perimeter of a Cone

# In[6]:


import math

def perimeter_of_cone(radius, slant_height):
    return math.pi * radius + 2 * slant_height

radius, slant_height = 5, 8
perimeter = perimeter_of_cone(radius, slant_height)
print(f"The perimeter of the cone with radius {radius} and slant height {slant_height} is {perimeter:.2f}.")


# ### 116. Print the Pattern of a Pascal's Triangle

# In[5]:


def print_pascals_triangle(n):
    for line in range(1, n + 1):
        num = 1
        for i in range(1, line + 1):
            print(num, end=" ")
            num = num * (line - i) // i
        print()

rows = 5
print_pascals_triangle(rows)


# ### 117. Generate a Random Password with Custom Length and Character Set

# In[4]:


import random
import string

def generate_random_password_custom(length, characters):
    random_password = ''.join(random.choice(characters) for _ in range(length))
    return random_password

custom_characters = "@#$%abcdef123"
password_length = 10
random_password = generate_random_password_custom(password_length, custom_characters)
print(f"Generated Random Password with custom characters: {random_password}")


# ### 118. Convert Base-N to Decimal (N > 10)

# In[3]:


def base_n_to_decimal(num, base):
    decimal_num = 0
    num_str = str(num)
    for i, digit in enumerate(num_str[::-1]):
        decimal_num += int(digit, base) * (base ** i)
    return decimal_num

number = "1A3"
base = 16
decimal_num = base_n_to_decimal(number, base)
print(f"The decimal representation of {number} in base {base} is {decimal_num}.")


# ### 119. Check if a Number is a Neon Number

# In[2]:


def is_neon_number(num):
    square = num ** 2
    return sum(int(digit) for digit in str(square)) == num

number = 9
if is_neon_number(number):
    print(f"{number} is a neon number.")
else:
    print(f"{number} is not a neon number.")


# ### 120. Calculate the Volume of a Cuboid

# In[1]:


def volume_of_cuboid(length, width, height):
    return length * width * height

length, width, height = 5, 3, 8
volume = volume_of_cuboid(length, width, height)
print(f"The volume of the cuboid with length {length}, width {width}, and height {height} is {volume}.")


# In[ ]:




