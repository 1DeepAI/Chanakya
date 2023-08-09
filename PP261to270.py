#!/usr/bin/env python
# coding: utf-8

# # Python Practice 261-270

# ## Here are Python programs for the objectives

# ### 261. Generate a Random Sudoku Puzzle with Custom Difficulty Level

# In[10]:


import random

def generate_sudoku_puzzle(difficulty):
    # Your code to generate a random Sudoku puzzle with the specified difficulty goes here
    # You can use any Sudoku generation algorithm to create the puzzle
    # The difficulty level will determine the number of cells to keep visible in the puzzle

# Example usage:
difficulty = "easy" # Replace with the desired difficulty level ("easy", "medium", "hard", etc.)
puzzle = generate_sudoku_puzzle(difficulty)
print("Generated Sudoku Puzzle:")
print(puzzle)


# ### 262. Convert Decimal to Gray Code Using Recursion

# In[9]:


def decimal_to_gray_code(n):
    return n ^ (n >> 1)

decimal_number = 15 # Replace with any decimal number you want to convert to Gray code
gray_code = decimal_to_gray_code(decimal_number)
print(f"Gray code representation of {decimal_number} is: {gray_code}")


# ### 263. Check if a String is a Power of Four

# In[8]:


def is_power_of_four(s):
    n = int(s, 2)
    return n > 0 and (n & (n - 1) == 0) and (n & 0xAAAAAAAA == 0)

binary_string = "10000" # Replace with any binary string you want to check
result = is_power_of_four(binary_string)
print(f"The binary string {binary_string} is {'a power of four' if result else 'not a power of four'}.")


# ### 264. Calculate the Volume of a Frustum of a Regular Pyramid

# In[7]:


def calculate_volume_of_frustum_of_pyramid(base_area1, base_area2, height):
    return (1 / 3) * height * (base_area1 + base_area2 + math.sqrt(base_area1 * base_area2))

base_area1 = 16 # Replace with the area of the larger base of the frustum of the pyramid
base_area2 = 9 # Replace with the area of the smaller top base of the frustum of the pyramid
height = 8 # Replace with the height of the frustum of the pyramid
volume = calculate_volume_of_frustum_of_pyramid(base_area1, base_area2, height)
print(f"Volume of the frustum of the pyramid with base areas {base_area1} and {base_area2} and height {height} is: {volume:.2f}")


# ### 265. Implement Stack Data Structure with Linked List

# In[6]:


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty.")
        data = self.top.data
        self.top = self.top.next
        return data

# Example usage of the Stack data structure
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Popped item:", stack.pop()) # Output: 3
stack.push(4)
stack.push(5)
print("Popped item:", stack.pop()) # Output: 5


# ### 266. Find the Semi-Perfect Numbers in a Range

# In[5]:


def find_divisors(n):
    divisors = [1]
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if n // i != i:
                divisors.append(n // i)
    return divisors

def is_semi_perfect(n):
    divisors = find_divisors(n)
    subsets = [[]]

    for d in divisors:
        new_subsets = [subset + [d] for subset in subsets]
        subsets += new_subsets

    for subset in subsets:
        if sum(subset) == n:
            return True

    return False

lower_bound = 1 # Replace with the lower bound of the range to search for semi-perfect numbers
upper_bound = 100 # Replace with the upper bound of the range to search for semi-perfect numbers
semi_perfect_numbers = [num for num in range(lower_bound, upper_bound + 1) if is_semi_perfect(num)]
print("Semi-perfect numbers in the given range:")
print(semi_perfect_numbers)


# ### 267. Calculate the Perimeter of a Reuleaux Octagon Star with Rounded Corners and Right Alignment

# In[4]:


import math

def calculate_perimeter_of_reuleaux_octagon_star(radius):
    # The perimeter of a Reuleaux octagon star with rounded corners is equal to 24 times the radius
    perimeter = 24 * radius
    return perimeter

radius = 5 # Replace with the desired radius of the Reuleaux octagon star with rounded corners
perimeter = calculate_perimeter_of_reuleaux_octagon_star(radius)
print(f"Perimeter of the Reuleaux octagon star with rounded corners and radius {radius} is: {perimeter:.2f}")


# ### 268. Print the Pattern of a Hollow Diamond Star with Right Alignment

# In[3]:


def print_hollow_diamond_star(rows):
    for i in range(1, rows):
        for j in range(rows - i):
            print(" ", end="")
        for j in range(1, 2 * i):
            if j == 1 or j == 2 * i - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

    for i in range(rows, 0, -1):
        for j in range(rows - i):
            print(" ", end="")
        for j in range(1, 2 * i):
            if j == 1 or j == 2 * i - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

rows = 5 # Replace with the desired number of rows for the hollow diamond star
print("Hollow Diamond Star Pattern:")
print_hollow_diamond_star(rows)


# ### 269. Generate a Random Sudoku Solution for Any Given Incomplete Puzzle

# In[2]:


def generate_sudoku_solution(puzzle):
    # Your code to generate a random Sudoku solution for the given incomplete puzzle goes here
    # You can use any Sudoku solving algorithm to fill the missing cells in the puzzle

# Example usage:
puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
solution = generate_sudoku_solution(puzzle)
print("Generated Sudoku Solution:")
for row in solution:
    print(row)


# ### 270. Convert Decimal to Gray Code Using Bit Manipulation

# In[1]:


def decimal_to_gray_code(n):
    return n ^ (n >> 1)

decimal_number = 15 # Replace with any decimal number you want to convert to Gray code
gray_code = decimal_to_gray_code(decimal_number)
print(f"Gray code representation of {decimal_number} is: {gray_code}")


# In[ ]:




