# QRLgym

A suite of OpenAI Gym-compatible environments for quantum control tasks, designed for reinforcement learning (RL) research on quantum systems.

---

## Features

- 🧠 **RL-Ready:** Standard Gym API for seamless integration with RL agents and libraries.
- ⚛️ **Quantum Control Simulation:** Simulates the evolution and control of quantum systems (qubits, gates, or custom Hamiltonians).
- 🏆 **Customizable Tasks:** Easily adapt control targets, reward functions, and dynamics.
- 📖 **Modular:** Extend with your own environments, Hamiltonians, or fidelity metrics.

---

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/CodeMesh15/QCControlGym.git
cd QCControlGym
pip install -e .
```

---

## Quick Start Example

Run a random agent in a quantum control RL environment:

```python
import gym
import QRLgym # This will register the custom environments

env = gym.make('QuantumControl-v0') # Replace with your named environment

obs = env.reset()
done = False
total_reward = 0

while not done:
action = env.action_space.sample() # Substitute with your agent!
obs, reward, done, info = env.step(action)
total_reward += reward
env.render()  # Optional: visualize the evolution
print("Finished episode, total reward:", total_reward)
```

---

## Environments Overview

- **QuantumControl-v0:**  
  Learn to drive a quantum system (e.g., qubit) from its initial state to a desired target using a sequence of control operations. The agent is rewarded based on how close the resulting transformation is to the target, using fidelity as a quantitative measure.

You can add your own custom environments and tasks by subclassing the provided templates.

---

## Directory Structure

QRLgym/
│
├── QRLgym/
│ ├── environments/
│ ├── hamiltonians/
│ └── fidelities/
│
├── setup.py
├── requirements.txt
└── README.md


- **environments/**: RL environment implementations (Gym API)
- **hamiltonians/**: Quantum Hamiltonian logic (system evolution)
- **fidelities/**: Reward functions (e.g., trace fidelity)

---

## Dependencies

- [gym](https://github.com/openai/gym)  
- numpy

---

## Citing

If you use QRLgym in academic work or published research, please cite this repository.

---

## Contributing

Contributions are welcome! Please open issues or pull requests for features, bug fixes, or documentation improvements.

---

## Contact

For questions, feedback, or collaborations, open an issue or contact the maintainer via GitHub.

---

*QRLgym: Power your quantum control research with RL!*



