# ================================================
# Operators and Control Flow Lab – Complete File
# ================================================

# -----------------------------
# 1. Arithmetic Operators
# -----------------------------
a = 10
b = 3

sum_result = a + b
sub_result = a - b
mul_result = a * b
div_result = a / b           # float division
floor_div = a // b           # integer division
remainder = a % b            # modulus
power = a ** b               # exponentiation

print("Arithmetic Operations:")
print("Sum:", sum_result)
print("Difference:", sub_result)
print("Multiplication:", mul_result)
print("Division:", div_result)
print("Floor Division:", floor_div)
print("Remainder:", remainder)
print("Power:", power)
print("-" * 40)

# -----------------------------
# 2. Comparison Operators
# -----------------------------
x = 15
y = 20

print("Comparison Operators:")
print("x > y:", x > y)
print("x < y:", x < y)
print("x == y:", x == y)
print("x != y:", x != y)
print("x >= y:", x >= y)
print("x <= y:", x <= y)
print("-" * 40)

# -----------------------------
# 3. Logical Operators & Conditions
# -----------------------------
is_member = True
has_coupon = False
total_amount = 250

if is_member and total_amount > 100:
    discount = "15%"
elif has_coupon or total_amount > 200:
    discount = "10%"
else:
    discount = "No discount"

print("Logical Operators & Control Flow:")
print("Discount:", discount)

# -----------------------------
# 4. If / Elif / Else Example
# -----------------------------
score = 75

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("Grade based on score:", grade)

# -----------------------------
# 5. Combining Arithmetic & Flow
# -----------------------------
num = 12

if num % 2 == 0:
    parity = "Even"
else:
    parity = "Odd"

print("Number parity:", parity)

# -----------------------------
# 6. Nested Conditions
# -----------------------------
age = 22
has_id = True

if age >= 18:
    if has_id:
        access = "Allowed"
    else:
        access = "Denied - No ID"
else:
    access = "Denied - Too Young"

print("Access check:", access)

# -----------------------------
# 7. Boolean Expressions
# -----------------------------
temperature = 30
is_raining = False

if temperature > 25 and not is_raining:
    activity = "Go to the beach"
elif temperature <= 25 and is_raining:
    activity = "Stay home and read"
else:
    activity = "Go for a walk"

print("Suggested activity:", activity)

# -----------------------------
# 8. Multiple Variable Comparisons
# -----------------------------
a = 5
b = 10
c = 7

if a < b and b > c:
    result = "b is the largest"
elif a > c and c > b:
    result = "a is largest"
else:
    result = "c is largest"

print("Largest value check:", result)

# -----------------------------
# 9. Using OR Operator
# -----------------------------
light_on = False
switch_override = True

if light_on or switch_override:
    status = "Light is on"
else:
    status = "Light is off"

print("Light status:", status)
