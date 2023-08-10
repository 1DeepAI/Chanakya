#!/usr/bin/env python
# coding: utf-8

# # Python Practice 81-90

# ## Here are the Python programs for each of the objectives along with the associated algorithm, mathematical calculations, and string manipulations:

# ### 81. Implement Singly Linked List Data Structure:

# In[10]:


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

# Example usage of the Singly Linked List data structure
linked_list = SinglyLinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.display()


# ### 82. Find the Armstrong Numbers in a Range Using Recursion:

# In[9]:


def is_armstrong_number_recursive(num, order):
    if num == 0:
        return 0
    else:
        return (num % 10) ** order + is_armstrong_number_recursive(num // 10, order)

def find_armstrong_numbers_recursive(start, end):
    armstrong_numbers = []
    for num in range(start, end + 1):
        order = len(str(num))
        if num == is_armstrong_number_recursive(num, order):
            armstrong_numbers.append(num)
    return armstrong_numbers

start_range, end_range = 100, 999
armstrong_numbers_list = find_armstrong_numbers_recursive(start_range, end_range)
print(f"Armstrong numbers in the range {start_range} to {end_range}: {armstrong_numbers_list}")


# ### 83. Calculate the Perimeter of a Rhombus:

# In[8]:


def perimeter_of_rhombus(side):
    return 4 * side

side_length = 7
perimeter = perimeter_of_rhombus(side_length)
print(f"The perimeter of the rhombus with side {side_length} is {perimeter}.")


# ### 84. Print the Pattern of a Hollow Diamond:

# In[7]:


def print_hollow_diamond(n):
    for i in range(1, n+1):
        print(" " * (n-i) + "* " * (2*i-1))
    for i in range(n-1, 0, -1):
        print(" " * (n-i) + "* " * (2*i-1))

rows = 5
print_hollow_diamond(rows)


# ### 85. Generate a Random Password with a Mix of Characters:

# In[6]:


import random
import string

def generate_random_password_with_mix(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

password_length = 12
random_password = generate_random_password_with_mix(password_length)
print(f"Generated Random Password with a mix of characters: {random_password}")


# ### 86. Convert Octal to Hexadecimal:

# In[5]:


def octal_to_hexadecimal(octal_num):
    decimal_num = int(octal_num, 8)
    return hex(decimal_num).replace("0x", "").upper()

octal_num = "72"
hexadecimal_num = octal_to_hexadecimal(octal_num)
print(f"The hexadecimal representation of {octal_num} is {hexadecimal_num}.")


# ### 87. Check if a Number is a Duck Number:

# In[4]:


def is_duck_number(num):
    num_str = str(num)
    return '0' in num_str and num_str[0] != '0'

number = 1023
if is_duck_number(number):
    print(f"{number} is a duck number.")
else:
    print(f"{number} is not a duck number.")


# ### 88. Calculate the Area of a Sphere:

# In[3]:


import math

def area_of_sphere(radius):
    return 4 * math.pi * radius ** 2

radius = 5
area = area_of_sphere(radius)
print(f"The area of the sphere with radius {radius} is {area:.2f}.")


# ### 89. Implement Doubly Linked List Data Structure:

# In[2]:


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" <-> ")
            current_node = current_node.next
        print("None")

# Example usage of the Doubly Linked List data structure
doubly_linked_list = DoublyLinkedList()
doubly_linked_list.append(1)
doubly_linked_list.append(2)
doubly_linked_list.append(3)
doubly_linked_list.display()


# ### 90. Find the Perfect Numbers in a Range:

# In[1]:


def find_divisors_sum(num):
    divisors_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i
    return divisors_sum

def find_perfect_numbers(start, end):
    perfect_numbers = []
    for num in range(start, end + 1):
        if num == find_divisors_sum(num):
            perfect_numbers.append(num)
    return perfect_numbers

start_range, end_range = 1, 1000
perfect_numbers_list = find_perfect_numbers(start_range, end_range)
print(f"Perfect numbers in the range {start_range} to {end_range}: {perfect_numbers_list}")


# In[ ]:




