#!/usr/bin/env python
# coding: utf-8

# # Python Practice 291-300

# ## Here are the Python programs for the given objectives:

# ### 291. Calculate the Perimeter of a Reuleaux Pentagon Star with Rounded Corners and Right Alignment

# In[10]:


import math

def calculate_perimeter_reuleaux_pentagon_star(radius):
    # The perimeter of a Reuleaux pentagon star with rounded corners is the same as the perimeter of a regular pentagon
    perimeter = 5 * 2 * radius
    return perimeter

radius = 5 # Replace with the radius of the Reuleaux pentagon star
perimeter = calculate_perimeter_reuleaux_pentagon_star(radius)
print(f"Perimeter of the Reuleaux pentagon star with radius {radius} is: {perimeter:.2f}")


# ### 292. Print the Pattern of a Hollow Rhombus Star with Right Alignment

# In[9]:


def print_hollow_rhombus_star(rows):
    for i in range(1, rows + 1):
        for j in range(1, rows - i + 1):
            print(" ", end="")
        for j in range(1, rows + 1):
            if i == 1 or i == rows or j == 1 or j == rows:
                print("*", end="")
            else:
                print(" ", end="")
        print()

rows = 5 # Replace with the desired number of rows for the hollow rhombus star
print("Hollow Rhombus Star Pattern:")
print_hollow_rhombus_star(rows)


# ### 293. Generate a Random Word Cloud from Web Data (Note: Generating a random word cloud from web data requires web scraping, which may be subject to website terms of service and legal considerations. Make sure you have permission to scrape data from the website.)

# In[8]:


# To generate a random word cloud from web data, you can use popular web scraping libraries like BeautifulSoup and requests.
# In this example, we'll generate a word cloud from the Wikipedia page on "Python" using BeautifulSoup.

import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate_word_cloud(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        text = soup.get_text()
        wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.show()
    else:
        print(f"Failed to fetch data from {url}")

url = "https://en.wikipedia.org/wiki/Python_(programming_language)" # Replace with the URL of the webpage you want to scrape
generate_word_cloud(url)


# ### 294. Convert Decimal to Roman Numeral Using Recursive Approach

# In[7]:


def decimal_to_roman_recursive(num):
    if num <= 0:
        return ""
    elif num >= 1000:
        return "M" + decimal_to_roman_recursive(num - 1000)
    elif num >= 900:
        return "CM" + decimal_to_roman_recursive(num - 900)
    elif num >= 500:
        return "D" + decimal_to_roman_recursive(num - 500)
    elif num >= 400:
        return "CD" + decimal_to_roman_recursive(num - 400)
    elif num >= 100:
        return "C" + decimal_to_roman_recursive(num - 100)
    elif num >= 90:
        return "XC" + decimal_to_roman_recursive(num - 90)
    elif num >= 50:
        return "L" + decimal_to_roman_recursive(num - 50)
    elif num >= 40:
        return "XL" + decimal_to_roman_recursive(num - 40)
    elif num >= 10:
        return "X" + decimal_to_roman_recursive(num - 10)
    elif num >= 9:
        return "IX" + decimal_to_roman_recursive(num - 9)
    elif num >= 5:
        return "V" + decimal_to_roman_recursive(num - 5)
    elif num >= 4:
        return "IV" + decimal_to_roman_recursive(num - 4)
    elif num >= 1:
        return "I" + decimal_to_roman_recursive(num - 1)

decimal_number = 1984 # Replace with the decimal number you want to convert to Roman numeral
roman_numeral = decimal_to_roman_recursive(decimal_number)
print(f"Roman numeral representation of {decimal_number} is: {roman_numeral}")


# ### 295. Check if a Number is a Generalized Fermat Number

# In[6]:


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_generalized_fermat_number(number, p):
    if number < 1 or p < 2:
        return False
    return is_prime(number**(p-1) - 1)

number = 5 # Replace with the number you want to check
p = 3 # Replace with the power 'p' for the generalized Fermat number
result = is_generalized_fermat_number(number, p)
print(f"{number} is {'a' if result else 'not a'} generalized Fermat number with power {p}.")


# ### 296. Calculate the Volume of a Frustum of a Reuleaux Tetrahedron

# In[5]:


import math

def calculate_volume_of_frustum_of_reuleaux_tetrahedron(radius, height1, height2):
    # The volume of a frustum of a Reuleaux tetrahedron can be calculated as the difference between two volumes of Reuleaux tetrahedra.
    volume1 = (math.sqrt(2) / 12) * radius**3
    volume2 = (math.sqrt(2) / 12) * radius**3 * (height1**3 / height2**3)
    volume = volume2 - volume1
    return volume

radius = 5 # Replace with the radius of the Reuleaux tetrahedron
height1 = 10 # Replace with the larger height of the frustum of the Reuleaux tetrahedron
height2 = 5 # Replace with the smaller height of the frustum of the Reuleaux tetrahedron
volume = calculate_volume_of_frustum_of_reuleaux_tetrahedron(radius, height1, height2)
print(f"Volume of the frustum of the Reuleaux tetrahedron with radius {radius}, height1 {height1}, and height2 {height2} is: {volume:.2f}")


# ### 297. Implement Merge Sort Algorithm on a Linked List

# In[4]:


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_sort_linked_list(head):
    if not head or not head.next:
        return head
    
    def merge_sorted_lists(list1, list2):
        dummy = ListNode(0)
        current = dummy
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        current.next = list1 or list2
        return dummy.next
    
    def get_middle(head):
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        if prev:
            prev.next = None
        return slow
    
    left = head
    right = get_middle(head)
    
    left = merge_sort_linked_list(left)
    right = merge_sort_linked_list(right)
    
    return merge_sorted_lists(left, right)

# Example usage of merge_sort_linked_list
# Create a linked list: 4 -> 2 -> 1 -> 3
node4 = ListNode(4)
node2 = ListNode(2)
node1 = ListNode(1)
node3 = ListNode(3)
node4.next = node2
node2.next = node1
node1.next = node3
sorted_head = merge_sort_linked_list(node4)

# Print the sorted linked list
while sorted_head:
    print(sorted_head.val, end=" -> ")
    sorted_head = sorted_head.next


# ### 298. Find the Eulerian Numbers in a Range

# In[3]:


def calculate_binomial_coefficient(n, k):
    if k == 0 or k == n:
        return 1
    return calculate_binomial_coefficient(n - 1, k - 1) + calculate_binomial_coefficient(n - 1, k)

def find_eulerian_numbers(lower_bound, upper_bound):
    eulerian_numbers = []
    for n in range(lower_bound, upper_bound + 1):
        eulerian_number = 0
        for k in range(n + 1):
            eulerian_number += calculate_binomial_coefficient(n + 1, k) * (n - k) ** n * (-1) ** k
        eulerian_numbers.append(eulerian_number)
    return eulerian_numbers

lower_bound = 1 # Replace with the lower bound of the range to find Eulerian numbers
upper_bound = 10 # Replace with the upper bound of the range to find Eulerian numbers
eulerian_numbers = find_eulerian_numbers(lower_bound, upper_bound)
print("Eulerian numbers in the given range:")
print(eulerian_numbers)


# ### 299. Calculate the Perimeter of a Reuleaux Ellipse with Rounded Corners

# In[2]:


import math

def calculate_perimeter_reuleaux_ellipse(a, b):
    # The perimeter of a Reuleaux ellipse with rounded corners can be approximated using the perimeter of an ellipse.
    # Let's use the Ramanujan's formula for approximating the perimeter of an ellipse.
    h = ((a - b) ** 2) / ((a + b) ** 2)
    perimeter = math.pi * (a + b) * (1 + (3 * h) / (10 + math.sqrt(4 - 3 * h)))
    return perimeter

a = 6 # Replace with the major semi-axis of the Reuleaux ellipse
b = 3 # Replace with the minor semi-axis of the Reuleaux ellipse
perimeter = calculate_perimeter_reuleaux_ellipse(a, b)
print(f"Perimeter of the Reuleaux ellipse with major semi-axis {a} and minor semi-axis {b} is: {perimeter:.2f}")


# ### 300. Print the Pattern of a Hollow Floyd's Triangle Star

# In[1]:


def print_hollow_floyds_triangle_star(rows):
    num = 1
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            if i == rows or j == 1 or j == i:
                print("*", end="")
            else:
                print(" ", end="")
        num += 1
        print()

rows = 5 # Replace with the desired number of rows for the hollow Floyd's triangle star
print("Hollow Floyd's Triangle Star Pattern:")
print_hollow_floyds_triangle_star(rows)


# In[ ]:




