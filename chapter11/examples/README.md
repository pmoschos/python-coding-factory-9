# 🐍 FastAPI Hands-On Examples 🐍

![Python](https://img.shields.io/badge/language-Python-blue.svg) ![FastAPI](https://img.shields.io/badge/framework-FastAPI-009688.svg) ![License](https://img.shields.io/badge/license-MIT-green.svg)

## Overview 🌟
Welcome to the FastAPI Examples collection — a progressive, hands-on guide that takes you from your first "Hello, World!" API endpoint to a fully authenticated, database-backed, tested application. Each folder is self-contained with its own README, runnable scripts, and (where applicable) enhanced implementations.

## About the Repository 📖
These 12 example modules mirror the theory covered in the companion `docs/` folder. The recommended workflow is: **read the theory** → **study the code** → **run & experiment**. Each example builds on concepts from the previous ones, forming a complete learning path.

## Repository Contents 📂
### Practical Applications 🛠️
- Modern REST API Development with FastAPI 🎯
- Data Validation, Error Handling, and Dependency Injection 🔍
- Database Integration, Authentication, and Testing 📐

## 🐍 FastAPI Examples Collection

<table>
  <tr>
    <td>01. <a href="https://github.com/pmoschos/python-coding-factory-9/tree/main/chapter11/examples/01_getting_started" title="Your first FastAPI app with a root endpoint and auto-generated docs.">Getting Started</a></td>
  </tr>
  <tr>
    <td>02. <a href="https://github.com/pmoschos/python-coding-factory-9/tree/main/chapter11/examples/02_parameters" title="Path parameters, query parameters, enums, and validation constraints.">Parameters</a></td>
  </tr>
  <tr>
    <td>03. <a href="https://github.com/pmoschos/python-coding-factory-9/tree/main/chapter11/examples/03_request_bodies" title="Pydantic models, field validation, nested models, and custom validators.">Request Bodies</a></td>
  </tr>
  <tr>
    <td>04. <a href="https://github.com/pmoschos/python-coding-factory-9/tree/main/chapter11/examples/04_responses" title="Response models, status codes, custom responses, and file downloads.">Responses</a></td>
  </tr>
  <tr>
    <td>05. <a href="https://github.com/pmoschos/python-coding-factory-9/tree/main/chapter11/examples/05_errors" title="HTTPException, custom exception handlers, and validation error overrides.">Error Handling</a></td>
  </tr>
  <tr>
    <td>06. <a href="https://github.com/pmoschos/python-coding-factory-9/tree/main/chapter11/examples/06_dependencies" title="Function dependencies, class dependencies, yield dependencies, and chaining.">Dependency Injection</a></td>
  </tr>
  <tr>
    <td>07. <a href="https://github.com/pmoschos/python-coding-factory-9/tree/main/chapter11/examples/07_async" title="Sync vs async endpoints, background tasks, and concurrency patterns.">Async & Concurrency</a></td>
  </tr>
  <tr>
    <td>08. <a href="https://github.com/pmoschos/python-coding-factory-9/tree/main/chapter11/examples/08_database" title="SQLModel (Pydantic + SQLAlchemy), CRUD operations, and relationships.">Database with SQLModel</a></td>
  </tr>
  <tr>
    <td>09. <a href="https://github.com/pmoschos/python-coding-factory-9/tree/main/chapter11/examples/09_auth" title="Password hashing, JWT tokens, OAuth2 password flow, and protected routes.">Authentication with JWT</a></td>
  </tr>
  <tr>
    <td>10. <a href="https://github.com/pmoschos/python-coding-factory-9/tree/main/chapter11/examples/10_structure_demo" title="Best practices for organizing a multi-file FastAPI project with routers.">Project Structure</a></td>
  </tr>
  <tr>
    <td>11. <a href="https://github.com/pmoschos/python-coding-factory-9/tree/main/chapter11/examples/11_middleware" title="Custom middleware, CORS configuration, and lifespan events.">Middleware & CORS</a></td>
  </tr>
  <tr>
    <td>12. <a href="https://github.com/pmoschos/python-coding-factory-9/tree/main/chapter11/examples/12_testing" title="TestClient, pytest, dependency overrides, and database test fixtures.">Testing</a></td>
  </tr>
</table>

### Educational Value 🎓
- Self-contained scripts that can be run individually for classroom demonstrations.
- Each folder includes a dedicated README with key concepts and code snippets.
- Enhanced implementations available in select folders for deeper exploration.

### Innovative Solutions 💡
- Progressive complexity from a 7-line Hello World to full JWT authentication.
- Real-world patterns including CRUD, dependency chains, and background tasks.

### Well-Documented Code 📄
- Every script includes docstrings and inline comments explaining its functionality.
- Companion theory notes available in the `docs/` folder for each topic.

## Getting Started 🚀
To get started with FastAPI Examples:
1. Ensure Python 3.11+ is installed on your machine.
2. Clone the repository: `git clone https://github.com/pmoschos/python-coding-factory-9`.
3. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS / Linux
   source .venv/bin/activate
   ```
4. Install dependencies:
   ```bash
   pip install fastapi uvicorn sqlmodel python-jose passlib bcrypt httpx pytest
   ```
5. Run any example:
   ```bash
   # From the examples/ directory
   uvicorn 01_getting_started.main:app --reload

   # Then open http://127.0.0.1:8000/docs
   ```

## 📢 Stay Updated

Be sure to ⭐ this repository to stay updated with new examples and enhancements!

## 📄 License

🔐 This project is protected under the [MIT License](https://mit-license.org/).

## Contact 📧
Panagiotis Moschos - pan.moschos86@gmail.com

🔗 *Note: This is a Python project and requires a Python interpreter to run.*

---
<h1 align=center>Happy Coding 👨‍💻 </h1>

<p align="center">
  Made with ❤️ by 
  <a href="https://www.linkedin.com/in/panagiotis-moschos" target="_blank">
  Panagiotis Moschos</a> (https://github.com/pmoschos)
</p>