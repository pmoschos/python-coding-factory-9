# ✂️ Python String Slicing Techniques

This lesson explores Python string slicing, a powerful technique for extracting substrings, reversing strings, and manipulating text efficiently. Mastering slicing will help you write concise, readable, and effective code for text processing tasks.

---

## 1. Learning Objectives

- Understand the syntax and semantics of Python string slicing.
- Use positive and negative indices to access string elements and substrings.
- Apply step values to select characters at intervals or reverse strings.
- Solve practical problems using string slicing (e.g., extracting substrings, reversing, skipping).
- Recognize and handle common slicing pitfalls and edge cases.

---

## 2. Prerequisites

- Basic Python syntax (variables, strings, print statements).
- Familiarity with zero-based indexing.
- Understanding of basic data types (especially strings and lists).

---

## 3. Key Concepts

- **String**: An immutable sequence of Unicode characters in Python.
- **Indexing**: Accessing individual characters using their position (starting at 0).
- **Slicing**: Extracting a substring using `[start:stop:step]` notation.
- **Start**: The index where the slice begins (inclusive).
- **Stop**: The index where the slice ends (exclusive).
- **Step**: The interval between indices (default is 1; can be negative).
- **Negative Index**: Indexing from the end of the string (`-1` is last character).
- **Immutability**: Strings cannot be changed in place; slicing creates new strings.

---

## 4. Lecture Outline

### 0:00–0:05 — Introduction to Strings and Indexing
- What is a string? How are characters indexed?
- Example: `"Python"` → P(0), y(1), t(2), h(3), o(4), n(5)

### 0:05–0:15 — Basic Slicing Syntax
- General form: `s[start:stop]`
- Examples:
    - `s[1:4]` extracts characters at indices 1, 2, 3.
    - Omitting start/stop: `s[:3]`, `s[2:]`

### 0:15–0:20 — Step Values and Advanced Slicing
- Syntax: `s[start:stop:step]`
- Using steps to skip characters: `s[::2]`
- Negative steps to reverse: `s[::-1]`

### 0:20–0:25 — Negative Indices and Edge Cases
- Accessing from the end: `s[-1]`, `s[-3:]`
- Out-of-range indices: behavior and safety
- Slicing with start > stop

### 0:25–0:30 — Practical Applications and Q&A
- Extracting substrings, reversing, skipping
- Common mistakes and debugging tips

---

## 5. Code Demos

```
s = "Coding Factory"

# Single character slicing using positive indexing
s1 = s[7]  # 'F', the character at index 7

# Slicing a substring from the beginning up to (but not including) index 6
s2 = s[:6]  # 'Coding'

# Slicing a substring from index 7 to the end of the string
s3 = s[7:]  # 'Factory'

# Slicing the whole string
s4 = s[:]  # 'Coding Factory'
# Alternatively, s4 = s[::] would yield the same result

# Negative slicing
# Slicing from the start up to (but not including) the last character
s5 = s[:-1]  # 'Coding Factor'

# Slicing from the start up to (but not including) the second to last character
s6 = s[:-2]  # 'Coding Facto'

# Print the results of the slicing operations
print(s1)  # Outputs: F
print(s2)  # Outputs: Coding
print(s3)  # Outputs: Factory
print(s4)  # Outputs: Coding Factory
print(s5)  # Outputs: Coding Factor
print(s6)  # Outputs: Coding Facto

# Reversing the string using slicing
r_s = s[::-1]  # 'yrotcaF gnidoC'
print(r_s)  # Outputs: yrotcaF gnidoC

# Slicing from index 7 to index 7, which results in an empty string
s_q = s[7:7]  # ''
print(s_q)  # Outputs: (an empty line)
```

## 5.1 Εxtra Code Demos
```python
# Basic string and indexing
s = "Python"
print(s[0])    # Output: 'P'
print(s[-1])   # Output: 'n'

# Basic slicing
print(s[1:4])  # Output: 'yth'
print(s[:2])   # Output: 'Py'
print(s[3:])   # Output: 'hon'

# Slicing with step
print(s[::2])  # Output: 'Pto'
print(s[1:5:2])# Output: 'yh'

# Negative step (reverse)
print(s[::-1]) # Output: 'nohtyP'

# Negative indices in slicing
print(s[-4:-1])# Output: 'tho'

# Edge cases
print(s[100:200]) # Output: ''
print(s[2:2])     # Output: ''
```

---

## 6. Exercises

### 1. (Level 1, MCQ)
What is the output of the following code?

```python
s = "abcdef"
print(s[2:5])
```
- a) 'bcd'
- b) 'cde'
- c) 'def'
- d) 'cdef'

<details>
<summary>Solution</summary>

**Answer:** b) 'cde'
</details>

---

### 2. (Level 1, Short Answer)
Given `s = "OpenAI"`, what does `s[::-1]` return?

<details>
<summary>Solution</summary>

**Answer:** 'IAnepO'
</details>

---

### 3. (Level 2, Coding)
Write a Python statement to extract every second character from the string `"DataScience"` starting from the first character.

<details>
<summary>Solution</summary>

```python
s = "DataScience"
print(s[::2])  # Output: 'DtSine'
```
</details>

---

### 4. (Level 2, Coding)
Given `s = "substring"`, write a statement to extract the substring `"str"` using negative indices.

<details>
<summary>Solution</summary>

```python
s = "substring"
print(s[-6:-3])  # Output: 'str'
```
</details>

---


## 7. Further Reading

- [Python Official Documentation: Sequence Types — str, bytes, bytearray](https://docs.python.org/3/library/stdtypes.html#typesseq)
- [Python String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)

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