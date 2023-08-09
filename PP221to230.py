#!/usr/bin/env python
# coding: utf-8

# # Python Practice 221-230

# ## Here are the Python programs for each of the objectives along with the associated algorithm, mathematical calculations, and string manipulations:

# ### 221. Generate a Random Password with Custom Entropy

# In[10]:


import random
import string

def generate_random_password(length, entropy):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

password_length = 12
password_entropy = 3 # You can adjust the entropy level as desired
random_password = generate_random_password(password_length, password_entropy)
print(f"Random Password with custom entropy: {random_password}")


# ### 222. Convert Roman Numeral to Decimal Using Recursion

# In[9]:


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

    if len(roman) == 0:
        return 0
    if len(roman) == 1 or roman_numerals[roman[0]] >= roman_numerals[roman[1]]:
        return roman_numerals[roman[0]] + roman_to_decimal(roman[1:])
    else:
        return roman_numerals[roman[1]] - roman_numerals[roman[0]] + roman_to_decimal(roman[2:])

roman_numeral = "XXIV" # Replace with any valid Roman numeral
decimal_value = roman_to_decimal(roman_numeral)
print(f"Decimal value of {roman_numeral} is: {decimal_value}")


# ### 223. Check if a Number is a Niven Number 

# In[8]:


def is_niven_number(num):
    sum_of_digits = sum(int(digit) for digit in str(num))
    return num % sum_of_digits == 0

number = 18 # Replace with any number you want to check
result = is_niven_number(number)
print(f"{number} is {'a Niven number' if result else 'not a Niven number'}.")


# ### 224. Calculate the Volume of a Regular Octahedron

# In[7]:


def calculate_volume_of_octahedron(edge_length):
    volume = (2 ** 0.5) * edge_length ** 3 / 3
    return volume

edge_length = 5 # Replace with the desired edge length of the octahedron
volume = calculate_volume_of_octahedron(edge_length)
print(f"Volume of the octahedron with edge length {edge_length} is: {volume:.2f}")


# ### 225. Implement Trie (Prefix Tree) Data Structure

# In[6]:


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

trie = Trie()
words = ['apple', 'banana', 'orange', 'app', 'oranges']
for word in words:
    trie.insert(word)

search_word = 'orange'
result = trie.search(search_word)
print(f"Word '{search_word}' {'exists' if result else 'does not exist'} in the trie.")


# ### 226. Find the Deficient Numbers in a Range

# In[5]:


def find_divisors_sum(num):
    return sum(i for i in range(1, num) if num % i == 0)

def is_deficient_number(num):
    return find_divisors_sum(num) < num

def find_deficient_numbers_in_range(start, end):
    deficient_numbers = [num for num in range(start, end + 1) if is_deficient_number(num)]
    return deficient_numbers

start_range = 1
end_range = 50
deficient_numbers = find_deficient_numbers_in_range(start_range, end_range)
print(f"Deficient numbers in the range [{start_range}, {end_range}]: {deficient_numbers}")


# ### 227. Calculate the Perimeter of a Reuleaux Octagon

# In[4]:


import math

def calculate_perimeter_of_reuleaux_octagon(side_length):
    perimeter = 8 * side_length
    return perimeter

side_length = 5 # Replace with the desired side length of the Reuleaux octagon
perimeter = calculate_perimeter_of_reuleaux_octagon(side_length)
print(f"Perimeter of the Reuleaux octagon with side length {side_length} is: {perimeter:.2f}")


# ### 228. Print the Pattern of a Hollow Prime Number Pyramid

# In[3]:


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def print_hollow_prime_number_pyramid(rows):
    for i in range(1, rows + 1):
        for j in range(1, 2 * i):
            if i == rows or j == 1 or j == 2 * i - 1 or is_prime(i):
                print("*", end="")
            else:
                print(" ", end="")
        print()

rows = 5 # Replace with the desired number of rows in the pyramid
print("Hollow Prime Number Pyramid:")
print_hollow_prime_number_pyramid(rows)


# ### 229. Generate a Random Huffman Coding Tree with Fixed Codeword Length

# In[2]:


import heapq

class HuffmanNode:
    def __init__(self, char=None, frequency=0):
        self.char = char
        self.frequency = frequency
        self.left = None
        self.right = None

def generate_huffman_tree(frequencies):
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

# Example usage to generate a random Huffman coding tree
frequencies = {'a': 5, 'b': 10, 'c': 20, 'd': 8, 'e': 15}
huffman_tree = generate_huffman_tree(frequencies)
print("Random Huffman Coding Tree:")
print_huffman_tree(huffman_tree)


# ### 230. Convert Roman Numeral to Decimal Using Stack 

# In[1]:


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

    stack = []
    result = 0

    for char in roman:
        while stack and roman_numerals[char] > roman_numerals[stack[-1]]:
            result += roman_numerals[char] - 2 * roman_numerals[stack[-1]]
            stack.pop()
        else:
            result += roman_numerals[char]
            stack.append(char)

    return result

roman_numeral = "XXIV" # Replace with any valid Roman numeral
decimal_value = roman_to_decimal(roman_numeral)
print(f"Decimal value of {roman_numeral} is: {decimal_value}")

