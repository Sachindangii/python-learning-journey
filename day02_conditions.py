# =============================
# Day 02 - Conditions (If/Else)
# Date: 17 March 2026
# =============================

name = "Sachin Dangi"

# Basic If/Else
temperature = 35

if temperature >= 30:
    print("It is hot outside!")
else:
    print("Weather is nice!")

# If/Elif/Else
marks = 85

if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Failed!")

# Nested If
is_learning = True
has_github = True

if is_learning:
    if has_github:
        print(f"{name} is learning and has GitHub!")
    else:
        print("No GitHub account found!")
else:
    print("Start learning today!")

# GitHub Contribution Checker
commits = 17

if commits >= 16:
    print("Darkest Green!")
elif commits >= 8:
    print("Dark Green!")
elif commits >= 4:
    print("Medium Green!")
elif commits >= 1:
    print("Light Green!")
else:
    print("No commits today!")
