#Gaussian Elimination v1.0
    # -Currently can only fully solve systems with unique solutions and numEqn = numUnk

import numpy as np

# Creating the system of linear equations

    # Basic Parameters
numEqn = int(input("Enter the number of equations in the system: "))
numUnk = int(input("Enter the number of variables in the system: "))
system = np.zeros((numEqn, numUnk+1))   # +1 to include column of =

    # Inputting the coefficients of the variables and the answers of each equation
for i in range(1, numEqn+1):
    for j in range(1, numUnk+2):
        if j != numUnk+1:
            aij = float(input(f"Enter the coefficient of Equation {i}, Variable {j}: "))
            system[i - 1, j - 1] = aij
        elif j == numUnk+1:
            bi = float(input(f"Enter the answer of Equation {i}: "))
            system[i - 1, j - 1] = bi
print(system, "\n")

# Gaussian Elimination

    # Defining a function to try to get leading non-zero number on row
def lead(i,j):
    global system
    for p in range(numEqn - i):
        if system[i-1, j-1] == 0:
            temp1 = tuple(system[i-1])
            system[i-1] = system[p+i]
            system[p+i] = np.array(temp1)
        else:
            break
    if system[i-1, j-1] == 0:
        print(f"The system of equations has no non-zero coefficients on column {j}")
    # Still need to implement cases where system of equations has no non-zero coefficients in a column
    # to avoid division by 0
        exit()
    return system

    # Defining a function to create zeros under leading number and make leading one
def Gaus(i, j):
    global system
    for p in range(i, numEqn):
        system[p] = system[p] - ((system[p,j-1]/system[i-1,j-1]) * system[i-1])
        print(system, "\n")
    system[i-1] = system[i-1] / system[i-1, j-1]
    print(system, "\n")
    return system

    # Actually performing Gaussian Elimination
for q in range(1, numEqn+1):
    lead(q,q)
    Gaus(q,q)       # must be altered if to be made compatible with systems with no / no unique solution

print("Gaussian Elimination Completed!\n")
print("Beginning Back-Substitution Process...\n")

# Back Substitution
if numEqn == numUnk:    # in current model will only work for unique solutions

    # Splitting Coefficients and Answers
    Coefficients = system[:, :numUnk]
    Answers = system[:, -1]
    solution = np.zeros(numEqn)

    # Actually back substituting
    for v in range(1, numEqn + 1):
        for u in range(v):
            if u == 0:
                x = Answers[-v]
            else:
                x -= Coefficients[-v, -u] * solution[-u]
        solution[-v] = x
    print(f"The solution to the provided system of linear equations is:\n{solution}")
