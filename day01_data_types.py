# =============================
# Day 01 - Data Types in Python
# Date: 16 March 2026
# =============================

# Python mein 6 main data types hain

# 1. String (text)
name = "Sachin Dangi"
city = "India"
print(type(name))   # <class 'str'>

# 2. Integer (whole number)
age = 17
year = 2026
print(type(age))    # <class 'int'>

# 3. Float (decimal number)
height = 5.9
gpa = 9.5
print(type(height)) # <class 'float'>

# 4. Boolean (true/false)
is_learning = True
is_done = False
print(type(is_learning)) # <class 'bool'>

# 5. List (multiple values)
skills = ["Python", "Git", "GitHub"]
print(type(skills)) # <class 'list'>

# 6. Dictionary (key-value pairs)
profile = {"name": "Sachin", "age": 17}
print(type(profile)) # <class 'dict'>

# Check all types together
print("------- My Data -------")
print(f"Name    : {name}  → {type(name)}")
print(f"Age     : {age}   → {type(age)}")
print(f"Height  : {height} → {type(height)}")
print(f"Learning: {is_learning} → {type(is_learning)}")
print(f"Skills  : {skills} → {type(skills)}")
