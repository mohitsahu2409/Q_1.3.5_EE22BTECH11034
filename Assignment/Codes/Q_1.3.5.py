import numpy as np

# Given input arrays

A = np.array([1, -1])
B = np.array([-4, 6])
C = np.array([-3, -5])

# H is the point of intersection of altitudes on side AB and AC from point C and B respectively...
H = np.array([17 / 6, -5 / 6])  # Reference from Question 1.3.4

result = int(((A - H).T) @ (B - C))    # Checking orthogonality condition...

if result == 0:
  print("(A - H)^T (B - C) = 0\nHence Verified...")

else:
  print("(A - H)^T (B - C)) != 0\nHence the given statement is wrong...")
