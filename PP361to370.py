#!/usr/bin/env python
# coding: utf-8

# # Python Practice 361-370

# ## Here are Python programs for the specified objectives:

# ### 361. Implement Quick Sort Algorithm on a Doubly Linked List with Custom Pivot and Partition Scheme
# Expected Output: 
# Original Linked List:
# 7 3 9 5 1 8 6 2 4 
# 
# Sorted Linked List:
# 1 2 3 4 5 6 7 8 9
# 

# In[1]:


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def print_list(head):
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()


def partition(head, tail, pivot):
    pivot_node = pivot
    pivot_data = pivot.data

    while head != pivot_node:
        if head.data > pivot_data:
            prev_head = head.prev
            prev_tail = tail.prev

            # Swap the nodes
            if prev_head:
                prev_head.next = tail
            else:
                head = tail

            if prev_tail:
                prev_tail.next = head
            else:
                tail = head

            head.prev, tail.next = tail, head

        head = head.next

    return head, pivot_node


def quick_sort_doubly_linked_list(head, tail):
    if not head or head == tail:
        return head

    pivot = tail
    head, tail = partition(head, tail, pivot)

    pivot.prev = quick_sort_doubly_linked_list(pivot.prev, head.prev)
    pivot.next = quick_sort_doubly_linked_list(pivot.next, tail)

    return head


def append_to_linked_list(head, data):
    new_node = Node(data)
    if not head:
        return new_node

    current = head
    while current.next:
        current = current.next

    current.next = new_node
    new_node.prev = current
    return head


if __name__ == "__main__":
    # Create a doubly linked list with custom elements
    linked_list = None
    elements = [7, 3, 9, 5, 1, 8, 6, 2, 4]

    for element in elements:
        linked_list = append_to_linked_list(linked_list, element)

    # Print the original linked list
    print("Original Linked List:")
    print_list(linked_list)

    # Perform quick sort on the doubly linked list
    linked_list = quick_sort_doubly_linked_list(linked_list, None)

    # Print the sorted linked list
    print("\nSorted Linked List:")
    print_list(linked_list)


# ### 362. Find the Parabolic Catalan Numbers in a Range

# In[2]:


def binomial_coefficient(n, k):
    if k > n - k:
        k = n - k
    res = 1
    for i in range(k):
        res *= (n - i)
        res //= (i + 1)
    return res


def parabolic_catalan_number(n):
    if n <= 0:
        return 1
    return binomial_coefficient(2 * n, n) // (n + 1)


def parabolic_catalan_numbers_in_range(start, end):
    result = []
    for i in range(start, end + 1):
        result.append(parabolic_catalan_number(i))
    return result


if __name__ == "__main__":
    start_range = 0
    end_range = 10

    parabolic_catalan_numbers = parabolic_catalan_numbers_in_range(start_range, end_range)

    print(f"Parabolic Catalan Numbers in the range [{start_range}, {end_range}]:")
    print(parabolic_catalan_numbers)


# ### 363. Calculate the Perimeter of a Reuleaux Pentagon Star with Rounded Corners, Right Alignment, Custom Size, and Custom Side Lengths. we can follow these steps:
# 
# 1. Define a function to calculate the side length of the Reuleaux pentagon star based on the custom size.
# 2. Define a function to calculate the perimeter of the Reuleaux pentagon star using the side length.
# 3. Display the calculated perimeter as the expected output.

# In[3]:


import math

def reuleaux_pentagon_star_side_length(custom_size):
    inner_radius = custom_size / 2
    outer_radius = inner_radius + custom_size
    return outer_radius * math.cos(math.pi / 10) - inner_radius * math.sin(math.pi / 10)


def reuleaux_pentagon_star_perimeter(custom_size, custom_side_length):
    return 5 * custom_side_length


if __name__ == "__main__":
    custom_size = 10
    custom_side_length = reuleaux_pentagon_star_side_length(custom_size)
    perimeter = reuleaux_pentagon_star_perimeter(custom_size, custom_side_length)

    print(f"Perimeter of Reuleaux Pentagon Star with Custom Size ({custom_size}) "
          f"and Custom Side Lengths ({custom_side_length}): {perimeter}")


