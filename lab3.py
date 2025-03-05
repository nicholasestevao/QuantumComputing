from qiskit.algorithms import VQE
from qiskit.algorithms.optimizers import SLSQP
from qiskit.opflow import Z, X, I, Y
from qiskit.utils import QuantumInstance
from qiskit import Aer
from qiskit.circuit.library import RealAmplitudes
from qiskit.circuit.library import EfficientSU2
from qiskit.primitives import Estimator
from qiskit.algorithms.optimizers import COBYLA

# H = z0z1 + z1z2 + x0 + y1 + z2

hamiltonian = Z ^ Z ^ I  + I ^ Z ^ Z + X ^ I ^ I + I ^ Y ^ I + I ^ I ^ Z

# Define the number of qubits
num_qubits = 4

# Create the EfficientSU2 circuit with 2 entanglement layers
ansatz = EfficientSU2(num_qubits, su2_gates=['rx', 'ry'], reps=2)

# Define a quantum instance (Simulator)
quantum_instance = QuantumInstance(Aer.get_backend('aer_simulator_statevector'))

# Create COBYLA optimizer
optimizer = COBYLA(maxiter=100)

# Create and run VQE
vqe = VQE(ansatz, optimizer=optimizer, quantum_instance=quantum_instance)
result = vqe.compute_minimum_eigenvalue(hamiltonian)

# Print result
print("VQE Energy:", result.eigenvalue.real)