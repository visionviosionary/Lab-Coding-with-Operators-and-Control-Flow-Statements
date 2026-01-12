# ================================================
# Operators and Control Flow Lab – CodeGrade Ready
# ================================================

# -----------------------------
# 1. Arithmetic Operators
# -----------------------------
a = 10
b = 3

# Basic operations
sum_result = a + b
sub_result = a - b
mul_result = a * b
div_result = a / b           # float division
floor_div = a // b           # integer division
remainder = a % b            # modulus
power = a ** b               # exponentiation

print("Sum:", sum_result)
print("Difference:", sub_result)
print("Multiplication:", mul_result)
print("Division:", div_result)
print("Floor Division:", floor_div)
print("Remainder:", remainder)
print("Power:", power)

# -----------------------------
# 2. Comparison Operators
# -----------------------------
x = 10
y = 5

print("x > y:", x > y)
print("x < y:", x < y)
print("x == y:", x == y)
print("x != y:", x != y)
print("x >= y:", x >= y)
print("x <= y:", x <= y)

# -----------------------------
# 3. Logical Operators & Control Flow
# -----------------------------
is_member = True
has_coupon = False
total_amount = 120

# Discount logic
if is_member and total_amount > 100:
    discount = "15%"
elif has_coupon or total_amount > 200:
    discount = "10%"
else:
    discount = "No discount"

print("Discount:", discount)

# -----------------------------
# 4. Grade Calculation
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

print("Grade:", grade)

# -----------------------------
# 5. Number parity
# -----------------------------
num = 12
if num % 2 == 0:
    parity = "Even"
else:
    parity = "Odd"

print("Number is:", parity)

# -----------------------------
# 6. Nested if / else example
# -----------------------------
age = 20
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
# 7. Temperature / activity example
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
# 8. Multiple variable comparison
# -----------------------------
a = 5
b = 10
c = 7

if a < b and b > c:
    largest = "b is the largest"
elif a > c and c > b:
    largest = "a is the largest"
else:
    largest = "c is the largest"

print("Largest value check:", largest)

# -----------------------------
# 9. Using OR operator
# -----------------------------
light_on = False
switch_override = True

if light_on or switch_override:
    status = "Light is on"
else:
    status = "Light is off"

print("Light status:", status)
