# =============================
# Day 01 - Tuples in Python
# Date: 16 March 2026
# =============================

# Tuple banao — list jaisa par change nahi hota!
coordinates = (28.6139, 77.2090)  # Delhi coordinates
rgb_color = (255, 0, 0)           # Red color
days = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")

# Access karo
print(f"Latitude : {coordinates[0]}")
print(f"Longitude: {coordinates[1]}")
print(f"Red value: {rgb_color[0]}")

# Length
print(f"Days in week: {len(days)}")

# Loop karo
print(f"\n--- Days ---")
for day in days:
    print(f"  📅 {day}")

# Tuple unpacking
lat, lon = coordinates
print(f"\nLat: {lat}, Lon: {lon}")

# My info tuple — change nahi hoga kabhi!
my_info = ("Sachin Dangi", 17, "India", "Python")
name, age, country, lang = my_info
print(f"\n--- My Info ---")
print(f"Name    : {name}")
print(f"Age     : {age}")
print(f"Country : {country}")
print(f"Language: {lang}")

# List vs Tuple
print(f"\nList  = change ho sakta hai ✏️")
print(f"Tuple = fixed rehta hai 🔒")
