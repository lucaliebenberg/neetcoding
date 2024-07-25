"""
Dynamic Programming --> 2D Grid (4x4)
"""

# Brute Force - Time: 0(2 ^ (n + m)), Space: 0(n + m)
def bruteForce(r,c, rows, cols):
    if r == rows or c == cols:
        return 0
    if r == rows - 1 and c == cols - 1:
        return 1
    
    return (bruteForce(c, r + 1, rows, cols) + bruteForce(r, c + 1, rows, cols))

print(bruteForce(0,0,4,4))

# Memoization - Time and Space: 0(n * m)
def memoization(r, c, rows, cols, cache):
    if r == rows or c == cols:
        return 0
    if cache[c][r] > 0:
        return cache[c][r]
    if r == rows - 1 and c == cols - 1:
        return 1
        
    cache[r][c] = (memoization(r + 1, c, rows, cols, cache)) + (memoization(c + 1, r , rows, cols, cache))
    return cache[r][c]

print(memoization(0,0,4,4, [[0] * 4 for i in range(4)]))

# Dynamic Programming - Time: O(n * m), Space: O(m), where m is num of cols
def dp(rows, cols):
    prevRow = [0] * cols

    for r in range(rows - 1, -1, -1):
        curRow = [0] * cols
        curRow[cols - 1] = 1
        for c in range(cols - 2, -1, -1):
            curRow[c] = curRow[c + 1] + prevRow[c]
        prevRow = curRow
    return prevRow[0] 