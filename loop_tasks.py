# Internship Task 4: Loops & Iterations

# 1. For loop to print numbers 1-100
print("Numbers from 1 to 100:")
for i in range(1, 101):
    print(i, end=' ')
print("\n")

# 2. While loop for countdown timer
print("Countdown from 10 to 1:")
count = 10
while count > 0:
    print(count, end=' ')
    count -= 1
print("\nBlastoff!\n")

# 3. Demonstrate break and continue
print("Demonstrate break and continue:")
for num in range(1, 11):
    if num == 7:
        print("Breaking at 7")
        break  # stops the loop
    if num % 2 == 0:
        continue  # skips even numbers
    print(num, end=' ')
print("\n")

# 4. Iterate over string characters
sample_string = "Python"
print("Characters in string:", sample_string)
for char in sample_string:
    print(char, end=' ')
print("\n")

# 5. Generate multiplication table for 5
print("Multiplication Table of 5:")
for i in range(1, 11):
    print(f"5 x {i} = {5*i}")
print("\n")

# 6. Using range with steps
print("Odd numbers from 1 to 20 using step:")
for i in range(1, 21, 2):
    print(i, end=' ')
print("\n")

# 7. Combine loop with conditions
print("Numbers divisible by 3 and 5 from 1 to 50:")
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print(i, end=' ')
print("\n")

# 8. Real-world example: Simple shopping cart
print("Shopping Cart Example:")
cart = ["apple", "banana", "mango", "milk"]
for item in cart:
    if item == "mango":
        print(f"Skipping {item} as it's out of stock")
        continue
    print(f"Buying {item}")
print("\nAll items processed!")