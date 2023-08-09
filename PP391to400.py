#!/usr/bin/env python
# coding: utf-8

# # Python Practice 391-400

# ## Here are Python Codes for Practice

# ### 391. Check if a Number is a Generalized Hexagonal Pentagonal Number
# A generalized hexagonal pentagonal number would be a number that is both hexagonal and pentagonal.

# In[2]:


def is_int(n):
    return int(n) == n

def is_pentagonal(x):
    n = (1 + (1 + 24 * x)**0.5) / 6
    return is_int(n)

def is_hexagonal(x):
    n = (1 + (1 + 8 * x)**0.5) / 4
    return is_int(n)

def is_hexagonal_pentagonal(x):
    return is_hexagonal(x) and is_pentagonal(x)

# Testing the function
number = 153
if is_hexagonal_pentagonal(number):
    print(f"{number} is a generalized hexagonal pentagonal number.")
else:
    print(f"{number} is NOT a generalized hexagonal pentagonal number.")


# ### 392. Calculate the Volume of a Frustum of a Regular Icosahedron with Custom Height and Base Length with Variable Base
# let's break down the problem.
# 
# A frustum is a portion of a solid that lies between two parallel planes cutting the solid, especially the portion of a right circular cone between the base and a plane parallel to the base.
# 
# However, for an icosahedron (which is not a shape that naturally produces a frustum like a cone or a pyramid does), the "frustum" would be an irregular shape, and calculating its volume isn't straightforward.
# 
# To simplify the problem, let's make some assumptions:
# 
# Our "frustum" is formed by cutting off the top of a regular icosahedron such that the cut produces a flat surface.
# The base length referred to is the side length of the original icosahedron.
# The height is the perpendicular distance from the original base to the cut surface.
# Given these assumptions, the volume of the frustum can be calculated as the difference between the volume of the original icosahedron and the volume of the smaller icosahedron (the portion we've "cut off").
# 
# 
# 

# In[3]:


def volume_of_icosahedron(a):
    """Return the volume of a regular icosahedron with side length a."""
    return (5 * (3 + 5**0.5) / 12) * a**3

def frustum_volume(a, height, original_height):
    """Calculate the volume of the frustum of a regular icosahedron."""
    # First, get the side length of the smaller icosahedron using similar triangles
    smaller_a = a * (original_height - height) / original_height
    
    # Then, calculate the volume difference
    return volume_of_icosahedron(a) - volume_of_icosahedron(smaller_a)

# Example
a = 2  # side length of the original icosahedron
original_height = 3.5  # assuming an original height
height = 2  # height after cutting off the top

volume = frustum_volume(a, height, original_height)
print(f"Volume of the frustum: {volume:.2f}")


# ### 393. Implement Quick Sort Algorithm on a Doubly Linked List with Custom Pivot, Partition Scheme, Right Alignment, and Variable Size
# Let's implement a quicksort algorithm for a doubly linked list:
# 
# Create a doubly linked list structure with Node class.
# Implement the quicksort algorithm, which will include a function to partition the linked list and a function to pick a pivot (in our case, we'll use the rightmost element as the pivot, based on your "right alignment" instruction).
# Write a function to print the sorted doubly linked list.

# In[5]:


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def partition(start, end):
    if start == end:
        return start

    pivot = end.data
    i = start.prev

    j = start
    while j != end:
        if j.data <= pivot:
            # Similar to i++
            if i is None:
                i = start
            else:
                i = i.next
            i.data, j.data = j.data, i.data
        j = j.next

    if i is None:
        i = start
    else:
        i = i.next
    i.data, end.data = end.data, i.data

    return i

def _quickSort(start, end):
    if not start or not end or start == end or start == end.next:
        return

    pi = partition(start, end)
    if pi and pi.prev:
        _quickSort(start, pi.prev)
    if pi and pi.next:
        _quickSort(pi.next, end)

def quickSort(node):
    start = node
    end = None
    while node:
        end = node
        node = node.next
    _quickSort(start, end)

