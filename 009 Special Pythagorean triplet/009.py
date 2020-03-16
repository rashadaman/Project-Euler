
pyth_sum = 1000

for a in range(1, int(pyth_sum / 3.414) + 1):

    b = int((pyth_sum / 2 - a) / (1 - a / pyth_sum))
    c1 = pyth_sum - (a + b)
    c2 = int((a ** 2 + b ** 2) ** 0.5)

    if c1 == c2:
        print(a, b, c1, sep=" * ")
        print(a * b * c1)
        break
