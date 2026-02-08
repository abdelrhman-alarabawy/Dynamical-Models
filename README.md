# Dynamical Models (from *Bayesian Reasoning and Machine Learning* by David Barber)

This repository is your **step-by-step learning and implementation track** for the Dynamical Models part of the book.

The goal is simple:
- Learn each concept clearly.
- Build one practical mini-project per topic.
- Keep notes and code in a format that other people can understand and reuse.

---

## Why this repo exists

You said you are reading chapter by chapter and want to build practical understanding in parallel. This repo is designed exactly for that workflow.

Instead of trying to implement everything at once, we move in four stages:

1. **Discrete-State Markov Models**
2. **Continuous-State Markov Models**
3. **Switching Linear Dynamical Systems**
4. **Distributed Computation**

Each stage has its own folder with:
- Plain-language explanation
- Learning objectives
- A practical mini-project idea
- A concrete implementation checklist
- Suggested outputs for your GitHub portfolio

---

## Recommended learning rhythm (weekly loop)

For each chapter/topic:

1. **Read** the relevant section in the book.
2. **Summarize** what you understood in your own words.
3. **Implement** one small example from scratch.
4. **Test and visualize** the result.
5. **Write a short reflection**: what worked, what was confusing.
6. **Commit and push** your progress.

This loop helps convert passive reading into applied skill.

---

## Repository structure

```text
Dynamical-Models/
├── 01-discrete-state-markov-models/
├── 02-continuous-state-markov-models/
├── 03-switching-linear-dynamical-systems/
└── 04-distributed-computation/
```

---

## Suggested repo strategy (if you want one repo per part)

You have two good options:

### Option A (recommended now): single monorepo
Keep everything in this repo while you are learning.
- Easier to maintain.
- Easier to compare models.
- One timeline of progress.

### Option B (later): split into four repos
When the content matures, split by topic:
- `discrete-state-markov-models`
- `continuous-state-markov-models`
- `switching-linear-dynamical-systems`
- `distributed-computation-for-dynamical-models`

This is better when you want standalone portfolio projects.

---

## How to start today (first actionable step)

Start with folder **`01-discrete-state-markov-models`**:
1. Read the local README in that folder.
2. Create a tiny transition-matrix simulation.
3. Add one notebook/script that estimates transition probabilities from synthetic data.
4. Commit with message: `feat: add first discrete-state markov chain simulation`

When done, move to `02-continuous-state-markov-models`.

---

## Contribution style for your future self

Use simple commit categories:
- `docs:` explanation or notes
- `feat:` new implementation
- `refactor:` code cleanup
- `test:` validation scripts

This keeps your history clean and easy to review.

---

## Final note

You can absolutely build this **step by step** and still end up with a complete, impressive portfolio.
If you want, next step I can generate the **initial Python starter files** (simulation + plotting + simple tests) for Topic 1.
