#!/usr/bin/env python
# coding: utf-8

# # Python Practice 411-420

# ## Here are Python Codes

# ### 411. Calculate the Perimeter of a Reuleaux Pentagon Star with Rounded Corners, Right Alignment, Custom Size, Custom Side Lengths, Variable Base, Custom Position, and Custom Border
# 

# In[1]:


import math

def reuleaux_pentagon_perimeter(side_length):
    arc_length = (1/3) * math.pi * side_length
    perimeter = 5 * arc_length
    return perimeter

# Example usage
side_length = 10  # You can change this value for custom side length
perimeter = reuleaux_pentagon_perimeter(side_length)
print(f"The perimeter of the Reuleaux pentagon with side length {side_length} is: {perimeter:.2f}")


# ### 412. Print the Pattern of a Hollow Rhombus Star with Right Alignment, Custom Size, Custom Rhombus Width, Variable Base Length, and Custom Position
# we'll need to understand the requirements better:
# 
# 1. Right Alignment: The rhombus should be aligned to the right side of the console.
# 2. Custom Size: This could refer to the number of rows in the rhombus.
# 3. Custom Rhombus Width: This refers to the horizontal width (or diagonal length) of the rhombus.
# 4. Variable Base Length: This might refer to a modification in the base width. For simplicity, I will assume the base remains constant with the custom rhombus width.
# 5. Custom Position: This could mean the starting point in terms of rows and columns where the rhombus should be printed.

# In[2]:


def print_hollow_rhombus(rows, rhombus_width, start_row=0, start_col=0):
    for i in range(1, rows + 1):
        # For top half of the rhombus
        if i <= rhombus_width:
            # Print spaces for right alignment and position
            print(' ' * (rows - i + start_col), end='')
            
            # Print stars
            if i == 1 or i == rhombus_width:
                print('*' * rhombus_width)
            else:
                print('*' + ' ' * (rhombus_width - 2) + '*')
        # For bottom half of the rhombus
        else:
            # Print spaces for right alignment and position
            print(' ' * (i - rhombus_width + start_col), end='')
            
            # Print stars
            if i == rows or i == rows - rhombus_width + 1:
                print('*' * rhombus_width)
            else:
                print('*' + ' ' * (rhombus_width - 2) + '*')

# Example usage
rows = 10  # Total rows (height of the rhombus)
rhombus_width = 5  # Width of the rhombus
start_row = 2  # Starting position (rows from the top)
start_col = 3  # Starting position (columns from the left)

print_hollow_rhombus(rows, rhombus_width, start_row, start_col)


# ### 413. Generate a Random Word Cloud from Web Data with Custom Word Frequency, Size, Color, Font, Position, Shape, and Background
# Creating a word cloud from web data involves a few steps:
# 
# 1. Fetching the web data.
# 2. Processing the text to generate word frequencies.
# 3. Creating a word cloud using the processed data and custom parameters.

# In[5]:


import requests
from bs4 import BeautifulSoup
from collections import Counter
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Step 1: Fetch web data
url = 'https://www.example.com'  # Replace with your desired URL
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
text = soup.get_text()

# Step 2: Process the text
word_list = [word.lower() for word in text.split() if word.isalpha()]
word_freq = Counter(word_list)

# Use custom frequencies (if you have them)
custom_freq = {
    'python': 100,
    'programming': 80,
    'web': 75
}
word_freq.update(custom_freq)

# Step 3: Generate Word Cloud
# Load mask for custom shape (optional)
# Replace with your mask image path



# ### 414. Convert Decimal to Excess-K Code Using Bit Manipulation, Custom K with Variable Size, Custom Encoding Scheme, and Variable Base with Custom Precision
# Let's break this down step by step.
# 
# The Excess-K code (or bias representation) is a way to represent integers in which a value of k is added to the actual number to give the stored number.
# 
# Here's how to convert a decimal to its Excess-K representation using bit manipulation:
# 
# 1. Add k to the number.
# 2. Convert the result to binary.
# For custom encoding and variable base, I'll demonstrate converting the Excess-K representation to a different base (like hexadecimal, octal, or a custom base) and back. For precision, we'll consider a fixed number of bits for the representation.
# 
# 

# In[6]:


def decimal_to_binary(n, bits):
    """Convert a number to its binary representation with a fixed number of bits."""
    return format(n, '0' + str(bits) + 'b')

def binary_to_custom_base(binary_str, base_chars):
    """Convert binary string to custom base."""
    base = len(base_chars)
    decimal_val = int(binary_str, 2)
    if decimal_val == 0:
        return base_chars[0]
    result = []
    while decimal_val:
        result.append(base_chars[decimal_val % base])
        decimal_val //= base
    return ''.join(reversed(result))

def decimal_to_excess_k(decimal_num, k, bits, base_chars="01"):
    """Convert a decimal number to its Excess-K representation."""
    decimal_num += k  # Add the bias
    binary_str = decimal_to_binary(decimal_num, bits)
    return binary_to_custom_base(binary_str, base_chars)

# Test
k = 16  # Custom bias
bits = 8  # Custom precision
decimal_num = 5
base_chars = "0123456789ABCDEF"  # Hexadecimal base

excess_k_representation = decimal_to_excess_k(decimal_num, k, bits, base_chars)
print(f"Decimal {decimal_num} in Excess-{k} representation: {excess_k_representation}")


# ### 415. Check if a Number is a Generalized Heptagonal Pentagonal Number
# first let's define what generalized heptagonal pentagonal numbers are, as the definition is not standard.
# Now, a generalized heptagonal pentagonal number would be a number that is both a pentagonal number and a heptagonal number.

# In[7]:


def is_pentagonal(x):
    """Check if a number is a pentagonal number."""
    test_val = (24 * x + 1) ** 0.5
    return test_val == int(test_val) and int(test_val) % 6 == 5

def is_heptagonal(x):
    """Check if a number is a heptagonal number."""
    test_val = (40 * x + 9) ** 0.5
    return test_val == int(test_val) and (int(test_val) % 10 == 3 or int(test_val) % 10 == 7)

def is_generalized_heptagonal_pentagonal(x):
    """Check if a number is both heptagonal and pentagonal."""
    return is_pentagonal(x) and is_heptagonal(x)

# Test
num = 70  # Just a sample number, you can replace with any integer
if is_generalized_heptagonal_pentagonal(num):
    print(f"{num} is a generalized heptagonal pentagonal number!")
else:
    print(f"{num} is NOT a generalized heptagonal pentagonal number!")


# ### 416. Calculate the Volume of a Frustum of a Regular Icosahedron with Custom Height and Base Length with Variable Base and Custom Volume Calculation with Custom Units
# This is a challenging and intricate problem. Let's tackle it step by step.
# 
# Steps:
# 1. Volume of a Regular Icosahedron
# 2. Volume of a Frustum of a Regular Icosahedron:
# 3. Determining Edge Lengths

# In[8]:


import math

def volume_of_icosahedron(a):
    """Calculate the volume of a regular icosahedron with edge length a."""
    return (5 * (3 + math.sqrt(5))) * a**3 / 12

def volume_of_frustum(base_length, height, units="cubic units"):
    """Calculate the volume of a frustum of a regular icosahedron."""
    
    # Calculate the volume of the original icosahedron
    V_original = volume_of_icosahedron(base_length)
    
    # Using similar triangles, determine the edge length of the smaller icosahedron
    height_of_original_icosahedron = (base_length * (1 + math.sqrt(5))) / (2 * math.sqrt(3))
    smaller_edge_length = (height / height_of_original_icosahedron) * base_length
    
    # Calculate the volume of the smaller icosahedron
    V_smaller = volume_of_icosahedron(smaller_edge_length)
    
    # The volume of the frustum is the difference between the volumes of the original and smaller icosahedron
    V_frustum = V_original - V_smaller
    
    return f"The volume of the frustum is {V_frustum:.2f} {units}"

# Test
base_length = 2  # Change to your desired base length
height = 1       # Change to your desired height of the frustum
print(volume_of_frustum(base_length, height))


