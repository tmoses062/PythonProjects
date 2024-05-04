sum1 = 0
for number in range(2, 101, 2):
    sum1 += number

print(f"The sum of the even numbers between 1 and 100 inclusive is {sum1}")

sum2 = 0
for number in range(1, 101):
    if number % 2 == 0:
        sum2 += number

print(f"The sum of the even numbers between 1 and 100 inclusive is {sum2}")
