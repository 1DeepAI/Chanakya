#!/usr/bin/env python
# coding: utf-8

# # Python Practice 281-290

# ## Here are the Python programs for the given objectives:

# ### 281. Implement Doubly Ended Queue (Deque) Data Structure with Custom Node Class

# In[10]:


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None and self.rear is None

    def push_front(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node

    def push_back(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node

    def pop_front(self):
        if self.is_empty():
            return None
        data = self.front.data
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.front.prev = None
        return data

    def pop_back(self):
        if self.is_empty():
            return None
        data = self.rear.data
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None
        return data

# Example usage of the Deque data structure
deque = Deque()
deque.push_front(1)
deque.push_back(2)
deque.push_front(3)
print(deque.pop_front()) # Output: 3
print(deque.pop_back()) # Output: 2


# ### 282. Find the Perfect Pairs in a Range

# In[9]:


def find_perfect_pairs(lower_bound, upper_bound):
    def get_divisors_sum(number):
        sum_of_divisors = 0
        for i in range(1, int(number**0.5) + 1):
            if number % i == 0:
                sum_of_divisors += i
                if i != number // i:
                    sum_of_divisors += number // i
        return sum_of_divisors - number

    perfect_pairs = []
    for num1 in range(lower_bound, upper_bound + 1):
        num2 = get_divisors_sum(num1)
        if num2 != num1 and get_divisors_sum(num2) == num1:
            if num1 < num2:
                perfect_pairs.append((num1, num2))
            else:
                perfect_pairs.append((num2, num1))
    return perfect_pairs

lower_bound = 1 # Replace with the lower bound of the range to search for perfect pairs
upper_bound = 1000 # Replace with the upper bound of the range to search for perfect pairs
perfect_pairs = find_perfect_pairs(lower_bound, upper_bound)
print("Perfect pairs in the given range:")
print(perfect_pairs)


# ### 283. Calculate the Perimeter of a Reuleaux Hexagon Star with Rounded Corners and Right Alignment

# In[8]:


def calculate_perimeter_of_reuleaux_hexagon_star(radius1, radius2):
    # The perimeter of a Reuleaux hexagon star is the same as the perimeter of a Reuleaux hexagon with the same radii
    perimeter = 6 * (radius1 + radius2)
    return perimeter

radius1 = 5 # Replace with the first radius of the Reuleaux hexagon star
radius2 = 3 # Replace with the second radius of the Reuleaux hexagon star
perimeter = calculate_perimeter_of_reuleaux_hexagon_star(radius1, radius2)
print(f"Perimeter of the Reuleaux hexagon star with radii {radius1} and {radius2} is: {perimeter:.2f}")


# ### 284. Print the Pattern of a Hollow Prime Number Pyramid Star with Right Alignment

# In[7]:


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_hollow_prime_number_pyramid_star(rows):
    for i in range(1, rows + 1):
        for j in range(1, 2 * rows):
            if i + j == rows + 1 or j - i == rows - 1 or (i == 1 and j % 2 != 0 and is_prime(j)):
                print("*", end="")
            else:
                print(" ", end="")
        print()

rows = 5 # Replace with the desired number of rows for the hollow prime number pyramid star
print("Hollow Prime Number Pyramid Star Pattern:")
print_hollow_prime_number_pyramid_star(rows)


# ### 285. Generate a Random Maze with Custom Dimensions and Path Density

# In[6]:


import random

def generate_random_maze(rows, cols, path_density):
    maze = [[1 for _ in range(cols)] for _ in range(rows)]
    for i in range(1, rows, 2):
        for j in range(1, cols, 2):
            maze[i][j] = 0

    for i in range(2, rows - 2, 2):
        for j in range(2, cols - 2, 2):
            if random.random() < path_density:
                maze[i][j] = 0

    return maze

rows = 9 # Replace with the desired number of rows for the maze (should be odd)
cols = 9 # Replace with the desired number of columns for the maze (should be odd)
path_density = 0.3 # Replace with the desired path density (a value between 0 and 1)
maze = generate_random_maze(rows, cols, path_density)
print("Random Maze:")
for row in maze:
    print(" ".join(str(cell) for cell in row))


# ### 286. Convert Decimal to Excess-K Code Using Bit Manipulation

# In[5]:


def decimal_to_excess_k(decimal_number, k):
    if decimal_number >= 0:
        return bin(decimal_number + k)[2:]
    else:
        return bin(2**len(bin(k))-1 + decimal_number + k)[2:]

decimal_number = 10 # Replace with the decimal number you want to convert
k = 3 # Replace with the value of k for the excess-k code conversion
excess_k_code = decimal_to_excess_k(decimal_number, k)
print(f"Excess-{k} code representation of {decimal_number} is: {excess_k_code}")


# ### 287. Check if a Number is a Generalized Hamming Number

# In[4]:


def is_generalized_hamming_number(number, factors):
    while number > 1:
        found_factor = False
        for factor in factors:
            if number % factor == 0:
                number //= factor
                found_factor = True
                break
        if not found_factor:
            return False
    return True

number = 120 # Replace with the number you want to check
factors = [2, 3, 5] # Replace with the list of prime factors for the generalized Hamming numbers
result = is_generalized_hamming_number(number, factors)
print(f"{number} is {'a' if result else 'not a'} generalized Hamming number with factors {factors}.")


# ### 288. Calculate the Volume of a Frustum of a Regular Dodecahedron

# In[3]:


def calculate_volume_of_frustum_of_regular_dodecahedron(edge1, edge2, height):
    volume = (15 / 4) * (edge1**2 + edge1 * edge2 + edge2**2) * height
    return volume

edge1 = 4 # Replace with the length of the larger edge of the frustum of the regular dodecahedron
edge2 = 2 # Replace with the length of the smaller top edge of the frustum of the regular dodecahedron
height = 6 # Replace with the height of the frustum of the regular dodecahedron
volume = calculate_volume_of_frustum_of_regular_dodecahedron(edge1, edge2, height)
print(f"Volume of the frustum of the regular dodecahedron with edge lengths {edge1} and {edge2} and height {height} is: {volume:.2f}")


# ### 289. Implement Binary Search Algorithm on a Rotated Sorted Array

# In[1]:


def binary_search_rotated(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

# Example usage of binary_search_rotated
rotated_sorted_array = [4, 5, 6, 7, 8, 9, 1, 2, 3]
target = 6
index = binary_search_rotated(rotated_sorted_array, target)
print(f"Element {target} found at index {index}")


# ### 290. Find the Cullen Numbers in a Range

# In[2]:


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_cullen_numbers(lower_bound, upper_bound):
    cullen_numbers = []
    for n in range(lower_bound, upper_bound + 1):
        if is_prime(n):
            cullen_number = n * (2**n) + 1
            cullen_numbers.append(cullen_number)
    return cullen_numbers

lower_bound = 1 # Replace with the lower bound of the range to search for Cullen numbers
upper_bound = 100 # Replace with the upper bound of the range to search for Cullen numbers
cullen_numbers = find_cullen_numbers(lower_bound, upper_bound)
print("Cullen numbers in the given range:")
print(cullen_numbers)


# In[ ]:




