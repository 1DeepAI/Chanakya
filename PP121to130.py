#!/usr/bin/env python
# coding: utf-8

# # Python Practice 121-130

# ## Here are the Python programs for each of the objectives along with the associated algorithm, mathematical calculations, and string manipulations:[Please rectify error in 121 and 129 codes]

# ### 121. Implement AVL Tree Data Structure

# In[11]:


cclass TreeNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if not node:
            return 0
        return node.height

    def update_height(self, node):
        node.height = max(self.height(node.left), self.height(node.right)) + 1

    def balance_factor(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def rotate_left(self, z):
        y = z.right
        z.right = y.left
        y.left = z
        self.update_height(z)
        self.update_height(y)
        return y

    def rotate_right(self, y):
        x = y.left
        y.left = x.right
        x.right = y
        self.update_height(y)
        self.update_height(x)
        return x

    def rebalance(self, node):
        self.update_height(node)
        if self.balance_factor(node) > 1:
            if self.balance_factor(node.left) < 0:
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        elif self.balance_factor(node) < -1:
            if self.balance_factor(node.right) > 0:
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        return node

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if not node:
            return TreeNode(key)
        if key < node.key:
            node.left = self._insert_recursive(node.left, key)
        else:
            node.right = self._insert_recursive(node.right, key)
        return self.rebalance(node)

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if not node or node.key == key:
            return node
        if key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)

# Example usage of the AVL Tree data structure
avl_tree = AVLTree()
avl_tree.insert(50)
avl_tree.insert(30)
avl_tree.insert(70)
avl_tree.insert(20)
avl_tree.insert(40)
avl_tree.insert(60)
avl_tree.insert(80)

search_key = 40
if avl_tree.search(search_key):
    print(f"{search_key} is present in the AVL Tree.")
else:
    print(f"{search_key} is not present in the AVL Tree.")


# ### 122. Find the Smith Numbers in a Range

# In[10]:


def prime_factors(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def is_smith_number(num):
    prime_factors_sum = sum(prime_factors(num))
    return prime_factors_sum == sum_of_digits(num)

def find_smith_numbers(start, end):
    smith_numbers = [num for num in range(start, end+1) if is_smith_number(num)]
    return smith_numbers

start_range, end_range = 1, 1000
smith_numbers_list = find_smith_numbers(start_range, end_range)
print(f"Smith numbers in the range {start_range} to {end_range}: {smith_numbers_list}")


# ### 123. Calculate the Perimeter of a Sphere

# In[9]:


import math

def perimeter_of_sphere(radius):
    return 2 * math.pi * radius

radius = 5
perimeter = perimeter_of_sphere(radius)
print(f"The perimeter of the sphere with radius {radius} is {perimeter:.2f}.")


# ### 124. Print the Pattern of a Floyd's Triangle

# In[8]:


def print_floyds_triangle(n):
    num = 1
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(num, end=" ")
            num += 1
        print()

rows = 5
print_floyds_triangle(rows)


# ### 125. Generate a Random Password with Required Complexity

# In[7]:


import random
import string

def generate_random_password_complex(length, requires_digits=True, requires_special_chars=True):
    characters = string.ascii_letters
    if requires_digits:
        characters += string.digits
    if requires_special_chars:
        characters += string.punctuation
    random_password = ''.join(random.choice(characters) for _ in range(length))
    return random_password

password_length = 12
password_requires_digits = True
password_requires_special_chars = True
random_password = generate_random_password_complex(password_length, password_requires_digits, password_requires_special_chars)
print(f"Generated Random Password with required complexity: {random_password}")


# ### 126. Convert Decimal to Base-N (N < 10)

# In[6]:


def decimal_to_base_n(num, base):
    if num == 0:
        return "0"
    result = ""
    while num > 0:
        digit = num % base
        result = str(digit) + result
        num //= base
    return result

decimal_num = 42
base = 5
base_n_num = decimal_to_base_n(decimal_num, base)
print(f"The base-{base} representation of {decimal_num} is {base_n_num}.")


# ### 127. Check if a Number is a Perfect Square

# In[5]:


def is_perfect_square(num):
    square_root = int(num ** 0.5)
    return square_root * square_root == num

number = 25
if is_perfect_square(number):
    print(f"{number} is a perfect square.")
else:
    print(f"{number} is not a perfect square.")


# ### 128. Calculate the Volume of a Cylinder

# In[4]:


import math

def volume_of_cylinder(radius, height):
    return math.pi * radius ** 2 * height

radius, height = 5, 8
volume = volume_of_cylinder(radius, height)
print(f"The volume of the cylinder with radius {radius} and height {height} is {volume:.2f}.")


# ### 129. Implement Red-Black Tree Data Structure

# In[3]:


def __init__(self):
   self.nil_node = TreeNode(None, "black")
   self.root = self.nil_node

    def left_rotate(self, node):
   y = node.right
   node.right = y.left
   if y.left != self.nil_node:
       y.left.parent = node
   y.parent = node.parent
   if node.parent == self.nil_node:
       self.root = y
   elif node == node.parent.left:
       node.parent.left = y
   else:
       node.parent.right = y
   y.left = node
   node.parent = y

    def right_rotate(self, node):
   y = node.left
   node.left = y.right
   if y.right != self.nil_node:
       y.right.parent = node
   y.parent = node.parent
   if node.parent == self.nil_node:
       self.root = y
   elif node == node.parent.left:
       node.parent.left = y
   else:
       node.parent.right = y
   y.right = node
   node.parent = y

    def insert(self, key):
   new_node = TreeNode(key)
   y = self.nil_node
   x = self.root
   while x != self.nil_node:
       y = x
       if key < x.key:
           x = x.left
       else:
           x = x.right
   new_node.parent = y
   if y == self.nil_node:
       self.root = new_node
   elif key < y.key:
       y.left = new_node
   else:
       y.right = new_node
   new_node.left = self.nil_node
   new_node.right = self.nil_node
   new_node.color = "red"
   self.insert_fixup(new_node)

    def insert_fixup(self, node):
   while node.parent.color == "red":
       if node.parent == node.parent.parent.left:
           y = node.parent.parent.right
           if y.color == "red":
               node.parent.color = "black"
               y.color = "black"
               node.parent.parent.color = "red"
               node = node.parent.parent
           else:
               if node == node.parent.right:
                   node = node.parent
                   self.left_rotate(node)
               node.parent.color = "black"
               node.parent.parent.color = "red"
               self.right_rotate(node.parent.parent)
       else:
           y = node.parent.parent.left
           if y.color == "red":
               node.parent.color = "black"
               y.color = "black"
               node.parent.parent.color = "red"
               node = node.parent.parent
           else:
               if node == node.parent.left:
                   node = node.parent
                   self.right_rotate(node)
               node.parent.color = "black"
               node.parent.parent.color = "red"
               self.left_rotate(node.parent.parent)
   self.root.color = "black"

    def search(self, key):
   return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
   if node == self.nil_node or key == node.key:
       return node
   if key < node.key:
       return self._search_recursive(node.left, key)
   else:
       return self._search_recursive(node.right, key)

# Example usage of the Red-Black Tree data structure
rb_tree = RedBlackTree()
rb_tree.insert(50)
rb_tree.insert(30)
rb_tree.insert(70)
rb_tree.insert(20)
rb_tree.insert(40)
rb_tree.insert(60)
rb_tree.insert(80)

search_key = 40
if rb_tree.search(search_key) != rb_tree.nil_node:
    print(f"{search_key} is present in the Red-Black Tree.")
else:
    print(f"{search_key} is not present in the Red-Black Tree.")
 


# ### 130. Find the Abundant Numbers in a Range

# In[1]:


def sum_of_divisors(num):
    divisors_sum = 1
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            divisors_sum += i
            if num // i != i:
                divisors_sum += num // i
    return divisors_sum

def is_abundant_number(num):
    return sum_of_divisors(num) > num

def find_abundant_numbers(start, end):
    abundant_numbers = [num for num in range(start, end+1) if is_abundant_number(num)]
    return abundant_numbers

start_range, end_range = 1, 100
abundant_numbers_list = find_abundant_numbers(start_range, end_range)
print(f"Abundant numbers in the range {start_range} to {end_range}: {abundant_numbers_list}")

