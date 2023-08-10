#!/usr/bin/env python
# coding: utf-8

# # Python Practice 51-60

# ## Here are the Python programs for each of the objectives along with the associated algorithm, mathematical calculations, and string manipulations:

# ### 51. Generate a Random Number between a Given Range:

# In[10]:


import random

def generate_random_number(start, end):
    return random.randint(start, end)

start_range, end_range = 1, 100
random_number = generate_random_number(start_range, end_range)
print(f"A random number between {start_range} and {end_range}: {random_number}")


# ### 52. Convert Octal to Decimal: 

# In[9]:


def octal_to_decimal(octal_num):
    return int(octal_num, 8)

octal_num = "72"
decimal_num = octal_to_decimal(octal_num)
print(f"The decimal representation of {octal_num} is {decimal_num}.")


# ### 53.  Check if a String is a Palindrome Using Recursion:

# In[8]:


def is_palindrome_recursive(s):
    if len(s) <= 1:
        return True
    return s[0] == s[-1] and is_palindrome_recursive(s[1:-1])

word = "level"
if is_palindrome_recursive(word):
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")


# ### 54.  Calculate the Area of a Parallelogram:

# In[7]:


def area_of_parallelogram(base, height):
    return base * height

base = 5
height = 8
area = area_of_parallelogram(base, height)
print(f"The area of the parallelogram with base {base} and height {height} is {area}.")


# ### 55. Implement Linear Search Algorithm: 

# In[6]:


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

numbers_list = [11, 22, 34, 45, 56, 67, 78, 89, 99]
target_number = 45
index = linear_search(numbers_list, target_number)
if index != -1:
    print(f"{target_number} is found at index {index}.")
else:
    print(f"{target_number} is not found in the list.")


# ### 56. Find the Prime Factors of a Number:

# In[5]:


def prime_factors(num):
    factors = []
    divisor = 2
    while divisor * divisor <= num:
        if num % divisor == 0:
            factors.append(divisor)
            num //= divisor
        else:
            divisor += 1
    if num > 1:
        factors.append(num)
    return factors

number = 84
prime_factors_list = prime_factors(number)
print(f"The prime factors of {number} are: {prime_factors_list}")


# ### 57. Calculate the Exponentiation of a Number Using the Power Function:

# In[4]:


def power_function(base, exponent):
    return pow(base, exponent)

base, exponent = 2, 3
result = power_function(base, exponent)
print(f"{base} raised to the power of {exponent} is {result}.")


# ### 58. Check if a Number is a Narcissistic Number:

# In[3]:


def is_narcissistic_number(num):
    num_str = str(num)
    order = len(num_str)
    sum = 0
    for digit in num_str:
        sum += int(digit) ** order
    return num == sum

number = 153
if is_narcissistic_number(number):
    print(f"{number} is a narcissistic number.")
else:
    print(f"{number} is not a narcissistic number.")


# ### 59. Calculate the Perimeter of a Triangle:

# In[2]:


def perimeter_of_triangle(side1, side2, side3):
    return side1 + side2 + side3

side1, side2, side3 = 3, 4, 5
perimeter = perimeter_of_triangle(side1, side2, side3)
print(f"The perimeter of the triangle with sides {side1}, {side2}, and {side3} is {perimeter}.")


# ### 60. Print the Pattern of an Inverted Pyramid:

# In[1]:


def print_inverted_pyramid(n):
    for i in range(n, 0, -1):
        print(" " * (n - i) + "* " * (2 * i - 1))

rows = 5
print_inverted_pyramid(rows)


# In[ ]:




