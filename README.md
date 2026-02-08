# Dynamical Models Learning Repo

Practical companion repository for the Dynamical Models part of
*Bayesian Reasoning and Machine Learning* (David Barber).

## Goal
Learn chapter-by-chapter while building runnable artifacts.

## Structure
```text
Dynamical-Models/
├── 01-discrete-state-markov-models/
├── 02-continuous-state-markov-models/
├── 03-switching-linear-dynamical-systems/
└── 04-distributed-computation/
```

## What is implemented now
- ✅ Topic 1 has working utilities + demo + tests.
- ✅ Topics 2–4 each have runnable starter scripts.

## Quickstart
From repo root:

```bash
python 01-discrete-state-markov-models/src/demo.py
python -m unittest discover -s 01-discrete-state-markov-models/tests -p "test_*.py"
python 02-continuous-state-markov-models/src/simulate_linear_gaussian.py
python 03-switching-linear-dynamical-systems/src/simulate_slds.py
python 04-distributed-computation/src/parallel_simulation.py
```

## Suggested workflow while reading
For each chapter:
1. Read and summarize in plain language.
2. Run current script(s).
3. Extend one feature (plotting, inference, evaluation, etc.).
4. Commit with a focused message (`docs:`, `feat:`, `test:`).

## If you want one repo per part later
Keep this as monorepo while learning, then split mature folders into dedicated repos.
