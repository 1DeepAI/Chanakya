#!/usr/bin/env python
# coding: utf-8

# # Python Practice 211-220

# ## Here are the Python programs for each of the objectives along with the associated algorithm, mathematical calculations, and string manipulations:

# ### 211. Calculate the Perimeter of a Reuleaux Pentagon Star

# In[15]:


def calculate_perimeter_of_reuleaux_pentagon_star(radius):
    import math
    perimeter = 10 * math.pi * radius
    return perimeter

radius = 5
perimeter = calculate_perimeter_of_reuleaux_pentagon_star(radius)
print(f"The perimeter of the Reuleaux Pentagon Star with radius {radius} is {perimeter:.2f}.")


# ### 212. Print the Pattern of a Hollow Sierpinski Triangle with Right Alignment

# In[16]:


def print_hollow_sierpinski_triangle(rows):
    def sierpinski_row(row_width, base_width):
        left_padding = (base_width - row_width) // 2
        return " " * left_padding + "*" * row_width

    base_width = 2 ** (rows - 1)
    for i in range(rows):
        row_width = base_width // (2 ** i)
        print(sierpinski_row(row_width, base_width))

rows = 5
print("Hollow Sierpinski Triangle:")
print_hollow_sierpinski_triangle(rows)


# ### 213. Generate a Random Huffman Coding Tree from Text Data

# In[17]:


from collections import Counter
import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(data):
    frequency = Counter(data)
    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left_child = heapq.heappop(heap)
        right_child = heapq.heappop(heap)
        combined_freq = left_child.freq + right_child.freq
        combined_node = Node(None, combined_freq)
        combined_node.left = left_child
        combined_node.right = right_child
        heapq.heappush(heap, combined_node)

    return heap[0]

def generate_huffman_codes(root, code="", huffman_codes={}):
    if root is None:
        return
    if root.char:
        huffman_codes[root.char] = code
    generate_huffman_codes(root.left, code + "0", huffman_codes)
    generate_huffman_codes(root.right, code + "1", huffman_codes)
    return huffman_codes

text_data = "this is an example for huffman encoding"
huffman_tree = build_huffman_tree(text_data)
huffman_codes = generate_huffman_codes(huffman_tree)
print("Huffman Codes:")
for char, code in huffman_codes.items():
    print(f"{char}: {code}")


# ### 214. Convert Roman Numeral to Decimal Using Iterative Approach

# In[18]:


def roman_to_decimal(roman):
    roman_numerals = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    decimal = 0
    prev_value = 0
    for char in reversed(roman):
        value = roman_numerals[char]
        if value < prev_value:
            decimal -= value
        else:
            decimal += value
        prev_value = value
    return decimal

roman_numeral = "CXLII"
decimal_num = roman_to_decimal(roman_numeral)
print(f"The decimal representation of {roman_numeral} is {decimal_num}.")


# ### 215. Check if a String is a Repeated Substring Pattern

# In[19]:


def is_repeated_substring_pattern(s):
    for i in range(1, len(s)):
        substring = s[:i]
        repetitions = len(s) // i
        if substring * repetitions == s:
            return True
    return False

text = "abcabcabcabc"
if is_repeated_substring_pattern(text):
    print(f"The string '{text}' is a repeated substring pattern.")
else:
    print(f"The string '{text}' is not a repeated substring pattern.")


# ### 216. Calculate the Volume of a Regular Pyramid

# In[6]:


def volume_of_regular_pyramid(base_area, height):
    volume = (1 / 3) * base_area * height
    return volume

base_area = 25
height = 10
volume = volume_of_regular_pyramid(base_area, height)
print(f"The volume of the regular pyramid with base area {base_area} and height {height} is {volume:.2f}.")


# ### 217. Implement B-tree Data Structure

# In[34]:


class BTreeNode:
    def __init__(self, leaf=True):
        self.leaf = leaf
        self.keys = []
        self.children = []

class BTree:
    def __init__(self, degree):
        self.root = BTreeNode(leaf=True)
        self.degree = degree

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1

        if i < len(node.keys) and key == node.keys[i]:
            return node

        if node.leaf:
            return None

        return self._search(node.children[i], key)

    def insert(self, key):
        root = self.root

        if len(root.keys) == (2 * self.degree) - 1:
            new_root = BTreeNode(leaf=False)
            self.root = new_root
            new_root.children.append(root)
            self._split_child(new_root, 0)

        self._insert_non_full(self.root, key)

    def _insert_non_full(self, node, key):
        i = len(node.keys) - 1

        if node.leaf:
            node.keys.append(None)
            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = key
        else:
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == (2 * self.degree) - 1:
                self._split_child(node, i)
                if key > node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], key)

    def _split_child(self, parent, index):
        degree = self.degree
        new_node = BTreeNode(leaf=False)
        child = parent.children[index]
        parent.keys.insert(index, child.keys[degree - 1])
        parent.children.insert(index + 1, new_node)
        new_node.keys = child.keys[degree:]
        child.keys = child.keys[:degree - 1]
        if not child.leaf:
            new_node.children = child.children[degree:]
            child.children = child.children[:degree]

# Example usage of the B-tree data structure
btree = BTree(3)
for key in [1, 3, 5, 7, 9]:
    btree.insert(key)
print("B-tree traversal:")
print(btree.root.keys)
print(btree.root.children[0].keys)
print(btree.root.children[1].keys)
print(btree.root.children[2].keys)
print(btree.root.children[3].keys)


# ### 218. Find the Abundant Pairs in a Range

# In[32]:


def find_abundant_pairs_in_range(start, end):
    def get_divisors(num):
        divisors = []
        for i in range(1, num // 2 + 1):
            if num % i == 0:
                divisors.append(i)
        return divisors

    abundant_pairs = []
    for num in range(start, end + 1):
        divisors = get_divisors(num)
        if sum(divisors) > num:
            abundant_pairs.append((num, divisors))

    return abundant_pairs

start_range = 1
end_range = 100
abundant_pairs = find_abundant_pairs_in_range(start_range, end_range)
print(f"Abundant pairs in the range [{start_range}, {end_range}]:")
for num, divisors in abundant_pairs:
    print(f"{num}: {divisors}")



# ### 219. Calculate the Perimeter of a Reuleaux Hexagon Star

# In[30]:


def calculate_perimeter_of_reuleaux_hexagon_star(side_length):
    perimeter = 6 * side_length
    return perimeter

side_length = 5
perimeter = calculate_perimeter_of_reuleaux_hexagon_star(side_length)
print(f"The perimeter of the Reuleaux Hexagon Star with side length {side_length} is {perimeter:.2f}.")


# ### 220. Print the Pattern of a Hollow Rhombic Pyramid

# In[31]:


def print_hollow_rhombic_pyramid(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * (2 * i - 1))
    for i in range(rows - 1, 0, -1):
        print(" " * (rows - i) + "*" * (2 * i - 1))

rows = 5
print("Hollow Rhombic Pyramid:")
print_hollow_rhombic_pyramid(rows)

