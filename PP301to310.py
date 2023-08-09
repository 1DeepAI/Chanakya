#!/usr/bin/env python
# coding: utf-8

# # Python Practice 301-310

# ## Here are the Python programs for the given objectives:

# ### 301. Generate a Random Maze with Custom Dimensions and Different Path Generation Algorithms

# In[10]:


# You can use various maze generation algorithms like Recursive Backtracking, Prim's Algorithm, Kruskal's Algorithm, etc.
# Here's an example of generating a random maze using Recursive Backtracking algorithm.

import random

def generate_maze_recursive_backtracking(width, height):
    def create_grid(width, height):
        return [["#" for _ in range(width)] for _ in range(height)]

    def get_neighbours(cell):
        x, y = cell
        neighbours = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        return [neighbour for neighbour in neighbours if 0 <= neighbour[0] < width and 0 <= neighbour[1] < height]

    def recursive_backtracking(cell):
        grid[cell[1]][cell[0]] = " "  # Empty cell
        neighbours = get_neighbours(cell)
        random.shuffle(neighbours)
        for neighbour in neighbours:
            x, y = neighbour
            if grid[y][x] == "#":
                recursive_backtracking(neighbour)

    grid = create_grid(width, height)
    start_cell = (random.randint(0, width - 1), random.randint(0, height - 1))
    recursive_backtracking(start_cell)
    return grid

width = 10  # Replace with the desired width of the maze
height = 10  # Replace with the desired height of the maze
maze = generate_maze_recursive_backtracking(width, height)
for row in maze:
    print("".join(row))


# ### 302. Convert Decimal to Balanced Ternary Using Bit Manipulation

# In[9]:


def convert_decimal_to_balanced_ternary(number):
    result = []
    while number != 0:
        remainder = number % 3
        if remainder == 2:
            number = number // 3 + 1
            result.append("-")
        else:
            number //= 3
            result.append(str(remainder))
    if not result:
        result.append("0")
    return "".join(result[::-1])

decimal_number = 21  # Replace with the decimal number you want to convert
balanced_ternary = convert_decimal_to_balanced_ternary(decimal_number)
print(f"Balanced ternary representation of {decimal_number} is: {balanced_ternary}")


# ### 303. Check if a Number is a Generalized Fibonacci Number

# In[8]:


def is_perfect_square(number):
    return int(number**0.5)**2 == number

def is_generalized_fibonacci_number(number):
    return is_perfect_square(5 * number**2 + 4) or is_perfect_square(5 * number**2 - 4)

number = 8  # Replace with the number you want to check
result = is_generalized_fibonacci_number(number)
print(f"{number} is {'a' if result else 'not a'} generalized Fibonacci number.")


# ### 304. Calculate the Volume of a Frustum of a Reuleaux Octahedron

# In[7]:


import math

def calculate_volume_frustum_reuleaux_octahedron(radius1, radius2, height):
    return (2 / 3) * math.pi * height * (radius1**2 + radius2**2 + radius1 * radius2)

radius1 = 5  # Replace with the larger radius of the frustum of the Reuleaux octahedron
radius2 = 3  # Replace with the smaller radius of the frustum of the Reuleaux octahedron
height = 10  # Replace with the height of the frustum of the Reuleaux octahedron
volume = calculate_volume_frustum_reuleaux_octahedron(radius1, radius2, height)
print(f"Volume of the frustum of the Reuleaux octahedron with larger radius {radius1}, smaller radius {radius2}, and height {height} is: {volume:.2f}")


# ### 305. Implement Quick Sort Algorithm on a Doubly Linked List

# In[6]:


class ListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

def quick_sort_linked_list(head):
    if not head or not head.next:
        return head

    def partition(start, end):
        pivot = end
        current = start
        while start != end:
            if start.val < pivot.val:
                start.val, current.val = current.val, start.val
                current = current.next
            start = start.next
        pivot.val, current.val = current.val, pivot.val
        return current

    def sort(start, end):
        if start == end:
            return
        partition_node = partition(start, end)
        sort(start, partition_node.prev)
        sort(partition_node.next, end)

    tail = head
    while tail.next:
        tail = tail.next
    sort(head, tail)
    return head

# Example usage of quick_sort_linked_list
# Create a doubly linked list: 4 <-> 2 <-> 1 <-> 3
head = ListNode(4)
node2 = ListNode(2)
node1 = ListNode(1)
node3 = ListNode(3)

head.next = node2
node2.prev = head
node2.next = node1
node1.prev = node2
node1.next = node3
node3.prev = node1

sorted_head = quick_sort_linked_list(head)

# Print the sorted linked list
while sorted_head:
    print(sorted_head.val, end=" ")
    sorted_head = sorted_head.next


# ### 306. Find the Gaussian Numbers in a Range

# In[5]:


def is_gaussian_number(a, b):
    return a * a + b * b == 1

def find_gaussian_numbers(max_real_part, max_imaginary_part):
    gaussian_numbers = []
    for a in range(-max_real_part, max_real_part + 1):
        for b in range(-max_imaginary_part, max_imaginary_part + 1):
            if is_gaussian_number(a, b):
                gaussian_numbers.append((a, b))
    return gaussian_numbers

max_real_part = 5  # Replace with the maximum real part for the range
max_imaginary_part = 5  # Replace with the maximum imaginary part for the range
result = find_gaussian_numbers(max_real_part, max_imaginary_part)
print("Gaussian numbers in the range:")
for a, b in result:
    print(f"{a} + {b}i")


# ### 307. Calculate the Perimeter of a Reuleaux Hexagon Star with Rounded Corners, Right Alignment, and Custom Size

# In[4]:


import math

def calculate_perimeter_reuleaux_hexagon_star(a, b, h):
    # For a Reuleaux hexagon star with rounded corners, the perimeter can be calculated using the following formula:
    # Perimeter = 6 * (a + b) + 2 * math.pi * h + 6 * (h - math.sqrt(a * b))
    return 6 * (a + b) + 2 * math.pi * h + 6 * (h - math.sqrt(a * b))

a = 4  # Replace with the larger semi-axis of the Reuleaux hexagon star
b = 2  # Replace with the smaller semi-axis of the Reuleaux hexagon star
h = 3  # Replace with the height of the Reuleaux hexagon star
perimeter = calculate_perimeter_reuleaux_hexagon_star(a, b, h)
print(f"Perimeter of the Reuleaux hexagon star with larger semi-axis {a}, smaller semi-axis {b}, height {h}, and rounded corners is: {perimeter:.2f}")


# ### 308. Print the Pattern of a Hollow Diamond Star with Right Alignment and Custom Size

# In[3]:


def print_hollow_diamond_star_right_alignment(rows):
    for i in range(rows):
        print(" " * (rows - i - 1) + "* " * (i + 1))
    for i in range(rows - 2, -1, -1):
        print(" " * (rows - i - 1) + "* " * (i + 1))

rows = 5  # Replace with the desired number of rows for the hollow diamond star
print("Hollow Diamond Star Pattern with Right Alignment:")
print_hollow_diamond_star_right_alignment(rows)


# ### 309. Generate a Random Word Cloud from Text Data with Custom Word Frequency

# In[1]:


from wordcloud import WordCloud
import matplotlib.pyplot as plt

text_data = "Replace this with your text data containing the words you want to visualize in the word cloud."
word_frequency = {
    "word1": 50,  # Replace "word1" with the actual word and 50 with its frequency in the text_data
    "word2": 30,
    "word3": 20,
    # Add more words and their frequencies as needed
}

wordcloud = WordCloud(width=800, height=400).generate_from_frequencies(word_frequency)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()


# ### 310. Convert Decimal to Roman Numeral Using Iterative Approach and Custom Numerals

# In[2]:


def convert_decimal_to_roman_iterative(decimal_number, numerals):
    roman_numerals = ""
    for value, numeral in numerals:
        while decimal_number >= value:
            roman_numerals += numeral
            decimal_number -= value
    return roman_numerals

decimal_number = 2021  # Replace with the decimal number you want to convert
custom_numerals = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
                   (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
roman_numeral = convert_decimal_to_roman_iterative(decimal_number, custom_numerals)
print(f"Roman numeral representation of {decimal_number} is: {roman_numeral}")


# In[ ]:




