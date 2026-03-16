# =============================
# Day 01 - Strings in Python
# Date: 16 March 2026
# =============================

# String banane ke tarike
name = "Sachin Dangi"
language = 'Python'
goal = """Full Stack
AI/ML Developer"""

# String Length
print(f"Name length: {len(name)}")

# Upper & Lower case
print(name.upper())   # SACHIN DANGI
print(name.lower())   # sachin dangi

# Replace
print(name.replace("Sachin", "S."))

# Split
words = name.split(" ")
print(f"Words: {words}")

# Strip (extra spaces hatao)
messy = "   Sachin   "
print(messy.strip())

# Check karo
print(name.startswith("Sachin"))  # True
print(name.endswith("Dangi"))     # True
print("Python" in language)       # True

# f-string
age = 17
print(f"My name is {name} and I am {age} years old")
print(f"I am learning {language} to become a {goal}")
