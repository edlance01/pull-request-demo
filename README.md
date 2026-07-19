```python
readme_content = """# Git & GitHub Pull Request Demo Guide v1.2

This guide walks you through setting up a basic Python project using `uv`, creating a bug deliberately, and fixing it via a GitHub Pull Request (PR) workflow.

---

## Phase 1: Initial Repository Setup

### 1. Project Structure
Create the following files in your root directory (`pull-request-demo/`):

**`.gitignore`**
```text
# Virtual environments
.venv/
env/
venv/
ENV/

# Python caching
__pycache__/
*.pyc
*.pyo
*.pyd

# uv specific paths
.uv/

# OS metadata
.DS_Store
Thumbs.db

```

**`calculator.py`** (With an intentional bug)

```python
def add(a, b):
    return a + b

def divide(a, b):
    # Intentional bug for the demo: we forgot to handle division by zero!
    return a / b

if __name__ == "__main__":
    print(f"2 + 3 = {add(2, 3)}")
    print(f"10 / 2 = {divide(10, 2)}")

```

**`test_calculator.py`**

```python
from calculator import add, divide

def test_add():
    assert add(2, 3) == 5

def test_divide():
    assert divide(10, 2) == 5
    # The pull request will later add a test for dividing by zero!

```

### 2. Push the Baseline to GitHub

Run the following commands in your terminal to initialize Git and push the main branch:

```bash
# Initialize and commit baseline code
git init
git add .gitignore calculator.py test_calculator.py
git commit -m "Initial commit: basic calculator setup"

# Link to GitHub (Replace with your actual GitHub username)
git remote add origin [https://github.com/YOUR-USERNAME/pull-request-demo.git](https://github.com/YOUR-USERNAME/pull-request-demo.git)
git branch -M main
git push -u origin main

```

*Note: Create a blank repository on GitHub named `pull-request-demo` before running the remote commands. Do **not** initialize it with a README, license, or .gitignore on GitHub.*

---

## Phase 2: The Pull Request Workflow

### 1. Create a Feature Branch

Switch to a new branch where you will fix the bug:

```bash
git checkout -b fix-zero-division

```

### 2. Apply the Fix & Add Tests

Update your local files to handle the zero-division error gracefully.

**Updated `calculator.py**`

```python
def add(a, b):
    return a + b

def divide(a, b):
    # Bug fixed: now handling division by zero gracefully
    if b == 0:
        return "Cannot divide by zero"
    return a / b

if __name__ == "__main__":
    print(f"2 + 3 = {add(2, 3)}")
    print(f"10 / 2 = {divide(10, 2)}")
    print(f"10 / 0 = {divide(10, 0)}")  # Added to verify the fix

```

**Updated `test_calculator.py**`

```python
from calculator import add, divide

def test_add():
    assert add(2, 3) == 5

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    # Testing our new fix
    assert divide(10, 0) == "Cannot divide by zero"

```

### 3. Push and Open the Pull Request

Submit your changes to GitHub to propose the fix:

```bash
# Commit the updates to your branch
git add calculator.py test_calculator.py
git commit -m "Fix: handle division by zero gracefully"

# Push the branch to GitHub
git push -u origin fix-zero-division

```

### 4. Merge on GitHub

1. Go to your repository on GitHub.
2. Click the green **"Compare & pull request"** banner that appears.
3. Add a short title and description, then click **"Create pull request"**.
4. Review the side-by-side diff, and click the green **"Merge pull request"** button to bring the fix into your `main` branch!
"""

with open("README.md", "w", encoding="utf-8") as f:
f.write(readme_content)

```

Your Markdown file is ready
[file-tag: code-generated-file-750d6879-face-48f2-9843-284df736a582]

I have consolidated all the configuration files, the buggy code, the corrected code, and the step-by-step Git instructions into a single clean `README.md` file. 

You can save this file directly into your `pull-request-demo/` root directory. When you push it to GitHub, it will beautifully render on your repository homepage, making it an excellent reference guide for practicing your branch and PR workflows!

```