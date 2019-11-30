import numpy as np
from numpy import linalg as LA


#This method works for nxn Hermitian matrices, WLOG we will test with 3x3 Hermitian matrices
#In general, the eigenvalues of a real 3x3 Hermitian matrix can be
#(i) three distinct real numbers
#(ii) three real numbers with repetitions

values = np.array([1,2,3])

print("We shall calculate the eigenvectors generated from arbitrary eigenvalues of a matrix A and its respective submatrices eigenvalues\n")

def difference(vectorindex,eigenvalues) :
    """returns the difference of eigenvalue i with all eigenvalues of matrix A"""
    return np.add(values[vectorindex], -eigenvalues)

def leftProd(vectorindex):
    """returns the product of all differences, excluding the difference of eigenvalue i with itself"""
    dif = difference(vectorindex,values)
    return np.prod(dif[:vectorindex]) * np.prod(dif[vectorindex+1:])

def rightProd(vectorindex,subvalues):
    """returns the product of all differences between eigenvalue i and eigenvalues of the submatrix j, 
    generated from removing the jth row and column from A"""
    return np.prod(difference(vectorindex,subvalues))

def norm(i,subvalues):
    """returns the norm of the jth component of ith eigenvector given the jth submatrix eigenvectors for a given i"""
    return rightProd(i,subvalues) / leftProd(i)



values = np.array([1,2,3]) #arbitrary eigenvalues for a 3x3 Hermitian matrix

subvalues_0 = np.array([1.25,2.25])
subvalues_1 = np.array([1.5,2.5])
subvalues_2 = np.array([1.75,2.75]) #arbitrary eigenvalues for submatrices 

#Eventually, we will use the min-max principle to restrict the possible submatrix eigenvalues

print("Given eigenvalues of matrix A: ", values)
print("Additionally, eigenvalues of submatrices: ", subvalues_0, ", ", subvalues_1, ", ", subvalues_2, "\n")

norm_0 = np.array([norm(0,subvalues_0),norm(0,subvalues_1),norm(0,subvalues_2)])
v_0 = np.sqrt(norm_0)

print("Then the Norm Squared of V_0 (V_0^2): ", norm_0)
print("Norm of V_0: ", v_0)
#Our first eigenvector result!

