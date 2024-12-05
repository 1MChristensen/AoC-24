from qiskit import QuantumCircuit
from qiskit.circuit.library import GroverOperator, StatePreparation
from qiskit.quantum_info import Statevector
import numpy as np
import matplotlib.pyplot as plt

# Get binary representation of a number (since n<=3 we only need two digits)
binary = lambda n: format(n, '02b')

# Target string - string we are looking for

target_string = 'XMAS'

dict = {'X': 0, 'M': 1, 'A': 2, 'S': 3}

# Convert into binary with mappings X->0, M->1, A->2, S->3
target_nums = [dict[i] for i in target_string]

target = ''.join([binary(i) for i in target_nums])

# Test string to search
test_string = 'MMMSXXMASM'

N = len(test_string)

test_nums = [dict[i] for i in test_string]
test = ''.join([binary(i) for i in test_nums])

# Split into sub-lists of length 8
sub_test = [test[2*i:2*i + 8] for i in range(N-3)]
print(np.array(sub_test))

# Now, in fairness any sane human being would just check the list for the target, but since we are doing a PhD we are not sane

# We need to put the qubits into a superposition of these specific states
# It is way too complicated for me to build the circuit by hand, so I will just use the qiskit library

# Create a quantum circuit with 8 qubits
circ = QuantumCircuit(9)

# Undo the binary
undo_binary = lambda n: int(n, 2)

initial_states = [undo_binary(i) for i in sub_test]

N_states = len(initial_states)

state_vector = np.zeros(2**8)
for state in initial_states:
    state_vector[state] = 1/np.sqrt(N_states)

# Initialize the circuit with the state vector 
state_prep = StatePreparation(state_vector)
#circ.append(state_prep, [0,1,2,3,4,5,6,7])
#circ.initialize(state_vector)

# Now we need to perform Grovers algorithm to find the target state

# Define the oracle

oracle = QuantumCircuit(9)

# Add gates at the appropriate positions - in this case we are looking for the state 00011011

oracle.append(state_prep, [0,1,2,3,4,5,6,7])

oracle.mcx([0,1,3,4], 8)

oracle_inv = oracle.inverse()

circ.append(oracle, [0,1,2,3,4,5,6,7,8])
circ.z(8)

circ.append(oracle_inv, [0,1,2,3,4,5,6,7,8])

# Start of diffuser
for i in range(8):
    circ.x(i)
circ.mcx([0,1,2,3,4,5,6,7], 8)
for i in range(8):
    circ.x(i)

# Middle of diffuser
circ.h(8)
for i in range(8):
    circ.x(i)
circ.mcx([0,1,2,3,4,5,6,7], 8)
for i in range(8):
    circ.x(i)
circ.h(8)

# End of diffuser
for i in range(8):
    circ.x(i)
circ.mcx([0,1,2,3,4,5,6,7], 8)
for i in range(8):
    circ.x(i)


circ.append(oracle, [0,1,2,3,4,5,6,7,8])

state = Statevector.from_int(0, 2**9)

state = state.evolve(circ)

threshold = 0.1
filtered_amplitudes = {k: v for k, v in state.to_dict().items() if abs(v) > threshold}
print(filtered_amplitudes)

# Plot the probabilities of the state
probabilities = {k: abs(v)**2 for k, v in filtered_amplitudes.items()}
plt.bar(probabilities.keys(), probabilities.values())
plt.xlabel('State')
plt.ylabel('Probability')
plt.title('Probabilities of Quantum States')
plt.show()