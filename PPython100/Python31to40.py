#!/usr/bin/env python
# coding: utf-8

# # Python Practice 31-40

# ## Here are the Python programs for each of the objectives along with the associated algorithm, mathematical calculations, and string manipulations:

# #### 31. Generate Prime Numbers in a Range:

# In[10]:


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

start_range, end_range = 1, 50
prime_numbers = [num for num in range(start_range, end_range+1) if is_prime(num)]
print(f"Prime numbers in the range {start_range} to {end_range}: {prime_numbers}")


# ### 32. Calculate the Area of a Triangle:

# In[9]:


def area_of_triangle(base, height):
    return 0.5 * base * height

base = 5
height = 8
area = area_of_triangle(base, height)
print(f"The area of the triangle with base {base} and height {height} is {area}.")


# ### 33. Implement Selection Sort Algorithm:

# In[8]:


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

numbers_list = [64, 34, 25, 12, 22, 11, 90]
selection_sort(numbers_list)
print("Sorted list using Selection Sort:", numbers_list)


# ### 34. Find the Third Largest Number in a List:

# In[7]:


def find_third_largest(numbers):
    sorted_numbers = sorted(set(numbers), reverse=True)
    return sorted_numbers[2] if len(sorted_numbers) >= 3 else None

numbers_list = [10, 20, 5, 30, 15]
third_largest_number = find_third_largest(numbers_list)
print("Third Largest Number:", third_largest_number)


# ### 35. Print the Pattern of a Right Triangle: 

# In[6]:


def print_right_triangle(n):
    for i in range(1, n+1):
        print("* " * i)

rows = 5
print_right_triangle(rows)


# ### 36. Convert Decimal to Octal:

# In[5]:


def decimal_to_octal(decimal_num):
    return oct(decimal_num).replace("0o", "")

decimal_num = 25
octal_num = decimal_to_octal(decimal_num)
print(f"The octal representation of {decimal_num} is {octal_num}.")


# ### 37. Find the Greatest Common Divisor of Multiple Numbers:

# In[4]:


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def gcd_of_multiple_numbers(numbers):
    result = numbers[0]
    for i in range(1, len(numbers)):
        result = gcd(result, numbers[i])
    return result

numbers_list = [24, 36, 48]
gcd_value = gcd_of_multiple_numbers(numbers_list)
print(f"The GCD of {numbers_list} is {gcd_value}.")


# ### 38. Calculate the Perimeter of a Rectangle:

# In[3]:


def perimeter_of_rectangle(length, width):
    return 2 * (length + width)

length = 6
width = 4
perimeter = perimeter_of_rectangle(length, width)
print(f"The perimeter of the rectangle with length {length} and width {width} is {perimeter}.")


# ### 39. Implement Insertion Sort Algorithm:

# In[2]:


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

numbers_list = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(numbers_list)
print("Sorted list using Insertion Sort:", numbers_list)


# ### 40. Check if a String is a Pangram:

# In[1]:


import string

def is_pangram(s):
    alphabet = set(string.ascii_lowercase)
    return set(s.lower()) >= alphabet

sentence = "The quick brown fox jumps over the lazy dog"
if is_pangram(sentence):
    print("The sentence is a pangram.")
else:
    print("The sentence is not a pangram.")

