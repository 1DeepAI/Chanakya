#!/usr/bin/env python
# coding: utf-8

# # Python Practice 21-30

# ## Below are Python programs for each of the objectives along with the associated algorithm, mathematical calculations, and string manipulations

# ### 21. Calculate the LCM of Two Numbers:

# In[1]:


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

num1, num2 = 12, 18
lcm_value = lcm(num1, num2)
print(f"The LCM of {num1} and {num2} is {lcm_value}.")


# ### 22. Remove Duplicates from a List:

# In[2]:


def remove_duplicates(numbers):
    return list(set(numbers))

numbers_list = [1, 2, 3, 2, 4, 5, 4, 6, 7]
unique_numbers = remove_duplicates(numbers_list)
print("List with duplicates removed:", unique_numbers)


# ### 23. Check if a Number is Armstrong Number:

# In[3]:


def is_armstrong_number(num):
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    return num == sum

number = 153
if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")


# ### 24. Implement Quick Sort Algorithm: 

# In[4]:


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

numbers_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = quick_sort(numbers_list)
print("Sorted list using Quick Sort:", sorted_list)


# ### 25. Calculate the Simple Interest: 

# In[5]:


def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

principal_amount = 1000
interest_rate = 5
time_period = 2
interest = simple_interest(principal_amount, interest_rate, time_period)
print(f"The simple interest for {principal_amount} at {interest_rate}% for {time_period} years is {interest}.")


# ### 26. Check if a Number is a Perfect Number: 

# In[6]:


def is_perfect_number(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    return sum == num

number = 28
if is_perfect_number(number):
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")


# ### 27. Find the ASCII Value of a Character:

# In[7]:


character = 'A'
ascii_value = ord(character)
print(f"The ASCII value of '{character}' is {ascii_value}.")


# ### 28. Convert Binary to Decimal: 

# In[8]:


def binary_to_decimal(binary_num):
    return int(binary_num, 2)

binary_num = "1010"
decimal_num = binary_to_decimal(binary_num)
print(f"The decimal representation of '{binary_num}' is {decimal_num}.")


# ### 29. Reverse a Number:

# In[9]:


def reverse_number(num):
    reversed_num = int(str(num)[::-1])
    return reversed_num

number = 12345
reversed_number = reverse_number(number)
print(f"The reversed number of {number} is {reversed_number}.")


# ### 30. Check if a String is Anagram:

# In[10]:


def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

string1 = "listen"
string2 = "silent"
if is_anagram(string1, string2):
    print(f"{string1} and {string2} are anagrams.")
else:
    print(f"{string1} and {string2} are not anagrams.")

