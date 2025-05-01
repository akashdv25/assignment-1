![image](https://github.com/user-attachments/assets/9ee42a69-81d7-496b-a5f7-5da96d86310d)# 🐍 Python Concepts Explorer

Welcome to our awesome Python learning journey! This project is all about exploring some of the coolest and most powerful features in Python. Let's dive in! 🚀

## 🎯 What's Inside?

### 1. 🎩 Magic Methods (Dunder Methods)
Ever wondered how Python objects know what to do when you add them together or try to print them? That's where dunder methods come in! We've got examples of:
- `__str__` - Making our objects print beautifully
- `__len__` - Giving our objects a length
- `__add__` - Teaching our objects math!
- And many more magical methods...

### 2. 🎨 Decorators
Want to add superpowers to your functions without changing their code? Decorators are here to help! We explore:
- Basic function decorators
- Real-world use cases (like in Flask!)
- How to write your own decorators
- Logging, timing, and authentication examples

### 3. 📦 Modules and Packages
Learn how to organize your Python code like a pro! We cover:
- What makes a directory a Python package
- The mysterious `__init__.py` file and its powers
- How to structure your code for maximum reusability
- Importing and using modules effectively

### 4. 📈 Interactive Stock Portfolio Tracker
A Streamlit web app that demonstrates our Python concepts in action:
- Track stock transactions and portfolio performance
- Real-time stock data visualization
- Uses decorators, args, and string formatting
- Interactive user interface with Streamlit

![](app-image)



## 🚀 Getting Started

1. Clone this repository
2. Create a virtual environment:
   ```bash
   python -m venv myvenv
   source myvenv/bin/activate  # On Windows: myvenv\Scripts\activate
   ```
3. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Streamlit app:
   ```bash
   streamlit run main.py
   ```

## 📁 Project Structure
```
assignment-1/
│
├── src/                          # Source code directory
│   ├── __init__.py              # Makes src a package
│   ├── dunder-magic-methods.py  # Magic methods examples
│   ├── decorators.py            # Decorator patterns and examples
│   ├── string-formatters.py     # String formatting techniques
│   ├── list-comprehension.py    # List comprehension examples
│   ├── keyword-args.py          # Keyword arguments usage
│   └── positional-args.py       # Positional arguments examples
│
├── __init__.py                 # Root package initialization
├── main.py                     # Streamlit app entry point
└── requirements.txt            # Project dependencies
```

## Web-View of README.md 

[Access Here ](https://akashdv25.github.io/assignment-1/)

## 🎓 What You'll Learn

- How to make your objects behave like built-in Python types
- The power of function decoration and meta-programming
- Best practices for organizing Python code
- Real-world applications of these concepts
- Advanced Python features like list comprehensions and argument handling
- Building interactive web apps with Streamlit
- Working with real-time financial data

Happy Coding! 🎉
