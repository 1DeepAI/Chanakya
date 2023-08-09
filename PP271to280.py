#!/usr/bin/env python
# coding: utf-8

# # Python Practice 271-280

# ## Here are the Python programs for the given objectives:

# ### 271. Check if a Number is a Power of N

# In[10]:


def is_power_of_n(number, n):
    while number % n == 0:
        number //= n
    return number == 1

number = 32 # Replace with the number you want to check
n = 2 # Replace with the base 'n' for the power check
result = is_power_of_n(number, n)
print(f"The number {number} is {'a power of {n}' if result else 'not a power of {n}'}.")


# ### 272. Calculate the Volume of a Frustum of a Regular Cone

# In[9]:


def calculate_volume_of_frustum_of_cone(radius1, radius2, height):
    volume = (1 / 3) * math.pi * height * (radius1**2 + radius1 * radius2 + radius2**2)
    return volume

radius1 = 5 # Replace with the radius of the larger base of the frustum of the cone
radius2 = 3 # Replace with the radius of the smaller top base of the frustum of the cone
height = 8 # Replace with the height of the frustum of the cone
volume = calculate_volume_of_frustum_of_cone(radius1, radius2, height)
print(f"Volume of the frustum of the cone with base radii {radius1} and {radius2} and height {height} is: {volume:.2f}")


# ### 273. Implement Circular Linked List Data Structure with Custom Node Class

# In[8]:


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.head.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def display(self):
        if self.is_empty():
            print("Circular linked list is empty.")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("HEAD")

# Example usage of the CircularLinkedList data structure
cll = CircularLinkedList()
cll.append(1)
cll.append(2)
cll.append(3)
cll.display() # Output: 1 -> 2 -> 3 -> HEAD


# ### 274. Find the Power-ful Numbers in a Range

# In[7]:


def is_powerful(n):
    # A number is powerful if all its prime factors have at least a multiplicity of 2
    for i in range(2, int(n**0.5) + 1):
        count = 0
        while n % i == 0:
            count += 1
            n //= i
        if count > 1:
            return False
    return n > 1

lower_bound = 1 # Replace with the lower bound of the range to search for powerful numbers
upper_bound = 100 # Replace with the upper bound of the range to search for powerful numbers
powerful_numbers = [num for num in range(lower_bound, upper_bound + 1) if is_powerful(num)]
print("Powerful numbers in the given range:")
print(powerful_numbers)


# ### 275. Calculate the Perimeter of a Reuleaux Ellipse with Right Alignment

# In[6]:


def calculate_perimeter_of_reuleaux_ellipse(radius1, radius2):
    # The perimeter of a Reuleaux ellipse is the same as the perimeter of a Reuleaux triangle with the same radii
    perimeter = 6 * (radius1 + radius2)
    return perimeter

radius1 = 5 # Replace with the first radius of the Reuleaux ellipse
radius2 = 3 # Replace with the second radius of the Reuleaux ellipse
perimeter = calculate_perimeter_of_reuleaux_ellipse(radius1, radius2)
print(f"Perimeter of the Reuleaux ellipse with radii {radius1} and {radius2} is: {perimeter:.2f}")


# ### 276. Print the Pattern of a Hollow Sierpinski Triangle Star

# In[5]:


def print_hollow_sierpinski_triangle_star(rows):
    for i in range(1, rows + 1):
        for j in range(1, 2 * rows):
            if i == rows or i + j == rows + 1 or j - i == rows - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

rows = 5 # Replace with the desired number of rows for the hollow Sierpinski triangle star
print("Hollow Sierpinski Triangle Star Pattern:")
print_hollow_sierpinski_triangle_star(rows)


# ### 277. Generate a Random Password with Custom Strength and Entropy

# In[4]:


import string
import random

def generate_random_password(strength, length):
    characters = ""
    if strength == "weak":
        characters = string.ascii_lowercase
    elif strength == "medium":
        characters = string.ascii_letters + string.digits
    elif strength == "strong":
        characters = string.ascii_letters + string.digits + string.punctuation

    password = "".join(random.choice(characters) for _ in range(length))
    return password

strength = "strong" # Replace with the desired strength of the password ("weak", "medium", "strong", etc.)
length = 10 # Replace with the desired length of the password
password = generate_random_password(strength, length)
print(f"Generated {strength} password with length {length}: {password}")


# ### 278. Convert Decimal to Excess-K Code Using Recursion

# In[3]:


def decimal_to_excess_k(decimal_number, k):
    if decimal_number >= 0:
        return bin(decimal_number + k)[2:]
    else:
        return bin(2**len(bin(k))-1 + decimal_number + k)[2:]

decimal_number = 10 # Replace with the decimal number you want to convert
k = 3 # Replace with the value of k for the excess-k code conversion
excess_k_code = decimal_to_excess_k(decimal_number, k)
print(f"Excess-{k} code representation of {decimal_number} is: {excess_k_code}")


# ### 279. Check if a String is a Perfect Power of Another String

# In[2]:


def is_perfect_power(string1, string2):
    if len(string1) % len(string2) != 0:
        return False
    n = len(string1) // len(string2)
    return string2 * n == string1

string1 = "abcdabcdabcd" # Replace with the first string
string2 = "abcd" # Replace with the second string
result = is_perfect_power(string1, string2)
print(f"The first string is {'a perfect power' if result else 'not a perfect power'} of the second string.")


# ### 280. Calculate the Volume of a Frustum of a Regular Icosahedron

# In[1]:


def calculate_volume_of_frustum_of_icosahedron(edge1, edge2, height):
    volume = (5 / 12) * (edge1**2 + edge1 * edge2 + edge2**2) * height
    return volume

edge1 = 4 # Replace with the length of the larger edge of the frustum of the icosahedron
edge2 = 2 # Replace with the length of the smaller top edge of the frustum of the icosahedron
height = 6 # Replace with the height of the frustum of the icosahedron
volume = calculate_volume_of_frustum_of_icosahedron(edge1, edge2, height)
print(f"Volume of the frustum of the icosahedron with edge lengths {edge1} and {edge2} and height {height} is: {volume:.2f}")


# In[ ]:




