#!/usr/bin/env python
# coding: utf-8

# # Python Practice 421-430

# ## 

# ### 421. Implement Bucket Sort Algorithm on a List of Floating-Point Numbers
# Bucket sort works by dividing a list into several smaller "buckets" based on the range of the input, sorting those buckets, and then concatenating the sorted buckets to get the final sorted list.

# In[1]:


def bucket_sort(arr):
    # Step 1: Create empty buckets
    num_buckets = len(arr)
    buckets = [[] for _ in range(num_buckets)]

    # Step 2: Insert elements into buckets
    for num in arr:
        index = int(num * num_buckets)
        buckets[index].append(num)

    # Step 3: Sort each bucket
    for bucket in buckets:
        bucket.sort()

    # Step 4: Concatenate the sorted buckets
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)

    return sorted_arr

# Example usage:
arr = [0.42, 0.32, 0.67, 0.12, 0.78, 0.55, 0.89, 0.07]
sorted_arr = bucket_sort(arr)
print(sorted_arr)


# ### 422. Find the Partitions of a Specific Integer with Custom Partition Scheme, Variable Size, Custom Position, Custom Border, and Custom Units
# Let's break down your request into specific requirements:
# 
# 1. Partitions of a Specific Integer: This means you want to split an integer into various parts based on some conditions.
# 2. Custom Partition Scheme: The way in which you want to split the integer.
# 3. Variable Size: Each partition might have a different size.
# 4. Custom Position: The position/order in which partitions are presented.
# 5. Custom Border: Visual representation of each partition.
# 6. Custom Units: The unit representation of each partition.

# In[11]:


def custom_partition(n, partition_scheme, position, border, units):
    """
    Custom partition function.

    Parameters:
    - n (int): Number to be partitioned.
    - partition_scheme (list): List of integers, where each integer represents the size of a partition.
    - position (list): List of integers representing the position/order of each partition.
    - border (list): List of strings representing the border for each partition. Each string must have exactly 2 characters.
    - units (list): List of strings representing the unit for each partition.

    Returns:
    - result (str): String representing the partitioned number.
    """
    
    # Ensure all lists are of the same length
    if not all(len(lst) == len(partition_scheme) for lst in [position, border, units]):
        raise ValueError("All lists must have the same length.")

    # Ensure each border string has exactly 2 characters
    if any(len(b) != 2 for b in border):
        raise ValueError("Each border string must have exactly 2 characters.")
    
    partitions = []
    for size in partition_scheme:
        partition_value = n // size
        partitions.append(partition_value)
        n %= size
    
    # Reorder partitions based on position
    ordered_partitions = [partitions[idx] for idx in position]
    
    result = []
    for value, b, u in zip(ordered_partitions, border, units):
        result.append(f"{b[0]}{value}{u}{b[1]}")

    return " ".join(result)

# Example
n = 123456
partition_scheme = [1000, 100, 10]
position = [1, 0, 2]
border = ["[]", "()", "{}"]
units = ["k", "h", "d"]

print(custom_partition(n, partition_scheme, position, border, units))


# ### 423. Calculate the Perimeter of a Reuleaux Hexagon Star with Rounded Corners, Right Alignment, Custom Size, Custom Side Lengths, Variable Base, Custom Position, Custom Border, and Custom Units
# Calculating the perimeter of such a shape can be complex. If you were to "unroll" the perimeter of the Reuleaux hexagon, you'd have six arcs, each corresponding to one-sixth of the circumference of a circle with a radius equal to the side length of the hexagon.
# 
# However, this task has some additional complexities:
# 
# 1. Rounded Corners: Typically, a Reuleaux polygon doesn't have "rounded corners" as it is already formed by arcs. I'll assume you mean some additional rounding on the point where arcs meet, and that would alter the perimeter slightly.
# 2. Right Alignment, Custom Position, Custom Border, and Custom Units: These seem more like display or formatting requirements. They would not influence the actual computation of the perimeter.
# 

# In[12]:


import math

def reuleaux_hexagon_perimeter(side_length):
    # A Reuleaux hexagon's perimeter is made of 6 arcs.
    # Each arc is 1/6th of the circumference of a circle with a radius of the hexagon's side length.
    arc_length = (1/6) * 2 * math.pi * side_length
    return 6 * arc_length

