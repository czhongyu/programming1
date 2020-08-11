from cs50 import get_float

# get int
while True:
    change = get_float("Change owed: ")
    if change >= 0:
        break

# covert to cents
change *= 100
# count coins
coins = change // 25
change %= 25
coins += change // 10
change %= 10
coins += change // 5 + change % 5
# print result
print(coins)