def printList(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()

# Example
node1 = Node(4)
node2 = Node(2)
node3 = Node(5)
node4 = Node(3)
node5 = Node(1)
node6 = Node(8)
node7 = Node(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

node2.prev = node1
node3.prev = node2
node4.prev = node3
node5.prev = node4
node6.prev = node5
node7.prev = node6

print("Original List:")
printList(node1)

quickSort(node1)

print("\nSorted List:")
printList(node1)


# ### 394. Find the Partitions of a Specific Integer with Custom Partition Scheme
# First, let's clarify what we mean by "partitions of a specific integer with custom partition scheme".
# 
# Let's say the integer is n. A partition of n is a way of writing n as a sum of positive integers. For example, for n = 4, one of its partitions could be 3 + 1.
# 
# A "custom partition scheme" might involve constraints like:
# 
# Use only odd numbers.
# Use numbers from a specific list.
# Do not use any number more than once.
# For this example, let's assume that the custom scheme is to partition the integer using only odd numbers.

# In[6]:


def partitions(n, I=1):
    yield (n,)
    for i in range(I, n//2 + 1, 2):  # ensuring we only use odd numbers by incrementing by 2
        for p in partitions(n-i, i):
            yield (i,) + p

n = 7
print(f"Partitions of {n} using only odd numbers:")
for partition in partitions(n):
    print(' + '.join(map(str, partition)))


# ### 395. Calculate the Perimeter of a Reuleaux Ellipse with Rounded Corners, Custom Size, Right Alignment, Custom Major and Minor Axes Length, and Variable Base
# First, let's discuss the concept of a "Reuleaux Ellipse". The term "Reuleaux" is usually associated with a curve of constant width derived from a triangle, known as the Reuleaux triangle. This triangle is essentially a triangle with rounded corners where each side's arc is a portion of a circle with the triangle's vertices as centers.
# 
# However, an "ellipse" is a different shape, characterized by its major and minor axes. I'm assuming by "Reuleaux Ellipse," you're referring to an ellipse with rounded corners. If that's not the case, please provide more clarity.

# In[7]:


import math

def ellipse_perimeter(a, b):
    # Ellipse perimeter approximation
    h = ((a-b)/(a+b))**2
    return math.pi * (a+b) * (1 + (3/8)*h)

def reuleaux_ellipse_perimeter(a, b, r):
    # Standard ellipse perimeter
    P = ellipse_perimeter(a, b)
    
    # Adjustment for the rounded corners (assuming quarter circles)
    delta_P = 4 * r * (math.pi - 2)
    
    return P + delta_P

a = 5  # Major axis
b = 3  # Minor axis
r = 0.5  # Radius of the rounded corners

print(f"Perimeter of the Reuleaux Ellipse: {reuleaux_ellipse_perimeter(a, b, r)} units")


# ### 396. Print the Pattern of a Hollow Sierpinski Triangle Star with Custom Size, Depth, Right Alignment, and Variable Triangle Width
# The Sierpinski triangle is a fractal that's made by recursively removing equilateral triangles from larger equilateral triangles. When we refer to the "hollow" Sierpinski triangle, it means we're showing the pattern of removed triangles, and only the boundaries of the larger triangles remain.
# 
# Let's make a function that can print the Sierpinski triangle pattern given a custom size, depth, and alignment. This code will handle:
# 
# 1. Custom size: The overall triangle's side length.
# 2. Depth: The recursive depth to which the Sierpinski triangle is drawn.
# 3. Right alignment: The entire pattern will be right aligned.
# 4. Variable triangle width: The width of the triangle on each level of recursion.
# For the sake of simplicity, let's represent our triangle as a 2D list of characters where a * denotes a star and a space denotes an empty spot.

# In[10]:


def draw_triangle(matrix, top_x, top_y, size):
    """Draws a triangle onto the matrix with the top vertex at (top_x, top_y)."""
    for i in range(size):
        matrix[top_y + i][top_x - i] = '*'
        matrix[top_y + i][top_x + i] = '*'
        if i == size - 1:
            for j in range(top_x - i + 1, top_x + i):
                matrix[top_y + i][j] = '*'

def sierpinski(matrix, top_x, top_y, size, depth):
    """Recursively draws the Sierpinski triangle pattern."""
    if depth <= 0:
        return
    if depth == 1:
        draw_triangle(matrix, top_x, top_y, size)
    else:
        h = size // 2
        sierpinski(matrix, top_x, top_y, h, depth - 1)  # top
        sierpinski(matrix, top_x - h // 2, top_y + h, h, depth - 1)  # bottom left
        sierpinski(matrix, top_x + h // 2, top_y + h, h, depth - 1)  # bottom right

def print_sierpinski(size, depth):
    """Generates the matrix representing the pattern and prints it."""
    matrix = [[' ' for _ in range(size * 2)] for _ in range(size)]
    sierpinski(matrix, size - 1, 0, size, depth)
    for row in matrix:
        print(''.join(row).rstrip())

# Test
print_sierpinski(16, 2)


# ### 397. Generate a Random Huffman Coding Tree with Custom Probabilities, Codeword Lengths, Fixed Codeword Size, Custom Prefix Length, and Custom Node Weights
# Let's break this down step by step:
# 
# 1. Random Huffman Coding Tree with Custom Probabilities: Huffman coding is usually based on the probabilities (or frequencies) of different symbols. If you give custom probabilities, we can use them to create the Huffman Tree.
# 2. Codeword Lengths: Once the Huffman tree is constructed, the codeword length for each symbol is essentially the depth of that symbol's leaf in the tree. However, for "custom" codeword lengths, you'd need to ensure the lengths provided can actually form a valid Huffman tree.
# 3. Fixed Codeword Size: Huffman codes are variable-length by nature. If you want fixed-size codes, you'd typically look at other encoding methods, but it can be done by padding shorter codes.
# 4. Custom Prefix Length and Node Weights: These are non-standard additions to the Huffman process, but we can incorporate them.

# In[12]:


import heapq
from collections import defaultdict, namedtuple

# Node structure for Huffman Tree
Node = namedtuple("Node", ["weight", "char", "left", "right"])

def create_huffman_tree(probabilities):
    # Initial heap of nodes
    heap = [Node(weight=prob, char=char, left=None, right=None) for char, prob in probabilities.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        # Pop the two nodes with the smallest weights
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        # Merge them into a new node
        merged = Node(weight=left.weight + right.weight, char=None, left=left, right=right)
        heapq.heappush(heap, merged)
        
    return heap[0]

def traverse_tree(tree, prefix="", code={}):
    if tree.char is not None:
        code[tree.char] = prefix
    else:
        traverse_tree(tree.left, prefix + "0", code)
        traverse_tree(tree.right, prefix + "1", code)
    return code

# Custom probabilities
probabilities = {"a": 0.4, "b": 0.3, "c": 0.2, "d": 0.1}

# Construct Huffman Tree
huffman_tree = create_huffman_tree(probabilities)

# Generate codewords
codes = traverse_tree(huffman_tree)
print("Generated Huffman Codes:", codes)

# To get fixed codeword size, you can pad the shorter codes:
max_len = max(map(len, codes.values()))
fixed_codes = {k: v.rjust(max_len, "0") for k, v in codes.items()}
print("Fixed Size Huffman Codes:", fixed_codes)


# ### 398. Convert Decimal to Gray Code Using Recursive Approach and Custom Bit Size with Variable Base and Custom Encoding Scheme
# Gray code is a binary numeral system where two successive numbers differ in only one bit.
# 
# The formula to convert a binary number b to its Gray code 
# g is:..(1)
# Let's break down the requirements:
# 
# 1. Convert Decimal to Gray Code: This can be achieved using the formula above.
# 2. Recursive Approach: We can use a recursive function to generate Gray codes of a certain length.
# 3. Custom Bit Size: The number of bits in the output Gray code.
# 4. Variable Base: This seems to indicate a non-binary base, which is interesting since standard Gray code is binary.
# 5. Custom Encoding Scheme: This is ambiguous without more information. For the sake of simplicity, I'll assume that after converting to Gray code, you might want to replace '0' and '1' with other characters, e.g., '+' and '-'.
# 
# - First, generate the gray codes with binary representation.
# - Convert the binary representation to the desired base.
# - Lastly, apply the custom encoding.

# In[15]:


def decimal_to_gray(n):
    """Convert decimal number to Gray code"""
    return n ^ (n >> 1)

def binary_to_baseN(value, base):
    """Convert a binary number to a given base"""
    result = 0
    multiplier = 1
    while value:
        result += (value % base) * multiplier
        multiplier *= 10
        value //= base
    return result

def gray_code_recursive(n, base=2, encoding={"0": "0", "1": "1"}):
    """Generate Gray code recursively for custom bit size n"""
    if n == 0:
        return ['0' * base]
    
    # First, we recursively generate the smaller Gray code in binary
    smaller_gray = gray_code_recursive(n-1, 2)

    # First half of the Gray code list
    first_half = ['0' + code for code in smaller_gray]
    
    # Second half (mirror of the first half)
    second_half = ['1' + code for code in reversed(smaller_gray)]
    
    # Combine both
    gray_codes_binary = first_half + second_half

    # Convert binary gray codes to the desired base
    gray_codes_baseN = [str(binary_to_baseN(decimal_to_gray(int(code, 2)), base)).rjust(n, '0') for code in gray_codes_binary]

    # Apply custom encoding
    gray_codes = [''.join([encoding[char] for char in code]) for code in gray_codes_baseN]

    return gray_codes

# Test
bit_size = 3
base = 3
encoding = {"0": "A", "1": "B", "2": "C"}

gray_codes = gray_code_recursive(bit_size, base, encoding)
print(gray_codes)


# ### 399. Check if a Number is a Generalized Heptagonal Hexagonal Number
# Firstly, let's clarify the mathematical definitions of the numbers:
# 1. Heptagonal Number:
# 2. Hexagonal Number: 
# For a number to be a generalized heptagonal hexagonal number, it needs to be both a heptagonal number and a hexagonal number.
# Here's a corrected approach:
# 
# 1. Given a number y, if it satisfies the conditions to be both hexagonal and heptagonal, we will determine it as a generalized heptagonal hexagonal number.
# 2. We'll use the quadratic formula to determine if a value of n makes the number y hexagonal and heptagonal.

# In[18]:


def is_integer(value):
    """Check if a value is close to an integer."""
    return abs(value - round(value)) < 1e-10

def is_heptagonal(y):
    """Check if a number y is heptagonal."""
    # Using the quadratic formula to solve: 5n^2 - 3n - 2y = 0
    discriminant = 9 + 40 * y
    if discriminant < 0:
        return False
    n1 = (3 + discriminant**0.5) / 10
    n2 = (3 - discriminant**0.5) / 10
    return is_integer(n1) or is_integer(n2)

def is_hexagonal(y):
    """Check if a number y is hexagonal."""
    # Using the quadratic formula to solve: 2n^2 - n - y = 0
    discriminant = 1 + 8 * y
    if discriminant < 0:
        return False
    n1 = (1 + discriminant**0.5) / 4
    n2 = (1 - discriminant**0.5) / 4
    return is_integer(n1) or is_integer(n2)

def is_generalized_heptagonal_hexagonal(y):
    """Check if a number y is both heptagonal and hexagonal."""
    return is_heptagonal(y) and is_hexagonal(y)

# Test
number = 45
if is_generalized_heptagonal_hexagonal(number):
    print(f"{number} is a generalized heptagonal hexagonal number!")
else:
    print(f"{number} is NOT a generalized heptagonal hexagonal number!")


# ### 400. Calculate the Volume of a Frustum of a Regular Dodecahedron with Custom Height and Base Length with Variable Base and Custom Volume Calculation
#  Let's first clarify our problem statement:
# 
# A frustum is the portion of a solid that lies between two parallel planes cutting it, especially the section between the base and a plane parallel to the base.
# 
# The volume of a frustum for a pyramid or cone is:..(1)
#  Let's first clarify our problem statement:
# 
# A frustum is the portion of a solid that lies between two parallel planes cutting it, especially the section between the base and a plane parallel to the base.
# 
# The volume of a frustum for a pyramid or cone is:..(2)
# Given that the height of the frustum is h, and the height of the complete dodecahedron is H, the height of the smaller dodecahedron will be H−h. From here, you can derive the proportionality between the side lengths a and a′using similar triangles.

# In[19]:


import math

def pentagon_area(side_length):
    """Calculate the area of a regular pentagon."""
    return (5 / 4) * math.tan(math.radians(54)) * side_length**2

def dodecahedron_volume(side_length):
    """Calculate the volume of a regular dodecahedron."""
    return (15 + 7*math.sqrt(5)) / 4 * side_length**3

def dodecahedron_height(side_length):
    """Calculate the height of a regular dodecahedron."""
    return side_length * math.sqrt((3 + math.sqrt(5)) / 2)

def frustum_volume(a, h):
    """Calculate the volume of a frustum of a regular dodecahedron."""
    H = dodecahedron_height(a)
    a_prime = a * (H - h) / H

    A1 = pentagon_area(a)
    A2 = pentagon_area(a_prime)
    
    return (h/3) * (A1 + A2 + math.sqrt(A1 * A2))

# Test
side_length = 3  # Example side length for the larger dodecahedron
height = 5       # Example height for the frustum

volume = frustum_volume(side_length, height)
print(f"Volume of the frustum: {volume:.2f} cubic units")

