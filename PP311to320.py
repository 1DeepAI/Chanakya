#!/usr/bin/env python
# coding: utf-8

# # Python Practice 311-320

# ## Here are the Python programs for the given objectives:

# ### 311. Check if a Number is a Generalized Harmonic Number

# In[ ]:


def is_generalized_harmonic_number(number, r):
    # Generalized harmonic number H(n, r) is the sum of the reciprocals of the rth powers of the first n natural numbers.
    # H(n, r) = 1/1^r + 1/2^r + 1/3^r + ... + 1/n^r

    if number <= 0 or r <= 0:
        return False

    sum_harmonic = 0
    for i in range(1, number + 1):
        sum_harmonic += 1 / (i ** r)

    return sum_harmonic

number = 5  # Replace with the number you want to check
r = 3  # Replace with the power of the harmonic number
result = is_generalized_harmonic_number(number, r)
print(f"{number} is {'a' if result else 'not a'} generalized harmonic number with power {r}.")


# ### 312. Calculate the Volume of a Frustum of a Reuleaux Dodecahedron

# In[ ]:


import math

def calculate_volume_frustum_reuleaux_dodecahedron(radius1, radius2, height):
    return (1 / 3) * math.pi * height * (radius1**2 + radius2**2 + radius1 * radius2)

radius1 = 5  # Replace with the larger radius of the frustum of the Reuleaux dodecahedron
radius2 = 3  # Replace with the smaller radius of the frustum of the Reuleaux dodecahedron
height = 10  # Replace with the height of the frustum of the Reuleaux dodecahedron
volume = calculate_volume_frustum_reuleaux_dodecahedron(radius1, radius2, height)
print(f"Volume of the frustum of the Reuleaux dodecahedron with larger radius {radius1}, smaller radius {radius2}, and height {height} is: {volume:.2f}")


# ### 313. Implement Merge Sort Algorithm on a Circular Linked List

# In[ ]:


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_sort_circular_linked_list(head):
    if not head or not head.next:
        return head

    def get_mid(node):
        slow = node
        fast = node.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == node or fast == node:
                break
        return slow

    def merge(left, right):
        dummy = ListNode()
        current = dummy
        while left and right:
            if left.val <= right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next
        current.next = left or right
        return dummy.next

    def merge_sort(node):
        if not node or node.next == node:
            return node

        mid = get_mid(node)
        mid_next = mid.next
        mid.next = None

        left = merge_sort(node)
        right = merge_sort(mid_next)
        return merge(left, right)

    tail = head
    while tail.next:
        tail = tail.next
    tail.next = head  # Make the linked list circular
    sorted_head = merge_sort(head)
    tail.next = None  # Break the circular link
    return sorted_head

# Example usage of merge_sort_circular_linked_list
# Create a circular linked list: 4 -> 2 -> 1 -> 3 -> 4 (points back to 4)
head = ListNode(4)
node2 = ListNode(2)
node1 = ListNode(1)
node3 = ListNode(3)

head.next = node2
node2.next = node1
node1.next = node3
node3.next = head

sorted_head = merge_sort_circular_linked_list(head)

# Print the sorted circular linked list
current = sorted_head
while current:
    print(current.val, end=" -> ")
    current = current.next
    if current == sorted_head:
        break


# ### 314. Find the Lucas-Lehmer Numbers in a Range

# In[9]:


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def find_lucas_lehmer_numbers(max_exponent):
    lucas_lehmer_numbers = []
    for exponent in range(2, max_exponent + 1):
        if is_prime(2 ** exponent - 1):
            lucas_lehmer_numbers.append(2 ** exponent - 1)
    return lucas_lehmer_numbers

max_exponent = 10  # Replace with the maximum exponent for the range
result = find_lucas_lehmer_numbers(max_exponent)
print("Lucas-Lehmer numbers in the range:")
print(result)


# ### 315. Calculate the Perimeter of a Reuleaux Pentagon Star with Rounded Corners, Right Alignment, and Custom Size

# In[8]:


import math

def calculate_perimeter_reuleaux_pentagon_star(a, b, h):
    # For a Reuleaux pentagon star with rounded corners, the perimeter can be calculated using the following formula:
    # Perimeter = 5 * (a + b) + 2 * math.pi * h + 5 * (h - math.sqrt(a * b))
    return 5 * (a + b) + 2 * math.pi * h + 5 * (h - math.sqrt(a * b))

a = 4  # Replace with the larger semi-axis of the Reuleaux pentagon star
b = 2  # Replace with the smaller semi-axis of the Reuleaux pentagon star
h = 3  # Replace with the height of the Reuleaux pentagon star
perimeter = calculate_perimeter_reuleaux_pentagon_star(a, b, h)
print(f"Perimeter of the Reuleaux pentagon star with larger semi-axis {a}, smaller semi-axis {b}, height {h}, and rounded corners is: {perimeter:.2f}")


# ### 316. Print the Pattern of a Hollow Rhombus Star with Right Alignment and Custom Size

# In[7]:


def print_hollow_rhombus_star_right_alignment(rows):
    for i in range(rows):
        print(" " * (rows - i - 1) + "* " * rows)

rows = 5  # Replace with the desired number of rows for the hollow rhombus star
print("Hollow Rhombus Star Pattern with Right Alignment:")
print_hollow_rhombus_star_right_alignment(rows)


# ### 317. Generate a Random Word Cloud from Web Data with Custom Word Frequency and Size

# In[6]:


from wordcloud import WordCloud
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import re

def get_web_data(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        # Replace <tag_name> with the HTML tag containing the text you want to extract from the webpage
        # Use regex to remove any unwanted characters or symbols from the extracted text
        text_data = " ".join(re.findall(r'\b\w+\b', " ".join(tag.get_text() for tag in soup.find_all("<tag_name>"))))
        return text_data
    except Exception as e:
        print(f"Error: {e}")
        return ""

url = "https://www.example.com"  # Replace with the URL of the webpage you want to fetch data from
word_frequency = {
    "word1": 50,  # Replace "word1" with the actual word and 50 with its frequency in the fetched web data
    "word2": 30,
    "word3": 20,
    # Add more words and their frequencies as needed
}

wordcloud = WordCloud(width=800, height=400).generate_from_frequencies(word_frequency)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()


# ### 318. Convert Decimal to Gray Code Using Recursive Approach

# In[5]:


def convert_decimal_to_gray_recursive(decimal_number):
    if decimal_number == 0:
        return 0
    else:
        return decimal_number ^ (decimal_number >> 1)

decimal_number = 21  # Replace with the decimal number you want to convert
gray_code = convert_decimal_to_gray_recursive(decimal_number)
print(f"Gray code representation of {decimal_number} is: {gray_code}")


# ### 319. Check if a Number is a Generalized Hexagonal Number

# In[1]:


def is_generalized_hexagonal_number(number, n):
    # A generalized hexagonal number H(n) = n(2n−1).
    # Given n, check if the number is a generalized hexagonal number.

    if number < 1 or n < 1:
        return False

    return number == n * (2 * n - 1)

number = 15  # Replace with the number you want to check
n = 5  # Replace with the value of n for the generalized hexagonal number
result = is_generalized_hexagonal_number(number, n)
print(f"{number} is {'a' if result else 'not a'} generalized hexagonal number with n = {n}.")


# ### 320. Calculate the Volume of a Frustum of a Regular Tetrahedron with Custom Height3

# In[4]:


def calculate_volume_frustum_regular_tetrahedron(base_edge1, base_edge2, height1, height2):
    # Given two edges (base_edge1 and base_edge2) of a regular tetrahedron and their corresponding heights (height1 and height2),
    # the volume of the frustum of the regular tetrahedron can be calculated using the formula:
    # Volume = 1/3 * h1 * (A1 + sqrt(A1 * A2) + A2)

    area1 = (3 ** 0.5 / 4) * base_edge1 * height1
    area2 = (3 ** 0.5 / 4) * base_edge2 * height2

    return (1 / 3) * height1 * (area1 + (area1 * area2) ** 0.5 + area2)

base_edge1 = 5  # Replace with the first base edge of the regular tetrahedron
base_edge2 = 3  # Replace with the second base edge of the regular tetrahedron
height1 = 8  # Replace with the first height of the regular tetrahedron
height2 = 5  # Replace with the second height of the regular tetrahedron
volume = calculate_volume_frustum_regular_tetrahedron(base_edge1, base_edge2, height1, height2)
print(f"Volume of the frustum of the regular tetrahedron with base edges {base_edge1} and {base_edge2}, heights {height1} and {height2} is: {volume:.2f}")


# In[ ]:




