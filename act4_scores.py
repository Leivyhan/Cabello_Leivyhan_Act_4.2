s = int(input("Students: "))
total = 0
highest = 0

for s in range(1, s+1):
    score = int(input(f"Score {s}: "))
    total += score

    if score > highest:
        highest = score

Avg = total/s

print(f"Total: {total}", end=" ")
print(f"Avg = {Avg}")
print(f"Highest: {highest}")