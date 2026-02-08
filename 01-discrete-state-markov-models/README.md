# 01 — Discrete-State Markov Models

## Concept in plain words
A discrete-state Markov model describes a process that moves between a finite set of states.
The key assumption is the **Markov property**:

> The next state depends only on the current state, not the full past history.

Example: weather states `Sunny`, `Cloudy`, `Rainy`.

---

## What you should learn here

- Represent states and transitions with a transition matrix.
- Simulate trajectories from a Markov chain.
- Estimate transition probabilities from observed sequences.
- Compute and interpret stationary distributions.

---

## Practical mini-project

### Project: Customer behavior state model
Model user movement through states:
- `Visitor`
- `Trial`
- `Subscriber`
- `Churned`

Tasks:
1. Create a transition matrix.
2. Simulate 1,000 users for 30 steps.
3. Estimate long-term proportions in each state.
4. Visualize transition graph and state proportions.

---

## Implementation checklist

- [ ] `src/simulate_chain.py`: simulate Markov chain paths
- [ ] `src/estimate_transition_matrix.py`: estimate matrix from data
- [ ] `notebooks/01_intro_markov_chain.ipynb`: step-by-step explanation
- [ ] `figures/`: save plots
- [ ] `tests/`: verify matrix rows sum to 1 and outputs are valid states

---

## Deliverables for GitHub

- A clear README with one intuitive example.
- One runnable script with command-line arguments.
- One notebook with visual explanation.
- At least one figure (state distribution over time).

