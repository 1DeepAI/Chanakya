#!/usr/bin/env python
# coding: utf-8

# # Python Practice 61-70

# ## Here are the Python programs for each of the objectives along with the associated algorithm, mathematical calculations, and string manipulations: 

# ### 61. Generate a Random Password:

# In[10]:


import random
import string

def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

password_length = 10
random_password = generate_random_password(password_length)
print(f"Generated Random Password: {random_password}")


# ### 62. Convert Binary to Octal:

# In[9]:


def binary_to_octal(binary_num):
    decimal_num = int(binary_num, 2)
    return oct(decimal_num).replace("0o", "")

binary_num = "101010"
octal_num = binary_to_octal(binary_num)
print(f"The octal representation of {binary_num} is {octal_num}.")


# ### 63. Check if a Number is a Harshad Number:

# In[8]:


def is_harshad_number(num):
    return num % sum(int(digit) for digit in str(num)) == 0

number = 18
if is_harshad_number(number):
    print(f"{number} is a Harshad number.")
else:
    print(f"{number} is not a Harshad number.")


# ### 64. Calculate the Area of a Rhombus:

# In[7]:


def area_of_rhombus(diagonal1, diagonal2):
    return 0.5 * diagonal1 * diagonal2

diagonal1 = 8
diagonal2 = 12
area = area_of_rhombus(diagonal1, diagonal2)
print(f"The area of the rhombus with diagonals {diagonal1} and {diagonal2} is {area}.")


# ### 65. Implement Stack Data Structure:

# In[6]:


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)

# Example usage of the Stack data structure
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Stack size:", stack.size())
print("Top element:", stack.peek())
print("Popped element:", stack.pop())
print("Is the stack empty?", stack.is_empty())


# ### 66. Find the HCF of Multiple Numbers:

# In[5]:


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def hcf_of_multiple_numbers(numbers):
    result = numbers[0]
    for i in range(1, len(numbers)):
        result = gcd(result, numbers[i])
    return result

numbers_list = [48, 36, 72]
hcf_value = hcf_of_multiple_numbers(numbers_list)
print(f"The HCF of {numbers_list} is {hcf_value}.")


# ### 67. Calculate the Perimeter of a Square:

# In[4]:


def perimeter_of_square(side):
    return 4 * side

side_length = 6
perimeter = perimeter_of_square(side_length)
print(f"The perimeter of the square with side {side_length} is {perimeter}.")


# ### 68. Print the Pattern of a Diamond:

# In[3]:


def print_diamond(n):
    for i in range(1, n+1):
        print(" " * (n-i) + "* " * i)
    for i in range(n-1, 0, -1):
        print(" " * (n-i) + "* " * i)

rows = 5
print_diamond(rows)


# ### 69. Generate a Random String of a Given Length:

# In[2]:


import random
import string

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

string_length = 8
random_string = generate_random_string(string_length)
print(f"Generated Random String: {random_string}")


# ### 70. Convert Octal to Binary:

# In[1]:


def octal_to_binary(octal_num):
    decimal_num = int(octal_num, 8)
    return bin(decimal_num).replace("0b", "")

octal_num = "72"
binary_num = octal_to_binary(octal_num)
print(f"The binary representation of {octal_num} is {binary_num}.")


# In[ ]:




