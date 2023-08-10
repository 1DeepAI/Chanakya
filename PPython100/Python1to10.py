#!/usr/bin/env python
# coding: utf-8

# # Python Practice 1-10

# ## Below are Python programs for each of the objectives along with the associated algorithms, mathematical calculations, and string manipulations

# ### 1. Hello World Program:

# In[1]:


print("Hello, World!")


# ### 2. Calculate the Sum of Two Numbers: 

# In[2]:


def sum_of_two_numbers(a, b):
    return a + b

num1 = 10
num2 = 20
result = sum_of_two_numbers(num1, num2)
print("Sum:", result)


# ### 3. Find the Largest Number in a List: 

# In[3]:


def find_largest_number(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

numbers_list = [10, 20, 5, 30, 15]
largest_number = find_largest_number(numbers_list)
print("Largest Number:", largest_number)


# ### 4. Check if a Number is Prime:

# In[4]:


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

num = 17
if is_prime(num):
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")


# ### 5. Convert Celsius to Fahrenheit: 

# In[5]:


def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius_value = 25
fahrenheit_value = celsius_to_fahrenheit(celsius_value)
print(f"{celsius_value} degrees Celsius is equal to {fahrenheit_value:.2f} degrees Fahrenheit.")


# ### 6. Calculate the Factorial of a Number: 

# In[6]:


def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

num = 5
factorial_result = factorial(num)
print(f"The factorial of {num} is {factorial_result}.")


# ### 7. Generate Fibonacci Series: 

# In[7]:


def fibonacci_series(n):
    fib_list = [0, 1]
    for i in range(2, n):
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list

n_terms = 10
fibonacci_list = fibonacci_series(n_terms)
print("Fibonacci Series:", fibonacci_list)


# ### 8. Check if a String is Palindrome: 

# In[8]:


def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

word = "level"
if is_palindrome(word):
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")


# ### 9. Count the Number of Words in a Sentence: 

# In[9]:


def count_words(sentence):
    words = sentence.split()
    return len(words)

sentence = "Hello, how are you today?"
word_count = count_words(sentence)
print("Number of words in the sentence:", word_count)


# ### 10.Find the Square Root of a Number: 

# In[10]:


def square_root(num):
    return num ** 0.5

num = 25
square_root_value = square_root(num)
print(f"The square root of {num} is {square_root_value:.2f}.")


# In[ ]:




