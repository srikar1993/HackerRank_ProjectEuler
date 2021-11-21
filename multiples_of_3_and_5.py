import sys

# Test Cases
t = int(input().strip())

for i in range(t):
    
    # If n = 10
    n = int(input().strip())
    
    # three = 3
    three = (n - 1) // 3
    
    # five = 1
    five = (n - 1) // 5
    
    # fifteen = 0
    fifteen = (n - 1) // 15
    
    # sum = (3 * 6) + (5 * 1) - (0) => sum = 18 + 5 => sum = 23
    sum = 3 * (three * (three + 1) // 2) + 5 * (five * (five + 1) // 2) - 15 * (fifteen * (fifteen + 1) //2)
    
    print(sum)
