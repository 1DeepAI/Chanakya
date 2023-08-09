#!/usr/bin/env python
# coding: utf-8

# # Python Practice 101-110

# ## Here are the Python programs for each of the objectives along with the associated algorithm, mathematical calculations, and string manipulations:

# ### 101.  Generate a Random Password with Special Characters

# In[10]:


import random
import string

def generate_random_password_with_special(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    random_password = ''.join(random.choice(characters) for _ in range(length))
    return random_password

password_length = 12
random_password = generate_random_password_with_special(password_length)
print(f"Generated Random Password with special characters: {random_password}")


# ### 102. Convert Hexadecimal to Octal 

# In[9]:


def hexadecimal_to_octal(hexadecimal_num):
    decimal_num = int(hexadecimal_num, 16)
    return oct(decimal_num).replace("0o", "")

hexadecimal_num = "1A3"
octal_num = hexadecimal_to_octal(hexadecimal_num)
print(f"The octal representation of {hexadecimal_num} is {octal_num}.")


# ### 103. Check if a Number is a Pronic Harshad Number 

# In[8]:


def is_pronic_harshad_number(num):
    def is_harshad_number(n):
        return n % sum(int(digit) for digit in str(n)) == 0

    for i in range(num):
        if i * (i + 1) == num and is_harshad_number(num):
            return True
    return False

number = 42
if is_pronic_harshad_number(number):
    print(f"{number} is a pronic harshad number.")
else:
    print(f"{number} is not a pronic harshad number.")


# ### 104. Calculate the Area of a Cone 

# In[7]:


import math

def area_of_cone(radius, height):
    base_area = math.pi * radius ** 2
    side_area = math.pi * radius * math.sqrt(radius ** 2 + height ** 2)
    return base_area + side_area

radius, height = 5, 8
area = area_of_cone(radius, height)
print(f"The surface area of the cone with radius {radius} and height {height} is {area:.2f}.")


# ### 105. Implement Doubly Ended Queue (Deque) Data Structure 

# In[6]:


class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def append_left(self, item):
        self.items.insert(0, item)

    def append_right(self, item):
        self.items.append(item)

    def pop_left(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def pop_right(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek_left(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None

    def peek_right(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)

# Example usage of the Deque data structure
deque = Deque()
deque.append_left(1)
deque.append_left(2)
deque.append_right(3)
deque.append_right(4)
print("Deque size:", deque.size())
print("Leftmost element:", deque.peek_left())
print("Rightmost element:", deque.peek_right())
print("Popped left element:", deque.pop_left())
print("Popped right element:", deque.pop_right())


# ### 106. Find the Prime Numbers in a Range Using Sieve of Eratosthenes 

# In[5]:


def sieve_of_eratosthenes(n):
    sieve = [True] * (n+1)
    sieve[0], sieve[1] = False, False

    for p in range(2, int(n ** 0.5) + 1):
        if sieve[p]:
            for i in range(p*p, n+1, p):
                sieve[i] = False

    primes = [num for num in range(n+1) if sieve[num]]
    return primes

start_range, end_range = 1, 100
prime_numbers_list = sieve_of_eratosthenes(end_range)
print(f"Prime numbers in the range {start_range} to {end_range}: {prime_numbers_list}")


# ### 107. Calculate the Perimeter of a Cylinder 

# In[4]:


import math

def perimeter_of_cylinder(radius, height):
    return 2 * math.pi * radius + 2 * math.pi * height

radius, height = 5, 8
perimeter = perimeter_of_cylinder(radius, height)
print(f"The perimeter of the cylinder with radius {radius} and height {height} is {perimeter:.2f}.")


# ### 108. Print the Pattern of a Hollow Number Diamond 

# In[3]:


def print_hollow_number_diamond(n):
    for i in range(1, n+1):
        print(" " * (n-i), end="")
        for j in range(1, i+1):
            if j == 1 or j == i:
                print(j, end=" ")
            else:
                print(" ", end=" ")
        print()
    for i in range(n-1, 0, -1):
        print(" " * (n-i), end="")
        for j in range(1, i+1):
            if j == 1 or j == i:
                print(j, end=" ")
            else:
                print(" ", end=" ")
        print()

rows = 5
print_hollow_number_diamond(rows)


# ### 109. Generate a Random String with Custom Character Set and Length 

# In[2]:


import random

def generate_random_string_custom(characters, length):
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

custom_characters = "abcdef123!@#"
string_length = 8
random_string = generate_random_string_custom(custom_characters, string_length)
print(f"Generated Random String with custom characters: {random_string}")


# ### 110. Convert Base-N to Decimal (N < 10) 

# In[1]:


def base_n_to_decimal(num, base):
    decimal_num = 0
    num_str = str(num)
    for i, digit in enumerate(num_str[::-1]):
        decimal_num += int(digit) * (base ** i)
    return decimal_num

number = 1010
base = 2
decimal_num = base_n_to_decimal(number, base)
print(f"The decimal representation of {number} in base {base} is {decimal_num}.")


# In[ ]:




