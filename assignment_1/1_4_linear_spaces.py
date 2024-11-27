import numpy as np

# Define the set of vectors S
s1 = np.array([1, 0, 1, 1])
s2 = np.array([1, 0, 1, 0])
s3 = np.array([0, 1, 1, 1])

print(f"s1: {s1}")

# Step 1: Obtain the orthonormal vector u1
u1 = s1 / np.linalg.norm(s1)
print(f"u1: {u1}")

# Step 2: Find a vector u2 that is orthogonal to u1
proj_s2_u1 = np.dot(s2, u1) / np.dot(u1, u1) * u1
u2 = s2 - proj_s2_u1
u2 = u2 / np.linalg.norm(u2)
print(f"u2: {u2}")

# Step 3: Find a vector u3 orthogonal to both u1 and u2
proj_s3_u1 = np.dot(s3, u1) / np.dot(u1, u1) * u1
proj_s3_u2 = np.dot(s3, u2) / np.dot(u2, u2) * u2
u3 = s3 - proj_s3_u1 - proj_s3_u2
u3 = u3 / np.linalg.norm(u3)
print(f"u3: {u3}")

