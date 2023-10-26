import numpy as np
#import random
from numpy import linalg as lin

def GaussSeidel(A,n,x0,TOL,N):
    n = len(A)   # n=len(A) making the n = length of the matrix A
    x = np.zeros((n,1))     #assigning x to a vector


    k = 1
    while k <= N:
        for i in range(0,n):
            sum = 0
            for j in range(0,i):
                sum =  sum + A[i][j]*x[j]     # the 1st summation from  j=1 to i-1 (NB: we start from *x[j] instead of x0[j])
            s = 0
            for j in range(i+1,n):
                s = s + A[i][j]*x0[j]     #the second summmation from j= i+1 to n (NB for seidel we start from x0[j] for s)
            x[i] = (1/A[i][i])*(-sum -s + b[i])  #getting the iterations of xi
        if lin.norm(x-x0)/lin.norm(x) <= TOL:  # lin.norm(x-xo) is the norm of x-x0 which is less or equal to TOL
            return(x)
        
        k = k+1
        print("Current solution: ", k, x.T)  #prints every iteration of xi
        for i in range(0,n):
            x0 = x.copy()  # it replaces the x0 every after iteration to restart the calculations
    return(x)
    print("Maximum number of iterations exceeded")
    
n = 3 #number of unknowns and  equtions
A = np.array([[1,2,1],[1,-1,5],[3,1,-1]])  #A is the given system to be turned into matrix
b = np.array([[3],[7],[5]])       #given solution of the system
x0 = np.array([[0],[0],[0]])   # x0 is given if not use the zeros
TOL = 0.00001    #Tol is given as well ( if notb assumes this)
N = 5       # maximum number of iteration ( you can increase this to see if the X's converges)
x = (GaussSeidel(A,n,x0,TOL,N))
print(x)