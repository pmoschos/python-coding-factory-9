# 📋 Python List Operations Demonstration 🔄

Welcome to the Python List Operations Demonstration! This script covers essential operations for manipulating Python lists, such as adding, updating, deleting, and searching for elements. It’s a comprehensive guide for mastering Python’s list methods.

---

## 1. Learning Objectives

- Understand how to create and access elements in Python lists.
- Perform fundamental list operations: indexing, slicing, adding, removing, and updating elements.
- Utilize built-in list methods for common tasks (e.g., `append`, `insert`, `remove`, `pop`, `sort`, `reverse`).
- Apply list operations to solve practical programming problems.
- Recognize the difference between list copying (shallow vs. deep) and its implications.

---

## 2. Prerequisites

- Basic Python syntax (variables, data types, print statements).
- Understanding of strings and numbers.
- Familiarity with loops and conditional statements.

---

## 3. Key Concepts

- **List**: An ordered, mutable collection of elements, defined with square brackets (e.g., `[1, 2, 3]`).
- **Indexing**: Accessing elements by their position (zero-based).
- **Slicing**: Extracting sublists using `[start:stop:step]` notation.
- **Mutability**: Lists can be changed after creation (add, remove, update elements).
- **List Methods**: Functions like `append()`, `insert()`, `remove()`, `pop()` etc.

---

### 💻 Script Code

```python
# Populate a list with initial values
fruits = ["Apple", "Banana", "Cherry", "Apple"]
print("Initial list of fruits:", fruits)

# Add a single element at the end of the list
fruits.append("Berry")
print("After adding Berry:", fruits)

# Add multiple elements at the end of the list
fruits.extend(["Grapes", "Fig"])
print("After adding Grapes and Fig:", fruits)

# Insert an element at a specific position
fruits.insert(1, "Coconut")  # Insert Coconut at position 1
print("After inserting Coconut at position 1:", fruits)

# Update the first element
fruits[0] = "Melon"
print("After updating the first element to Melon:", fruits)

# Update a slice of the list (two elements)
fruits[1:3] = ["A"]  # Replace elements at index 1 and 2
print("After updating two elements:", fruits)

# Delete an element by position using pop()
removed_item = fruits.pop(1)  # Remove the second element
print(f"Removed item: {removed_item}")
print("List after removal:", fruits)

# Delete an element by value using remove()
fruits.remove("Cherry")  # Remove the first occurrence of "Cherry"
print("List after removing Cherry:", fruits)

# Check if a removed item exists in the list
if "Cherry" in fruits:
    print("Cherry still exists in the list")
else:
    print("Cherry doesn't exist in the list")

# Search for an element in the list and get its position
pos = fruits.index("Berry")
print(f"'Berry' is at position {pos} in the list.")
```

## 4. Exercises

### 1. (Level 1, MCQ)
Which method adds an element to the end of a list?
- a) `insert()`
- b) `append()`
- c) `extend()`
- d) `add()`

<details>
<summary>Solution</summary>

**Answer:** b) `append()`
</details>

---

### 2. (Level 1, Short Answer)
What is the output of the following code?

```python
nums = [5, 10, 15, 20]
print(nums[1:3])
```

<details>
<summary>Solution</summary>

**Output:** `[10, 15]`
</details>

---

### 3. (Level 2, Coding)
Write Python code to remove the first occurrence of `'cat'` from the list below.

```python
animals = ['dog', 'cat', 'bird', 'cat']
# Your code here
```

<details>
<summary>Solution</summary>

```python
animals.remove('cat')
print(animals)  # Output: ['dog', 'bird', 'cat']
```
</details>

---

### 4. (Level 2, Coding)
Given the list `numbers = [3, 1, 4, 1, 5, 9]`, write code to sort the list in descending order and print it.

<details>
<summary>Solution</summary>

```python
numbers.sort(reverse=True)
print(numbers)  # Output: [9, 5, 4, 3, 1, 1]
```
</details>

---

## 6. Further Reading

- [Python Official Documentation: Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

---


## 📢 Stay Updated
Be sure to ⭐ this repository to stay updated with new examples and enhancements!

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