#!/usr/bin/env python
# coding: utf-8

# # Python Practice 191-200

# ## Here are the Python programs for each of the objectives along with the associated algorithm, mathematical calculations, and string manipulations:

# ### 191. Check if a String is an Isogram

# In[10]:


def is_isogram(string):
    seen = set()
    for char in string:
        if char.isalpha() and char.lower() in seen:
            return False
        seen.add(char.lower())
    return True

word = "algorithm"
if is_isogram(word):
    print(f"{word} is an isogram.")
else:
    print(f"{word} is not an isogram.")


# ### 192. Calculate the Volume of a Reuleaux Tetrahedron

# In[9]:


def volume_of_reuleaux_tetrahedron(a):
    import math
    volume = (4 / 3) * math.sqrt(2) * a**3
    return volume

side_length = 5
volume = volume_of_reuleaux_tetrahedron(side_length)
print(f"The volume of the Reuleaux tetrahedron with side length {side_length} is {volume:.2f}.")


# ### 193. Implement Priority Queue Data Structure

# In[8]:


class PriorityQueue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def insert(self, item, priority):
        self.queue.append((item, priority))
        self.queue.sort(key=lambda x: x[1])

    def remove(self):
        if self.is_empty():
            raise IndexError("Priority queue is empty")
        return self.queue.pop(0)[0]

# Example usage of the Priority Queue data structure
priority_queue = PriorityQueue()
priority_queue.insert("Task 1", 3)
priority_queue.insert("Task 2", 1)
priority_queue.insert("Task 3", 2)

while not priority_queue.is_empty():
    task = priority_queue.remove()
    print(f"Processing: {task}")


# ### 194. Find the Amicable Pairs in a Range

# In[7]:


def sum_of_divisors(n):
    divisors_sum = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:
                divisors_sum += n // i
    return divisors_sum

def find_amicable_pairs(start_range, end_range):
    amicable_pairs = []
    for num in range(start_range, end_range + 1):
        sum_divisors = sum_of_divisors(num)
        if sum_of_divisors(sum_divisors) == num and num != sum_divisors:
            amicable_pairs.append((num, sum_divisors))
    return amicable_pairs

start_range, end_range = 1, 1000
amicable_pairs_list = find_amicable_pairs(start_range, end_range)
print(f"Amicable pairs in the range {start_range} to {end_range}: {amicable_pairs_list}")


# ### 195. Calculate the Perimeter of a Reuleaux Pentagon

# In[6]:


def calculate_perimeter_of_reuleaux_pentagon(radius):
    import math
    perimeter = 5 * math.pi * radius
    return perimeter

radius = 5
perimeter = calculate_perimeter_of_reuleaux_pentagon(radius)
print(f"The perimeter of the Reuleaux pentagon with radius {radius} is {perimeter:.2f}.")


# ### 196. Print the Pattern of a Hollow Number Diamond with Right Alignment

# In[5]:


def print_hollow_number_diamond(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i), end="")
        for j in range(1, 2 * i):
            if j == 1 or j == 2 * i - 1:
                print(j, end="")
            else:
                print(" ", end="")
        print()

    for i in range(rows - 1, 0, -1):
        print(" " * (rows - i), end="")
        for j in range(1, 2 * i):
            if j == 1 or j == 2 * i - 1:
                print(j, end="")
            else:
                print(" ", end="")
        print()

rows = 5
print("Hollow Number Diamond:")
print_hollow_number_diamond(rows)


# ### 197. Generate a Random Sudoku Solution

# In[4]:


import random

def generate_sudoku_solution():
    n = 9
    grid = [[0 for _ in range(n)] for _ in range(n)]
    numbers = list(range(1, n + 1))

    def is_safe(row, col, num):
        for i in range(n):
            if grid[row][i] == num or grid[i][col] == num:
                return False
        row_start, col_start = 3 * (row // 3), 3 * (col // 3)
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                if grid[i][j] == num:
                    return False
        return True

    def solve_sudoku():
        empty_cell = find_empty_cell()
        if not empty_cell:
            return True
        row, col = empty_cell
        random.shuffle(numbers)
        for num in numbers:
            if is_safe(row, col, num):
                grid[row][col] = num
                if solve_sudoku():
                    return True
                grid[row][col] = 0
        return False

    def find_empty_cell():
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    return i, j
        return None

    solve_sudoku()
    return grid

def print_sudoku(grid):
    for row in grid:
        print(" ".join(map(str, row)))

sudoku_solution = generate_sudoku_solution()
print("Random Sudoku Solution:")
print_sudoku(sudoku_solution)


# ### 198. Convert Decimal to Excess-K Code Using Bit Manipulation

# In[3]:


def decimal_to_excess_k(decimal, k):
    excess_k = decimal + k
    return bin(excess_k)[2:]

decimal_num, k_value = 15, 3
excess_k_code = decimal_to_excess_k(decimal_num, k_value)
print(f"The Excess-{k_value} code representation of {decimal_num} is {excess_k_code}.")


# ### 199. Check if a String is a Pangrammatic Lipogram

# In[2]:


def is_pangrammatic_lipogram(string):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    string_chars = set(string.lower().replace(" ", ""))
    return string_chars != alphabet

text = "The quick brown fox jumps over the lazy dog"
if is_pangrammatic_lipogram(text):
    print("The text is a pangrammatic lipogram.")
else:
    print("The text is not a pangrammatic lipogram.")


# ### 200. Calculate the Volume of a Reuleaux Octahedron

# In[1]:


def volume_of_reuleaux_octahedron(a):
    import math
    volume = (16 / 3) * math.sqrt(2) * a**3
    return volume

side_length = 5
volume = volume_of_reuleaux_octahedron(side_length)
print(f"The volume of the Reuleaux octahedron with side length {side_length} is {volume:.2f}.")

