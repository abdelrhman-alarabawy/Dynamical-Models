# 04 — Distributed Computation for Dynamical Models

## Concept in plain words
As models/data get larger, a single machine may be too slow or memory-limited.
Distributed computation splits work across multiple workers (CPUs, nodes, or GPUs).

---

## What you should learn here

- Which parts of inference/training can be parallelized.
- Trade-offs: speed, synchronization cost, and numerical consistency.
- Batch vs streaming updates.
- Practical workflow for scaling experiments.

---

## Practical mini-project

### Project: Parallel simulation and evaluation pipeline
Use parallel workers to run many trajectory simulations and aggregate metrics.

Tasks:
1. Parallelize simulation with `multiprocessing`.
2. Aggregate summary statistics.
3. Benchmark runtime for serial vs parallel execution.
4. Document scalability limits and bottlenecks.

---

## Implementation checklist

- [ ] `src/parallel_simulation.py`
- [ ] `src/benchmark.py`
- [ ] `notebooks/04_distributed_workflow.ipynb`
- [ ] `results/` for benchmark outputs
- [ ] Simple reproducibility setup (fixed random seeds)

---

## Deliverables for GitHub

- Benchmark table/plot comparing serial and parallel runs.
- Reproducible script with clear CLI usage.
- Short section: “When distributed computation is worth it.”

