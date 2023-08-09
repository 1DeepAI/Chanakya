#!/usr/bin/env python
# coding: utf-8

# # Python Practice 231-240

# ## Here are Python programs to achieve the objectives

# ### 231. Check if a Number is a Repunit

# In[10]:


def is_repunit(num):
    return '1' * num == str(int('1' * num))

number = 111 # Replace with any number you want to check
result = is_repunit(number)
print(f"{number} is {'a repunit' if result else 'not a repunit'}.")


# ### 232. Calculate the Volume of a Regular Icosahedron

# In[9]:


def calculate_volume_of_icosahedron(edge_length):
    volume = 5 * (3 + 5 ** 0.5) * edge_length ** 3 / 12
    return volume

edge_length = 5 # Replace with the desired edge length of the icosahedron
volume = calculate_volume_of_icosahedron(edge_length)
print(f"Volume of the icosahedron with edge length {edge_length} is: {volume:.2f}")


# ### 233. Implement Skip List Data Structure with Variable Levels

# In[8]:


import random

class SkipListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.forward = []

class SkipList:
    def __init__(self):
        self.head = SkipListNode()
        self.levels = 1

    def random_level(self):
        level = 1
        while random.random() < 0.5 and level < self.levels + 1:
            level += 1
        return level

    def insert(self, key, value):
        new_node = SkipListNode(key, value)
        level = self.random_level()
        new_node.forward = [None] * level

        current = self.head
        for i in range(level - 1, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            new_node.forward[i] = current.forward[i]
            current.forward[i] = new_node

        if level > self.levels:
            self.levels = level

    def search(self, key):
        current = self.head
        for i in range(self.levels - 1, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
        current = current.forward[0]

        if current and current.key == key:
            return current.value
        return None

# Example usage of the Skip List data structure
skip_list = SkipList()
skip_list.insert(10, 'A')
skip_list.insert(20, 'B')
skip_list.insert(15, 'C')

print("Search results:")
print("Key 10:", skip_list.search(10))
print("Key 20:", skip_list.search(20))
print("Key 15:", skip_list.search(15))
print("Key 25:", skip_list.search(25))


# ### 234. Find the Harmful Numbers in a Range

# In[7]:


def sum_of_divisors(num):
    return sum(i for i in range(1, num) if num % i == 0)

def is_harmful_number(num):
    return sum_of_divisors(num) > num

def find_harmful_numbers_in_range(start, end):
    harmful_numbers = [num for num in range(start, end + 1) if is_harmful_number(num)]
    return harmful_numbers

start_range = 1
end_range = 50
harmful_numbers = find_harmful_numbers_in_range(start_range, end_range)
print(f"Harmful numbers in the range [{start_range}, {end_range}]: {harmful_numbers}")


# ### 235. Calculate the Perimeter of a Reuleaux Hexagon Star with Rounded Corners

# In[6]:


import math

def calculate_perimeter_of_reuleaux_hexagon_star(side_length):
    radius = side_length * (3 ** 0.5) / 2
    corner_area = math.pi * radius ** 2
    edge_perimeter = 6 * side_length
    total_perimeter = corner_area + edge_perimeter
    return total_perimeter

side_length = 5 # Replace with the desired side length of the Reuleaux hexagon star
perimeter = calculate_perimeter_of_reuleaux_hexagon_star(side_length)
print(f"Perimeter of the Reuleaux hexagon star with side length {side_length} is: {perimeter:.2f}")


# ### 236. Print the Pattern of a Hollow Diamond Star

# In[5]:


def print_hollow_diamond_star(rows):
    for i in range(1, rows + 1):
        for j in range(rows - i):
            print(" ", end="")
        for j in range(2 * i - 1):
            if j == 0 or j == 2 * i - 2 or i == rows:
                print("*", end="")
            else:
                print(" ", end="")
        print()

    for i in range(rows - 1, 0, -1):
        for j in range(rows - i):
            print(" ", end="")
        for j in range(2 * i - 1):
            if j == 0 or j == 2 * i - 2 or i == rows:
                print("*", end="")
            else:
                print(" ", end="")
        print()

rows = 5 # Replace with the desired number of rows for the hollow diamond star
print("Hollow Diamond Star Pattern:")
print_hollow_diamond_star(rows)


# ### 237. Generate a Random Huffman Coding Tree with Custom Probabilities

# In[4]:


import heapq

class HuffmanNode:
    def __init__(self, char=None, frequency=0):
        self.char = char
        self.frequency = frequency
        self.left = None
        self.right = None

def generate_huffman_tree_with_custom_probabilities(probabilities):
    heap = []
    for char, probability in probabilities.items():
        heapq.heappush(heap, (probability, HuffmanNode(char, probability)))

    while len(heap) > 1:
        prob1, node1 = heapq.heappop(heap)
        prob2, node2 = heapq.heappop(heap)
        merged_node = HuffmanNode(frequency=prob1 + prob2)
        merged_node.left = node1
        merged_node.right = node2
        heapq.heappush(heap, (prob1 + prob2, merged_node))

    return heap[0][1]

def print_huffman_tree(node, prefix=""):
    if node.char is not None:
        print(f"{node.char}: {prefix}")
    else:
        print_huffman_tree(node.left, prefix + "0")
        print_huffman_tree(node.right, prefix + "1")

# Example usage to generate a random Huffman coding tree with custom probabilities
probabilities = {'a': 0.3, 'b': 0.5, 'c': 0.2}
huffman_tree = generate_huffman_tree_with_custom_probabilities(probabilities)
print("Random Huffman Coding Tree with Custom Probabilities:")
print_huffman_tree(huffman_tree)


# ### 238. Convert Roman Numeral to Decimal Using Bit Manipulation

# In[3]:


def roman_to_decimal(roman):
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    decimal_value = 0
    prev_value = 0

    for char in reversed(roman):
        value = roman_numerals[char]
        if value < prev_value:
            decimal_value -= value
        else:
            decimal_value += value
        prev_value = value

    return decimal_value

roman_numeral = "XXIV" # Replace with any valid Roman numeral
decimal_value = roman_to_decimal(roman_numeral)
print(f"Decimal value of {roman_numeral} is: {decimal_value}")


# ### 239. Check if a Number is a Fibonacci Number

# In[2]:


def is_perfect_square(num):
    return int(num ** 0.5) ** 2 == num

def is_fibonacci_number(num):
    return is_perfect_square(5 * num * num + 4) or is_perfect_square(5 * num * num - 4)

number = 21 # Replace with any number you want to check
result = is_fibonacci_number(number)
print(f"{number} is {'a Fibonacci number' if result else 'not a Fibonacci number'}.")


# ### 240. Calculate the Volume of a Regular Dodecahedron

# In[1]:


def calculate_volume_of_dodecahedron(edge_length):
    volume = (15 + 7 * 5 ** 0.5) * edge_length ** 3 / 4
    return volume

edge_length = 5 # Replace with the desired edge length of the dodecahedron
volume = calculate_volume_of_dodecahedron(edge_length)
print(f"Volume of the dodecahedron with edge length {edge_length} is: {volume:.2f}")


# In[ ]:




