import sys
from cs50 import get_string

# check argv count
if len(sys.argv) != 2:
    sys.exit(1)

# get the key and check
key = sys.argv[1]
if key.isalpha() == 0:
    sys.exit(1)
length = len(key)

# get plaintext
plain = get_string("plaintext: ")
i = 0

# print ciphertext
print("ciphertext: ", end="")
for c in plain:
    if c.isalpha():
        if c.isupper():
            plainbase = 'A'
        else:
            plainbase = 'a'
        if key[i].isupper():
            keybase = 'A'
        else:
            keybase = 'a'

        print(chr((ord(c) - ord(plainbase) + ord(key[i]) - ord(keybase)) % 26 + ord(plainbase)), end="")
        i = (i + 1) % length
    else:
        print(c, end="")

print()