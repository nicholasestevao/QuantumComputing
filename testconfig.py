from qiskit import *
from qiskit_aer import AerSimulator, StatevectorSimulator
import numpy as np
from math import pi

q = QuantumRegister(1)
c = ClassicalRegister(1)

qc = QuantumCircuit(q,c)

qc.h(q[0])
qc.measure(q, c)

print(qc)

print("\nSampling 1000...\n")

simulator = AerSimulator()
job = simulator.run(qc.decompose(reps=6), shots=1000)
res = dict(job.result().get_counts(qc))

print(res)