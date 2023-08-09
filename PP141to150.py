#!/usr/bin/env python
# coding: utf-8

# # Python Practice 141-150

# ##  Here are the Python programs for each of the objectives along with the associated algorithm, mathematical calculations, and string manipulations:

# ### 141. Generate a Random Password with Required Strength

# In[11]:


import random
import string

def generate_random_password_strength(length, requires_uppercase=True, requires_lowercase=True, requires_digits=True, requires_special_chars=True):
    characters = ""
    if requires_uppercase:
        characters += string.ascii_uppercase
    if requires_lowercase:
        characters += string.ascii_lowercase
    if requires_digits:
        characters += string.digits
    if requires_special_chars:
        characters += string.punctuation
    random_password = ''.join(random.choice(characters) for _ in range(length))
    return random_password

password_length = 12
password_requires_uppercase = True
password_requires_lowercase = True
password_requires_digits = True
password_requires_special_chars = True
random_password = generate_random_password_strength(password_length, password_requires_uppercase, password_requires_lowercase, password_requires_digits, password_requires_special_chars)
print(f"Generated Random Password with required strength: {random_password}")


# ### 142. Convert Decimal to Roman Numeral

# In[10]:


def decimal_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_numeral = ""
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_numeral += syms[i]
            num -= val[i]
        i += 1
    return roman_numeral

decimal_num = 42
roman_numeral = decimal_to_roman(decimal_num)
print(f"The Roman numeral representation of {decimal_num} is {roman_numeral}.")


# ### 143. Check if a Number is a Happy Prime

# In[9]:


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_happy_number(num):
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(digit)**2 for digit in str(num))
    return num == 1

def is_happy_prime(num):
    return is_prime(num) and is_happy_number(num)

number = 23
if is_happy_prime(number):
    print(f"{number} is a happy prime.")
else:
    print(f"{number} is not a happy prime.")


# ### 144. Calculate the Volume of a Cone

# In[8]:


import math

def volume_of_cone(radius, height):
    return (1/3) * math.pi * radius ** 2 * height

radius, height = 5, 8
volume = volume_of_cone(radius, height)
print(f"The volume of the cone with radius {radius} and height {height} is {volume:.2f}.")


# ### 145. Implement Graph Data Structure

# In[7]:


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def get_vertices(self):
        return list(self.graph.keys())

    def get_neighbors(self, vertex):
        return self.graph[vertex]

# Example usage of the Graph data structure
graph = Graph()
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 3)
graph.add_edge(3, 4)

print("Vertices:", graph.get_vertices())
print("Neighbors of vertex 1:", graph.get_neighbors(1))
print("Neighbors of vertex 3:", graph.get_neighbors(3))


# ### 146. Find the Amicable Numbers in a Range

# In[6]:


def sum_of_divisors(num):
    divisors_sum = 1
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            divisors_sum += i
            if num // i != i:
                divisors_sum += num // i
    return divisors_sum

def are_amicable_numbers(num1, num2):
    return sum_of_divisors(num1) == num2 and sum_of_divisors(num2) == num1

def find_amicable_numbers(start, end):
    amicable_numbers = [(num1, num2) for num1 in range(start, end+1) for num2 in range(num1+1, end+1) if are_amicable_numbers(num1, num2)]
    return amicable_numbers

start_range, end_range = 1, 1000
amicable_numbers_list = find_amicable_numbers(start_range, end_range)
print(f"Amicable numbers in the range {start_range} to {end_range}: {amicable_numbers_list}")


# ### 147. Calculate the Perimeter of a Regular Octahedron

# In[5]:


def perimeter_of_regular_octahedron(edge_length):
    return 6 * edge_length

edge_length = 5
perimeter = perimeter_of_regular_octahedron(edge_length)
print(f"The perimeter of the regular octahedron with edge length {edge_length} is {perimeter:.2f}.")


# ### 148. Print the Pattern of a Hollow Floyd's Triangle

# In[4]:


def print_hollow_floyds_triangle(n):
    num = 1
    for i in range(1, n+1):
        for j in range(1, i+1):
            if i == n or j == 1 or j == i:
                print(num, end=" ")
            else:
                print(" ", end=" ")
            num += 1
        print()

rows = 5
print_hollow_floyds_triangle(rows)


# ### 149. Generate a Random Password with Pronounceable Syllables

# In[3]:


import random
import string

vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"

def generate_random_syllable():
    return random.choice(consonants) + random.choice(vowels)

def generate_random_password_pronounceable(length):
    password = ""
    for _ in range(length // 2):
        password += generate_random_syllable()
    if length % 2 != 0:
        password += random.choice(consonants)
    return password

password_length = 10
random_password = generate_random_password_pronounceable(password_length)
print(f"Generated Random Password with pronounceable syllables: {random_password}")


# ### 150. Convert Roman Numeral to Decimal

# In[2]:


def roman_to_decimal(roman_numeral):
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    decimal_num = 0
    prev_value = 0

    for char in reversed(roman_numeral):
        value = roman_values[char]
        if value < prev_value:
            decimal_num -= value
        else:
            decimal_num += value
        prev_value = value

    return decimal_num

roman_numeral = "XLII"
decimal_num = roman_to_decimal(roman_numeral)
print(f"The decimal representation of {roman_numeral} is {decimal_num}.")

