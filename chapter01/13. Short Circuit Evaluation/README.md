# 🧠 Python Logical Operators & Short-Circuit Evaluation

This lesson explores Python's logical operators (`and`, `or`, `not`), their behavior, and the concept of short-circuit evaluation. You'll learn how these operators work with Boolean expressions and other data types, and how short-circuiting can impact program flow and efficiency.

---

## 1. Learning Objectives

- Understand the function and syntax of Python's logical operators: `and`, `or`, and `not`.
- Predict the result of logical expressions, including those involving non-Boolean values.
- Explain and identify short-circuit evaluation in logical expressions.
- Apply logical operators to control program flow and optimize code.
- Recognize common pitfalls and best practices when using logical operators.

---

## 2. Prerequisites

- Familiarity with Python variables, data types, and basic expressions.
- Understanding of Boolean values (`True`, `False`) and comparison operators (`==`, `<`, `>`, etc.).
- Basic experience with conditional statements (`if`, `else`).

---

## 3. Key Concepts

- **Logical Operators**: Special operators used to combine or invert Boolean expressions.
    - **`and`**: Returns `True` if both operands are true.
    - **`or`**: Returns `True` if at least one operand is true.
    - **`not`**: Inverts the Boolean value.
- **Short-Circuit Evaluation**: The process where Python stops evaluating further operands in a logical expression as soon as the result is determined.
    - For `and`, if any operand is `False`, evaluation stops and `False` is returned.
    - For `or`, if any operand is `True`, evaluation stops and `True` is returned.
- **Truthiness**: In Python, values like `0`, `''`, `[]`, `None` are considered `False` in a Boolean context; all others are `True`.
- **Non-Boolean Return Values**: Logical operators return the actual operand value, not just `True` or `False`, when used with non-Boolean types.

---

## 4. Lecture Outline

### 0:00–0:05 — Introduction to Logical Operators
- Overview of `and`, `or`, `not`
- Boolean logic: truth tables

### 0:05–0:12 — Using Logical Operators in Python
- Syntax and usage with Booleans
- Examples:
    - `True and False`
    - `True or False`
    - `not True`

### 0:12–0:18 — Truthiness and Non-Boolean Values
- What is "truthy" and "falsy"?
- Examples with numbers, strings, lists:
    - `0 and 5`
    - `'' or 'hello'`
    - `not []`

### 0:18–0:25 — Short-Circuit Evaluation
- Definition and motivation (efficiency, avoiding errors)
- Demonstration: expressions with side effects
- Example: `x != 0 and (10 / x > 1)`
    - Why does this avoid ZeroDivisionError?
- Caution: Side effects and function calls

### 0:25–0:30 — Q&A, Recap, and Best Practices
- When to use logical operators
- Common mistakes (e.g., assuming always Boolean return)
- Summary

---

## 5. Code Demos

```
# Define a string variable for the name
name = "Bob"

# Demonstrate the use of the `or` logical operator for variable assignment
print("====== or ======")
# Use `or` to assign "User" to valid_user if the left-hand side (None in this case) is falsy
valid_user = None or "User"
# Output: Hello User
print("Hello", valid_user)
print()

# If `name` has a truthy value, it will be assigned to valid_user; otherwise, "User" would be assigned
valid_user = name or "User"
# Output: Hello Bob
print("Hello", valid_user)
print()

# Demonstrate the use of the `and` logical operator for conditional checking
print("====== and ======")

# Define a string variable for the email
email = "bob@example.com"
# Use `and` to check that email is not empty and assign the email to valid_email if it's true
valid_email = email and email != ""
# Output: Valid Email: bob@example.com
print("Valid Email:", valid_email)

# EXTRA: Conditional output based on the value of valid_email
if valid_email:
    # If valid_email is truthy, print a greeting and the email address
    print(f"Hello {valid_user}, your email is {email}")
else:
    # If valid_email is falsy, prompt the user to provide a valid email address
    print(f"Hello {valid_user}, please provide a valid email address.")
```

### 5.1 Extra Code Demos
```python
# Basic logical operators
print(True and False)   # Output: False
print(True or False)    # Output: True
print(not True)         # Output: False

# Logical operators with non-Boolean values
print(0 and 5)          # Output: 0 (0 is falsy, so returned)
print(3 and 5)          # Output: 5 (both truthy, returns last)
print('' or 'hello')    # Output: 'hello' ('' is falsy, so returns 'hello')
print([] or [1, 2, 3])  # Output: [1, 2, 3]

# Short-circuit evaluation
def side_effect():
    print("Function called!")
    return True

print(False and side_effect())  # Output: False (function not called)
print(True or side_effect())    # Output: True (function not called)

# Avoiding ZeroDivisionError with short-circuit
x = 0
print(x != 0 and (10 / x > 1))  # Output: False (second part not evaluated)
```

---

## 6. Exercises

### 1. (Level 1, MCQ)
What is the output of the following code?

```python
print(0 or 'Python')
```

- a) 0
- b) 'Python'
- c) True
- d) False

<details>
<summary>Solution</summary>

**Answer:** b) 'Python'
</details>

---

### 2. (Level 1, Short Answer)
What will be printed by the following code?

```python
print(not [])
```

<details>
<summary>Solution</summary>

**Output:** `True`  
Explanation: `[]` is falsy, so `not []` is `True`.
</details>

---

### 3. (Level 2, Coding)
Write a Python expression that prints `'Non-empty'` if the variable `s` is a non-empty string, otherwise prints `'Empty'`. Use logical operators.

```python
s = "hello"
# Your code here
```

<details>
<summary>Solution</summary>

```python
print(s and 'Non-empty' or 'Empty')
# Output: 'Non-empty' if s is non-empty, 'Empty' if s is ''
```
</details>


---

## 7. Further Reading

- [Python Documentation: Boolean Operations](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not)

---

## 📢 Stay Updated
Be sure to ⭐ this repository to stay updated with new examples and enhancements!

## 📄 License
🔐 This project is protected under the [MIT License](https://mit-license.org/).

## Contact 📧
Panagiotis Moschos - pan.moschos86@gmail.com

🔗 *Note: This is a Python script and requires a Python interpreter to run.*

---

<h1 align=center>Happy Coding 👨‍💻 </h1>
<p align="center">
  Made with ❤️ by Panagiotis Moschos (https://github.com/pmoschos)
</p>