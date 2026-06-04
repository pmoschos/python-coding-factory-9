# 🧩 Python Input Handling and Logical Operations

This lesson explores how to safely handle user input in Python and how logical operators (and, or, not) interact with input validation. You'll also learn about short-circuit evaluation and best practices for robust, user-friendly programs.

Reference: [python-CF7/chapter01/14. Short Circuit Application](https://github.com/pmoschos/python-CF7/tree/main/chapter01/14.%20Short%20Circuit%20Application)

---

## 1. Learning Objectives

- Understand how to safely receive and validate user input in Python.
- Explain and apply logical operators (`and`, `or`, `not`) in input validation.
- Describe and utilize short-circuit evaluation in logical expressions.
- Write Python code that prevents runtime errors from invalid input.
- Apply best practices for combining input handling with logical operations.

---

## 2. Prerequisites

- Basic Python syntax (variables, functions, `input()`, `print()`).
- Understanding of data types (strings, integers, floats).
- Familiarity with conditional statements (`if`, `else`).
- Experience with simple error handling (try/except is a plus).

---

## 3. Key Concepts

- **Input Handling**: The process of receiving and validating data from the user.
- **Logical Operators**: `and`, `or`, `not`—used to combine or invert boolean expressions.
- **Short-Circuit Evaluation**: Logical expressions stop evaluating as soon as the outcome is determined (e.g., in `A and B`, if `A` is `False`, `B` is not evaluated).
- **Input Validation**: Checking if user input meets required criteria before using it.
- **Type Conversion**: Changing data from one type to another (e.g., `int("5")`).
- **Error Prevention**: Techniques to avoid runtime errors (like `ValueError` from invalid conversions).

---

## 4. Lecture Outline

### 0:00–0:05 — Introduction & Motivation
- Why is user input risky? (e.g., entering "abc" when a number is expected)
- Common errors: `ValueError` when converting input.

### 0:05–0:12 — Input Handling Basics
- Using `input()` to get user data.
- The need for validation before using input.
- Example: `age = int(input("Enter your age: "))`—what could go wrong?

### 0:12–0:20 — Logical Operators & Short-Circuiting
- Review: `and`, `or`, `not`—truth tables and usage.
- Short-circuit behavior:
    - `and`: stops at first `False`
    - `or`: stops at first `True`
- Why does this matter for input validation?

### 0:20–0:25 — Safe Input Validation Patterns
- Checking input before conversion: `if s and s.isdigit():`
- Using logical operators to guard conversions.
- Example: Only convert if input is not empty and is numeric.

### 0:25–0:30 — Practical Demo & Q&A
- Walk through a robust input validation script.
- Discuss common pitfalls and best practices.

---

## 5. Code Demos

```
# Prompt the user to enter a username and store it in a variable
username = input(f"Enter your username: ")

# Prompt the user to enter an email address and store it in a variable
email = input("Enter your email: ")

# Using the 'or' logical operator to assign a fallback value
# If 'username' is truthy (non-empty), use it; otherwise, use the fallback value "User"
valid_user = username or "User"

# Repeat the operation to reinforce the example (this line could be omitted as it's redundant)
valid_user = username or "User"

# Use a combination of 'and' and 'or' to construct an output message
# 'email and f"your email is {email}"' evaluates to the email message if 'email' is non-empty
# If 'email' is empty, the expression after 'or' is used, asking for a valid email address
print(f"Hello {valid_user}, " + ((email and f"your email is {email}") or ("please provide a valid email address.")))
```

## 5.1 Extra Code Demos
```python
# Example 1: Unsafe input conversion (can crash)
s = input("Enter a number: ")
n = int(s)  # Fails if s is not numeric

# Example 2: Safe input with validation using logical operators and short-circuiting
s = input("Enter a number: ")
if s and s.isdigit():  # Only True if s is non-empty and all digits
    n = int(s)
    print("You entered:", n)
else:
    print("Invalid input! Please enter a numeric value.")

# Example 3: Using 'or' for default values
s = input("Enter your name (or leave blank): ")
name = s or "Anonymous"
print("Hello,", name)
```

---

## 6. Exercises

### 1. (Level 1, MCQ)
Which statement about short-circuit evaluation in Python is correct?
- a) Both sides of an `and` expression are always evaluated.
- b) In `A or B`, if `A` is `True`, `B` is not evaluated.
- c) In `A and B`, if `A` is `True`, `B` is not evaluated.
- d) Short-circuiting only applies to arithmetic operators.

<details>
<summary>Solution</summary>

**Answer:** b) In `A or B`, if `A` is `True`, `B` is not evaluated.
</details>

---

### 2. (Level 1, Short Answer)
What will the following code print if the user enters nothing (just presses Enter)?

```python
s = input("Enter something: ")
if s and s.isdigit():
    print("Valid number")
else:
    print("Invalid input")
```

<details>
<summary>Solution</summary>

**Output:** `Invalid input`
</details>

---

### 3. (Level 2, Coding)
Write a Python snippet that asks the user for a positive integer and prints its double. If the input is invalid (empty, not a number, or not positive), print "Invalid input".

<details>
<summary>Solution</summary>

```python
s = input("Enter a positive integer: ")
if s and s.isdigit() and int(s) > 0:
    print(int(s) * 2)
else:
    print("Invalid input")
```
</details>

---

### 4. (Level 2, Coding)
Given the following code, explain why it is safe from `ValueError`:

```python
s = input("Enter a number: ")
if s and s.isdigit():
    n = int(s)
    print(n)
```

<details>
<summary>Solution</summary>

**Explanation:**  
The code only attempts to convert `s` to an integer if `s` is not empty and contains only digits. This prevents `int(s)` from raising a `ValueError` due to invalid input.
</details>

---

### 5. (Level 3, Coding)
Write a Python program that asks the user for two numbers. If both are valid integers, print their sum. Otherwise, print "At least one input is invalid". Use logical operators and short-circuiting to avoid exceptions.

<details>
<summary>Solution</summary>

```python
a = input("Enter first number: ")
b = input("Enter second number: ")

if a and a.isdigit() and b and b.isdigit():
    print(int(a) + int(b))
else:
    print("At least one input is invalid")
```
</details>

---


## 7. Further Reading

- [Python Official Documentation: Logical Operators](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not)
- [Python Input and Output](https://docs.python.org/3/tutorial/inputoutput.html)

---

## 📢 Stay Updated
Be sure to ⭐ this repository to keep up with updates and new learning materials!

## 📄 License
🔐 This project is protected under the [MIT License](https://mit-license.org/).

## Contact 📧
Panagiotis Moschos - pan.moschos86@gmail.com

🔗 *Note: This is a Python script and requires a Python interpreter to run.*

---
<h1 align="center">Happy Coding 👨‍💻</h1>

<p align="center">
  Made with ❤️ by <a href="https://www.linkedin.com/in/panagiotis-moschos">Panagiotis Moschos</a> (<a href="https://github.com/pmoschos">GitHub</a>)
</p>