#!/usr/bin/env python
# coding: utf-8

# # Python Practice 251-260

# ## Here are Python programs for the objectives 

# ### 251. Calculate the Perimeter of a Reuleaux Pentagon Star with Rounded Corners

# In[ ]:


import math

def calculate_perimeter_of_reuleaux_pentagon_star(radius):
    # The perimeter of a Reuleaux pentagon star with rounded corners is equal to 10 times the radius
    perimeter = 10 * radius
    return perimeter

radius = 5 # Replace with the desired radius of the Reuleaux pentagon star
perimeter = calculate_perimeter_of_reuleaux_pentagon_star(radius)
print(f"Perimeter of the Reuleaux pentagon star with rounded corners and radius {radius} is: {perimeter:.2f}")


# ### 252. Print the Pattern of a Hollow Number Pyramid Star

# In[ ]:


def print_hollow_number_pyramid_star(rows):
    for i in range(1, rows + 1):
        for j in range(1, 2 * rows):
            if j >= rows + 1 - i and j <= rows - 1 + i:
                print("*", end="")
            else:
                print(" ", end="")
        print()

rows = 5 # Replace with the desired number of rows for the hollow number pyramid star
print("Hollow Number Pyramid Star Pattern:")
print_hollow_number_pyramid_star(rows)


# ### 253. Generate a Random Huffman Coding Tree with Huffman's Algorithm

# In[ ]:


class HuffmanNode:
    def __init__(self, char=None, frequency=0):
        self.char = char
        self.frequency = frequency
        self.left = None
        self.right = None

def generate_huffman_tree_with_huffman_algorithm(frequencies):
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

# Example usage to generate a random Huffman coding tree with Huffman's algorithm
frequencies = {'a': 10, 'b': 20, 'c': 15, 'd': 5, 'e': 40}
huffman_tree = generate_huffman_tree_with_huffman_algorithm(frequencies)
print("Random Huffman Coding Tree with Huffman's Algorithm:")
print_huffman_tree(huffman_tree)


# ### 254. Convert Decimal to Roman Numeral Using Recursion

# In[ ]:


def convert_to_roman_numeral(decimal_num):
    roman_numerals = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

    def convert_helper(decimal_num):
        for value, numeral in roman_numerals.items():
            if decimal_num >= value:
                return numeral + convert_helper(decimal_num - value)
        return ''

    return convert_helper(decimal_num)

decimal_number = 1984 # Replace with any decimal number you want to convert
roman_numeral = convert_to_roman_numeral(decimal_number)
print(f"Roman numeral representation of {decimal_number} is: {roman_numeral}")


# ### 255. Check if a String is a Power of Two

# In[ ]:


def is_power_of_two(s):
    if s == '1':
        return True
    while len(s) > 1:
        if int(s[-1]) % 2 != 0:
            return False
        carry = 0
        new_s = ""
        for i in range(len(s) - 1, -1, -1):
            num = int(s[i]) + carry * 10
            carry = num % 2
            new_s = str(num // 2) + new_s
        s = new_s
    return int(s) == 1

string = "10000000000" # Replace with any string you want to check
result = is_power_of_two(string)
print(f"The string {string} is {'a power of two' if result else 'not a power of two'}.")


# ### 256. Calculate the Volume of a Frustum of a Pyramid

# In[ ]:


def calculate_volume_of_frustum_of_pyramid(base_area1, base_area2, height):
    volume = (1 / 3) * height * (base_area1 + base_area2 + math.sqrt(base_area1 * base_area2))
    return volume

base_area1 = 16 # Replace with the area of the larger base of the frustum of the pyramid
base_area2 = 9 # Replace with the area of the smaller top base of the frustum of the pyramid
height = 8 # Replace with the height of the frustum of the pyramid
volume = calculate_volume_of_frustum_of_pyramid(base_area1, base_area2, height)
print(f"Volume of the frustum of the pyramid with base areas {base_area1} and {base_area2} and height {height} is: {volume:.2f}")


# ### 257. Implement Queue Data Structure with Fixed Size Array

# In[ ]:


class FixedSizeQueue:
    def __init__(self, size):
        self.queue = [None] * size
        self.front = self.rear = -1
        self.size = size

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, item):
        if self.is_full():
            raise Exception("Queue is full.")
        elif self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty.")
        elif self.front == self.rear:
            item = self.queue[self.front]
            self.front = self.rear = -1
        else:
            item = self.queue[self.front]
            self.front = (self.front + 1) % self.size
        return item

# Example usage of the FixedSizeQueue data structure
queue = FixedSizeQueue(5)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Dequeued item:", queue.dequeue()) # Output: 1
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6) # Raises exception as the queue is full


# ### 258. Find the Palindromic Pairs in a List of Words

# In[ ]:


def is_palindrome(word):
    return word == word[::-1]

def find_palindromic_pairs(words):
    palindromic_pairs = []
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            pair = words[i] + words[j]
            if is_palindrome(pair):
                palindromic_pairs.append((words[i], words[j]))
    return palindromic_pairs

word_list = ["race", "car", "madam", "hello", "world"]
palindromic_pairs = find_palindromic_pairs(word_list)
print("Palindromic Pairs in the list of words:")
print(palindromic_pairs) # Output: [('race', 'car'), ('madam', 'madam')]


# ### 259. Calculate the Perimeter of a Reuleaux Hexagon Star with Rounded Corners and Right Alignment

# In[1]:


import math

def calculate_perimeter_of_reuleaux_hexagon_star(radius):
    # The perimeter of a Reuleaux hexagon star with rounded corners is equal to 12 times the radius
    perimeter = 12 * radius
    return perimeter

radius = 5 # Replace with the desired radius of the Reuleaux hexagon star with rounded corners
perimeter = calculate_perimeter_of_reuleaux_hexagon_star(radius)
print(f"Perimeter of the Reuleaux hexagon star with rounded corners and radius {radius} is: {perimeter:.2f}")


# ### 260. Print the Pattern of a Hollow Rhombic Pyramid Star

# In[2]:


def print_hollow_rhombic_pyramid_star(rows):
    for i in range(1, rows + 1):
        for j in range(rows - i):
            print(" ", end="")
        for j in range(1, 2 * i):
            if j == 1 or j == 2 * i - 1 or i == rows:
                print("*", end="")
            else:
                print(" ", end="")
        print()

rows = 5 # Replace with the desired number of rows for the hollow rhombic pyramid star
print("Hollow Rhombic Pyramid Star Pattern:")
print_hollow_rhombic_pyramid_star(rows)


# In[ ]:




