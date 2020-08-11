from cs50 import get_int

# get int
while True:
    height = get_int("Height: ")
    if height >= 0 and height <= 23:
        break

# print pyramid
for i in range(height):
    print(" " * (height - i - 1), end="")
    print("#" * (i + 1), end="")
    print(" " * 2, end="")
    print("#" * (i + 1))