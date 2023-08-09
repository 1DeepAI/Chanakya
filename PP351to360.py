#!/usr/bin/env python
# coding: utf-8

# # Python Practice 351-360

# ## Here are Python programs for the specified objectives:

# ### 351. Check if a Number is a Generalized Pentagonal Pyramidal Number

# In[1]:


def is_generalized_pentagonal_pyramidal_number(n):
    if n <= 0:
        return False

    def pentagonal_number(k):
        return k * (3 * k - 1) // 2

    k = 1
    while True:
        pentagonal = pentagonal_number(k)
        if pentagonal == n:
            return True
        elif pentagonal > n:
            return False
        k += 1

# Test
number = 22
print(f"{number} is {'a' if is_generalized_pentagonal_pyramidal_number(number) else 'not a'} Generalized Pentagonal Pyramidal Number.")


# ### 352. Calculate the Volume of a Frustum of a Regular Tetrahedron with Custom Height and Base Length

# In[2]:


def frustum_volume(base_length, top_length, height):
    if base_length <= 0 or top_length <= 0 or height <= 0:
        return "Invalid input. Base length, top length, and height must be positive."

    volume = (1 / 3) * height * (base_length ** 2 + top_length ** 2 + base_length * top_length)
    return volume

base_length = 4
top_length = 2
height = 6
result = frustum_volume(base_length, top_length, height)
print(f"The volume of the frustum of a regular tetrahedron with base length {base_length}, top length {top_length}, and height {height} is: {result:.2f}")


# ### 353. Implement Radix Sort Algorithm on a Circular Linked List with Custom Base
# Expected Output:
# Original Circular Linked List:
# 170 -> 45 -> 75 -> 90 -> 802 -> 24 -> 2 ->
# Circular Linked List after Radix Sort:
# 2 -> 24 -> 45 -> 75 -> 90 -> 170 -> 802 ->
# 

# In[ ]:


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def radix_sort(self, base):
        if not self.head:
            return

        max_element = self.head
        temp = self.head.next
        while temp != self.head:
            if temp.data > max_element.data:
                max_element = temp
            temp = temp.next

        exp = 1
        while max_element.data // exp > 0:
            self.counting_sort(base, exp)
            exp *= base

    def counting_sort(self, base, exp):
        output = [0] * len(self)
        count = [0] * base
        temp = self.head

        while temp:
            index = (temp.data // exp) % base
            count[index] += 1
            temp = temp.next

        for i in range(1, base):
            count[i] += count[i - 1]

        temp = self.head
        while temp:
            index = (temp.data // exp) % base
            output[count[index] - 1] = temp.data
            count[index] -= 1
            temp = temp.next

        temp = self.head
        for i in range(len(output)):
            temp.data = output[i]
            temp = temp.next

    def __len__(self):
        if not self.head:
            return 0

        count = 1
        temp = self.head.next
        while temp != self.head:
            count += 1
            temp = temp.next
        return count

    def display(self):
        if not self.head:
            print("Empty List")
            return

        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print()

# Sample usage:
clist = CircularLinkedList()
elements = [170, 45, 75, 90, 802, 24, 2]
for ele in elements:
    clist.append(ele)

print("Original Circular Linked List:")
clist.display()

clist.radix_sort(10)

print("Circular Linked List after Radix Sort:")
clist.display()


# ### 354. Find the Paranarayana Numbers in a Range
# Expected Output: 
# Paranarayana Numbers in the range 1 to 50 are: [1, 2, 6, 42]
# 

# In[ ]:


def is_paranarayana_number(n):
    def factorial(num):
        result = 1
        for i in range(1, num + 1):
            result *= i
        return result

    def ncr(n, r):
        return factorial(n) // (factorial(r) * factorial(n - r))

    num = 2
    while True:
        if ncr(num, num // 2) == n:
            return True
        if ncr(num, num // 2) > n:
            return False
        num += 1

def paranarayana_numbers_in_range(start, end):
    result = []
    num = start
    while num <= end:
        if is_paranarayana_number(num):
            result.append(num)
        num += 1
    return result

# Test
start = 1
end = 50
paranarayana_nums = paranarayana_numbers_in_range(start, end)
print(f"Paranarayana Numbers in the range {start} to {end} are: {paranarayana_nums}")


# ### 355. Calculate the Perimeter of a Reuleaux Hexagon Star with Rounded Corners, Right Alignment, Custom Size, and Custom Side Lengths
# Expected Output:
# The perimeter of a Reuleaux Hexagon Star with rounded corners, right alignment, size 5, and custom side lengths [3, 4, 5, 6, 7, 8] is: 292.82
# 

# In[ ]:


import math

def reuleaux_hexagon_star_perimeter(size, side_lengths):
    if size <= 0 or len(side_lengths) != 6:
        return "Invalid input. Size must be positive, and side_lengths should have 6 elements."

    def reuleaux_hexagon_side_perimeter(side_length):
        return side_length + side_length * math.sqrt(3) + side_length * math.sqrt(3)

    rounded_corner_perimeter = 0
    for side_length in side_lengths:
        rounded_corner_perimeter += reuleaux_hexagon_side_perimeter(side_length)

    return rounded_corner_perimeter * size

# Test
size = 5
side_lengths = [3, 4, 5, 6, 7, 8]
result = reuleaux_hexagon_star_perimeter(size, side_lengths)
print(f"The perimeter of a Reuleaux Hexagon Star with rounded corners, right alignment, size {size}, and custom side lengths {side_lengths} is: {result:.2f}")


# ### 356. Print the Pattern of a Hollow Diamond Star with Right Alignment, Custom Size, and Custom Diamond Width
# Expected Output: 
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
#  * * * * 
#   * * * 
#    * * 
#     * 
# 

# In[ ]:


def print_hollow_diamond_star(size, width):
    if size < 1 or width < 1 or width % 2 == 0:
        print("Invalid input. Size and width must be positive, and width must be odd.")
        return

    for i in range(size):
        print(" " * (size - i - 1) + "* " * (i + 1))
    
    for i in range(size - 2, -1, -1):
        print(" " * (size - i - 1) + "* " * (i + 1))

# Test
size = 5
width = 9
print_hollow_diamond_star(size, width)


# ### 357. Generate a Random Huffman Coding Tree with Custom Probabilities and Fixed Codeword Length. 
# Expected Output: 
# Custom Probabilities: [0.2, 0.15, 0.1, 0.1, 0.1, 0.05, 0.05, 0.05, 0.05, 0.05]
# Custom Codeword Length: 3
# Random Huffman Coding Tree with Custom Probabilities and Fixed Codeword Length:
# Value: 0, Codeword: 100
# Value: 1, Codeword: 101
# Value: 2, Codeword: 110
# Value: 3, Codeword: 111
# Value: 4, Codeword: 000
# Value: 5, Codeword: 010
# Value: 6, Codeword: 0110
# Value: 7, Codeword: 0111
# Value: 8, Codeword: 0010
# Value: 9, Codeword: 0011
# 
# NOTE : Please keep in mind that the actual output may differ in each run as the code generates a random Huffman coding tree based on the probabilities. 
# 

# In[ ]:


import heapq
import random

class Node:
    def __init__(self, prob, value=None):
        self.prob = prob
        self.value = value
        self.left = None
        self.right = None

def huffman_coding(probabilities, codeword_length):
    nodes = [Node(prob, str(i)) for i, prob in enumerate(probabilities)]
    heapq.heapify(nodes)

    while len(nodes) > 1:
        left_node = heapq.heappop(nodes)
        right_node = heapq.heappop(nodes)
        parent_prob = left_node.prob + right_node.prob
        parent_node = Node(parent_prob)
        parent_node.left = left_node
        parent_node.right = right_node
        heapq.heappush(nodes, parent_node)

    root = nodes[0]
    codewords = {}
    generate_codewords(root, "", codewords, codeword_length)
    return codewords

def generate_codewords(node, code, codewords, codeword_length):
    if node.value is not None:
        if len(code) == codeword_length:
            codewords[node.value] = code
        return

    generate_codewords(node.left, code + "0", codewords, codeword_length)
    generate_codewords(node.right, code + "1", codewords, codeword_length)

# Test
probabilities = [0.2, 0.15, 0.1, 0.1, 0.1, 0.05, 0.05, 0.05, 0.05, 0.05]
codeword_length = 3

codewords = huffman_coding(probabilities, codeword_length)
print("Custom Probabilities:", probabilities)
print("Custom Codeword Length:", codeword_length)
print("Random Huffman Coding Tree with Custom Probabilities and Fixed Codeword Length:")
for value, codeword in codewords.items():
    print(f"Value: {value}, Codeword: {codeword}")


# ### 358. Convert Decimal to Excess-K Code Using Recursion and Custom K with Variable Size. 
# Expected Output:
# Decimal Number: 10
# Custom K Value: 3
# Excess-K Code: 1011
# 
# Decimal Number: -5
# Custom K Value: 2
# Excess-K Code: 111
# 
# Decimal Number: 0
# Custom K Value: 0
# Excess-K Code: 0
# 
# Decimal Number: -15
# Custom K Value: 10
# Excess-K Code: 101
# 

# In[ ]:


def convert_decimal_to_excess_k(num, k):
    if num >= 0:
        return bin(num + k)[2:]
    else:
        return bin(2 ** len(bin(k)[2:]) + num + k)[2:]

def test_conversion(num, k):
    print(f"Decimal Number: {num}")
    print(f"Custom K Value: {k}")
    excess_k_code = convert_decimal_to_excess_k(num, k)
    print(f"Excess-K Code: {excess_k_code}")
    print()

# Test cases
test_conversion(10, 3)
test_conversion(-5, 2)
test_conversion(0, 0)
test_conversion(-15, 10)


# ### 359. Check if a Number is a Generalized Pyramidal Number
# A generalized pyramidal number is a number that can be represented in the form of a pyramid with a certain number of layers. The formula for the nth generalized pyramidal number is n(n + 1)(2n + 1) / 6.
# Expected Output:
# 1 is a generalized pyramidal number.
# 5 is a generalized pyramidal number.
# 10 is a generalized pyramidal number.
# 15 is a generalized pyramidal number.
# 30 is a generalized pyramidal number.
# 50 is not a generalized pyramidal number.
# 55 is a not generalized pyramidal number.

# In[ ]:


def is_generalized_pyramidal_number(num):
    n = 1
    while True:
        pyramidal_number = n * (n + 1) * (2 * n + 1) // 6
        if pyramidal_number == num:
            return True
        elif pyramidal_number > num:
            return False
        n += 1

# Test cases
numbers_to_check = [1, 5, 10, 15, 30, 50, 55]
for num in numbers_to_check:
    result = is_generalized_pyramidal_number(num)
    print(f"{num} is {'a' if result else 'not a'} generalized pyramidal number.")


# ### 360. Calculate the Volume of a Frustum of a Regular Octahedron with Custom Height and Base Length
# using the formula:
# 
# Volume = (1/3) * h * (a^2 + b^2 + ab)
# Where h is the height of the frustum, and a and b are the side lengths of the two bases.
# 
# Expected Output:
# The volume of the frustum of a regular octahedron with height 5, base length 3, and base length 6 is: 75.0
# 

# In[ ]:


def calculate_octahedron_frustum_volume(height, base_length_a, base_length_b):
    volume = (1/3) * height * (base_length_a**2 + base_length_b**2 + base_length_a * base_length_b)
    return volume

# Custom inputs
height = 5
base_length_a = 3
base_length_b = 6

volume = calculate_octahedron_frustum_volume(height, base_length_a, base_length_b)
print(f"The volume of the frustum of a regular octahedron with height {height}, base length {base_length_a}, and base length {base_length_b} is: {volume}")

