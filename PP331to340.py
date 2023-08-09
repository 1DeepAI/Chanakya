#!/usr/bin/env python
# coding: utf-8

# # Python Practice 331-340

# ## Here are the Python programs for the specified objectives:

# ### 331. Calculate the Perimeter of a Reuleaux Hexagon Star with Rounded Corners, Right Alignment, Custom Size, and Custom Side Length

# In[1]:


import math

def reuleaux_hexagon_star_perimeter(custom_size, custom_side_length):
    if custom_size <= 0 or custom_side_length <= 0:
        return "Invalid input. Size and side length must be positive."

    r = custom_size
    a = custom_side_length
    side_perimeter = 3 * a
    rounded_corner_perimeter = (2 * math.pi - math.sqrt(3)) * r
    total_perimeter = side_perimeter + rounded_corner_perimeter

    return total_perimeter

custom_size = 5
custom_side_length = 8
result = reuleaux_hexagon_star_perimeter(custom_size, custom_side_length)
print(f"The perimeter of the Reuleaux Hexagon Star with size {custom_size} and side length {custom_side_length} is: {result:.2f}")


# ### 332. Print the Pattern of a Hollow Prime Number Pyramid Star with Right Alignment and Custom Size

# In[2]:


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def print_hollow_prime_number_pyramid(custom_size):
    if custom_size <= 0:
        return "Invalid input. Size must be positive."

    for i in range(1, custom_size + 1):
        for j in range(custom_size - i):
            print(" ", end="")
        for j in range(2 * i - 1):
            if j == 0 or j == 2 * i - 2 or is_prime(i):
                print("*", end="")
            else:
                print(" ", end="")
        print()

custom_size = 5
print_hollow_prime_number_pyramid(custom_size)


# ### 333. Generate a Random Maze with Custom Dimensions and Different Path Generation Algorithms (DFS, BFS)

# In[3]:


import random

def generate_random_maze_dfs(rows, cols):
    maze = [["#" for _ in range(cols)] for _ in range(rows)]

    def dfs(x, y):
        maze[x][y] = " "
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == "#":
                maze[x + dx][y + dy] = " "
                dfs(nx, ny)

    dfs(0, 0)
    return maze

def generate_random_maze_bfs(rows, cols):
    maze = [["#" for _ in range(cols)] for _ in range(rows)]
    queue = [(0, 0)]
    maze[0][0] = " "

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols and maze[x][y] == "#"

    def bfs():
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            x, y = queue.pop(0)
            random.shuffle(directions)

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny):
                    maze[nx][ny] = " "
                    queue.append((nx, ny))

    bfs()
    return maze

rows = 5
cols = 5
maze_dfs = generate_random_maze_dfs(rows, cols)
maze_bfs = generate_random_maze_bfs(rows, cols)

print("Random Maze using DFS:")
for row in maze_dfs:
    print("".join(row))

print("\nRandom Maze using BFS:")
for row in maze_bfs:
    print("".join(row))


# ### 334. Convert Decimal to Excess-K Code Using Bit Manipulation and Custom K

# In[4]:


def decimal_to_excess_k(decimal_num, k):
    if k <= 0:
        return "Invalid input. K must be positive."

    excess_k_code = bin(decimal_num + k)[3:]
    return excess_k_code

decimal_num = 10
k = 3
result = decimal_to_excess_k(decimal_num, k)
print(f"The Excess-{k} code of {decimal_num} is: {result}")


# ### 335. Check if a Number is a Generalized Hexagon Number

# In[5]:


def is_generalized_hexagon_number(n):
    if n <= 0:
        return False
    x = (1 + (1 + 8 * n) ** 0.5) / 4
    return x == int(x)

num = 91
result = is_generalized_hexagon_number(num)
print(f"{num} is {'a' if result else 'not a'} generalized hexagon number.")


# ### 336. Calculate the Volume of a Frustum of a Regular Icosahedron with Custom Height

# In[6]:


def volume_of_frustum_of_icosahedron(side_length, height):
    if side_length <= 0 or height <= 0:
        return "Invalid input. Side length and height must be positive."

    volume = (5 / 12) * (3 + 5 ** 0.5) * side_length ** 2 * height
    return volume

side_length = 6
height = 10
result = volume_of_frustum_of_icosahedron(side_length, height)
print(f"The volume of the frustum of a regular icosahedron with side length {side_length} and height {height} is: {result:.2f}")


# ### 337. Implement Merge Sort Algorithm on a Circular Linked List with Custom Merge

# In[7]:


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
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

    def display(self):
        if not self.head:
            return "Circular Linked List is empty."
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print()

    def merge_sort(self, start):
        def merge(a, b):
            result = None
            if not a:
                return b
            if not b:
                return a

            if a.data <= b.data:
                result = a
                result.next = merge(a.next, b)
            else:
                result = b
                result.next = merge(a, b.next)
            return result

        if not start or not start.next:
            return start

        mid = self.find_mid(start)
        mid_next = mid.next
        mid.next = start
        left = self.merge_sort(start)
        mid.next = mid_next
        right = self.merge_sort(mid_next)
        return merge(left, right)

    def find_mid(self, start):
        slow = start
        fast = start
        while fast.next != start and fast.next.next != start:
            slow = slow.next
            fast = fast.next.next
        return slow

# Sample usage:
clist = CircularLinkedList()
elements = [170, 45, 75, 90, 802, 24, 2]
for ele in elements:
    clist.insert(ele)

print("Original Circular Linked List:")
clist.display()

clist.head = clist.merge_sort(clist.head)

print("Circular Linked List after Merge Sort:")
clist.display()


# ### 338. Find the Motzkin Numbers in a Range

# In[8]:


def motzkin_numbers(n):
    if n == 0:
        return 1
    if n == 1:
        return 1

    prev = 1
    current = 1
    for i in range(2, n + 1):
        new_num = (2 * i + 1) * current + (i - 1) * prev
        prev = current
        current = new_num

    return current

lower_bound = 0
upper_bound = 7
motzkin_nums = [motzkin_numbers(i) for i in range(lower_bound, upper_bound + 1)]
print(f"Motzkin Numbers from {lower_bound} to {upper_bound}: {motzkin_nums}")


# ### 339. Calculate the Perimeter of a Reuleaux Pentagon Star with Rounded Corners, Right Alignment, Custom Size, and Custom Side Length

# In[9]:


import math

def reuleaux_pentagon_star_perimeter(custom_size, custom_side_length):
    if custom_size <= 0 or custom_side_length <= 0:
        return "Invalid input. Size and side length must be positive."

    r = custom_size
    a = custom_side_length
    side_perimeter = 5 * a
    rounded_corner_perimeter = (2 * math.pi - 2 * math.pi / 5) * r
    total_perimeter = side_perimeter + rounded_corner_perimeter

    return total_perimeter

custom_size = 6
custom_side_length = 7
result = reuleaux_pentagon_star_perimeter(custom_size, custom_side_length)
print(f"The perimeter of the Reuleaux Pentagon Star with size {custom_size} and side length {custom_side_length} is: {result:.2f}")


# ### 340. Print the Pattern of a Hollow Rhombic Pyramid Star with Right Alignment and Custom Size

# In[10]:


def print_hollow_rhombic_pyramid_star(custom_size):
    if custom_size <= 0:
        return "Invalid input. Size must be positive."

    for i in range(1, custom_size + 1):
        for j in range(custom_size - i):
            print(" ", end="")
        for j in range(2 * i - 1):
            if j == 0 or j == 2 * i - 2 or i == custom_size:
                print("*", end="")
            else:
                print(" ", end="")
        print()

custom_size = 5
print_hollow_rhombic_pyramid_star(custom_size)


# In[ ]:




