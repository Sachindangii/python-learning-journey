# =============================
# Day 01 - Practice & Revision
# Date: 16 March 2026
# =============================

# Aaj jo seekha uska revision!

# 1. String
name = "Sachin Dangi"
print(f"👤 Name: {name.upper()}")

# 2. Integer & Float
age = 17
height = 5.9
print(f"🎂 Age: {age}")
print(f"📏 Height: {height} ft")

# 3. Boolean
is_learning = True
print(f"📚 Learning: {is_learning}")

# 4. List
skills = ["Python", "Git", "GitHub"]
skills.append("HTML")
print(f"🛠️ Skills: {skills}")

# 5. Tuple
my_info = ("Sachin Dangi", 17, "India")
print(f"📌 Info: {my_info}")

# 6. Dictionary
profile = {
    "name": "Sachin Dangi",
    "age": 17,
    "goal": "AI/ML Developer",
    "github": "Sachindangii"
}

print(f"\n====== Day 01 Complete ======")
for key, value in profile.items():
    print(f"  {key:10} : {value}")

print(f"\n✅ Topics covered today:")
topics = ["Strings", "Integers", "Floats", 
          "Booleans", "Lists", "Tuples", "Dictionaries"]
for i, topic in enumerate(topics, 1):
    print(f"  {i}. {topic}")

print(f"\n🔥 Day 01 Done — Sachin Dangi")
print(f"🚀 Journey to AI/ML starts NOW!")
