import sys


t = int(input().strip()) # Test Cases
for i in range(t):
    n = int(input().strip()) # If n = 10
    three = (n - 1) // 3 # three = 3
    five = (n - 1) // 5 # five = 1
    fifteen = (n - 1) // 15 # fifteen = 0
    sum = 3 * (three * (three + 1) // 2) + 5 * (five * (five + 1) // 2) - 15 * (fifteen * (fifteen + 1) //2) # sum = (3 * 6) + (5 * 1) - (0) => sum = 18 + 5 => sum = 23
    print(sum)
