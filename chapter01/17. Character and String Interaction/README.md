# 📝 Python Character as String

This lesson explores how Python treats characters and strings, how to interact with single characters, and how to convert between characters and their integer (Unicode) representations. You'll learn practical techniques for manipulating characters and strings in Python.

---

## 1. Learning Objectives

- Understand that Python does not have a separate character type; characters are strings of length 1.
- Use indexing and slicing to access and manipulate characters in strings.
- Convert between characters and their Unicode integer values using `ord()` and `chr()`.
- Iterate over strings character by character.
- Apply character and string manipulation in practical coding scenarios.

---

## 2. Prerequisites

- Basic Python syntax (variables, data types, functions).
- Familiarity with strings and string methods.
- Understanding of loops and basic control flow.

---

## 3. Key Concepts

- **String**: A sequence of characters, e.g., `"hello"`.
- **Character**: In Python, a string of length 1, e.g., `"a"`.
- **Indexing**: Accessing a specific character in a string using its position, e.g., `s[0]`.
- **Slicing**: Extracting a substring using `s[start:end]`.
- **Unicode**: A standard for representing characters as integers.
- **`ord()`**: Converts a single character to its Unicode integer value.
- **`chr()`**: Converts a Unicode integer value to its corresponding character.

---

## 4. Lecture Outline

### 0:00–0:05 — Introduction: Characters vs. Strings in Python
- Python does **not** have a separate `char` type.
- Example: `'a'` is a string of length 1, not a char.

### 0:05–0:10 — Indexing and Slicing Strings
- Accessing individual characters: `s[0]`, `s[-1]`.
- Extracting substrings: `s[1:4]`.
- Example: `"Python"[0]` → `'P'`.

### 0:10–0:15 — Unicode, `ord()`, and `chr()`
- Every character has a Unicode code point.
- `ord('A')` → `65`, `chr(65)` → `'A'`.
- Demonstrate with various characters.

### 0:15–0:20 — Iterating Over Strings
- Using `for` loops to process each character.
- Example: Counting vowels, changing case.

### 0:20–0:25 — Practical Character Manipulation
- Convert between uppercase/lowercase.
- Build new strings by processing characters.
- Example: Caesar cipher (simple shift).

### 0:25–0:30 — Q&A and Summary
- Recap: No char type, use strings of length 1.
- When and why to use `ord()`/`chr()`.

---

## 5. Code Demos

```
# In Python, there is no specific 'char' data type like in some other languages; every character is treated as a string of length one.
character = 'a'  # Defined as a string with a single character

# Print the character and its data type using formatted string literals (f-strings)
print(f"'{character}' is type of: {type(character)}")
# Output will show that the type of 'character' is <class 'str'>, indicating it's a string
```

## 5.1 Extra Code Demos
```python
# 1. Indexing and Slicing
s = "Python"
print(s[0])    # Output: 'P'
print(s[-1])   # Output: 'n'
print(s[1:4])  # Output: 'yth'

# 2. ord() and chr()
print(ord('A'))  # Output: 65
print(chr(66))   # Output: 'B'
print(ord('π'))  # Output: 960

# 3. Iterating over a string
for c in "abc":
    print(c, ord(c))
# Output:
# a 97
# b 98
# c 99

# 4. Building a string by shifting each character (Caesar cipher, shift by 1)
text = "abc"
shifted = ""
for c in text:
    shifted += chr(ord(c) + 1)
print(shifted)  # Output: 'bcd'
```

---

## 6. Exercises

### 1. (Level 1, MCQ)
Which of the following statements is **true** about characters in Python?
- a) Python has a built-in `char` type.
- b) A character is represented as a string of length 1.
- c) You must use `ord()` to create a character.
- d) Characters cannot be indexed from a string.

<details>
<summary>Solution</summary>

**Answer:** b) A character is represented as a string of length 1.
</details>

---

### 2. (Level 1, Short Answer)
What is the output of the following code?

```python
s = "hello"
print(s[1], s[-1])
```

<details>
<summary>Solution</summary>

**Output:** `e o`
</details>

---

### 3. (Level 2, Coding)
Write a function that takes a lowercase letter and returns its position in the English alphabet (e.g., 'a' → 1, 'b' → 2, ..., 'z' → 26).

<details>
<summary>Solution</summary>

```python
def letter_position(c):
    return ord(c) - ord('a') + 1

# Example:
print(letter_position('c'))  # Output: 3
```
</details>

---

### 4. (Level 2, Coding)
Given a string, print a new string where each character is replaced by the next character in Unicode (e.g., 'a' → 'b', 'b' → 'c', ..., 'z' → '{').

```python
s = "abc"
# Your code here
```

<details>
<summary>Solution</summary>

```python
s = "abc"
result = ""
for c in s:
    result += chr(ord(c) + 1)
print(result)  # Output: 'bcd'
```
</details>

---

### 5. (Level 3, Coding)
Write a function that takes a string and returns a new string with only the uppercase letters, using indexing and string concatenation.

```python
s = "PyThOn123!"
# Your code here
```

<details>
<summary>Solution</summary>

```python
def extract_uppercase(s):
    result = ""
    for c in s:
        if 'A' <= c <= 'Z':
            result += c
    return result

# Example:
print(extract_uppercase("PyThOn123!"))  # Output: 'PTO'
```
</details>

---


## 7. Further Reading

- [Python Official Documentation: Strings](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)
- [Unicode HOWTO](https://docs.python.org/3/howto/unicode.html)

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