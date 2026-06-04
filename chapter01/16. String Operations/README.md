# 📝 Python String Types Demonstration

This lesson explores how to define and use strings in Python, including single-quoted, double-quoted, triple-quoted, and raw strings. You'll learn how to handle special characters, multi-line text, and escape sequences.

---

## 1. Learning Objectives

- Understand the different ways to define strings in Python.
- Recognize the use and behavior of single, double, and triple quotes.
- Use escape sequences to represent special characters within strings.
- Create multi-line strings and raw strings.
- Identify common pitfalls when working with string literals.

---

## 2. Prerequisites

- Familiarity with Python variables and basic data types.
- Ability to run Python scripts or use an interactive shell.
- Basic understanding of print statements and string output.

---

## 3. Key Concepts

- **String Literal**: A sequence of characters enclosed in quotes.
- **Single-Quoted String (`'...'`)**: String defined with single quotes.
- **Double-Quoted String (`"..."`)**: String defined with double quotes.
- **Triple-Quoted String (`'''...'''` or `"""..."""`)**: String that can span multiple lines.
- **Escape Sequence (`\`)**: Special character combination starting with backslash, e.g., `\n` for newline.
- **Raw String (`r'...'` or `r"..."`)**: String where backslashes are treated as literal characters.

---

## 4. Lecture Outline

### 0:00–0:05 — Introduction to Strings
- What is a string in Python?
- Why are there multiple ways to define strings?

### 0:05–0:10 — Single and Double Quotes
- Defining strings with `'...'` and `"..."`.
- When to use each; handling quotes inside strings.
- **Example:** `'Hello'`, `"World"`, `"It's Python!"`, `'He said "Hi"'`

### 0:10–0:15 — Escape Sequences
- Using backslash (`\`) to insert special characters.
- Common escape sequences: `\n`, `\t`, `\\`, `\'`, `\"`
- **Example:** `"Line1\nLine2"`, `'It\'s Python'`

### 0:15–0:20 — Triple-Quoted Strings
- Defining multi-line strings with `'''...'''` or `"""..."""`
- Preserving line breaks and formatting.
- **Example:** `"""First line\nSecond line"""`

### 0:20–0:25 — Raw Strings
- Prefixing with `r` to avoid escape sequence processing.
- Useful for file paths and regular expressions.
- **Example:** `r"C:\new_folder\test.txt"`

### 0:25–0:30 — Q&A and Summary
- Recap: When to use each string type.
- Common pitfalls and best practices.

---

## 5. Code Demos

```
# Define two string variables using different quote styles for demonstration
str1 = "Hello "  # Notice the space after 'Hello' to ensure proper spacing in concatenation
str2 = 'Coding Factory'

# Concatenate two strings using the '+' operator and store the result in a new variable
str3 = str1 + str2
# Print the concatenated string
print(str3)  # Outputs: Hello Coding Factory
# Directly concatenate and print the two strings
print(str1 + str2)  # Outputs: Hello Coding Factory

# Print an empty line for better readability of output
print()

# Demonstrate string multiplication
# Multiply a string by an integer to repeat the string multiple times
str4 = 7 * str1
# Print the result of string multiplication
print(str4)  # Outputs: Hello Hello Hello Hello Hello Hello Hello 

# Directly print the result of string multiplication
print("CF" * 7)  # Outputs: CFCFCFCFCFCFCF
```

## 5.1 Extra Code Demos
```python
# Single-quoted and double-quoted strings
s1 = 'Hello, world!'
s2 = "Python's syntax is easy."

print(s1)  # Output: Hello, world!
print(s2)  # Output: Python's syntax is easy.

# Including quotes inside strings
s3 = 'He said "Hi!"'
s4 = "It's a sunny day."

print(s3)  # Output: He said "Hi!"
print(s4)  # Output: It's a sunny day.

# Escape sequences
s5 = 'First line\nSecond line'
print(s5)
# Output:
# First line
# Second line

# Triple-quoted strings (multi-line)
s6 = """This is a
multi-line string.
It preserves line breaks."""
print(s6)

# Raw strings
path = r"C:\Users\Name\Documents\file.txt"
print(path)  # Output: C:\Users\Name\Documents\file.txt
```

---

## 6. Exercises

### 1. (Level 1, MCQ)
Which of the following is **not** a valid way to define a string in Python?

a) `'Hello'`  
b) `"Hello"`  
c) `'''Hello'''`  
d) `"""Hello"`  

<details>
<summary>Solution</summary>

**Answer:** d) `"""Hello"`
</details>

**Auto-Grading Rubric:**
- Correct option selected (2 pts)
- Incorrect option (0 pts)

---

### 2. (Level 1, Short Answer)
What is the output of the following code?

```python
print('It\'s Python!')
```

<details>
<summary>Solution</summary>

**Output:**  
It's Python!
</details>

**Auto-Grading Rubric:**
- Correct output (2 pts)
- Minor formatting error (1 pt)
- Incorrect (0 pts)

---

### 3. (Level 2, Coding)
Write a Python statement to print the following exactly (including the quotes):

```
She said, "It's a beautiful day!"
```

<details>
<summary>Solution</summary>

```python
print('She said, "It\'s a beautiful day!"')
# or
print("She said, \"It's a beautiful day!\"")
```
</details>

**Auto-Grading Rubric:**
- Correct string with both types of quotes and escape as needed (3 pts)
- Minor syntax error (1 pt)
- Incorrect (0 pts)

---

### 4. (Level 2, Coding)
Create a multi-line string that prints:

```
Line 1
Line 2
Line 3
```

Write the code to print this using a triple-quoted string.

<details>
<summary>Solution</summary>

```python
multi_line = """Line 1
Line 2
Line 3"""
print(multi_line)
```
</details>

**Auto-Grading Rubric:**
- Correct use of triple quotes and output (3 pts)
- Minor formatting issue (1 pt)
- Incorrect (0 pts)

---

### 5. (Level 3, Coding)
Suppose you want to store the Windows file path `C:\new_folder\test.txt` in a string variable without escape sequences being processed. Write the Python code to do this and print the result.

<details>
<summary>Solution</summary>

```python
path = r"C:\new_folder\test.txt"
print(path)
```
</details>

---


## 6. Further Reading

- [Python 3 Documentation: String and Bytes Literals](https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals)

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