# =============================
# Day 01 - Lists in Python
# Date: 16 March 2026
# =============================

# List banao
skills = ["Python", "Git", "GitHub"]
numbers = [1, 2, 3, 4, 5]

# Access karo
print(f"First skill : {skills[0]}")
print(f"Last skill  : {skills[-1]}")

# Add karo
skills.append("HTML")
print(f"After append: {skills}")

# Insert karo specific position pe
skills.insert(1, "VS Code")
print(f"After insert: {skills}")

# Remove karo
skills.remove("VS Code")
print(f"After remove: {skills}")

# Length
print(f"Total skills: {len(skills)}")

# Loop through list
print(f"\n--- My Skills ---")
for skill in skills:
    print(f"  ✅ {skill}")

# Coming soon list
coming_soon = ["Full Stack", "React", "Django", "AI/ML"]
print(f"\n--- Coming Soon ---")
for topic in coming_soon:
    print(f"  🔜 {topic}")

# Combine lists
all_topics = skills + coming_soon
print(f"\nTotal topics to learn: {len(all_topics)}")