# ### 364. Print the Pattern of a Hollow Rhombus Star with Right Alignment, Custom Size, and Custom Rhombus Width. we can follow these steps:
# 
# 1. Define a function to print spaces for right alignment.
# 2. Define a function to print the hollow rhombus star pattern based on custom size and custom rhombus width.
# 3. Display the pattern as the expected output.
# 

# In[4]:


def print_spaces(n):
    for i in range(n):
        print(" ", end="")


def print_hollow_rhombus_star(custom_size, custom_width):
    for i in range(1, custom_size + 1):
        print_spaces(custom_size - i)
        if i == 1 or i == custom_size:
            print("*" * custom_width)
        else:
            print("*" + " " * (custom_width - 2) + "*")


if __name__ == "__main__":
    custom_size = 5
    custom_width = 7

    print(f"Hollow Rhombus Star Pattern with Custom Size ({custom_size}) "
          f"and Custom Width ({custom_width}):")
    print_hollow_rhombus_star(custom_size, custom_width)


# ### 365. Generate a Random Word Cloud from Web Data with Custom Word Frequency, Size, Color, and Font. 
# Creating a word cloud involves several steps:
# 
# 1. Fetching web data: We'll use the requests library to fetch data from the web.
# 2. Text cleaning and pre-processing: This involves removing common words, HTML tags, etc. We'll use BeautifulSoup for HTML parsing.
# 3. Generating a word cloud: We'll use the wordcloud library.
# 
# Expected Output:
# 
# When you run the code, you should see a word cloud image pop up, displaying the most frequent words from the web page in various sizes and colors.
# Customization:
# 
# Word Frequency: The word cloud automatically computes word frequencies.
# Size: Adjust the width and height in the WordCloud() initialization.
# Color: You can use any matplotlib colormap for the colormap parameter.
# Font: Download a .ttf font file and provide the path to the font_path parameter.
# Required libraries:
# 
# You'll need to install requests, beautifulsoup4, wordcloud, and matplotlib using pip:
# 
# NOTE: Remember, this is a simple word cloud generator, and there are numerous ways you can expand upon this, such as using more advanced tokenization or leveraging other Python libraries to improve data cleaning.

# In[ ]:


import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

def fetch_web_data(url):
    """
    Fetch web content from a given URL and return the textual data.
    """
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Failed to fetch data from the web.")
    
    return response.text

def clean_and_parse_html(content):
    """
    Parse HTML content using BeautifulSoup and return the textual data.
    """
    soup = BeautifulSoup(content, "html.parser")
    for script in soup(["script", "style"]):  # Remove script and style elements
        script.decompose()
    return " ".join(soup.stripped_strings)

def generate_word_cloud(text, font_path='path_to_font.ttf'):
    """
    Generate a word cloud from the given text.
    """
    # Define stopwords and any other customizations
    stopwords = set(STOPWORDS)

    # Define word cloud parameters
    wc = WordCloud(
        width=800,
        height=600,
        background_color="white",
        stopwords=stopwords,
        max_words=200,
        font_path=font_path,
        min_font_size=10,
        colormap="viridis"
    )

    # Generate word cloud
    wc.generate(text)

    # Display the word cloud
    plt.figure(figsize=(10, 8))
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()

if __name__ == "__main__":
    url = "https://www.example.com"  # Replace with your target URL
    content = fetch_web_data(url)
    text = clean_and_parse_html(content)
    generate_word_cloud(text)


# ### 366. Convert Decimal to Excess-K Code Using Bit Manipulation and Custom K with Variable Size
# Excess-K encoding, also known as Bias-K encoding, is a form of binary encoding where the actual represented value is the value in binary plus a bias of K. So, for an Excess-K code, to get the original number, you subtract K from the decoded number. This encoding is particularly useful in certain computer arithmetic contexts.
# 
# For example, with Excess-8 encoding:
# 
# The decimal 0 is encoded as 1000 (i.e., 8 in binary).
# The decimal 1 is encoded as 1001 (i.e., 9 in binary).
# The decimal -1 is encoded as 0111 (i.e., 7 in binary).
# Here's how to implement this:

