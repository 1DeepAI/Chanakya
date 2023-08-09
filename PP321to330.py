#!/usr/bin/env python
# coding: utf-8

# # Python Practice 321-330

# ## Here are the Python programs for the given objectives:

# ### 321. Implement Radix Sort Algorithm on a Linked List

# In[ ]:


# Implementation of the Radix Sort algorithm on a singly linked list

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def radix_sort_linked_list(head):
    if not head or not head.next:
        return head

    # Find the maximum number in the linked list
    max_value = head.value
    current = head.next
    while current:
        max_value = max(max_value, current.value)
        current = current.next

    exp = 1
    while max_value // exp > 0:
        head = counting_sort_linked_list(head, exp)
        exp *= 10

    return head

def counting_sort_linked_list(head, exp):
    count = [0] * 10
    output = [0] * 10
    current = head

    while current:
        count[(current.value // exp) % 10] += 1
        current = current.next

    for i in range(1, 10):
        count[i] += count[i - 1]

    current = head
    while current:
        output[count[(current.value // exp) % 10] - 1] = current.value
        count[(current.value // exp) % 10] -= 1
        current = current.next

    current = head
    for i in range(10):
        current.value = output[i]
        current = current.next

    return head

# Example usage
# Construct a sample linked list: 170 -> 45 -> 75 -> 90 -> 802 -> 24 -> 2 -> 66
head = ListNode(170)
head.next = ListNode(45)
head.next.next = ListNode(75)
head.next.next.next = ListNode(90)
head.next.next.next.next = ListNode(802)
head.next.next.next.next.next = ListNode(24)
head.next.next.next.next.next.next = ListNode(2)
head.next.next.next.next.next.next.next = ListNode(66)

sorted_head = radix_sort_linked_list(head)

# Print the sorted linked list
current = sorted_head
while current:
    print(current.value, end=" -> ")
    current = current.next


# ### 322. Find the Magic Square Numbers in a Range

# In[ ]:


def is_magic_square_number(num):
    # A magic square number is a number that is the sum of all the elements in a 3x3 magic square.
    # A 3x3 magic square is a square matrix with unique positive integers such that each row, column, and diagonal
    # has the same sum.
    # Here, we can check if a number is a magic square number by brute force approach.

    def is_magic_square(matrix):
        target_sum = sum(matrix[0])

        # Check rows
        for row in matrix:
            if sum(row) != target_sum:
                return False

        # Check columns
        for col in range(3):
            if sum(matrix[row][col] for row in range(3)) != target_sum:
                return False

        # Check diagonals
        if sum(matrix[i][i] for i in range(3)) != target_sum or sum(matrix[i][2 - i] for i in range(3)) != target_sum:
            return False

        return True

    for a in range(1, num // 2 + 1):
        for b in range(a + 1, num - a):
            c = num - a - b
            matrix = [[a, b, c], [b, c, a], [c, a, b]]
            if is_magic_square(matrix):
                return True

    return False

# Example usage
num = 50  # Replace with the number you want to check
result = is_magic_square_number(num)
print(f"{num} is {'a' if result else 'not a'} magic square number.")


# ### 323. Calculate the Perimeter of a Reuleaux Ellipse with Rounded Corners and Custom Size

# In[ ]:


import math

def calculate_perimeter_reuleaux_ellipse(a, b, h):
    # For a Reuleaux ellipse with rounded corners, the perimeter can be calculated using the following formula:
    # Perimeter = 4 * (a + b) + 2 * math.pi * h

    return 4 * (a + b) + 2 * math.pi * h

a = 5  # Replace with the first semi-axis of the Reuleaux ellipse
b = 3  # Replace with the second semi-axis of the Reuleaux ellipse
h = 4  # Replace with the height of the Reuleaux ellipse
perimeter = calculate_perimeter_reuleaux_ellipse(a, b, h)
print(f"Perimeter of the Reuleaux ellipse with first semi-axis {a}, second semi-axis {b}, and height {h} is: {perimeter:.2f}")


# ### 324. Print the Pattern of a Hollow Sierpinski Triangle Star with Custom Size

# In[ ]:


def print_hollow_sierpinski_triangle_star(size):
    def print_star_pattern(row, col):
        return row % 2 != col % 2

    for row in range(size):
        for col in range(size * 2 - 1):
            if print_star_pattern(row, col):
                print("*", end="")
            else:
                print(" ", end="")
        print()

size = 5  # Replace with the size of the pattern you want to print
print_hollow_sierpinski_triangle_star(size)


# ### 325. Generate a Random Huffman Coding Tree from Web Data

# In[ ]:


import requests
from bs4 import BeautifulSoup
import re
import random

def generate_random_huffman_tree_from_web_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.get_text()

    # Remove special characters and split text into words
    words = re.findall(r'\w+', text)

    # Create a dictionary with word frequencies
    word_frequency = {}
    for word in words:
        word_frequency[word] = word_frequency.get(word, 0) + 1

    # Create a list of (word, frequency) tuples
    word_frequency_list = list(word_frequency.items())

    # Sort the list based on frequency in descending order
    word_frequency_list.sort(key=lambda x: x[1], reverse=True)

    # Generate the Huffman coding tree
    while len(word_frequency_list) > 1:
        left = word_frequency_list.pop()
        right = word_frequency_list.pop()
        combined_word = f"{left[0]}{right[0]}"
        combined_frequency = left[1] + right[1]
        word_frequency_list.append((combined_word, combined_frequency))
        word_frequency_list.sort(key=lambda x: x[1], reverse=True)

    return word_frequency_list[0][0]

url = "https://en.wikipedia.org/wiki/Huffman_coding"  # Replace with the URL you want to use for generating the tree
huffman_tree = generate_random_huffman_tree_from_web_data(url)
print(f"Randomly generated Huffman coding tree from web data: {huffman_tree}")


# ### 326. Convert Decimal to Excess-K Code Using Recursion and Custom K

# In[ ]:


def decimal_to_excess_k_code(number, k):
    if number == 0:
        return "0"
    if number < 0:
        return ""

    return decimal_to_excess_k_code(number // k, k) + str(number % k)

number = 17  # Replace with the decimal number you want to convert
k = 3  # Replace with the value of k for the excess-k code
excess_k_code = decimal_to_excess_k_code(number, k)
print(f"The excess-{k} code of {number} is: {excess_k_code}")


# ### 327. Check if a Number is a Generalized Heptagonal Number

# In[ ]:


def is_generalized_heptagonal_number(num):
    # A number is a generalized heptagonal number if it can be represented in the form n(5n-3)/2 for some positive integer n.

    def is_perfect_square(number):
        root = int(number ** 0.5)
        return root * root == number

    def is_pentagonal_number(number):
        # A number is a pentagonal number if it can be represented in the form n(3n-1)/2 for some positive integer n.
        return is_perfect_square(24 * number + 1) and (int((24 * number + 1) ** 0.5) + 1) % 6 == 0

    # A generalized heptagonal number is also a pentagonal number.
    return is_pentagonal_number(num)

# Example usage
num = 41  # Replace with the number you want to check
result = is_generalized_heptagonal_number(num)
print(f"{num} is {'a' if result else 'not a'} generalized heptagonal number.")


# ### 328. Calculate the Volume of a Frustum of a Regular Octahedron with Custom Height

# In[ ]:


def calculate_volume_frustum_regular_octahedron(base_edge1, base_edge2, height):
    # For a frustum of a regular octahedron, the volume can be calculated using the following formula:
    # Volume = (1/3) * ((base_edge1^2 + base_edge2^2 + base_edge1 * base_edge2) * height)

    return (1 / 3) * ((base_edge1 ** 2 + base_edge2 ** 2 + base_edge1 * base_edge2) * height)

base_edge1 = 5  # Replace with the first base edge of the frustum
base_edge2 = 3  # Replace with the second base edge of the frustum
height = 7  # Replace with the height of the frustum
volume = calculate_volume_frustum_regular_octahedron(base_edge1, base_edge2, height)
print(f"Volume of the frustum of a regular octahedron with first base edge {base_edge1}, second base edge {base_edge2}, and height {height} is: {volume:.2f}")


# ### 329. Implement Quick Sort Algorithm on a Circular Linked List with Custom Pivot

# In[ ]:


# Definition for a node of the circular linked list
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def quick_sort_linked_list(head, pivot):
    if not head:
        return None

    # Partition the list into three sublists: less than pivot, equal to pivot, and greater than pivot
    less_head = less_tail = ListNode()
    equal_head = equal_tail = ListNode()
    greater_head = greater_tail = ListNode()

    current = head
    while current:
        if current.value < pivot:
            less_tail.next = current
            less_tail = less_tail.next
        elif current.value == pivot:
            equal_tail.next = current
            equal_tail = equal_tail.next
        else:
            greater_tail.next = current
            greater_tail = greater_tail.next

        current = current.next

    # Join the three sublists together
    less_tail.next = None
    equal_tail.next = None
    greater_tail.next = None

    # Recursively sort the less and greater sublists
    less_head = quick_sort_linked_list(less_head.next, pivot)
    greater_head = quick_sort_linked_list(greater_head.next, pivot)

    # Concatenate the three sorted sublists
    sorted_head = concatenate_linked_lists(less_head, equal_head.next)
    sorted_head = concatenate_linked_lists(sorted_head, greater_head)

    return sorted_head

def concatenate_linked_lists(head1, head2):
    if not head1:
        return head2
    if not head2:
        return head1

    current = head1
    while current.next:
        current = current.next

    current.next = head2
    return head1

# Example usage
# Construct a sample circular linked list: 3 -> 5 -> 1 -> 8 -> 4
head = ListNode(3)
head.next = ListNode(5)
head.next.next = ListNode(1)
head.next.next.next = ListNode(8)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = head

pivot = 4  # Replace with the pivot value you want to use for sorting
sorted_head = quick_sort_linked_list(head, pivot)

# Print the sorted linked list
current = sorted_head
while current.next != sorted_head:
    print(current.value, end=" -> ")
    current = current.next
print(current.value)


# ### 330. Find the Menage Numbers in a Range

# In[ ]:


def find_menage_numbers_in_range(start, end):
    # A Menage number is a number that can be expressed as (n-1)*(2n-1) for some positive integer n.
    menage_numbers = []
    n = 1
    while (n - 1) * (2 * n - 1) <= end:
        menage_number = (n - 1) * (2 * n - 1)
        if menage_number >= start:
            menage_numbers.append(menage_number)
        n += 1

    return menage_numbers

# Example usage
start_range = 1  # Replace with the starting range value
end_range = 100  # Replace with the ending range value
menage_numbers = find_menage_numbers_in_range(start_range, end_range)
print(f"Menage numbers in the range {start_range} to {end_range}: {menage_numbers}")


# In[ ]:




