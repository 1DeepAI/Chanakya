#!/usr/bin/env python
# coding: utf-8

# # Python Practice 201-210

# ## Here are the Python programs for each of the objectives along with the associated algorithm, mathematical calculations, and string manipulations: 

# ### 201. Implement Circular Queue Data Structure

# In[14]:


class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full. Cannot enqueue.")
            return
        if self.is_empty():
            self.front = 0
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        item = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        return item

# Example usage of the Circular Queue data structure
cq = CircularQueue(5)
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.enqueue(4)
cq.enqueue(5)
cq.enqueue(6)  # Queue is full.
print(cq.dequeue())  # Output: 1
cq.enqueue(6)
print(cq.dequeue())  # Output: 2


# ### 202. Find the Untouchable Numbers in a Range

# In[13]:


def sum_of_divisors(n):
    divisors_sum = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:
                divisors_sum += n // i
    return divisors_sum

def find_untouchable_numbers(start_range, end_range):
    untouchable_numbers = []
    for num in range(start_range, end_range + 1):
        if sum_of_divisors(sum_of_divisors(num)) == num and num != sum_of_divisors(num):
            untouchable_numbers.append(num)
    return untouchable_numbers

start_range, end_range = 1, 1000
untouchable_numbers_list = find_untouchable_numbers(start_range, end_range)
print(f"Untouchable numbers in the range {start_range} to {end_range}: {untouchable_numbers_list}")


# ### 203. Calculate the Perimeter of a Reuleaux Hexagon

# In[12]:


def calculate_perimeter_of_reuleaux_hexagon(radius):
    import math
    perimeter = 6 * math.pi * radius
    return perimeter

radius = 5
perimeter = calculate_perimeter_of_reuleaux_hexagon(radius)
print(f"The perimeter of the Reuleaux hexagon with radius {radius} is {perimeter:.2f}.")


# ### 204. Print the Pattern of a Hollow Pascal's Triangle with Right Alignment

# In[11]:


def print_hollow_pascals_triangle(rows):
    for i in range(rows):
        print(" " * (2 * (rows - i - 1)), end="")
        for j in range(i + 1):
            if j == 0 or j == i or i == rows - 1:
                print(1, end=" ")
            else:
                print(" ", end=" ")
        print()

rows = 5
print("Hollow Pascal's Triangle:")
print_hollow_pascals_triangle(rows)


# ### 205. Generate a Random Word Cloud from Text Data

# In[10]:


from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate_word_cloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

text_data = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
generate_word_cloud(text_data)


# ### 206. Convert Roman Numeral to Decimal Using a Dictionary

# In[9]:


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


# ### 207. Check if a String is a Rotated Palindrome

# In[8]:


def is_palindrome(string):
    return string == string[::-1]

def is_rotated_palindrome(string):
    for i in range(len(string)):
        rotated_string = string[i:] + string[:i]
        if is_palindrome(rotated_string):
            return True
    return False

text = "radar"
if is_rotated_palindrome(text):
    print(f"The string '{text}' is a rotated palindrome.")
else:
    print(f"The string '{text}' is not a rotated palindrome.")


# ### 208. Calculate the Volume of a Reuleaux Dodecahedron

# In[7]:


def volume_of_reuleaux_dodecahedron(a):
    import math
    volume = (35 / 8) * math.sqrt(2) * a**3
    return volume

side_length = 5
volume = volume_of_reuleaux_dodecahedron(side_length)
print(f"The volume of the Reuleaux dodecahedron with side length {side_length} is {volume:.2f}.")


# ### 209. Implement Bloom Filter Data Structure

# In[16]:


import mmh3
from bitarray import bitarray

class BloomFilter:
    def __init__(self, size, num_hash_functions):
        self.size = size
        self.num_hash_functions = num_hash_functions
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)

    def add(self, item):
        for seed in range(self.num_hash_functions):
            index = mmh3.hash(item, seed) % self.size
            self.bit_array[index] = 1

    def contains(self, item):
        for seed in range(self.num_hash_functions):
            index = mmh3.hash(item, seed) % self.size
            if self.bit_array[index] == 0:
                return False
        return True

# Example usage of the Bloom Filter data structure
bloom_filter = BloomFilter(100, 3)
bloom_filter.add("apple")
bloom_filter.add("orange")
print(bloom_filter.contains("apple"))  # Output: True
print(bloom_filter.contains("banana"))  # Output: False


# ### 210. Find the Narcissistic Numbers in a Range

# In[4]:


def is_narcissistic_number(num):
    num_str = str(num)
    n = len(num_str)
    total = sum(int(digit)**n for digit in num_str)
    return total == num

def find_narcissistic_numbers(start_range, end_range):
    narcissistic_numbers = []
    for num in range(start_range, end_range + 1):
        if is_narcissistic_number(num):
            narcissistic_numbers.append(num)
    return narcissistic_numbers

start_range, end_range = 1, 1000
narcissistic_numbers_list = find_narcissistic_numbers(start_range, end_range)
print(f"Narcissistic numbers in the range {start_range} to {end_range}: {narcissistic_numbers_list}")