def formatted_perimeter(side_length, base, position, border, units):
    # Calculate the raw perimeter
    perimeter = reuleaux_hexagon_perimeter(side_length)

    # Convert to the desired base (assuming the default base is 10)
    if base != 10:
        perimeter_str = format(perimeter, f".{position}f").split(".")
        int_part = int(perimeter_str[0], 10)  # convert integer part to base 10
        frac_part = int(perimeter_str[1], 10) / (10 ** position)  # convert fractional part
        perimeter = int_part + frac_part
        perimeter = round(perimeter, position)

    # Format the string
    formatted_str = f"{border[0]}{perimeter:>{position}}{units}{border[1]}"
    return formatted_str

# Example usage
side_length = 10
base = 10
position = 2
border = ["[", "]"]
units = "cm"

print(formatted_perimeter(side_length, base, position, border, units))


# ### 424. Print the Pattern of a Hollow Diamond Star with Right Alignment, Custom Size, Custom Diamond Width, Variable Base Length, Custom Position, and Custom Border
# To produce a hollow diamond star pattern with the provided customizations, let's break down the requirements:
# 
# 1. Right Alignment: The pattern should be right-aligned.
# 2. Custom Size: This probably refers to the number of rows for the diamond.
# 3. Custom Diamond Width: Determines the width of the diamond.
# 4. Variable Base Length: A base to determine the overall width of the pattern.
# 5. Custom Position: I assume you mean the start position or offset for the pattern.
# 6. Custom Border: Characters to be printed at the border of the diamond.

# In[16]:


def hollow_diamond_star_pattern(rows, diamond_width, base_length, position, border):
    """
    Print a hollow diamond star pattern.

    Parameters:
    - rows (int): Number of rows for the diamond.
    - diamond_width (int): Width of the diamond.
    - base_length (int): The base width for alignment.
    - position (int): The start position or offset.
    - border (str): Characters for the diamond border.
    """
    
    # For the given number of rows, iterate and print pattern
    for i in range(rows):
        # For the upper part of the diamond
        if i < rows // 2:
            print(' ' * (base_length - position - i) + border * diamond_width + ' ' * (2 * i) + border * diamond_width)
        # For the middle of the diamond
        elif i == rows // 2:
            if rows % 2 == 0:
                print(' ' * (base_length - position - i) + border * diamond_width + ' ' * (2 * i) + border * diamond_width)
            else:
                print(' ' * (base_length - position - i) + border * diamond_width + ' ' * (2 * i) + border * diamond_width)
        # For the lower part of the diamond
        else:
            print(' ' * (base_length - position + i - rows + 1) + border * diamond_width + ' ' * (2 * (rows - i) - 2) + border * diamond_width)

# Example usage
rows = 5
diamond_width = 2
base_length = 25
position = 10
border = '*'

hollow_diamond_star_pattern(rows, diamond_width, base_length, position, border)


# ### 425. Generate a Random Word Cloud from Web Data with Custom Word Frequency, Size, Color, Font, Position, Shape, Background, and Custom Image Mask
# Creating a word cloud from web data with the specified customizations is a complex process, but I'll provide you with an outline and code to get started.
# 
# Steps:
# 
# - Extract web data.
# - Process and filter the text.
# - Generate the word cloud with custom parameters.
# Here's a code outline for these steps:
# 
# 1. Extract web data:
# We'll use requests and BeautifulSoup for this purpose.
# 2. Process the text:
# Tokenize the text, remove stopwords, and determine word frequencies using nltk or simple Python string methods.
# 
# 3. Generate the word cloud:
# We'll use the wordcloud library. To customize the appearance, you can use a custom image mask.
# 

# In[ ]:


import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import nltk

# 1. Extract web data
url = 'YOUR_TARGET_URL_HERE'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
text = soup.get_text()

# 2. Process the text
# Tokenization (using NLTK here, but you can choose your method)
nltk.download('punkt')
tokens = nltk.word_tokenize(text)
tokens = [word.lower() for word in tokens if word.isalpha()]

# Remove stopwords
stopwords = set(STOPWORDS)
filtered_tokens = [word for word in tokens if word not in stopwords]

# Here, you can add custom word frequency if needed
# For demonstration, we're using the default frequency computation

# 3. Generate the word cloud
# Load the image mask if you have one
mask = np.array(Image.open('YOUR_IMAGE_MASK_PATH.png'))

wc = WordCloud(
    background_color='white',
    max_words=2000,
    mask=mask,
    contour_width=1,
    contour_color='blue',
    colormap='viridis',   # Choose a colormap: https://matplotlib.org/stable/tutorials/colors/colormaps.html
    font_path='YOUR_FONT_PATH.ttf',   # Path to a font file for custom font
    max_font_size=90,     # Maximum font size
    random_state=42,      # Random state for reproducibility
    collocations=False,   # To not consider bi-grams
)

wc.generate(' '.join(filtered_tokens))

# Display the word cloud
plt.figure(figsize=(10, 8))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()


# ### 426. Convert Decimal to Excess-K Code Using Recursion, Custom K with Variable Size, Custom Encoding Scheme, Variable Base, Custom Precision, and Custom Position
# The Excess-K code, also known as the biased representation, is a way to represent integers where the represented integer is the sum of the actual integer and K. This coding scheme is often used in floating-point arithmetic to represent the exponent.
# 
# The process to convert a decimal number to Excess-K:
# 
# 1. Add K to the decimal number.
# 2. Convert the resultant decimal to binary.
# For this problem, we'll consider K as an input and use a recursive function to convert the sum to binary.

# In[5]:


def decimal_to_binary(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_to_binary(n // 2) + str(n % 2)

def decimal_to_excess_k(number, k, position="right"):
    biased_number = number + k
    binary_representation = decimal_to_binary(biased_number)
    
    if position == "right":
        return binary_representation.rjust(8, '0')  # Padding to 8 bits for example
    elif position == "left":
        return binary_representation.ljust(8, '0')
    else:
        return binary_representation.center(8, '0')

# Testing the function
decimal_number = 5  # Example number
k = 128  # Example bias
print(decimal_to_excess_k(decimal_number, k))


# ### 427. Check if a Number is a Generalized Heptagonal Hexagonal Number Using Modular Arithmetic
# A basic (and possibly inefficient) approach is to generate heptagonal and hexagonal numbers and check if any number exists in both sequences up to a reasonable limit. However, for modular arithmetic, we're often considering residues and checking if numbers satisfy specific properties under modular arithmetic, which can sometimes allow for quicker identification of properties of numbers without computing them directly.
# 
# Without further clarifications on the specific modular arithmetic approach desired, here's a basic function that checks if a number is both heptagonal and hexagonal:

# In[6]:


def is_heptagonal(n):
    # Formula for heptagonal numbers
    return ((8*n + 1)**0.5 + 1) / 2 % 1 == 0

def is_hexagonal(n):
    # Formula for hexagonal numbers
    return ((1 + 8*n)**0.5 + 1) / 4 % 1 == 0

def is_heptagonal_hexagonal(n):
    return is_heptagonal(n) and is_hexagonal(n)

# Testing
x = 40755  # This is an example of a number that is both heptagonal and hexagonal
print(is_heptagonal_hexagonal(x))


# ### 428. Calculate the Volume of a Frustum of a Regular Octahedron with Custom Height and Base Length with Variable Base, Custom Volume Calculation, Custom Units, and Custom Position
# A frustum is a portion of a solid that lies between two parallel planes cutting the solid, especially the section between the base and a plane parallel to the base.
# 
# For the problem at hand, consider a regular octahedron (a polyhedron with 8 equilateral triangle faces). When you slice off the top of an octahedron by a plane parallel to its base, you get a frustum of an octahedron. The frustum will have an upper triangular face, a larger lower triangular base, and three trapezoidal lateral faces.
# 
# We will:
# 
# 1. Calculate the volume of the original octahedron using the given base length.
# 2. Calculate the volume of the smaller octahedron that was sliced off to create the frustum.
# 3. Subtract the smaller octahedron's volume from the original octahedron's volume to get the volume of the frustum.
# Volume of an Octahedron = (sqrt(2)/3) * edge_length^3

# In[4]:


import math

def octahedron_volume(edge_length):
    return (math.sqrt(2) / 3) * edge_length**3

def frustum_volume(base_length, height, units="cm^3", position="right"):
    # Volume of the full octahedron
    full_volume = octahedron_volume(base_length)
    
    # Height of the original octahedron
    original_height = base_length * math.sqrt(2)
    
    # Edge length of the smaller octahedron
    smaller_edge_length = base_length * (original_height - height) / original_height
    
    # Volume of the smaller octahedron
    small_volume = octahedron_volume(smaller_edge_length)
    
    # Volume of the frustum
    frustum_vol = full_volume - small_volume
    
    result = f"{frustum_vol:.2f} {units}"
    
    if position == "right":
        return result.rjust(15)
    elif position == "left":
        return result.ljust(15)
    else:
        return result.center(15)

# Test the function
base_length = 5  # Example base length
height = 4       # Example height (should be less than base_length * sqrt(2))
print(frustum_volume(base_length, height))


# ### 429. Implement Bucket Sort Algorithm on a List of Floating-Point Numbers with Custom Bucket Size and Variable Data Distribution
# Bucket sort works by distributing the input over a set of buckets. Each bucket is then sorted individually, either using a different sorting algorithm or recursively applying the bucket sort algorithm.
# 
# For floating-point numbers between 0 and 1, we can use their value directly to decide on which bucket they should be placed. If our numbers are not in this range, we'll need to normalize them first.
# 
# Here's how you can implement bucket sort for a list of floating-point numbers:
# 
# 1. Step 1: Create empty buckets.
# 2. Step 2: Insert the numbers in the buckets.
# 3. Step 3: Sort each bucket.
# 4. Step 4: Concatenate the buckets.
# 

# In[3]:


def bucket_sort(arr, bucket_size=5):
    # Step 1: Create empty buckets
    min_value, max_value = min(arr), max(arr)
    bucket_count = (max_value - min_value) // bucket_size + 1
    buckets = [[] for _ in range(int(bucket_count))]

    # Step 2: Insert numbers in buckets
    for num in arr:
        index = int((num - min_value) // bucket_size)
        buckets[index].append(num)

    # Step 3: Sort each bucket and Step 4: Concatenate
    return [num for bucket in buckets for num in sorted(bucket)]

# Example:
arr = [0.42, 0.32, 0.59, 0.85, 0.92, 0.38, 0.22, 0.99, 0.20, 0.16]
sorted_arr = bucket_sort(arr, bucket_size=0.1)
print(sorted_arr)


# ### 430. Find the Partitions of a Specific Integer with Custom Partition Scheme, Variable Size, Custom Position, Custom Border, Custom Units, and Custom Precision
# 
# Objective:
# Partition a specific integer based on a custom scheme. The output should display the partitions in a formatted way, based on various customization parameters.
# 
# Parameters:
# 
# 1. Specific Integer: The integer that we want to partition.
# 2. Custom Partition Scheme: A list of ratios to determine the partitions. For instance, if our integer is 100 and our scheme is [0.5, 0.3, 0.2], the partitions would be 50, 30, and 20 respectively.
# 3. Variable Size: If True, the partitions can have variable sizes based on the scheme. If False, they must have fixed sizes.
# 4. Custom Position: A parameter to determine the position of the display (e.g., center, left, right). For simplicity, we'll handle left and right alignments.
# 5. Custom Border: A character to encapsulate the result.
# 6. Custom Units: The unit for each partition (e.g., "k", "m", "h").
# 7. Custom Precision: Decimal precision for the partitioned values.

# In[2]:


def partition_integer(n, scheme, variable_size=True, position="right", border="|", units="k", precision=2):
    # Calculate partitioned values
    if variable_size:
        partitions = [round(n * ratio, precision) for ratio in scheme]
    else:
        avg = round(n / len(scheme), precision)
        partitions = [avg for _ in scheme]

    # Format partitioned values
    partition_strs = [f"{value}{units}" for value in partitions]
    max_length = max(len(p) for p in partition_strs)

    # Align based on the position
    if position == "right":
        partition_strs = [p.rjust(max_length) for p in partition_strs]
    elif position == "left":
        partition_strs = [p.ljust(max_length) for p in partition_strs]

    # Add borders
    partition_strs = [f"{border}{p}{border}" for p in partition_strs]

    return " ".join(partition_strs)

# Example
n = 100
scheme = [0.5, 0.3, 0.2]
result = partition_integer(n, scheme, variable_size=True, position="right", border="[", units="h", precision=2)
print(result)

