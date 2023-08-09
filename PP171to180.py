#!/usr/bin/env python
# coding: utf-8

# # Python Practice 171-180

# ## 

# ### 171. Calculate the Perimeter of an Ellipse

# In[10]:


def calculate_perimeter_of_ellipse(a, b):
    import math
    perimeter = 2 * math.pi * math.sqrt((a ** 2 + b ** 2) / 2)
    return perimeter

semi_major_axis = 5
semi_minor_axis = 3
perimeter = calculate_perimeter_of_ellipse(semi_major_axis, semi_minor_axis)
print(f"The perimeter of the ellipse with semi-major axis {semi_major_axis} and semi-minor axis {semi_minor_axis} is {perimeter:.2f}.")


# ### 172. Print the Pattern of a Prime Number Pyramid

# In[9]:


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def print_prime_number_pyramid(rows):
    current_number = 1
    for i in range(1, rows+1):
        for j in range(1, i+1):
            while not is_prime(current_number):
                current_number += 1
            print(current_number, end=" ")
            current_number += 1
        print()

rows = 5
print("Prime number pyramid:")
print_prime_number_pyramid(rows)


# ### 173. Generate a Random Maze Using Prim's Algorithm

# In[8]:


import random

def generate_random_maze(rows, cols):
    maze = [["#"] * cols for _ in range(rows)]
    visited = set()

    def valid_neighbors(x, y):
        neighbors = [(x+2, y), (x-2, y), (x, y+2), (x, y-2)]
        valid_neighbors = [(nx, ny) for nx, ny in neighbors if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited]
        return valid_neighbors

    def break_wall(x1, y1, x2, y2):
        maze[x1][y1] = " "
        maze[x2][y2] = " "
        maze[(x1 + x2) // 2][(y1 + y2) // 2] = " "
        visited.add((x2, y2))

    start_x, start_y = random.randrange(0, rows, 2), random.randrange(0, cols, 2)
    visited.add((start_x, start_y))
    stack = [(start_x, start_y)]

    while stack:
        x, y = stack[-1]
        neighbors = valid_neighbors(x, y)
        if neighbors:
            nx, ny = random.choice(neighbors)
            break_wall(x, y, nx, ny)
            stack.append((nx, ny))
        else:
            stack.pop()

    return maze

rows, cols = 10, 20
maze = generate_random_maze(rows, cols)
for row in maze:
    print("".join(row))


# ### 174. Convert Decimal to Excess-K Code

# In[7]:


def decimal_to_excess_k(decimal, k):
    excess_k = decimal + k
    binary_repr = bin(excess_k)[2:]
    return binary_repr

decimal_num = 15
k_value = 5
excess_k_code = decimal_to_excess_k(decimal_num, k_value)
print(f"The Excess-{k_value} code representation of {decimal_num} is {excess_k_code}.")


# ### 175. Check if a Number is a Strobogrammatic Number

# In[6]:


def is_strobogrammatic_number(num):
    strobogrammatic_map = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
    strobogrammatic_num = "".join(strobogrammatic_map[digit] for digit in num[::-1] if digit in strobogrammatic_map)
    return strobogrammatic_num == num

number = "6969"
if is_strobogrammatic_number(number):
    print(f"{number} is a strobogrammatic number.")
else:
    print(f"{number} is not a strobogrammatic number.")


# ### 176. Calculate the Volume of a Dodecahedron

# In[5]:


def volume_of_dodecahedron(edge_length):
    import math
    phi = (1 + math.sqrt(5)) / 2
    volume = (15 + 7 * math.sqrt(5)) * edge_length**3 / (4 * phi)
    return volume

edge_length = 5
volume = volume_of_dodecahedron(edge_length)
print(f"The volume of the dodecahedron with edge length {edge_length} is {volume:.2f}.")


# ### 177. Implement Bitset Data Structure

# In[4]:


class BitSet:
    def __init__(self, size):
        self.size = size
        self.bits = [0] * ((size + 31) // 32)

    def set(self, index):
        if index < 0 or index >= self.size:
            raise ValueError("Index out of range.")
        self.bits[index // 32] |= 1 << (index % 32)

    def clear(self, index):
        if index < 0 or index >= self.size:
            raise ValueError("Index out of range.")
        self.bits[index // 32] &= ~(1 << (index % 32))

    def get(self, index):
        if index < 0 or index >= self.size:
            raise ValueError("Index out of range.")
        return (self.bits[index // 32] >> (index % 32)) & 1

# Example usage of the BitSet data structure
size = 10
bit_set = BitSet(size)
bit_set.set(2)
bit_set.set(5)
bit_set.set(9)

print("BitSet:")
for i in range(size):
    print(bit_set.get(i), end=" ")
print()


# ### 178. Find the Anti-Prime Numbers in a Range

# In[3]:


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def find_anti_prime_numbers(start, end):
    anti_prime_numbers = []
    max_divisors = -1
    for num in range(start, end+1):
        divisor_count = sum(1 for i in range(1, num+1) if num % i == 0)
        if divisor_count > max_divisors:
            anti_prime_numbers = [num]
            max_divisors = divisor_count
        elif divisor_count == max_divisors:
            anti_prime_numbers.append(num)
    return anti_prime_numbers

start_range, end_range = 1, 100
anti_prime_numbers_list = find_anti_prime_numbers(start_range, end_range)
print(f"Anti-prime numbers in the range {start_range} to {end_range}: {anti_prime_numbers_list}")


# ### 179. Calculate the Perimeter of a Lune

# In[2]:


def calculate_perimeter_of_lune(radius, angle_degrees):
    import math
    angle_radians = math.radians(angle_degrees)
    perimeter = 2 * radius * (1 + math.cos(angle_radians))
    return perimeter

radius = 5
angle_degrees = 60
perimeter = calculate_perimeter_of_lune(radius, angle_degrees)
print(f"The perimeter of the lune with radius {radius} and central angle {angle_degrees} degrees is {perimeter:.2f}.")


# ### 180. Print the Pattern of a Hollow Sierpinski Triangle

# In[1]:


def print_hollow_sierpinski_triangle(n):
    def draw_pattern(x, y, size):
        if size == 1:
            pattern[x][y] = "*"
        else:
            draw_pattern(x, y, size // 2)
            draw_pattern(x, y + size // 2, size // 2)
            draw_pattern(x + size // 2, y + size // 2, size // 2)

    pattern = [[" " for _ in range(n)] for _ in range(n)]
    draw_pattern(0, 0, n)
    for row in pattern:
        print("".join(row))

size_of_triangle = 4
print("Hollow Sierpinski Triangle:")
print_hollow_sierpinski_triangle(size_of_triangle)


# In[ ]:




