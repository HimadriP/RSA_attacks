# RSA_attacks
This project implements the various attacks mentioned in this [paper](https://crypto.stanford.edu/~dabo/papers/RSA-survey.pdf)

This project also has implementation of prime factorization techniques listed in this [paper](https://www.sciencedirect.com/science/article/pii/S0898122111001131)

Various other attacks have also been included.

## Exploits ( Novel Attacks )
1. Blind  Signature
2. Common Modulus
3. Hastad's Broadcast
4. Franklin Reiter
5. Wiener's Attack
6. Partial Message Exposure

## Factorization Attacks
1. Pollard rho
2. p-1  
3. p+1
4. Lenstra's
5. Quadratic Sieve

## Requirements
1. SageMath
SageMath is a free open-source mathematics software system licensed under the GPL. It builds on top of many existing open-source packages: NumPy, SciPy, matplotlib, Sympy, Maxima, GAP, FLINT, R and many more. 
For installation refer to : http://doc.sagemath.org/html/en/installation/quick-guide.html
Crucial steps involved in installation : 
  - Mirrors (for binaries) : http://www.sagemath.org/mirrors.html
  - After you have unzipped the binary, (for Linux Systems) you can update the `SAGE_ROOT` variable inside the file `sage` in the `SageMath` directory. Update the SageRoot to : `#SAGE_ROOT=/path/to/sage-version`
  - Next, copy this sage file to `/usr/local/bin/`
2. gmpy
