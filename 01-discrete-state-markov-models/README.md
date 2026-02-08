# 01 — Discrete-State Markov Models

This section is now **fully started** with runnable code and tests.

## What this models
A discrete-state Markov model assumes:

> The next state depends only on the current state.

## Included starter code
- `src/markov_chain.py`
  - transition matrix validation
  - chain simulation
  - transition estimation from observed data
  - stationary distribution approximation
- `src/demo.py`
  - end-to-end customer lifecycle example
- `tests/test_markov_chain.py`
  - basic correctness checks

## Run it
From repo root:

```bash
python 01-discrete-state-markov-models/src/demo.py
python -m unittest discover -s 01-discrete-state-markov-models/tests -p "test_*.py"
```

## Next incremental tasks
- [ ] Add CSV loader for real transition data
- [ ] Add plot of state occupancy over time
- [ ] Add notebook walkthrough (`notebooks/01_intro_markov_chain.ipynb`)
