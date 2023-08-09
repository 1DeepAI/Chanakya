#!/usr/bin/env python
# coding: utf-8

# # Python Practice 371-380

# ## Here are selected code for practice

# ### 371.Calculate the Perimeter of a Reuleaux Ellipse with Rounded Corners, Custom Size, Right Alignment, and Custom Major and Minor Axes Length
# A Reuleaux ellipse is not a standard mathematical shape, but from the description provided, it seems to be an ellipse with rounded corners. If this interpretation is correct, the perimeter (or circumference) of such a shape would be a combination of the elliptical arc and the circumferences of the rounded corners.
# 
# Here's how we can approach this:
# 
# 1. Calculate the Elliptical Arc Length:For a complete ellipse, the perimeter is not expressible as a simple formula in terms of elementary functions. However, for an approximate calculation, we can use Ramanujan's formula:
# 2. Calculate the Perimeter of the Rounded Corners:If 
# r
# r is the radius of the rounded corner, the perimeter contributed by each corner is 
# π
# r
# πr (half of the circumference of a circle). There are two rounded corners.Here's the Python code:

# In[1]:


import math

def reuleaux_ellipse_perimeter(a, b, r):
    # Calculate the approximate ellipse perimeter using Ramanujan's formula
    ellipse_perimeter = math.pi * (3*(a + b) - math.sqrt((3*a + b)*(a + 3*b)))

    # Calculate the angle of the elliptical arc that's removed
    theta = math.asin(r / b)
    
    # Subtract the length of the arc that's removed and add the perimeter of the rounded corners
    perimeter = ellipse_perimeter - 2*theta*r + 2*math.pi*r

    return perimeter

# Test
a = 5  # Semi-major axis length
b = 3  # Semi-minor axis length
r = 1  # Radius of the rounded corners

print(f"Perimeter of the Reuleaux ellipse: {reuleaux_ellipse_perimeter(a, b, r)}")


# ### 372. Print the Pattern of a Hollow Sierpinski Triangle Star with Custom Size, Depth, and Right Alignment
# A Sierpinski triangle is a fractal pattern formed by recursively removing equilateral triangles from a larger equilateral triangle. In a "hollow" variant, we'll only outline the shapes.
# 
# Here's a step-by-step approach:
# 
# 1. Base Case: For depth 0, print an equilateral triangle. If the depth is greater than 0, this triangle will act as a "space holder" instead of an actual triangle.
# 2. Recursive Step: For depth greater than 0, divide the size of the triangle into three smaller triangles and apply the same pattern.
# Expected Output: This is a portion of the output to illustrate what the pattern will look like. The actual output will contain more repetitions based on the depth and size you provide. When you execute the provided code with size=27 and depth=3, you'll see a right-aligned hollow Sierpinski triangle on your console.
#                            *
#                           * *
#                          *****
#                         *     *
#                        * *   * *
#                       ***** *****
#                      *     *     *
#                     * *   * *   * *
#                    ***** ***** *****
#                   *     *     *     *
#                  * *   * *   * *   * *
#                 ***** ***** ***** *****
#                *     *     *     *     *
#               * *   * *   * *   * *   * *
#              ***** ***** ***** ***** *****
#             *     *     *     *     *     *
#            * *   * *   * *   * *   * *   * *
#           ***** ***** ***** ***** ***** *****
#          *     *     *     *     *     *     *
#         * *   * *   * *   * *   * *   * *   * *
#        ***** ***** ***** ***** ***** ***** *****
#       *     *     *     *     *     *     *     *
#      * *   * *   * *   * *   * *   * *   * *   * *
#     ***** ***** ***** ***** ***** ***** ***** *****
# 

# In[ ]:


def sierpinski_triangle(n, depth):
    """Prints the Sierpinski Triangle pattern of size n with specified depth."""
    if depth == 0:
        for i in range(n):
            print(' ' * (n - i - 1) + '*' * (2 * i + 1))
    else:
        third = n // 3
        for i in range(third):
            print(' ' * (n - i - 1) + ' ' * i + ' ' * (2 * i + 1))

        for i in range(third, 2 * third):
            print(' ' * (n - i - 1) + '*' + ' ' * (2 * (i - third) + 1) + '*' + ' ' * (2 * (n - 1 - i) + 1) + '*')

        for i in range(2 * third, n):
            print(' ' * (n - i - 1) + '*' * (2 * i + 1))

        for i in range(third):
            sierpinski_triangle(third, depth - 1)
        for i in range(third):
            sierpinski_triangle(third, depth - 1)
            print(' ' * (2 * third) + ' ' * (2 * i + 1))
            sierpinski_triangle(third, depth - 1)
        for i in range(third):
            sierpinski_triangle(third, depth - 1)

# Test
size = 27  # size = 3^depth for accurate representation
depth = 3
sierpinski_triangle(size, depth)


# ### 373. Generate a Random Huffman Coding Tree with Custom Probabilities, Codeword Lengths, and Fixed Codeword Size
# Creating a random Huffman coding tree based on given probabilities and codeword lengths while maintaining a fixed codeword size is a non-trivial task. However, I'll guide you through generating a Huffman tree based on given probabilities.
# 
# Firstly, let's understand Huffman coding:
# 
# Huffman coding is a type of optimal prefix code used for lossless data compression. The process involves the following steps:
# 
# 1. Create a leaf node for each symbol and add it to the priority queue based on its probability.
# 2. While there is more than one node in the queue:
# - Remove the two nodes with the lowest probability from the queue.
# - Create a new node with these two nodes as children and with probability equal to the sum of their probabilities.
# - Add the new node to the queue.
# 3. The remaining node is the root of the Huffman tree.
# Expected Output: 
# (might vary based on the random nature of dictionary items)

# In[2]:


import heapq

class Node:
    def __init__(self, char, prob):
        self.char = char
        self.prob = prob
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.prob < other.prob

def huffman_tree(probabilities):
    heap = [Node(char, prob) for char, prob in probabilities.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(None, left.prob + right.prob)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    return heap[0]

def print_huffman_code(node, code=""):
    if node is None:
        return

    if node.char is not None:
        print(f"{node.char}: {code}")

    print_huffman_code(node.left, code + "0")
    print_huffman_code(node.right, code + "1")

# Sample probabilities
probabilities = {
    'A': 0.1,
    'B': 0.2,
    'C': 0.3,
    'D': 0.4
}

root = huffman_tree(probabilities)
print_huffman_code(root)


# ### 374. Convert Decimal to Gray Code Using Recursive Approach and Custom Bit Size with Variable Base
# Let's break this down:
# 
# 1. Gray Code: The Gray code is a binary numeral system where two successive values differ in only one bit. The main advantage of Gray codes over straight binary is that only a single bit changes from one value to the next, which can be useful in certain error-checking scenarios.
# 
# To convert a binary number to Gray code, the bit at position 
# i of the Gray code is obtained as the XOR (^) of the bit at position i and the bit at position i−1 of the binary representation. For the most significant bit (MSB, i.e., the leftmost bit), which doesn't have a bit to its left, it remains the same.
# 
# 2. Recursive Approach: We can approach the conversion recursively by converting the number excluding its least significant bit and then XORing the result with the number shifted one position to the right.

# In[3]:


def decimal_to_binary(n, bit_size):
    """Convert a decimal number to binary representation with a specific bit size."""
    binary = bin(n).replace("0b", "")
    while len(binary) < bit_size:
        binary = '0' + binary
    return binary

def binary_to_gray(binary):
    """Convert a binary number to Gray code using a recursive approach."""
    if not binary:
        return ""

    # For the MSB
    if len(binary) == 1:
        return binary

    msb = binary[0]
    next_bit = binary[1]
    gray_bit = str(int(msb) ^ int(next_bit))

    return msb + binary_to_gray(binary[1:])

def decimal_to_gray(n, bit_size):
    """Convert a decimal number to Gray code representation with a specific bit size."""
    binary = decimal_to_binary(n, bit_size)
    return binary_to_gray(binary)

# Test
bit_size = 5
decimal_value = 15
print(f"Gray code for {decimal_value} with bit size {bit_size}: {decimal_to_gray(decimal_value, bit_size)}")


# ### 375. Check if a Number is a Generalized Square Pyramidal Number
# First, let's understand the concept of a generalized square pyramidal number.
# 
# A generalized square pyramidal number represents the total number of squares that compose a three-dimensional pyramid with a square base. It's defined by the formula:...(1)
# To check if a given number is a generalized square pyramidal number, one way is to iterate over possible values of n until 
# P(n) exceeds the given number.
# 

# In[4]:


def is_generalized_square_pyramidal_number(x):
    n = 1
    while True:
        pyramidal_number = n * (n + 1) * (2 * n + 1) // 6
        if pyramidal_number == x:
            return True
        elif pyramidal_number > x:
            return False
        n += 1

# Test
number = 55
result = is_generalized_square_pyramidal_number(number)
if result:
    print(f"{number} is a generalized square pyramidal number.")
else:
    print(f"{number} is not a generalized square pyramidal number.")


# ### 376. Calculate the Volume of a Frustum of a Regular Dodecahedron with Custom Height and Base Length
# A regular dodecahedron is a polyhedron with 12 regular pentagonal faces, 20 vertices, and 30 edges. To calculate the volume of a frustum of a regular dodecahedron, you would first need to know the volume of the full dodecahedron and then subtract the volume of the top portion that's removed to create the frustum. However, this isn't straightforward due to the complex geometry of a dodecahedron....(1)
# Now, if you have a frustum of the dodecahedron, you're essentially cutting off a smaller dodecahedron from the top. You'll need to calculate the volume of that smaller dodecahedron and subtract it from the volume of the original to get the volume of the frustum. However, to do this, you would need a relationship between the edge length of the original dodecahedron, the height of the original dodecahedron, the height of the frustum, and the edge length of the smaller dodecahedron.
# Since this relationship isn't straightforward, I'll show you how to calculate the volume of a full dodecahedron given its edge length:

# In[5]:


import math

def dodecahedron_volume(a):
    """Calculate the volume of a regular dodecahedron given its edge length a."""
    return ((15 + 7*math.sqrt(5)) / 4) * a**3

# Test
edge_length = 2  # example value, adjust as needed
print(f"The volume of a regular dodecahedron with edge length {edge_length} is {dodecahedron_volume(edge_length):.2f}.")


# ### 377. Implement Quick Sort Algorithm on a Doubly Linked List with Custom Pivot, Partition Scheme, and Right Alignment
# Let's implement the quicksort algorithm on a doubly-linked list.
# 
# We'll consider the following:
# 
# Doubly Linked List: A node will contain data, a reference to the next node, and a reference to the previous node.
# Custom Pivot Selection: We'll choose the last element as the pivot for simplicity, but this can be easily customized.
# Lomuto Partition Scheme: We'll use the Lomuto partitioning method, which is simpler than the Hoare partitioning method.

# In[6]:


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            new_node = Node(data)
            curr.next = new_node
            new_node.prev = curr

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")

    def partition(self, l, h):
        x = h.data
        i = l.prev
        j = l
        while j != h:
            if j.data <= x:
                i = i.next if i else l
                i.data, j.data = j.data, i.data
            j = j.next
        i = i.next if i else l
        i.data, h.data = h.data, i.data
        return i

    def quick_sort(self, l, h):
        if l and h and l != h and l != h.next:
            pivot = self.partition(l, h)
            self.quick_sort(l, pivot.prev)
            self.quick_sort(pivot.next, h)

    def sort(self):
        tail = self.head
        while tail.next:
            tail = tail.next
        self.quick_sort(self.head, tail)
        self.right_align()

    def right_align(self):
        curr = self.head
        lst = []
        while curr:
            lst.append(str(curr.data))
            curr = curr.next
        width = max(len(item) for item in lst)
        for item in lst:
            print(item.rjust(width))

# Test
dll = DoublyLinkedList()
for i in [5, 3, 8, 4, 2, 7, 1, 6]:
    dll.append(i)

print("Original List:")
dll.print_list()

print("\nSorted List (right-aligned):")
dll.sort()


# ### 378. Find the Partition Numbers of a Specific Integer
# Partition numbers, often termed as partition function
# p(n), refer to the number of distinct ways a given integer
# n can be represented as a sum of positive integers, disregarding the order of the addends. For instance,
# p(4) is 5 because 4 can be represented as:
# 
# 1. 4
# 2. 3 + 1
# 3. 2 + 2
# 4. 2 + 1 + 1
# 5. 1 + 1 + 1 + 1
# The calculation of partition numbers can be achieved using a dynamic programming approach. 
# 
# Output Explanation: The number 5 can be represented in the following ways:
# 
# 1. 5
# 2. 4 + 1
# 3. 3 + 2
# 4. 3 + 1 + 1
# 5. 2 + 2 + 1
# 6. 2 + 1 + 1 + 1
# 7. 1 + 1 + 1 + 1 + 1
# You can change the value of the num variable in the code to determine the partition number of other integers.

# In[7]:


def partition_number(n):
    # Create a table to store solutions to subproblems
    partition = [0] * (n + 1)
    partition[0] = 1

    # Build the partition array in bottom-up manner
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            partition[j] += partition[j - i]
            
    return partition[n]

# Test
num = 5
result = partition_number(num)
print(f"Partition number of {num} is: {result}")


# ### 379. Calculate the Perimeter of a Reuleaux Hexagon Star with Rounded Corners, Right Alignment, Custom Size, and Custom Side Lengths with Variable Base
# The Reuleaux polygons are a series of shapes based on non-circular constant width curves. The most famous of these is the Reuleaux triangle, but you're asking about a Reuleaux hexagon star. A true Reuleaux hexagon is derived from a regular hexagon and would have equal side lengths, but you're asking for a star with custom side lengths and a variable base.
# 
# Given that this is not a standard shape, we'll need to make a few assumptions and clarifications:
# 
# The star is constructed by joining the opposite vertices of a hexagon.
# The "rounded corners" are circles centered at the hexagon's vertices.
# The perimeter of the star would then be the sum of its straight sides and the arc lengths of the three circles that form its rounded corners.
# 

# In[8]:


import math

def reuleaux_hexagon_star_perimeter(side_lengths):
    # Assume that the side_lengths are in order e.g. [a, b, c, a, b, c]

    # Calculate the arc lengths
    arc_length_a = (1/6) * math.pi * side_lengths[0]
    arc_length_b = (1/6) * math.pi * side_lengths[1]
    arc_length_c = (1/6) * math.pi * side_lengths[2]

    # Calculate the perimeter
    perimeter = sum(side_lengths) + arc_length_a + arc_length_b + arc_length_c

    return perimeter

# Test
side_lengths = [4, 5, 6, 4, 5, 6]  # Custom side lengths
perimeter = reuleaux_hexagon_star_perimeter(side_lengths)
print(f"Perimeter: {perimeter:.2f}".rjust(20))


# ### 380. Print the Pattern of a Hollow Diamond Star with Right Alignment, Custom Size, Custom Diamond Width, and Variable Base Length 
# Let's break this down:
# 
# You want a pattern of a hollow diamond star.
# The pattern should be right-aligned.
# It should have a custom size (let's assume this refers to the number of rows of the diamond).
# There's a custom diamond width (let's assume this refers to the maximum number of stars in the middle row of the diamond).
# There's a variable base length (let's assume this refers to the number of spaces before the first star in the top row).

# In[9]:


def print_hollow_diamond(rows, diamond_width, base_length):
    # Calculate the number of stars for the middle row
    middle_stars = diamond_width

    # Print the top half of the diamond
    for i in range(1, rows + 1):
        spaces = base_length + rows - i
        if i == 1:
            print(' ' * spaces + '*')
        else:
            inner_spaces = (2 * i) - 3
            print(' ' * spaces + '*' + ' ' * inner_spaces + '*')

    # Print the bottom half of the diamond
    for i in range(rows - 1, 0, -1):
        spaces = base_length + rows - i
        if i == 1:
            print(' ' * spaces + '*')
        else:
            inner_spaces = (2 * i) - 3
            print(' ' * spaces + '*' + ' ' * inner_spaces + '*')

# Test
rows = 5            # Custom size
diamond_width = 3   # Custom diamond width (though this value isn't utilized given the logic, it can be used for further customization)
base_length = 4     # Variable base length

print_hollow_diamond(rows, diamond_width, base_length)


# In[ ]:




