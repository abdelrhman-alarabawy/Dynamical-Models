"""Minimal SLDS simulator with two discrete regimes and 1D continuous state."""

from __future__ import annotations

import random
from typing import List, Tuple


TRANSITIONS = {
    0: {0: 0.92, 1: 0.08},  # regime 0: trending
    1: {0: 0.15, 1: 0.85},  # regime 1: mean-reverting
}


def _sample(regime_probs, rng):
    r = rng.random()
    c = 0.0
    selected = 0
    for k, p in regime_probs.items():
        c += p
        selected = k
        if r <= c:
            return k
    return selected


def simulate(steps: int = 80, seed: int = 4) -> Tuple[List[int], List[float]]:
    rng = random.Random(seed)
    regime = 0
    x = 0.0
    regimes: List[int] = [regime]
    obs: List[float] = [x]

    for _ in range(steps):
        regime = _sample(TRANSITIONS[regime], rng)
        if regime == 0:
            x = x + 0.7 + rng.gauss(0, 0.3)
        else:
            x = 0.5 * x + rng.gauss(0, 1.1)

        regimes.append(regime)
        obs.append(x)

    return regimes, obs


if __name__ == "__main__":
    regimes, obs = simulate()
    print("first 20 regimes:", regimes[:20])
    print("first 10 observations:", [round(v, 2) for v in obs[:10]])
