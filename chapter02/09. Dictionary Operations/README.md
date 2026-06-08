# 📖 Python Dictionary CRUD Functions Demonstration 🔍

Welcome to the Python Dictionary CRUD Functions Demonstration! This script showcases various methods for manipulating dictionaries in Python, including creating, reading, updating, and deleting elements. It's an ideal resource for anyone new to Python or those teaching programming concepts related to dictionary operations.

## 1. Learning Objectives

- Understand the structure and purpose of Python dictionaries.
- Perform CRUD (Create, Read, Update, Delete) operations on dictionaries.
- Use built-in dictionary methods for safe access and modification.
- Apply dictionary operations to solve practical programming tasks.
- Recognize and handle common errors when working with dictionaries.

---

## 2. Prerequisites

- Basic Python syntax and data types (strings, numbers, lists).
- Understanding of variables and assignment.
- Familiarity with functions and control flow (if/else, loops).

---

## 3. Key Concepts

- **Dictionary**: An unordered, mutable collection of key-value pairs (`{key: value}`).
- **Key**: An immutable and unique identifier in a dictionary.
- **Value**: Data associated with a key; can be any type.
- **CRUD**: Operations for Create, Read, Update, and Delete.
- **`get()`**: Safely retrieves a value for a given key, returning a default if the key is missing.
- **`pop()`**: Removes and returns the value for a specified key.
- **`update()`**: Modifies or adds multiple key-value pairs.
- **`in` operator**: Checks if a key exists in the dictionary.

---

## 4. Lecture Outline

### 0:00–0:05 — Introduction to Dictionaries
- What is a dictionary? Syntax and use-cases.
- Example: `person = {'name': 'Alice', 'age': 30}`

### 0:05–0:10 — Creating and Reading Dictionary Entries
- Creating dictionaries with literals and `dict()`.
- Accessing values by key: `person['name']`
- Safe access with `get()`: `person.get('email', 'N/A')`

### 0:10–0:15 — Updating and Adding Entries
- Assigning new values: `person['age'] = 31`
- Adding new key-value pairs: `person['email'] = 'alice@example.com'`
- Using `update()` for batch updates.

### 0:15–0:20 — Deleting Entries
- Removing with `del`: `del person['age']`
- Using `pop()`: `person.pop('email', None)`
- Clearing all entries: `person.clear()`

### 0:20–0:25 — Practical Examples and Common Pitfalls
- Checking for key existence: `'name' in person`
- Handling missing keys and KeyError.
- Iterating over keys, values, and items.

### 0:25–0:30 — Q&A and Summary
- Recap CRUD operations and best practices.
- When to use dictionaries in real-world scenarios.

---

## 5. :computer: Code Demos

```python
# Dictionary CRUD functions

# Initial dictionary of products
products = {1: "apples", 2: "bananas", 10: "honey", 3: "melons"}
print("Initial products:", products)

# Create: Insert a new item
products[3] = "oranges"
print("\nAfter inserting key 3 with value 'oranges':", products)

# Read: Access elements by key
product_10 = products.get(10, "Not Found")
print("\nProduct with key 10:", product_10)

# Update: Change the value of an existing item
products[2] = "milk"
print("\nAfter updating key 2 to 'milk':", products)

# Delete: Remove an item by key using del
del products[1]
print("\nAfter deleting key 1:", products)

# Delete: Remove an item by key using pop() and handle potential KeyError
removed_product = products.pop(3, "Not Found")
print("\nAfter popping key 3:", products)
print("Popped product:", removed_product)

# Delete: Remove the last inserted item using popitem()
key, value = products.popitem()
print("\nAfter popping the last item inserted:", products)
print(f"Popped item - Key: {key}, Value: {value}")

# Check for key existence
key_to_check = 2
if key_to_check in products:
    print(f"\nKey {key_to_check} exists in products.")
else:
    print(f"\nKey {key_to_check} does not exist in products.")

# Iterating through keys
print("\nIterating through keys:")
for key in products.keys():
    print(f"Key: {key}, Value: {products[key]}")

# Iterating through values
print("\nIterating through values:")
for value in products.values():
    print(f"Value: {value}")

# Iterating through key-value pairs
print("\nIterating through key-value pairs:")
for key, value in products.items():
    print(f"Key: {key}, Value: {value}")
```

## 6. Exercises

### 1. (Level 1, MCQ)
Which statement about Python dictionaries is **false**?
- a) Dictionary keys must be unique.
- b) Dictionary values must be unique.
- c) Dictionary keys must be immutable types.
- d) Dictionaries store data as key-value pairs.

<details>
<summary>Solution</summary>

**Answer:** b) Dictionary values must be unique.
</details>

---

### 2. (Level 1, Short Answer)
What will be printed by the following code?

```python
d = {'x': 1, 'y': 2}
print(d.get('z', 0))
```

<details>
<summary>Solution</summary>

**Output:** `0`
</details>

---

### 3. (Level 2, Coding)
Write Python code to add a new key `'country'` with value `'Greece'` to the following dictionary:

```python
person = {'name': 'Nikos', 'age': 28}
# Your code here
```

<details>
<summary>Solution</summary>

```python
person['country'] = 'Greece'
```
</details>

---

### 4. (Level 2, Coding)
Given the dictionary below, update the `'age'` to 29 and remove the `'city'` key.

```python
person = {'name': 'Maria', 'age': 28, 'city': 'Athens'}
# Your code here
```

<details>
<summary>Solution</summary>

```python
person['age'] = 29
del person['city']
```
</details>

---

### 5. (Level 3, Coding)
Write a function `safe_remove(d, key)` that removes the key from dictionary `d` if it exists, and does nothing otherwise. Demonstrate it with `d = {'a': 1, 'b': 2}`, removing `'b'` and then `'c'`.

<details>
<summary>Solution</summary>

```python
def safe_remove(d, key):
    d.pop(key, None)

d = {'a': 1, 'b': 2}
safe_remove(d, 'b')
print(d)  # Output: {'a': 1}
safe_remove(d, 'c')
print(d)  # Output: {'a': 1}
```
</details>

---

## 7. Further Reading

- [Python Official Documentation: Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

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