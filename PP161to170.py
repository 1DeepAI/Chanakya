#!/usr/bin/env python
# coding: utf-8

# # Python Practice 161-170

# ## Here are the Python programs for each of the objectives along with the associated algorithm, mathematical calculations, and string manipulations:

# ### 161. Implement Disjoint Set (Union-Find) Data Structure

# In[11]:


class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

# Example usage of the Disjoint Set data structure
n = 6
disjoint_set = DisjointSet(n)
disjoint_set.union(0, 1)
disjoint_set.union(1, 2)
disjoint_set.union(3, 4)
print("Parent of 0:", disjoint_set.find(0))
print("Parent of 3:", disjoint_set.find(3))


# ### 162. Find the Happy Numbers in a Range

# In[10]:


def is_happy_number(num):
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(digit)**2 for digit in str(num))
    return num == 1

def find_happy_numbers(start, end):
    happy_numbers = [num for num in range(start, end+1) if is_happy_number(num)]
    return happy_numbers

start_range, end_range = 1, 100
happy_numbers_list = find_happy_numbers(start_range, end_range)
print(f"Happy numbers in the range {start_range} to {end_range}: {happy_numbers_list}")


# ### 163. Calculate the Perimeter of a Regular Icosahedron

# In[9]:


def perimeter_of_regular_icosahedron(edge_length):
    return 20 * edge_length

edge_length = 5
perimeter = perimeter_of_regular_icosahedron(edge_length)
print(f"The perimeter of the regular icosahedron with edge length {edge_length} is {perimeter:.2f}.")


# ### 164. Print the Pattern of a Hollow Floyd's Triangle with Right Alignment

# In[8]:


def print_hollow_floyds_triangle_right_alignment(n):
    num = 1
    for i in range(1, n+1):
        for _ in range(n - i):
            print(" ", end=" ")
        for j in range(1, i+1):
            if i == n or j == 1 or j == i:
                print(num, end=" ")
            else:
                print(" ", end=" ")
            num += 1
        print()

rows = 5
print_hollow_floyds_triangle_right_alignment(rows)


# ### 165. Generate a Random Maze Using Recursive Backtracking Algorithm

# In[7]:


import random

def generate_maze(rows, cols):
    maze = [["#"] * cols for _ in range(rows)]

    def can_carve(x, y):
        return 0 <= x < rows and 0 <= y < cols and maze[x][y] == "#"

    def carve(x, y):
        maze[x][y] = " "
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + 2 * dx, y + 2 * dy
            if can_carve(nx, ny):
                maze[nx][ny] = " "
                carve(nx, ny)

    start_x, start_y = 1, 1
    carve(start_x, start_y)
    return maze

rows, cols = 10, 20
maze = generate_maze(rows, cols)
for row in maze:
    print(" ".join(row))


# ### 166. Convert Decimal to Gray Code

# In[6]:


def decimal_to_gray_code(num):
    return num ^ (num >> 1)

decimal_num = 42
gray_code_num = decimal_to_gray_code(decimal_num)
print(f"The Gray code representation of {decimal_num} is {gray_code_num}.")


# ### 167. Check if a Number is a Catalan Number

# In[5]:


def binomial_coefficient(n, k):
    if k > n - k:
        k = n - k
    res = 1
    for i in range(k):
        res *= (n - i)
        res //= (i + 1)
    return res

def is_catalan_number(num):
    if num <= 1:
        return True
    for i in range(num):
        if binomial_coefficient(2*num, i) % (i + 1) == 0:
            return False
    return True

number = 14
if is_catalan_number(number):
    print(f"{number} is a Catalan number.")
else:
    print(f"{number} is not a Catalan number.")


# ### 168. Calculate the Volume of an Octahedron

# In[4]:


def volume_of_octahedron(edge_length):
    return (2 ** 0.5) * (edge_length ** 3) / 3

edge_length = 5
volume = volume_of_octahedron(edge_length)
print(f"The volume of the octahedron with edge length {edge_length} is {volume:.2f}.")


# ### 169. Implement Skip List Data Structure

# In[3]:


import random

class SkipListNode:
    def __init__(self, value, level):
        self.value = value
        self.forward = [None] * (level + 1)

class SkipList:
    def __init__(self):
        self.max_level = 3
        self.header = SkipListNode(None, self.max_level)
        self.level = 0

    def random_level(self):
        level = 0
        while random.random() < 0.5 and level < self.max_level:
            level += 1
        return level

    def insert(self, value):
        update = [None] * (self.max_level + 1)
        x = self.header
        for i in range(self.level, -1, -1):
            while x.forward[i] and x.forward[i].value < value:
                x = x.forward[i]
            update[i] = x
        level = self.random_level()
        if level > self.level:
            for i in range(self.level + 1, level + 1):
                update[i] = self.header
            self.level = level
        x = SkipListNode(value, level)
        for i in range(level + 1):
            x.forward[i] = update[i].forward[i]
            update[i].forward[i] = x

    def search(self, value):
        x = self.header
        for i in range(self.level, -1, -1):
            while x.forward[i] and x.forward[i].value < value:
                x = x.forward[i]
        x = x.forward[0]
        if x and x.value == value:
            return True
        return False

    def delete(self, value):
        update = [None] * (self.max_level + 1)
        x = self.header
        for i in range(self.level, -1, -1):
            while x.forward[i] and x.forward[i].value < value:
                x = x.forward[i]
            update[i] = x
        x = x.forward[0]
        if x and x.value == value:
            for i in range(self.level + 1):
                if update[i].forward[i] != x:
                    break
                update[i].forward[i] = x.forward[i]
            while self.level > 0 and self.header.forward[self.level] is None:
                self.level -= 1
            return True
        return False

    def display(self):
        for i in range(self.level, -1, -1):
            x = self.header.forward[i]
            print(f"Level {i}: ", end=" ")
            while x:
                print(x.value, end=" -> ")
                x = x.forward[i]
            print("None")

# Example usage of the Skip List data structure
skip_list = SkipList()
elements = [10, 25, 7, 40, 15]
for elem in elements:
    skip_list.insert(elem)

print("Skip List:")
skip_list.display()

element_to_search = 25
if skip_list.search(element_to_search):
    print(f"{element_to_search} is present in the Skip List.")
else:
    print(f"{element_to_search} is not present in the Skip List.")

element_to_delete = 7
if skip_list.delete(element_to_delete):
    print(f"{element_to_delete} is deleted from the Skip List.")
else:
    print(f"{element_to_delete} is not present in the Skip List after deletion.")

print("Updated Skip List:")
skip_list.display()


# ### 170. Find the Pernicious Numbers in a Range

# #### Explanation:
# 
# - A pernicious number is a positive integer whose binary representation has an even number of set bits (1s).
# - To check if a number is pernicious, we first count the number of set bits (1s) in its binary representation.
# - Next, we count the number of set bits in the result obtained from the previous step.
# - If the count of set bits in the second step is equal to the length of the binary representation of the number, then the number is pernicious.
# 
# The program finds all pernicious numbers in the given range and prints them.

# In[2]:


def count_set_bits(num):
    count = 0
    while num:
        count += num & 1
        num >>= 1
    return count

def is_pernicious_number(num):
    binary_repr = bin(num)[2:]
    set_bits_count = count_set_bits(num)
    return count_set_bits(set_bits_count) == len(binary_repr)

def find_pernicious_numbers(start, end):
    pernicious_numbers = [num for num in range(start, end+1) if is_pernicious_number(num)]
    return pernicious_numbers

start_range, end_range = 1, 100
pernicious_numbers_list = find_pernicious_numbers(start_range, end_range)
print(f"Pernicious numbers in the range {start_range} to {end_range}: {pernicious_numbers_list}")


# In[ ]:




