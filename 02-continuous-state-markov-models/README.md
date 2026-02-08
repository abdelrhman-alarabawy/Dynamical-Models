# 02 — Continuous-State Markov Models

## Concept in plain words
Now states are continuous values (for example, real numbers) rather than a small list of categories.
A common view is stochastic dynamics of the form:

\[
x_{t+1} = f(x_t) + \epsilon_t
\]

where \(\epsilon_t\) is noise.

---

## What you should learn here

- Difference between discrete-state and continuous-state processes.
- Linear Gaussian state evolution.
- How uncertainty propagates over time.
- How to simulate and visualize trajectories.

---

## Practical mini-project

### Project: Noisy 1D motion tracker
Simulate a moving object with noisy dynamics and noisy measurements.

Tasks:
1. Define latent state (position, maybe velocity).
2. Simulate true dynamics and noisy observations.
3. Compare raw observations vs. latent trajectory.
4. Prepare for filtering/smoothing in later steps.

---

## Implementation checklist

- [ ] `src/simulate_linear_gaussian.py`
- [ ] `src/plot_trajectories.py`
- [ ] `notebooks/02_continuous_state_intro.ipynb`
- [ ] `figures/`
- [ ] Basic checks on distribution assumptions and dimensions

---

## Deliverables for GitHub

- Explanation of model assumptions.
- Trajectory plot (true state vs observed noise).
- Notes on when continuous models are more realistic.

