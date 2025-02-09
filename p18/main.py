"""
https://projecteuler.net/problem=18
from the bottom up, add the max value from the two numbers below
eg. 2 + max(4,5)
   1   |   1   |   10
  2 3  |  7 9  |
 4 5 6 |
"""
from pathlib import Path

pyramid = (Path(__file__).parent / "pyramid.txt").read_text()
pyramid = [[int(n) for n in row.split()] for row in pyramid.splitlines()]
 
for row in range(len(pyramid) - 2, -1, -1):
    for ele in range(row + 1):
        pyramid[row][ele] = pyramid[row][ele] + max(
            pyramid[row + 1][ele], pyramid[row + 1][ele + 1]
        )
    pyramid.pop()
print(pyramid[0][0])
