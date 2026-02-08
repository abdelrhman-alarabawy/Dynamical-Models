# 03 — Switching Linear Dynamical Systems (SLDS)

## Concept in plain words
SLDS combines:
- A discrete latent mode (which regime are we in?), and
- A continuous latent state (how the system evolves in that regime).

In other words: the process can switch between multiple linear dynamical behaviors.

---

## What you should learn here

- Why a single linear model is often insufficient.
- How regime switches explain abrupt behavior changes.
- The relation between HMMs and LDS models.
- Basic inference intuition for mixed discrete/continuous latent variables.

---

## Practical mini-project

### Project: Market regime simulator
Model two market regimes:
- Regime A: low volatility trend
- Regime B: high volatility mean reversion

Tasks:
1. Simulate switching regimes with a discrete Markov chain.
2. Simulate continuous dynamics conditional on regime.
3. Visualize hidden regime labels and observations.
4. Explain where a plain LDS fails.

---

## Implementation checklist

- [ ] `src/simulate_slds.py`
- [ ] `src/visualize_regimes.py`
- [ ] `notebooks/03_slds_intro.ipynb`
- [ ] `figures/`
- [ ] Validate regime transitions and trajectory dimensions

---

## Deliverables for GitHub

- Regime-aware simulation plot.
- README section comparing LDS vs SLDS.
- Clear explanation of practical use cases.