# ### 417. Implement Heap Sort Algorithm on a Max Heap with Custom Comparison Function and Custom Data Structure
# Below is a step-by-step implementation of the heap sort algorithm using a max heap along with a custom comparison function and data structure.
# 
# Steps:
# 
# 1. Heapify: A utility function to ensure the subtree rooted at a given index is a max heap. If not, rearrange to make it one.
# 2. Build Max Heap: Convert the array into a max heap.
# 3. Heap Sort: Repeatedly extract the maximum element from the heap and reduce its size.

# In[9]:


class MaxHeap:
    def __init__(self, data=[]):
        self.heap = data
        self.n = len(data)
        self.build_max_heap()
    
    def left(self, i):
        return 2*i + 1
    
    def right(self, i):
        return 2*i + 2
    
    def max_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        
        # Using custom comparison function
        largest = i
        if l < self.n and self.custom_compare(self.heap[l], self.heap[i]) > 0:
            largest = l
        if r < self.n and self.custom_compare(self.heap[r], self.heap[largest]) > 0:
            largest = r
            
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.max_heapify(largest)
    
    def build_max_heap(self):
        for i in range(self.n // 2, -1, -1):
            self.max_heapify(i)
    
    def custom_compare(self, a, b):
        # For now, just comparing the two values. Modify for custom comparison logic.
        if a > b:
            return 1
        elif a < b:
            return -1
        return 0

def heap_sort(arr):
    heap = MaxHeap(arr)
    sorted_array = []
    for _ in range(len(arr)):
        arr[0], arr[heap.n - 1] = arr[heap.n - 1], arr[0]
        sorted_array.append(heap.heap.pop())
        heap.n -= 1
        heap.max_heapify(0)
    return sorted_array

# Test
arr = [12, 11, 13, 5, 6, 7]
sorted_arr = heap_sort(arr)
print("Sorted array:", sorted_arr)


# ### 418. Find the Partitions of a Specific Integer with Custom Partition Scheme, Variable Size, Custom Position, and Custom Border
# Let's break down the problem:
# 
# 1. Specific Integer: This refers to the integer that needs to be partitioned.
# 2. Custom Partition Scheme: This could mean several things, but let's assume it refers to specifying whether we want to partition the number into 2 parts, 3 parts, etc.
# 3. Variable Size: This could mean the sizes of each partition. Let's interpret it as the maximum size any partition can be.
# 4. Custom Position: This could be interpreted as the starting point in the partition. However, without more clarity, it's a bit hard to make this actionable in the context of partitioning an integer. We'll need to make assumptions here.
# 5. Custom Border: This seems more visual, maybe indicating that we want to represent the partitions visually. However, it's hard to determine exactly what this means in the context of number partitioning. For simplicity, we'll assume it means that each partition should be separated by a specific character.
# 

# In[10]:


def integer_partitions(n, num_parts, max_size=None, border_char="-"):
    # Recursive function to generate partitions
    def partition_helper(num, parts, max_size):
        if num == 0 and len(parts) == num_parts:
            all_partitions.append(parts)
            return
        if len(parts) >= num_parts:
            return
        
        start = 1 if not parts else parts[-1]
        end = num
        
        if max_size:
            start = min(start, max_size)
            end = min(end, max_size)

        for i in range(start, end + 1):
            partition_helper(num - i, parts + [i], max_size)
    
    all_partitions = []
    partition_helper(n, [], max_size)
    return all_partitions

# Parameters
n = 10  # Specific Integer
num_parts = 3  # Partition into 3 parts
max_size = 4  # Each partition can be of maximum size 4
border_char = "-"  # Separate partitions with this character

# Find partitions
partitions = integer_partitions(n, num_parts, max_size)
for partition in partitions:
    print(border_char.join(map(str, partition)))

# Expected Output (can vary based on interpretations)
# 1-1-8
# 1-2-7
# 1-3-6
# 1-4-5
# 2-1-7
# ... and so on


# ### 419. Calculate the Perimeter of a Reuleaux Ellipse with Rounded Corners, Custom Size, Right Alignment, Custom Major and Minor Axes Length, Variable Base, Custom Position, and Custom Border
# Calculating the perimeter of a Reuleaux Ellipse isn't straightforward, as the term "Reuleaux Ellipse" isn't standard. A Reuleaux triangle, for example, is constructed using arcs that connect the vertices of an equilateral triangle. It has a constant width but isn't a circle. If by "Reuleaux Ellipse", you mean an ellipse that's been modified similarly, we'll have to make some assumptions.
# 
# Let's break this down:
# 
# 1. Reuleaux Ellipse: I'll assume this to be an ellipse where each quarter is replaced with a segment of a circle with the radius equal to the width of the ellipse at that quarter (so it'd be like smoothing out the ellipse at its four ends). If that's not your intended shape, then please provide a clearer definition.
# 2. Custom Major and Minor Axes Length: Let's use a and b respectively.
# 3. Rounded Corners: The Reuleaux shape will inherently have rounded corners (as described in the assumption above).
# 4. Right Alignment, Custom Position, and Custom Border: These seem more related to the display or positioning of the shape on a screen or canvas rather than its mathematical properties. For simplicity, I'll only calculate the perimeter here.

# In[11]:


import math

def reuleaux_ellipse_perimeter(a, b):
    """
    Calculates the perimeter of a Reuleaux Ellipse given major and minor axes length.

    Parameters:
    - a: major axis length
    - b: minor axis length

    Returns:
    - Perimeter of the Reuleaux Ellipse
    """
    
    # Width of the ellipse in the horizontal direction
    width_horizontal = 2 * a

    # Width of the ellipse in the vertical direction
    width_vertical = 2 * b

    # Arc length for horizontal segments (2 segments)
    arc_length_horizontal = (math.pi * width_horizontal) / 2

    # Arc length for vertical segments (2 segments)
    arc_length_vertical = (math.pi * width_vertical) / 2

    # Total perimeter is sum of all arcs
    perimeter = arc_length_horizontal + arc_length_vertical

    return perimeter

# Test
a = 5  # Example major axis length
b = 3  # Example minor axis length

perimeter = reuleaux_ellipse_perimeter(a, b)
print(f"The perimeter of the Reuleaux Ellipse with major axis {a} and minor axis {b} is: {perimeter:.2f}")



# ### 420. Print the Pattern of a Hollow Sierpinski Triangle Star with Custom Size, Depth, Right Alignment, Variable Triangle Width, and Custom Position
# The Sierpinski Triangle is a fractal pattern, where a triangle is recursively subdivided into smaller triangles. Here, I'll make an ASCII representation of a hollow Sierpinski Triangle with the given parameters.
# 
# Parameters:
# 
# 1. size: Height of the entire triangle.
# 2. depth: The recursion depth. For depth = 0, it's just a solid triangle. For depth = 1, there's one smaller triangle cut out from the center, and so on.
# 3. triangle_width: Width of the triangle at each depth level.
# 4. position: A tuple (x, y) representing the top-left position of the triangle in the output grid.
# The pattern will be right-aligned by default.

# In[12]:


def draw_triangle(grid, x, y, size, triangle_width):
    """Draws a triangle on the given grid starting at (x, y)."""
    for i in range(size):
        for j in range(triangle_width * i, triangle_width * (i + 1)):
            grid[y + i][x + j] = "*"

def sierpinski(grid, x, y, size, depth, triangle_width):
    """Recursive function to draw the Sierpinski triangle."""
    h = size
    if depth == 0:
        draw_triangle(grid, x, y, size, triangle_width)
        return

    sierpinski(grid, x, y, h // 2, depth - 1, triangle_width)
    sierpinski(grid, x + triangle_width * h // 2, y, h // 2, depth - 1, triangle_width)
    sierpinski(grid, x + triangle_width * h // 4, y + h // 2, h // 2, depth - 1, triangle_width)

def print_sierpinski(size, depth, triangle_width, position):
    """Main function to print the Sierpinski triangle."""
    # Create an empty grid
    grid = [[" " for _ in range(position[0] + triangle_width * size)] for _ in range(position[1] + size)]
    sierpinski(grid, position[0], position[1], size, depth, triangle_width)

    # Print the grid
    for row in grid:
        print("".join(row))

# Test
size = 27  # for clear visualization, better to use sizes like 3, 9, 27, 81, ...
depth = 2
triangle_width = 2
position = (5, 2)
print_sierpinski(size, depth, triangle_width, position)


# In[ ]:




