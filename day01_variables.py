# =============================
# Day 01 - Variables & Data Types
# Date: 16 March 2026
# =============================

# --- String ---
name = "Sachin Dangi"
language = "Python"
print(f"Name: {name}")
print(f"Learning: {language}")

# --- Integer ---
age = 17
day_number = 1
print(f"Age: {age}")
print(f"Day: {day_number}")

# --- Float ---
version = 3.11
print(f"Python Version: {version}")

# --- Boolean ---
is_learning = True
is_expert = False
print(f"Am I learning? {is_learning}")
print(f"Am I expert yet? {is_expert}")

# --- List ---
skills = ["Python", "Git", "GitHub"]
print(f"My Skills: {skills}")

# --- Dictionary ---
profile = {
    "name": "Sachin Dangi",
    "age": 17,
    "goal": "AI/ML Developer",
    "day": 1
}
print(f"Profile: {profile}")
# =============================
# Extra Practice
# =============================

# Type conversion
age_str = str(17)
age_int = int("17")
age_float = float("17")

print(f"String : {age_str}  → {type(age_str)}")
print(f"Integer: {age_int}  → {type(age_int)}")
print(f"Float  : {age_float} → {type(age_float)}")

print("Variables practice complete! 🔥")
# Input from user
user_name = input("Enter your name: ")
user_age = input("Enter your age: ")
print(f"Hello {user_name}! You are {user_age} years old!")
print("🔥 Keep coding every day!")

