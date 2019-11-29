import numpy as np
from numpy import linalg as LA

#In general, the eigenvalues of a real 3 by 3 matrix can be
#(i) three distinct real numbers, as here;
#(ii) three real numbers with repetitions;
#(iii) one real number and two conjugate non-real numbers.

values = np.array([1,2,3])

print("Let us first consider the product on the LHS of the equation in the readme\n")

i = 0
leftDifference = np.add(values[i],-values)
leftProduct = np.prod(leftDifference[:i]) * np.prod(leftDifference[i+1:])

