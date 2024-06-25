# QuantumWalk-Results

This repository contains the results of running a quantum walk - the basis probabilties of measuring the walk at each time step  
The CSV files are organized into directories indicating the shift, coin and basis they were measured in.

## Directory Naming
Directory names are in three parts, delimited by '.' (dot), representing the type of walk
### Part 1: Shift
`16nT`: 4x4 Node Torus
### Part 2: Coin
`H`: Hadamard
### Part 3: Measurement Basis
`Eigen`: The eigenvectors of the shift-coin operator  
`Z`: The Z basis  
`Qasm`: The qiskit QASM simulator
### Example
`16nT.H.Z`: 4x4 Node Torus Shift with Hadamard Coin measured in the Z basis

## CSV File structure
