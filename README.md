# Description

Starting at the top left corner of an N x M grid and facing towards the right, you keep walking one square at a time in the direction you are facing. If you reach the boundary of the grid or if the next square you are about to visit has already been visited, you turn right. You stop when all the squares in the grid have been visited. What direction will you be facing when you stop? For example: Consider the case with N = 3, M = 3. The path followed will be (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (2,1) -> (2,0) -> (1,0) -> (1,1). At this point, all squares have been visited, and you are facing right.

Input specification
The first line contains T the number of test cases. Each of the next T lines contain two integers N and M, denoting the number of rows and columns respectively.

Output specification
Output T lines, one for each test case, containing the required direction you will be facing at the end. Output L for left, R for right, U for up, and D for down. 1 <= T <= 5000, 1 <= N,M <= 10^9.

Entry 

4

1 1

2 2

3 1

3 3

Output 

R

L

D

R

# Analysis

After doing some drawings on paper, it became obvious that a pattern exists for these grids.

a) rows == columns

When the number of rows is odd, face direction is always Right --> 'R' otherwise is Left --> 'L'

b) colums > rows

Wider than taller.

When the number of rows is odd, face direction is always Right --> 'R' otherwise is Left --> 'L'

c) rows > columns

Taller than wider.

When the number of columns is odd, face direction is always Down --> 'D' otherwise is Up --> 'U'

# Install and Run the Script

You must have the python version 3 installed.

Clone the repository and run the logic-test.py script

```
git clone https://github.com/fernandogl/sunwise-logic.git
cd sunwise-logic
python3 logic-test.py
```
