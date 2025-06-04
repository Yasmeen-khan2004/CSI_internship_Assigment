# Create lower triangular, upper triangular and pyramid 
# containing the "*" character. write code in python A
def lower_triangle(n):
    for i in range(1, n + 1):
        print('*' * i)

def upper_triangle(n):
    for i in range(n, 0, -1):
        print(' ' * (n - i) + '*' * i)

def pyramid(n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + '*' * (2 * i - 1))

rows = 5

print("Lower Triangular Pattern:")
lower_triangle(rows)

print("\nUpper Triangular Pattern:")
upper_triangle(rows)

print("\nPyramid Pattern:")
pyramid(rows)
