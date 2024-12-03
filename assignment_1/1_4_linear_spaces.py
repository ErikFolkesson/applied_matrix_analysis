import numpy as np
import matplotlib.pyplot as plt

# 1. Define the vectors
S = np.array([[1, 0, 1, 1],
              [1, 0, 1, 0],
              [0, 1, 1, 1]])
v = np.array([-1, 2, -1, 2])

# 2. Gram-Schmidt process
def gram_schmidt(S):
  """
  Performs the Gram-Schmidt orthogonalization process.

  Args:
      S: A NumPy array where each row is a vector.

  Returns:
      A NumPy array with orthonormalized vectors.
  """
  U = np.zeros_like(S, dtype=float)
  U[0] = S[0] / np.linalg.norm(S[0])
  for i in range(1, S.shape[0]):
    u_i = S[i]
    for j in range(i):
      u_i = u_i - np.dot(S[i], U[j]) * U[j]
    U[i] = u_i / np.linalg.norm(u_i)
  return U

U = gram_schmidt(S)

# 3. Project v onto U
def project(v, U):
  """
  Projects vector v onto the subspace spanned by the columns of U.

  Args:
      v: The vector to be projected.
      U: A matrix whose columns form the basis of the subspace.

  Returns:
      The projection of v onto the subspace.
  """
  proj = np.zeros_like(v, dtype=float)
  for u_i in U:
    proj = proj + np.dot(v, u_i) * u_i
  return proj

v_proj = project(v, U)

# 4. Visualize (we'll do this in 3D since 4D is hard to visualize)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the original vectors from S (taking the first 3 components)
for s_i in S:
  ax.quiver(0, 0, 0, s_i[0], s_i[1], s_i[2], color='blue', alpha=0.5)

# Plot the orthonormal vectors from U (taking the first 3 components)
for u_i in U:
  ax.quiver(0, 0, 0, u_i[0], u_i[1], u_i[2], color='red')

# Plot v and its projection (taking the first 3 components)
ax.quiver(0, 0, 0, v[0], v[1], v[2], color='green', label='v')
ax.quiver(0, 0, 0, v_proj[0], v_proj[1], v_proj[2], color='purple', label='proj(v)')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Gram-Schmidt and Vector Projection')
ax.legend()
plt.show()