# In[10]:


def decimal_to_excess_k(number, K, size):
    """
    Convert a decimal number to its Excess-K representation.
    :param number: Integer, the decimal number.
    :param K: Integer, the bias for Excess-K encoding.
    :param size: Integer, the number of bits in the representation.
    :return: String, the Excess-K representation.
    """
    # Calculate the Excess-K value
    excess_k_value = number + K

    # Ensure the value can be represented with the given number of bits
    if excess_k_value >= 2 ** size or excess_k_value < 0:
        raise ValueError("The number can't be represented with the given number of bits using Excess-K encoding.")

    # Convert the value to binary and pad with zeros to the required size
    return format(excess_k_value, f'0{size}b')

# Test
K = 8
size = 4
numbers = [-8, -7, -1, 0, 1, 7]

for number in numbers:
    print(f"Decimal: {number} -> Excess-{K}: {decimal_to_excess_k(number, K, size)}")


# ### 367. Check if a Number is a Generalized Pyramidal Pentagonal Number
# First, let's clarify what a generalized pyramidal pentagonal number is.
# 
# A generalized pyramidal pentagonal number is the summation of the first n pentagonal numbers. The formula for the nth pentagonal number is:
# 
# P(n)= (n(3n−1))/ 2	
#  
# So, the generalized pyramidal pentagonal number for n would be:
# 
# GP(n)=∑ i=1 n​	P(i)
# 
# Let's write the code to check if a given number is a generalized pyramidal pentagonal number:

# In[11]:


def pentagonal(n):
    """Return the nth pentagonal number."""
    return n * (3 * n - 1) // 2

def is_generalized_pyramidal_pentagonal(num):
    """Check if a number is a generalized pyramidal pentagonal number."""
    summation = 0
    n = 1

    while summation < num:
        summation += pentagonal(n)
        if summation == num:
            return True
        n += 1

    return False

# Test
numbers = [1, 5, 12, 22, 70, 145, 9801]

for number in numbers:
    if is_generalized_pyramidal_pentagonal(number):
        print(f"{number} is a generalized pyramidal pentagonal number.")
    else:
        print(f"{number} is NOT a generalized pyramidal pentagonal number.")


# ### 368. Calculate the Volume of a Frustum of a Regular Icosahedron with Custom Height and Base Length
# To solve this problem, we need to understand a bit of geometry regarding the regular icosahedron and its frustum.
# 
# A regular icosahedron is a polyhedron with 20 equilateral triangular faces. A frustum of an icosahedron is obtained by cutting off the top part by a plane that's parallel to the base.
# 
# Here's a general approach:
# 1. Volume of a Regular Icosahedron:
# The formula for the volume 
# V
# V of an icosahedron with edge length 
# a
# a is:...(1)
#  
# 2. Height of a Regular Icosahedron:
# The height 
# h
# h of an icosahedron with edge length 
# a
# a can be found using Pythagoras' theorem and is:...(2)
#  
# 3. Volume of a Frustum:
# To find the volume of a frustum of the icosahedron, we'll use the formula for the volume of a frustum:...(3)
# 

# In[12]:


import math

def icosahedron_volume(a):
    """Return the volume of a regular icosahedron with edge length a."""
    return (5 * (3 + math.sqrt(5)) * a**3) / 12

def icosahedron_height(a):
    """Return the height of a regular icosahedron with edge length a."""
    return (a * math.sqrt(3 * (5 + math.sqrt(5)))) / 2

def frustum_volume(a, h_frustum):
    """Return the volume of a frustum of a regular icosahedron with base edge length a and height h_frustum."""
    h_ico = icosahedron_height(a)
    ratio = h_frustum / h_ico

    A1 = (1 - ratio)**2
    A2 = 1

    return h_frustum / 3 * (A1 + A2 + math.sqrt(A1 * A2)) * (5 * math.sqrt(3) * a**2) / 4

# Test
a = 2
h_frustum = 2.5

print(f"Volume of the frustum of the icosahedron with base edge length {a} and height {h_frustum} is: {frustum_volume(a, h_frustum)}")


# ### 369. Implement Merge Sort Algorithm on a Circular Linked List with Custom Merge and Comparison Functions
# Let's break down the problem:
# 
# 1. Circular Linked List (CLL): A CLL is similar to a regular singly linked list, but the last node's next pointer points to the head of the list instead of None.
# 2. Merge Sort on Linked List: The logic of merge sort for linked lists is slightly different from arrays. We don't have direct access to middle elements. So, the idea is to split the linked list into two halves (using Floyd's cycle-finding algorithm), sort each half recursively, and then merge them.
# 
# Given the custom requirements for merge and comparison functions, we'll have placeholders for those and use them as needed.
# 
# Expected Output:
# Original Circular Linked List:
# 3 -> 5 -> 2 -> 1 -> 4
# Sorted Circular Linked List:
# 1 -> 2 -> 3 -> 4 -> 5
# 

# In[ ]:


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def print_list(self):
        nodes = []
        temp = self.head
        while True:
            nodes.append(temp.data)
            temp = temp.next
            if temp == self.head:
                break
        print(" -> ".join(map(str, nodes)))


def custom_comparison_function(a, b):
    return a <= b

def custom_merge(left, right, compare):
    result = CircularLinkedList()

    while left and right:
        if compare(left.data, right.data):
            result.append(left.data)
            left = left.next
        else:
            result.append(right.data)
            right = right.next

    while left:
        result.append(left.data)
        left = left.next

    while right:
        result.append(right.data)
        right = right.next

    return result.head

def split_cll(cll):
    if not cll or not cll.next:
        left = cll
        right = None
        return left, right

    slow = cll
    fast = cll

    while fast.next != cll and fast.next.next != cll:
        slow = slow.next
        fast = fast.next.next

    if fast.next.next == cll:
        fast = fast.next

    left = cll

    if cll.next != cll:  # To handle the case of only one element in the CLL
        right = slow.next
    fast.next = slow.next
    slow.next = cll

    return left, right

def merge_sort_cll(cll, compare):
    if not cll or not cll.next or cll.next == cll:
        return cll

    left, right = split_cll(cll)
    left = merge_sort_cll(left, compare)
    right = merge_sort_cll(right, compare)

    return custom_merge(left, right, compare)


# Test
cll = CircularLinkedList()
data = [3, 5, 2, 1, 4]
for d in data:
    cll.append(d)

print("Original Circular Linked List:")
cll.print_list()

sorted_head = merge_sort_cll(cll.head, custom_comparison_function)
sorted_cll = CircularLinkedList()
sorted_cll.head = sorted_head

print("Sorted Circular Linked List:")
sorted_cll.print_list()


# ### 370. Find the Partition Numbers in a Range
# A partition number or a partition count represents the number of ways a given positive integer can be represented as the sum of positive integers, disregarding the order of the addends. For instance, the number 4 can be partitioned in the following ways:
# 4
# 3 + 1
# 2 + 2
# 2 + 1 + 1
# 1 + 1 + 1 + 1
# So, the partition count for 4 is 5.
# 
# To find the partition numbers for a given range, we'll use Euler's partition function. Here's how you can compute the partition numbers for a range:
# 
# Expected Output:
# 1: 1
# 2: 2
# 3: 3
# 4: 5
# 5: 7
# 6: 11
# 7: 15
# 8: 22
# 9: 30
# 10: 42
# 

# In[ ]:


def partition_numbers(n):
    """Return the first n partition numbers."""
    partition = [0] * (n + 1)
    partition[0] = 1
    
    for i in range(1, n + 1):
        j = 1
        k = 1
        while j > 0:
            if k % 2 == 0:
                sign = -1
            else:
                sign = 1
            j = i - (3 * k * k + k) // 2
            if j >= 0:
                partition[i] += sign * partition[j]
            j = i - (3 * k * k - k) // 2
            if j >= 0:
                partition[i] += sign * partition[j]
            k += 1
    return partition[1:]

# Test
n = 10
partitions = partition_numbers(n)
for i, p in enumerate(partitions, 1):
    print(f"{i}: {p}")

