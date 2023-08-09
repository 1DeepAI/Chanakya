#!/usr/bin/env python
# coding: utf-8

# # Pyhton Practice 341-350

# ## Here are the Python programs for the specified objectives:

# ### 341. Generate a Random Word Cloud from Web Data with Custom Word Frequency, Size, and Color
# Expected Output:
# (The word cloud image with random sizes, colors, and positions of the words will be displayed.) 

# In[1]:


# You can use a web scraping library like BeautifulSoup to extract text data from a web page.
# Since web scraping is not allowed on all websites, the following example uses a sample list of words for demonstration purposes.

import random
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def generate_random_word_cloud(words, word_frequency, custom_size, custom_color):
    wordcloud = WordCloud(width=custom_size[0], height=custom_size[1], background_color=custom_color).generate_from_frequencies(word_frequency)
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()

words = ["python", "programming", "data", "science", "machine", "learning", "AI", "artificial", "intelligence"]
word_frequency = {word: random.randint(5, 20) for word in words}
custom_size = (800, 800)  # Custom size in pixels (width, height)
custom_color = "white"    # Custom background color

generate_random_word_cloud(words, word_frequency, custom_size, custom_color)


# #### Expected Output:
# (The word cloud image with random sizes, colors, and positions of the words will be displayed.) 

# ### 342. Convert Decimal to Roman Numeral Using Recursive Approach and Custom Numerals

# In[2]:


def decimal_to_roman_recursive(decimal_num, numerals):
    if decimal_num == 0:
        return ""

    for value, numeral in numerals:
        if decimal_num >= value:
            return numeral + decimal_to_roman_recursive(decimal_num - value, numerals)

decimal_num = 3999
numerals = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

result = decimal_to_roman_recursive(decimal_num, numerals)
print(f"The Roman Numeral representation of {decimal_num} is: {result}")


# ### 343. Check if a Number is a Generalized Pentagonal Number

# In[3]:


def is_generalized_pentagonal_number(n):
    if n <= 0:
        return False

    k = 1
    while True:
        num1 = k * (3 * k - 1) // 2
        num2 = k * (3 * k + 1) // 2

        if n == num1 or n == num2:
            return True
        elif num1 > n and num2 > n:
            return False

        k += 1

num = 35
result = is_generalized_pentagonal_number(num)
print(f"{num} is {'a' if result else 'not a'} generalized pentagonal number.")


# ### 344. Calculate the Volume of a Frustum of a Regular Dodecahedron with Custom Height

# In[4]:


import math

def volume_of_frustum_of_dodecahedron(edge_length, height):
    if edge_length <= 0 or height <= 0:
        return "Invalid input. Edge length and height must be positive."

    volume = (15 + 7 * math.sqrt(5)) * edge_length ** 2 * height / 4
    return volume

edge_length = 6
height = 10
result = volume_of_frustum_of_dodecahedron(edge_length, height)
print(f"The volume of the frustum of a regular dodecahedron with edge length {edge_length} and height {height} is: {result:.2f}")


# ### 345. Implement Quick Sort Algorithm on a Doubly Linked List with Custom Pivot
# Expected Output: 
# Original Doubly Linked List:
# 170 -> 45 -> 75 -> 90 -> 802 -> 24 -> 2 ->
# Doubly Linked List after Quick Sort:
# 2 -> 24 -> 45 -> 75 -> 90 -> 170 -> 802 ->
# 

# In[5]:


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    def display(self):
        if not self.head:
            return "Doubly Linked List is empty."
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print()

    def quick_sort(self, start, end):
        if start is None or start == end:
            return start

        pivot = self.partition(start, end)

        if pivot != start:
            temp = pivot.prev
            temp.next = None
            pivot.prev = None
            pivot = self.quick_sort(pivot, temp)
            pivot.prev = temp
            temp.next = pivot

        pivot.next = self.quick_sort(pivot.next, end)
        return pivot

    def partition(self, start, end):
        pivot = end
        i = start.prev

        for j in range(start, end):
            if j.data <= pivot.data:
                i = start if i is None else i.next
                i.data, j.data = j.data, i.data

        i = start if i is None else i.next
        i.data, pivot.data = pivot.data, i.data
        return i

# Sample usage:
dlist = DoublyLinkedList()
elements = [170, 45, 75, 90, 802, 24, 2]
for ele in elements:
    dlist.insert(ele)

print("Original Doubly Linked List:")
dlist.display()

dlist.head = dlist.quick_sort(dlist.head, None)

print("Doubly Linked List after Quick Sort:")
dlist.display()


# ### 346. Find the Overlooked Numbers in a Range

# In[6]:


def is_overlooked_number(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

lower_bound = 1
upper_bound = 50
overlooked_numbers = [num for num in range(lower_bound, upper_bound + 1) if is_overlooked_number(num)]
print(f"Overlooked Numbers from {lower_bound} to {upper_bound}: {overlooked_numbers}")


# ### 347. Calculate the Perimeter of a Reuleaux Ellipse with Rounded Corners, Custom Size, and Right Alignment

# In[7]:


import math

def reuleaux_ellipse_perimeter(custom_size, custom_a, custom_b):
    if custom_size <= 0 or custom_a <= 0 or custom_b <= 0:
        return "Invalid input. Size, a, and b must be positive."

    a = custom_a
    b = custom_b
    r = custom_size
    perimeter = 4 * (a + b + math.sqrt((a - b) ** 2 + (a + b) ** 2 + 2 * (a + b) * r - 3 * r ** 2))

    return perimeter

custom_size = 5
custom_a = 8
custom_b = 4
result = reuleaux_ellipse_perimeter(custom_size, custom_a, custom_b)
print(f"The perimeter of the Reuleaux Ellipse with size {custom_size}, a {custom_a}, and b {custom_b} is: {result:.2f}")


# ### 348. Print the Pattern of a Hollow Sierpinski Triangle Star with Custom Size and Depth
# Expected Output:
#     *    
#    * *   
#   *   *  
#  *     * 
# * * * * *
# 

# In[9]:


def print_hollow_sierpinski_triangle_star(custom_size, custom_depth):
    if custom_size <= 0 or custom_depth <= 0:
        return "Invalid input. Size and depth must be positive."

    pattern = []
    for i in range(custom_size):
        if i % (2 ** (custom_depth - 1)) == 0:
            pattern.append("*")
        else:
            pattern.append(" ")

    for depth in range(custom_depth - 1):
        for i in range(len(pattern)):
            if i % (2 ** (custom_depth - depth - 1)) == 0:
                pattern[i] = "*"
            else:
                pattern[i] = " "

        print("".join(pattern).center(2 * custom_size - 1))
        pattern = pattern[:custom_size] + pattern[::-1][1:]

custom_size = 5
custom_depth = 3
print_hollow_sierpinski_triangle_star(custom_size, custom_depth)


# ### 349. Generate a Random Huffman Coding Tree with Fixed Codeword Length and Custom Frequencies
# Expected Output:
# a: 00
# b: 10
# c: 110
# d: 01
# e: 111
# 

# In[10]:


import heapq
import random

class HuffmanNode:
    def __init__(self, character, frequency):
        self.character = character
        self.frequency = frequency
        self.left = None
        self.right = None

def generate_random_huffman_tree(codeword_length, custom_frequencies):
    priority_queue = []
    for character, frequency in custom_frequencies.items():
        node = HuffmanNode(character, frequency)
        heapq.heappush(priority_queue, (frequency, node))

    while len(priority_queue) > 1:
        freq1, node1 = heapq.heappop(priority_queue)
        freq2, node2 = heapq.heappop(priority_queue)

        merged_node = HuffmanNode(None, freq1 + freq2)
        merged_node.left = node1
        merged_node.right = node2

        heapq.heappush(priority_queue, (merged_node.frequency, merged_node))

    root = heapq.heappop(priority_queue)[1]
    return root

# Sample usage:
codeword_length = 3
custom_frequencies = {'a': 10, 'b': 20, 'c': 15, 'd': 30, 'e': 25}
huffman_tree = generate_random_huffman_tree(codeword_length, custom_frequencies)

def print_huffman_tree(node, prefix=""):
    if node:
        if node.character:
            print(f"{node.character}: {prefix}")
        print_huffman_tree(node.left, prefix + "0")
        print_huffman_tree(node.right, prefix + "1")

print_huffman_tree(huffman_tree)


# ### 350. Convert Decimal to Gray Code Using Recursive Approach and Custom Bit Size

# In[11]:


def decimal_to_gray_recursive(decimal_num, bit_size):
    if bit_size == 0:
        return ""
    
    mask = 1 << (bit_size - 1)
    return str((decimal_num & mask != 0) ^ (decimal_num & mask >> 1 != 0)) + decimal_to_gray_recursive(decimal_num, bit_size - 1)

decimal_num = 15
bit_size = 5
result = decimal_to_gray_recursive(decimal_num, bit_size)
print(f"The Gray Code representation of {decimal_num} with {bit_size} bits is: {result}")

