import numpy as np

###################

#a)

A = np.matrix('0 1 2; 1 2 0')

AtA = np.matmul(A.T, A)
AAt = np.matmul(A, A.T)


# print(AAt)
# print(AtA)
#
# print(AAt == AAt.T) # Wahr -> symmetrisch
# print(AtA == AtA.T) # Wahr -> symmetrisch

#####################

#b)

# A-lambda*I
#identity = np.identity(3)
# print(np.subtract(AtA, l*identity))  Wie Matrix mit Variable multiplizieren?

eigenvals = np.linalg.eigvals(AtA)
print(eigenvals)

# für eigenwert 1

# eigenv1_zwischenergebnis = AtA - eigenvals[0] * np.identity(3)
#
# print(eigenv1_zwischenergebnis)
#
# v1 = np.linalg.solve(eigenv1_zwischenergebnis, np.matrix('0; 0; 0'))
#
# print(v1)
#
# # für eigenwert 2
#
# eigenv2_zwischenergebnis = AtA - (eigenvals[1] * np.identity(3))
#
# print(eigenv2_zwischenergebnis)
#
# v2 = np.linalg.solve(eigenv2_zwischenergebnis, np.matrix('0; 0; 0'))
#
# print(v2)

# für eigenwert 3

eigenv3_zwischenergebnis = AtA - (eigenvals[2] * np.identity(3))
print(AtA)
print(AtA - eigenvals[2] * np.identity(3))

print(eigenv3_zwischenergebnis)

v3 = np.linalg.solve(eigenv3_zwischenergebnis, np.matrix('0; 0; 0'))

print(v3)