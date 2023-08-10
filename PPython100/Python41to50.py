#!/usr/bin/env python
# coding: utf-8

# # PYTHON practice 41-50

# ## Here are the Python programs for each of the objectives along with the associated algorithm, mathematical calculations, and string manipulations:

# ### 41. Calculate the Area of a Square: 

# In[10]:


def area_of_square(side):
    return side ** 2

side_length = 4
area = area_of_square(side_length)
print(f"The area of the square with side {side_length} is {area}.")


# ### 42. Print the Pattern of an Inverted Right Triangle:

# In[9]:


def print_inverted_right_triangle(n):
    for i in range(n, 0, -1):
        print("* " * i)

rows = 5
print_inverted_right_triangle(rows)


# ### 43. Convert Decimal to Hexadecimal:

# In[8]:


def decimal_to_hexadecimal(decimal_num):
    return hex(decimal_num).replace("0x", "").upper()

decimal_num = 255
hexadecimal_num = decimal_to_hexadecimal(decimal_num)
print(f"The hexadecimal representation of {decimal_num} is {hexadecimal_num}.")


# ### 44. Find the Factorial of a Large Number Using Recursion:

# In[7]:


def factorial_recursive(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial_recursive(num - 1)

num = 10
factorial_result = factorial_recursive(num)
print(f"The factorial of {num} is {factorial_result}.")


# ### 45. Calculate the Exponentiation of a Number Using Recursion:

# In[6]:


def power_recursive(base, exponent):
    if exponent == 0:
        return 1
    return base * power_recursive(base, exponent - 1)

base, exponent = 2, 3
result = power_recursive(base, exponent)
print(f"{base} raised to the power of {exponent} is {result}.")


# ### 46. Implement Binary Search Algorithm:

# In[5]:


def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

numbers_list = [11, 22, 34, 45, 56, 67, 78, 89, 99]
target_number = 45
index = binary_search(numbers_list, target_number)
if index != -1:
    print(f"{target_number} is found at index {index}.")
else:
    print(f"{target_number} is not found in the list.")


# ### 47. Find the Armstrong Numbers in a Range:

# In[4]:


def is_armstrong_number(num):
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    return num == sum

start_range, end_range = 100, 999
armstrong_numbers = [num for num in range(start_range, end_range+1) if is_armstrong_number(num)]
print(f"Armstrong numbers in the range {start_range} to {end_range}: {armstrong_numbers}")


# ### 48. Check if a Number is a Strong Number:

# In[3]:


def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)

def is_strong_number(num):
    original_num = num
    sum_of_factorials = 0
    while num > 0:
        digit = num % 10
        sum_of_factorials += factorial(digit)
        num //= 10
    return original_num == sum_of_factorials

number = 145
if is_strong_number(number):
    print(f"{number} is a strong number.")
else:
    print(f"{number} is not a strong number.")


# ### 49. Calculate the Perimeter of a Circle:

# In[2]:


import math

def perimeter_of_circle(radius):
    return 2 * math.pi * radius

radius = 5
perimeter = perimeter_of_circle(radius)
print(f"The perimeter of the circle with radius {radius} is {perimeter:.2f}.")


# ### 50. Print the Pattern of a Pyramid:

# In[1]:


def print_pyramid(n):
    for i in range(n):
        print(" " * (n - i - 1) + "* " * (i + 1))

rows = 5
print_pyramid(rows)


# In[ ]:




