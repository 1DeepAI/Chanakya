#!/usr/bin/env python
# coding: utf-8

# # Python Practice 241-250

# ## Here are Python programs for the objectives

# ### 241. Implement Hash Table Data Structure with Open Addressing

# In[10]:


class HashTable:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = value
                return
            index = (index + 1) % self.size
        self.keys[index] = key
        self.values[index] = value

    def get(self, key):
        index = self.hash_function(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = (index + 1) % self.size
        return None

# Example usage of the Hash Table data structure with open addressing
hash_table = HashTable(size=10)
hash_table.insert('apple', 5)
hash_table.insert('banana', 10)
hash_table.insert('orange', 8)

print("Value of 'apple':", hash_table.get('apple'))
print("Value of 'banana':", hash_table.get('banana'))
print("Value of 'orange':", hash_table.get('orange'))
print("Value of 'grape':", hash_table.get('grape'))


# ### 242. Find the Joyful Numbers in a Range

# In[9]:


def is_joyful_number(num):
    digits = [int(digit) for digit in str(num)]
    for digit in digits:
        if digit == 0 or num % digit != 0:
            return False
    return True

def find_joyful_numbers_in_range(start, end):
    joyful_numbers = [num for num in range(start, end + 1) if is_joyful_number(num)]
    return joyful_numbers

start_range = 1
end_range = 100
joyful_numbers = find_joyful_numbers_in_range(start_range, end_range)
print(f"Joyful numbers in the range [{start_range}, {end_range}]: {joyful_numbers}")


# ### 243. Calculate the Perimeter of a Reuleaux Ellipse

# In[8]:


import math

def calculate_perimeter_of_reuleaux_ellipse(a, b):
    # The perimeter of a Reuleaux ellipse is equal to 4 times the perimeter of an ellipse with semi-major axis 'a' and semi-minor axis 'b'
    perimeter = 4 * math.pi * ((3 * (a + b)) - ((a + 3 * b) * math.sqrt(3)))
    return perimeter

semi_major_axis = 5
semi_minor_axis = 3
perimeter = calculate_perimeter_of_reuleaux_ellipse(semi_major_axis, semi_minor_axis)
print(f"Perimeter of the Reuleaux ellipse with semi-major axis {semi_major_axis} and semi-minor axis {semi_minor_axis} is: {perimeter:.2f}")


# ### 244. Print the Pattern of a Hollow Square Star with Right Alignment

# In[7]:


def print_hollow_square_star(rows):
    for i in range(rows):
        for j in range(rows - i - 1):
            print(" ", end="")
        for j in range(rows):
            if i == 0 or i == rows - 1 or j == 0 or j == rows - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

rows = 5 # Replace with the desired number of rows for the hollow square star
print("Hollow Square Star Pattern with Right Alignment:")
print_hollow_square_star(rows)


# ### 245. Generate a Random Huffman Coding Tree with Custom Frequencies

# In[6]:


import heapq

class HuffmanNode:
    def __init__(self, char=None, frequency=0):
        self.char = char
        self.frequency = frequency
        self.left = None
        self.right = None

def generate_huffman_tree_with_custom_frequencies(frequencies):
    heap = []
    for char, frequency in frequencies.items():
        heapq.heappush(heap, (frequency, HuffmanNode(char, frequency)))

    while len(heap) > 1:
        freq1, node1 = heapq.heappop(heap)
        freq2, node2 = heapq.heappop(heap)
        merged_node = HuffmanNode(frequency=freq1 + freq2)
        merged_node.left = node1
        merged_node.right = node2
        heapq.heappush(heap, (freq1 + freq2, merged_node))

    return heap[0][1]

def print_huffman_tree(node, prefix=""):
    if node.char is not None:
        print(f"{node.char}: {prefix}")
    else:
        print_huffman_tree(node.left, prefix + "0")
        print_huffman_tree(node.right, prefix + "1")

# Example usage to generate a random Huffman coding tree with custom frequencies
frequencies = {'a': 10, 'b': 20, 'c': 15, 'd': 5, 'e': 40}
huffman_tree = generate_huffman_tree_with_custom_frequencies(frequencies)
print("Random Huffman Coding Tree with Custom Frequencies:")
print_huffman_tree(huffman_tree)


# ### 246. Convert Decimal to Balanced Ternary Using Recursion

# In[5]:


def convert_to_balanced_ternary(decimal_num):
    if decimal_num == 0:
        return '0'
    digits = '012'
    result = ''
    while decimal_num != 0:
        decimal_num, remainder = divmod(decimal_num, 3)
        if remainder == 2:
            decimal_num += 1
        result = digits[remainder] + result
    return result

decimal_number = 17 # Replace with any decimal number you want to convert
balanced_ternary = convert_to_balanced_ternary(decimal_number)
print(f"Balanced ternary representation of {decimal_number} is: {balanced_ternary}")


# ### 247. Check if a Number is a Happy Prime Using Bit Manipulation

# In[4]:


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_happy_number(num):
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(digit) ** 2 for digit in str(num))
    return num == 1

def is_happy_prime(num):
    return is_prime(num) and is_happy_number(num)

number = 19 # Replace with any number you want to check
result = is_happy_prime(number)
print(f"{number} is {'a happy prime' if result else 'not a happy prime'}.")


# ### 248. Calculate the Volume of a Frustum of a Cone

# In[3]:


import math

def calculate_volume_of_frustum_of_cone(radius1, radius2, height):
    volume = (1 / 3) * math.pi * height * (radius1 ** 2 + radius2 ** 2 + radius1 * radius2)
    return volume

radius1 = 5 # Replace with the larger base radius of the frustum of the cone
radius2 = 3 # Replace with the smaller top radius of the frustum of the cone
height = 8 # Replace with the height of the frustum of the cone
volume = calculate_volume_of_frustum_of_cone(radius1, radius2, height)
print(f"Volume of the frustum of the cone with radii {radius1} and {radius2} and height {height} is: {volume:.2f}")


# ### 249. Implement Red-Black Tree Data Structure with Augmented Information

# In[2]:


class RedBlackNode:
    def __init__(self, key, color='RED'):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.color = color
        self.size = 1

class RedBlackTree:
    def __init__(self):
        self.nil = RedBlackNode(None, 'BLACK')
        self.root = self.nil

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
        y.size = x.size
        x.size = x.left.size + x.right.size + 1

    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.nil:
            x.right.parent = y
        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x
        x.right = y
        y.parent = x
        x.size = y.size
        y.size = y.left.size + y.right.size + 1

    def insert(self, key):
        new_node = RedBlackNode(key)
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            y.size += 1
            if new_node.key < x.key:
                x = x.left
            else:
                x = x.right
        new_node.parent = y
        if y is None:
            self.root = new_node
        elif new_node.key < y.key:
            y.left = new_node
        else:
            y.right = new_node
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.color = 'RED'
        self.insert_fixup(new_node)

    def insert_fixup(self, node):
        while node.parent.color == 'RED':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == 'RED':
                    node.parent.color = 'BLACK'
                    uncle.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == 'RED':
                    node.parent.color = 'BLACK'
                    uncle.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    self.left_rotate(node.parent.parent)
        self.root.color = 'BLACK'

    def size_of_subtree(self, node):
        if node == self.nil:
            return 0
        return node.size

# Example usage of the Red-Black Tree data structure with augmented information
red_black_tree = RedBlackTree()
keys = [5, 7, 3, 9, 2, 6, 4, 1, 8]
for key in keys:
    red_black_tree.insert(key)

print("Red-Black Tree Traversal:")
print("Keys:", red_black_tree.root.key)
print("Left Subtree:", red_black_tree.root.left.key)
print("Right Subtree:", red_black_tree.root.right.key)
print("Left-Left Subtree:", red_black_tree.root.left.left.key)
print("Left-Right Subtree:", red_black_tree.root.left.right.key)
print("Right-Left Subtree:", red_black_tree.root.right.left.key)
print("Right-Right Subtree:", red_black_tree.root.right.right.key)
print("Left-Left-Left Subtree:", red_black_tree.root.left.left.left.key)
print("Left-Left-Right Subtree:", red_black_tree.root.left.left.right.key)
print("Left-Right-Left Subtree:", red_black_tree.root.left.right.left.key)
print("Left-Right-Right Subtree:", red_black_tree.root.left.right.right.key)
print("Right-Left-Left Subtree:", red_black_tree.root.right.left.left.key)
print("Right-Left-Right Subtree:", red_black_tree.root.right.left.right.key)
print("Right-Right-Left Subtree:", red_black_tree.root.right.right.left.key)
print("Right-Right-Right Subtree:", red_black_tree.root.right.right.right.key)


# ### 250. Find the Zealous Numbers in a Range

# In[1]:


def sum_of_divisors(num):
    return sum(i for i in range(1, num // 2 + 1) if num % i == 0)

def is_zealous_number(num):
    return num < sum_of_divisors(num)

def find_zealous_numbers_in_range(start, end):
    zealous_numbers = [num for num in range(start, end + 1) if is_zealous_number(num)]
    return zealous_numbers

start_range = 1
end_range = 100
zealous_numbers = find_zealous_numbers_in_range(start_range, end_range)
print(f"Zealous numbers in the range [{start_range}, {end_range}]: {zealous_numbers}")


# In[ ]:




