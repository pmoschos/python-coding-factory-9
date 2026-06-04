# 📝 Python String Handling: Indexing and Traversal


## 1. Learning Objectives

- Understand how to access individual characters in a Python string using indexing.
- Apply positive and negative indexing to extract string elements.
- Traverse strings using loops for character-wise operations.
- Use string slicing to extract substrings.
- Recognize the immutability of strings and its implications for string manipulation.

---

## 2. Prerequisites

- Basic understanding of Python syntax and variables.
- Familiarity with data types (especially strings).
- Experience with loops (`for`, `while`).
- Knowledge of zero-based indexing in Python.

---

## 3. Key Concepts

- **String**: An immutable sequence of Unicode characters.
- **Indexing**: Accessing individual characters using their position (e.g., `s[0]`).
- **Positive Indexing**: Counting from the start (left) of the string, starting at 0.
- **Negative Indexing**: Counting from the end (right) of the string, starting at -1.
- **Slicing**: Extracting a substring using the syntax `s[start:end]`.
- **Traversal**: Iterating over each character in a string, usually with a loop.
- **Immutability**: Strings cannot be changed after creation; new strings are created for modifications.

---

## 4. Lecture Outline

### 0:00–0:05 — Introduction to Strings and Indexing
- What is a string in Python?
- Strings as sequences of characters.
- Example: `s = "Python"`

### 0:05–0:12 — Indexing: Positive and Negative
- Accessing characters with positive indices: `s[0]`, `s[1]`, etc.
- Accessing characters with negative indices: `s[-1]`, `s[-2]`, etc.
- Example: `s = "Python"; s[0]`, `s[-1]`

### 0:12–0:18 — String Slicing
- Syntax: `s[start:end]` (end is exclusive).
- Omitting start or end: `s[:4]`, `s[2:]`
- Example: `s[1:4]`, `s[:3]`, `s[3:]`

### 0:18–0:23 — Traversing Strings
- Using `for` loops to process each character.
- Example: Counting vowels, printing characters one per line.

### 0:23–0:27 — String Immutability and Common Pitfalls
- Strings cannot be changed in place.
- Attempting `s[0] = 'J'` raises an error.
- How to build new strings.

### 0:27–0:30 — Q&A and Summary
- Recap: Indexing, slicing, traversal, immutability.

---

## 5. Code Demos

```
# In Python, there is no specific 'char' data type like in some other languages; 
# every character is treated as a string of length one.

character = 'a'  # Defined as a string with a single character

# Print the character and its data type using formatted string literals (f-strings)

print(f"'{character}' is type of: {type(character)}")

# Output will show that the type of 'character' is <class 'str'>, indicating it's a string

# Define a string variable
message = "Coding Factory"

# Print individual characters using indexing (zero-indexed)
print(message[0])  # 'C'
print(message[1])  # 'o'
print(message[2])  # 'd'
print(message[3])  # 'i'
print(message[4])  # 'n'
print(message[5])  # 'g'

# Strings in Python are immutable, which means you cannot change an existing string directly
# The following line, if uncommented, would result in a TypeError because strings cannot be modified
# message[0] = 'c'

# Use len() to get the number of characters in the string
print(f"Number of letters inside the {message}: {len(message)}")  # Outputs the length of the message

# Iterate over each character in the string using a simple for-loop
for char in message:
    print(char)  # Prints each character on a new line

# The range function generates a sequence of numbers, which by default starts from 0 and goes up to n-1
for i in range(10):
    print(i)  # Prints numbers 0 to 9

# Iterate over the string by index using a for-loop with range based on the length of the message
for i in range(len(message)):
    print(message[i], end=" ")  # end=" " keeps the output on the same line
print()  # Print a newline at the end

# Numeric operations with strings
number = 12345678
number_str = str(number)

# Print individual characters using indexing
print("\nPrint the variable number_str per char\n")
print(int(number_str[0]))  # '1'
print(int(number_str[1]))  # '2'
print(number_str[2])  # '3'
print(number_str[3])  # '4'
print(number_str[4])  # '5'
print(number_str[5])  # '6'
print(number_str[6])  # '7'
print(int(number_str[7]))  # '8'
print("... end of variable number_str\n")

# Perform numeric operations on string-converted digits
print("\n-----\nThe sum of the first [0] and second digit [1] is:", int(number_str[0]) + int(number_str[1]), ".")
print("The sum of the first [0] and eighth digit [7] is:", int(number_str[0]) + int(number_str[7]), ".  \n-----\n")
```

## 5.1 Extra Code Demos
```python
# String Indexing
s = "Python"
print(s[0])   # Output: 'P'
print(s[3])   # Output: 'h'
print(s[-1])  # Output: 'n'
print(s[-3])  # Output: 'h'

# String Slicing
print(s[1:4])   # Output: 'yth'
print(s[:2])    # Output: 'Py'
print(s[3:])    # Output: 'hon'
print(s[-4:-1]) # Output: 'tho'

# Traversing a String
for char in s:
    print(char, end=' ')  # Output: P y t h o n
print()

# Counting vowels in a string
vowels = 'aeiouAEIOU'
count = 0
for c in s:
    if c in vowels:
        count += 1
print("Number of vowels:", count)  # Output: 1

# Attempting to modify a string (will raise an error)
try:
    s[0] = 'J'
except TypeError as e:
    print("Error:", e)  # Output: Error: 'str' object does not support item assignment

# Creating a new string by modification
new_s = 'J' + s[1:]
print(new_s)  # Output: 'Jython'
```

---

## 6. Exercises

### 1. (Level 1, MCQ)
What is the output of the following code?
```python
s = "abcdef"
print(s[-2])
```
- a) 'b'
- b) 'd'
- c) 'e'
- d) 'f'

<details>
<summary>Solution</summary>

**Answer:** c) 'e'
</details>

---

### 2. (Level 1, Short Answer)
Given `s = "hello"`, what is the result of `print(s[1:4])`?

<details>
<summary>Solution</summary>

**Output:** `ell`
</details>

---

### 3. (Level 2, Coding)
Write a Python loop to print each character of the string `s = "CS101"` on a separate line.

<details>
<summary>Solution</summary>

```python
s = "CS101"
for char in s:
    print(char)
# Output:
# C
# S
# 1
# 0
# 1
```
</details>

---

### 4. (Level 2, Coding)
Given `s = "algorithm"`, write code to print the substring `'gori'` using slicing.

<details>
<summary>Solution</summary>

```python
s = "algorithm"
print(s[2:6])  # Output: 'gori'
```
</details>

---


## 7. Further Reading

- [Python Official Documentation: Strings](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)

---

## 📢 Stay Updated

Be sure to ⭐ this repository to stay updated with new examples and enhancements!

## License 📜
🔐 This project is protected under the [MIT License](https://mit-license.org/).

## Contact 📧
Panagiotis Moschos - (pan.moschos86@gmail.com)

---
<h1 align=center>Happy Coding 👨‍💻 </h1>

<h3 align=center>🎉 Let's make learning Python an enjoyable and fruitful journey for everyone!</h3>  

<p align="center">
  Made with ❤️ by Panagiotis Moschos (https://github.com/pmoschos)
</p>