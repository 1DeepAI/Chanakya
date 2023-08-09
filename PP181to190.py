#!/usr/bin/env python
# coding: utf-8

# # Python Practice 181-190

# ## Here are the Python programs for each of the objectives along with the associated algorithm, mathematical calculations, and string manipulations:

# ### 181. Generate a Random Maze Using Kruskal's Algorithm

# In[10]:


import random

def generate_random_maze_kruskal(rows, cols):
    def find(node):
        while node != disjoint_set[node]:
            node = disjoint_set[node]
        return node

    def union(node1, node2):
        root1, root2 = find(node1), find(node2)
        if root1 != root2:
            disjoint_set[root2] = root1

    def generate_maze_cells(rows, cols):
        cells = []
        for i in range(rows):
            for j in range(cols):
                cells.append((i, j))
        return cells

    def generate_maze():
        random.shuffle(cells)
        for cell in cells:
            x, y = cell
            neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
            for nx, ny in neighbors:
                if 0 <= nx < rows and 0 <= ny < cols and find(cell) != find((nx, ny)):
                    union(cell, (nx, ny))
                    maze[x*2+1][y*2+1] = " "
                    maze[x*2+1+nx-x][y*2+1+ny-y] = " "
                    break

    maze = [["#" for _ in range(cols*2+1)] for _ in range(rows*2+1)]
    disjoint_set = {(i, j): (i, j) for i in range(rows) for j in range(cols)}
    cells = generate_maze_cells(rows, cols)
    generate_maze()
    return maze

rows, cols = 10, 20
maze = generate_random_maze_kruskal(rows, cols)
for row in maze:
    print("".join(row))


# ### 182. Convert Decimal to Gray Code Using Bit Manipulation

# In[9]:


def decimal_to_gray_code(decimal):
    return decimal ^ (decimal >> 1)

decimal_num = 15
gray_code = decimal_to_gray_code(decimal_num)
print(f"The Gray Code representation of {decimal_num} is {gray_code}.")


# ### 183. Check if a String is a Super Palindrome

# In[8]:


def is_palindrome(word):
    return word == word[::-1]

def is_super_palindrome(word):
    length = len(word)
    for i in range(length // 2):
        if word[i] != word[length - i - 1]:
            return False
    return is_palindrome(str(int(word)**2))

word = "12321"
if is_super_palindrome(word):
    print(f"{word} is a super palindrome.")
else:
    print(f"{word} is not a super palindrome.")


# ### 184. Calculate the Volume of an Icosahedron

# In[7]:


def volume_of_icosahedron(edge_length):
    import math
    phi = (1 + math.sqrt(5)) / 2
    volume = 5 * edge_length**3 * (3 + math.sqrt(5)) / 12
    return volume

edge_length = 5
volume = volume_of_icosahedron(edge_length)
print(f"The volume of the icosahedron with edge length {edge_length} is {volume:.2f}.")


# ### 185. Implement Matrix Data Structure

# In[6]:


class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols for _ in range(rows)]

    def set_element(self, row, col, value):
        self.data[row][col] = value

    def get_element(self, row, col):
        return self.data[row][col]

    def display(self):
        for row in self.data:
            print(" ".join(map(str, row)))

# Example usage of the Matrix data structure
rows, cols = 3, 4
matrix = Matrix(rows, cols)
matrix.set_element(0, 0, 1)
matrix.set_element(0, 1, 2)
matrix.set_element(1, 2, 3)
matrix.set_element(2, 3, 4)

print("Matrix:")
matrix.display()


# ### 186. Find the Powerful Numbers in a Range

# In[5]:


def is_powerful_number(num):
    def prime_factors(n):
        factors = set()
        while n % 2 == 0:
            factors.add(2)
            n //= 2
        for i in range(3, int(n**0.5) + 1, 2):
            while n % i == 0:
                factors.add(i)
                n //= i
        if n > 2:
            factors.add(n)
        return factors

    factors = prime_factors(num)
    for factor in factors:
        if num % (factor ** 2) != 0:
            return False
    return True

start_range, end_range = 1, 100
powerful_numbers_list = [num for num in range(start_range, end_range+1) if is_powerful_number(num)]
print(f"Powerful numbers in the range {start_range} to {end_range}: {powerful_numbers_list}")


# ### 187. Calculate the Perimeter of a Reuleaux Triangle

# In[4]:


def calculate_perimeter_of_reuleaux_triangle(radius):
    import math
    perimeter = 3 * math.pi * radius
    return perimeter

radius = 5
perimeter = calculate_perimeter_of_reuleaux_triangle(radius)
print(f"The perimeter of the Reuleaux triangle with radius {radius} is {perimeter:.2f}.")


# ### 188. Print the Pattern of a Hollow Diamond with Right Alignment

# In[3]:


def print_hollow_diamond(rows):
    for i in range(rows):
        print(" " * (rows - i - 1), end="")
        if i == 0 or i == rows - 1:
            print("*")
        else:
            print("*" + " " * (2 * i - 1) + "*")
    for i in range(rows - 2, -1, -1):
        print(" " * (rows - i - 1), end="")
        if i == 0 or i == rows - 1:
            print("*")
        else:
            print("*" + " " * (2 * i - 1) + "*")

rows = 5
print("Hollow Diamond:")
print_hollow_diamond(rows)


# ### 189. Generate a Random Sudoku Puzzle

# In[2]:


import random

def generate_sudoku():
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

sudoku = generate_sudoku()
print("Random Sudoku Puzzle:")
print_sudoku(sudoku)


# ### 190. Convert Decimal to Roman Numeral Using a Dictionary

# In[1]:


def decimal_to_roman(decimal):
    roman_numerals = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C',
        90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
    }
    roman_numeral = ''
    for value, symbol in roman_numerals.items():
        while decimal >= value:
            roman_numeral += symbol
            decimal -= value
    return roman_numeral

decimal_num = 1984
roman_numeral = decimal_to_roman(decimal_num)
print(f"The Roman numeral representation of {decimal_num} is {roman_numeral}.")


# In[ ]:




