# %%timeit
final_number = 1000

last_mul_3 = (final_number - 1) // 3
last_mul_5 = (final_number - 1) // 5
last_mul_15 = (final_number - 1) // 15

sum_3 = 3 * (last_mul_3 / 2) * (1 + last_mul_3)
sum_5 = 5 * (last_mul_5 / 2) * (1 + last_mul_5)
sum_15 = 15 * (last_mul_15 / 2) * (1 + last_mul_15)

total_sum = sum_3 + sum_5 - sum_15
print(total_sum)

# Why not to use a loop? 🤔


# %%timeit
result = 0
for i in range(final_number):
    if i % 3 == 0 or i % 5 == 0:
        result += i

print(result)


# The Loop is 4 Times Slower (if not even worse 😂)
gauss = 348e-9
loop = 1.34e-6
print(loop / gauss)

