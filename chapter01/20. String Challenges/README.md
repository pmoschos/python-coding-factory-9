# 🧩 Python String Manipulation

This lesson explores essential string manipulation techniques in Python, including indexing, slicing, concatenation, formatting, and common string methods. Mastering these skills is crucial for handling text data in real-world applications.

---

## 1. Learning Objectives

- Understand how to access and modify string data using indexing and slicing.
- Apply string methods for searching, replacing, and formatting text.
- Concatenate and split strings effectively.
- Solve practical problems involving string manipulation.
- Recognize the immutability of Python strings and its implications.

---

## 2. Prerequisites

- Basic Python syntax (variables, data types, functions)
- Familiarity with loops and conditional statements
- Understanding of lists and basic data structures

---

## 3. Key Concepts

- **String**: An immutable sequence of Unicode characters in Python, defined using quotes (`'...'` or `"..."`).
- **Indexing**: Accessing individual characters using zero-based indices, e.g., `s[0]`.
- **Slicing**: Extracting substrings using `[start:stop:step]` notation.
- **Immutability**: Strings cannot be changed in place; operations create new strings.
- **Concatenation**: Joining strings using `+` or `.join()`.
- **String Methods**: Built-in functions like `.lower()`, `.upper()`, `.replace()`, `.find()`, `.split()`, `.strip()`, etc.
- **String Formatting**: Inserting variables into strings using `f-strings`, `%` formatting, or `.format()`.

---

## 4. Lecture Outline

### 0:00–0:05 — Introduction to Strings
- What is a string? How are strings represented in Python?
- Example: `name = "Alice"`

### 0:05–0:15 — Indexing and Slicing
- Accessing characters: `s[0]`, `s[-1]`
- Slicing: `s[2:5]`, `s[:4]`, `s[::2]`
- Examples and pitfalls (out-of-range, negative indices)

### 0:15–0:20 — String Immutability & Concatenation
- Strings cannot be changed in place
- Concatenation with `+`, repetition with `*`
- Example: `greeting = "Hi, " + name`

### 0:20–0:25 — Common String Methods
- Changing case: `.upper()`, `.lower()`
- Searching: `.find()`, `.index()`
- Replacing: `.replace()`
- Splitting and joining: `.split()`, `.join()`
- Stripping whitespace: `.strip()`, `.lstrip()`, `.rstrip()`
- Examples for each

### 0:25–0:30 — String Formatting
- f-strings: `f"Hello, {name}!"`
- `.format()` and `%` formatting
- Example: `f"{name} is {age} years old."`

---

## 5. Code Demos

```
# Challenge 1
# Printing each character of the word "Factory" incrementally repeated on each line.
# F
# aa     
# ccc    
# tttt   
# ooooo
# rrrrrr
# yyyyyyy
print("Challenge 1")
message = "Factory"
for i in range(len(message)):
    print(message[i] * (i + 1))

# Challenge 2
# Printing each character of the word "Factory" incrementally repeated,
# followed by a decreasing number of asterisks to form a right-aligned triangle.
# F******
# aa*****
# ccc****
# tttt***
# ooooo**
# rrrrrr*
# yyyyyyy
print("Challenge 2")
for i in range(len(message)):
    print(message[i] * (i + 1), end="*" * (len(message) - i - 1))
    print()
```

## 5.1 Extra Code Demos
```python
# Indexing and Slicing
s = "Python"
print(s[0])      # Output: 'P'
print(s[-1])     # Output: 'n'
print(s[1:4])    # Output: 'yth'
print(s[::-1])   # Output: 'nohtyP' (reversed)

# Concatenation and Repetition
greet = "Hello"
name = "Bob"
message = greet + ", " + name + "!"
print(message)   # Output: 'Hello, Bob!'
print("Hi! " * 3)  # Output: 'Hi! Hi! Hi! '

# String Methods
text = "  Python is Fun!  "
print(text.lower())        # Output: '  python is fun!  '
print(text.strip())        # Output: 'Python is Fun!'
print(text.replace("Fun", "Awesome"))  # Output: '  Python is Awesome!  '

# Splitting and Joining
csv = "apple,banana,cherry"
fruits = csv.split(",")
print(fruits)              # Output: ['apple', 'banana', 'cherry']
sentence = " ".join(fruits)
print(sentence)            # Output: 'apple banana cherry'

# String Formatting
age = 25
print(f"{name} is {age} years old.")   # Output: 'Bob is 25 years old.'
```

---

## 6. Exercises

### 1. (Level 1, MCQ)
Which of the following statements about Python strings is **true**?
- a) Strings are mutable.
- b) Strings can be indexed and sliced.
- c) Strings cannot be concatenated.
- d) Strings do not support methods.

<details>
<summary>Solution</summary>

**Answer:** b) Strings can be indexed and sliced.
</details>

---

### 2. (Level 1, Short Answer)
What is the output of the following code?

```python
s = "Python"
print(s[2:5])
```

<details>
<summary>Solution</summary>

**Output:** `tho`
</details>

---

### 3. (Level 2, Coding)
Write Python code to convert the string `"  Hello, World!  "` to lowercase and remove leading/trailing whitespace.

<details>
<summary>Solution</summary>

```python
s = "  Hello, World!  "
result = s.lower().strip()
print(result)  # Output: 'hello, world!'
```
</details>

---

### 4. (Level 2, Coding)
Given the string `"apple,banana,cherry"`, split it into a list of fruits and print each fruit on a separate line.

<details>
<summary>Solution</summary>

```python
s = "apple,banana,cherry"
fruits = s.split(",")
for fruit in fruits:
    print(fruit)
# Output:
# apple
# banana
# cherry
```
</details>


---

## 7. Further Reading

- [Python Official Documentation: str methods](https://docs.python.org/3/library/stdtypes.html#string-methods)

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