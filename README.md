# EigenvectorGenerator
Calculating eigenvectors from given eigenvalues using the method defined in "Eigenvectors from Eigenvalues". The following is the theorem as stated by Terrence Tao on his blog. 

![Image of Theorem](https://i.imgur.com/CNnC3bt.png)

This equation will be used to calculate the norm of each component of an eigenvector when a set of eigenvalues is passed.

Now we can define this as a function, mapping eigenvalues of A and M_j  into R^n. 


![Image of Function](https://i.imgur.com/LkohfP7.png)

More generally, 

![Image of Function_1](https://i.imgur.com/PtgrAPD.png)

So to generate eigenvectors of n dimensions, we need n^2 eigenvalues as input. I will use this to check the validity of parameters passed to method.py

