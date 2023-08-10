#!/usr/bin/env python
# coding: utf-8

# # Python Practice 91-100

# ## Here are the Python programs for each of the objectives along with the associated algorithm, mathematical calculations, and string manipulations:

# ### 91. Calculate the Perimeter of a Trapezoid:

# In[10]:


def perimeter_of_trapezoid(base1, base2, side1, side2):
    return base1 + base2 + side1 + side2

base1, base2, side1, side2 = 5, 7, 4, 6
perimeter = perimeter_of_trapezoid(base1, base2, side1, side2)
print(f"The perimeter of the trapezoid is {perimeter}.")


# ### 92. Print the Pattern of a Number Pyramid:

# In[9]:


def print_number_pyramid(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()

rows = 5
print_number_pyramid(rows)


# ### 93. Generate a Random String with a Mix of Alphanumeric Characters:

# In[8]:


import random
import string

def generate_random_alphanumeric_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

string_length = 10
random_string = generate_random_alphanumeric_string(string_length)
print(f"Generated Random Alphanumeric String: {random_string}")


# ### 94. Convert Hexadecimal to Binary:

# In[7]:


def hexadecimal_to_binary(hexadecimal_num):
    decimal_num = int(hexadecimal_num, 16)
    return bin(decimal_num).replace("0b", "")

hexadecimal_num = "2A"
binary_num = hexadecimal_to_binary(hexadecimal_num)
print(f"The binary representation of {hexadecimal_num} is {binary_num}.")


# ### 95.  Check if a Number is a Happy Number:

# In[6]:


def is_happy_number(num):
    def square_sum(n):
        return sum(int(digit)**2 for digit in str(n))
    
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = square_sum(num)
    
    return num == 1

number = 19
if is_happy_number(number):
    print(f"{number} is a happy number.")
else:
    print(f"{number} is not a happy number.")


# ### 96. Calculate the Area of a Cylinder: 

# In[5]:


import math

def area_of_cylinder(radius, height):
    return 2 * math.pi * radius * (radius + height)

radius, height = 4, 10
area = area_of_cylinder(radius, height)
print(f"The lateral surface area of the cylinder with radius {radius} and height {height} is {area:.2f}.")


# ### 97. Implement Circular Linked List Data Structure:

# In[4]:


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            current_node = self.head
            while current_node.next != self.head:
                current_node = current_node.next
            current_node.next = new_node
            new_node.next = self.head

    def display(self):
        current_node = self.head
        while True:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
            if current_node == self.head:
                break
        print("Head")

# Example usage of the Circular Linked List data structure
circular_linked_list = CircularLinkedList()
circular_linked_list.append(1)
circular_linked_list.append(2)
circular_linked_list.append(3)
circular_linked_list.display()


# ### 98. Find the Automorphic Numbers in a Range:

# In[3]:


def is_automorphic_number(num):
    square = num ** 2
    return str(num) == str(square)[-len(str(num)):]

def find_automorphic_numbers(start, end):
    automorphic_numbers = []
    for num in range(start, end + 1):
        if is_automorphic_number(num):
            automorphic_numbers.append(num)
    return automorphic_numbers

start_range, end_range = 1, 1000
automorphic_numbers_list = find_automorphic_numbers(start_range, end_range)
print(f"Automorphic numbers in the range {start_range} to {end_range}: {automorphic_numbers_list}")


# ### 99. Calculate the Perimeter of a Regular Polygon:

# In[2]:


def perimeter_of_regular_polygon(side_length, num_sides):
    return side_length * num_sides

side_length, num_sides = 6, 5
perimeter = perimeter_of_regular_polygon(side_length, num_sides)


# ### 100. Print the Pattern of a Hollow Number Pyramid:

# In[1]:


def print_hollow_number_pyramid(n):
    for i in range(1, n+1):
        print(" " * (n-i), end="")
        for j in range(1, i+1):
            if j == 1 or j == i:
                print(j, end=" ")
            else:
                print(" ", end=" ")
        print()

rows = 5
print_hollow_number_pyramid(rows)


# In[ ]:




