#!/usr/bin/env python
# coding: utf-8

# # Python Practice 11-20

# ## Below are Python programs for each of the objectives along with the associated algorithm, mathematical calculations, and string manipulations  

# ### 11. Calculate the Area of a Circle:

# In[1]:


import math

def area_of_circle(radius):
    return math.pi * radius ** 2

radius = 5
area = area_of_circle(radius)
print(f"The area of the circle with radius {radius} is {area:.2f}.")


# ### 12. Convert Decimal to Binary: 

# In[2]:


def decimal_to_binary(decimal_num):
    return bin(decimal_num).replace("0b", "")

decimal_num = 25
binary_num = decimal_to_binary(decimal_num)
print(f"The binary representation of {decimal_num} is {binary_num}.")


# ### 13. Implement Bubble Sort Algorithm: 

# In[3]:


def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

numbers_list = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(numbers_list)
print("Sorted list using Bubble Sort:", numbers_list)


# ### 14. Reverse a String: 

# In[4]:


def reverse_string(s):
    return s[::-1]

text = "Hello, World!"
reversed_text = reverse_string(text)
print(f"The reversed string of '{text}' is '{reversed_text}'.")


# ### 15. Calculate the GCD of Two Numbers: 

# In[5]:


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

num1, num2 = 12, 18
gcd_value = gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is {gcd_value}.")


# ### 16. Check if a Number is Even or Odd: 

# In[6]:


def check_even_odd(num):
    return "Even" if num % 2 == 0 else "Odd"

num = 7
result = check_even_odd(num)
print(f"{num} is {result}.")


# ### 17. Implement Merge Sort Algorithm: 

# In[7]:


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

numbers_list = [64, 34, 25, 12, 22, 11, 90]
merge_sort(numbers_list)
print("Sorted list using Merge Sort:", numbers_list)


# ### 18. Calculate the Exponentiation of a Number: 

# In[8]:


def exponentiation(base, exponent):
    return base ** exponent

base, exponent = 2, 3
result = exponentiation(base, exponent)
print(f"{base} raised to the power of {exponent} is {result}.")


# ### 19. Find the Second Largest Number in a List: 

# In[9]:


def find_second_largest(numbers):
    largest = second_largest = float('-inf')
    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    return second_largest

numbers_list = [10, 20, 5, 30, 15]
second_largest_number = find_second_largest(numbers_list)
print("Second Largest Number:", second_largest_number)


# ### 20. Check if a Year is a Leap Year:

# In[10]:


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        return True
    return False

year = 2024
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

