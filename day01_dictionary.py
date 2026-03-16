# =============================
# Day 01 - Dictionary in Python
# Date: 16 March 2026
# =============================

# Dictionary banao — key:value pairs
profile = {
    "name": "Sachin Dangi",
    "age": 17,
    "country": "India",
    "language": "Python",
    "goal": "AI/ML Developer"
}

# Access karo
print(f"Name   : {profile['name']}")
print(f"Age    : {profile['age']}")
print(f"Goal   : {profile['goal']}")

# Add new key
profile["github"] = "Sachindangii"
print(f"GitHub : {profile['github']}")

# Update karo
profile["age"] = 18  # birthday aane pe!
print(f"New Age: {profile['age']}")

# Delete karo
del profile["age"]
print(f"After delete: {profile}")

# Check if key exists
print(f"\n'name' exists: {'name' in profile}")
print(f"'age' exists : {'age' in profile}")

# Loop karo
print(f"\n--- Full Profile ---")
for key, value in profile.items():
    print(f"  {key} : {value}")

# Nested dictionary
developer = {
    "name": "Sachin Dangi",
    "skills": {
        "current": ["Python", "Git"],
        "learning": ["HTML", "CSS"],
        "future": ["React", "Django", "AI/ML"]
    }
}

print(f"\n--- Developer Profile ---")
print(f"Current skills: {developer['skills']['current']}")
print(f"Future skills : {developer['skills']['future']}")
