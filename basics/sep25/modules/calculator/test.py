start = 1
end = 100
sum_of_squares = 0
while start <= end:
    sum_of_squares = sum_of_squares + start ** 2
    start = start + 1
square_sum = (end * (end +  1) // 2) ** 2
print(square_sum - sum_of_squares)