"""Simple continuous-state Markov process simulation (1D position + velocity)."""

from __future__ import annotations

import random
from typing import List, Tuple


def simulate(steps: int = 60, seed: int = 42) -> Tuple[List[float], List[float]]:
    rng = random.Random(seed)
    x, v = 0.0, 1.0
    true_positions: List[float] = []
    observations: List[float] = []

    for _ in range(steps):
        process_noise = rng.gauss(0.0, 0.3)
        measurement_noise = rng.gauss(0.0, 0.8)
        x = x + v + process_noise
        true_positions.append(x)
        observations.append(x + measurement_noise)

    return true_positions, observations


if __name__ == "__main__":
    true_positions, observations = simulate()
    print("first 10 true positions:", [round(v, 2) for v in true_positions[:10]])
    print("first 10 observations:", [round(v, 2) for v in observations[:10]])
