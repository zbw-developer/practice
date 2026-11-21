scores = [88,92,75,60,99]

total = 0
for s in scores:
    total = total + s

print(f"平均分:{total / len(scores)}")