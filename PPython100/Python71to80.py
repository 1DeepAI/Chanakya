#!/usr/bin/env python
# coding: utf-8

# # Python Practice 71-80

# ## Here are the Python programs for each of the objectives along with the associated algorithm, mathematical calculations, and string manipulations:

# ### 71. Check if a Number is a Pronic Number:

# In[10]:


def is_pronic_number(num):
    for i in range(num + 1):
        if i * (i + 1) == num:
            return True
    return False

number = 42
if is_pronic_number(number):
    print(f"{number} is a pronic number.")
else:
    print(f"{number} is not a pronic number.")


# ### 72. Calculate the Area of a Trapezoid:

# In[9]:


def area_of_trapezoid(base1, base2, height):
    return 0.5 * (base1 + base2) * height

base1, base2, height = 5, 7, 8
area = area_of_trapezoid(base1, base2, height)
print(f"The area of the trapezoid with bases {base1} and {base2} and height {height} is {area}.")


# ### 73. Implement Queue Data Structure:

# In[8]:


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None

    def size(self):
        return len(self.items)

# Example usage of the Queue data structure
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Queue size:", queue.size())
print("Front element:", queue.peek())
print("Dequeued element:", queue.dequeue())
print("Is the queue empty?", queue.is_empty())


# ### 74. Find the Divisors of a Number:

# In[7]:


def find_divisors(num):
    divisors = [i for i in range(1, num+1) if num % i == 0]
    return divisors

number = 28
divisors_list = find_divisors(number)
print(f"The divisors of {number} are: {divisors_list}")


# ### 75. Calculate the Perimeter of a Parallelogram:

# In[6]:


def perimeter_of_parallelogram(side1, side2):
    return 2 * (side1 + side2)

side1, side2 = 6, 9
perimeter = perimeter_of_parallelogram(side1, side2)
print(f"The perimeter of the parallelogram with sides {side1} and {side2} is {perimeter}.")


# ### 76.Print the Pattern of a Hollow Square:

# In[5]:


def print_hollow_square(n):
    for i in range(n):
        if i == 0 or i == n-1:
            print("* " * n)
        else:
            print("* " + "  " * (n-2) + "*")

rows = 5
print_hollow_square(rows)


# ### 77. Generate a Random Number with a Fixed Number of Digits:

# In[4]:


import random

def generate_random_number_with_digits(num_digits):
    min_limit = 10 ** (num_digits - 1)
    max_limit = 10 ** num_digits - 1
    return random.randint(min_limit, max_limit)

digits = 4
random_num = generate_random_number_with_digits(digits)
print(f"Generated Random Number with {digits} digits: {random_num}")


# ### 78. Convert Binary to Hexadecimal:

# In[3]:


def binary_to_hexadecimal(binary_num):
    decimal_num = int(binary_num, 2)
    return hex(decimal_num).replace("0x", "").upper()

binary_num = "101010"
hexadecimal_num = binary_to_hexadecimal(binary_num)
print(f"The hexadecimal representation of {binary_num} is {hexadecimal_num}.")


# ### 79. Check if a Number is a Disarium Number:

# In[2]:


def is_disarium_number(num):
    num_str = str(num)
    sum = 0
    for i, digit in enumerate(num_str, start=1):
        sum += int(digit) ** i
    return num == sum

number = 89
if is_disarium_number(number):
    print(f"{number} is a Disarium number.")
else:
    print(f"{number} is not a Disarium number.")


# ### 80. Calculate the Area of a Regular Polygon:

# In[1]:


import math

def area_of_regular_polygon(side_length, num_sides):
    return (side_length ** 2 * num_sides) / (4 * math.tan(math.pi / num_sides))

side_length, num_sides = 6, 5
area = area_of_regular_polygon(side_length, num_sides)
print(f"The area of the regular polygon with side length {side_length} and {num_sides} sides is {area:.2f}.")


# In[ ]:




