"""Utilities for discrete-state Markov models (no third-party dependencies)."""

from __future__ import annotations

import random
from typing import Dict, Iterable, List, Sequence, Tuple

State = str
TransitionMatrix = Dict[State, Dict[State, float]]


def validate_transition_matrix(matrix: TransitionMatrix) -> None:
    """Validate row-stochastic matrix properties."""
    if not matrix:
        raise ValueError("Transition matrix cannot be empty.")

    states = set(matrix.keys())
    for state, row in matrix.items():
        if not row:
            raise ValueError(f"Row for state '{state}' cannot be empty.")
        if set(row.keys()) != states:
            raise ValueError(
                f"Row for '{state}' must contain exactly these states: {sorted(states)}"
            )
        total = sum(row.values())
        if abs(total - 1.0) > 1e-9:
            raise ValueError(f"Probabilities for '{state}' must sum to 1.0. Got {total}")
        for nxt, prob in row.items():
            if prob < 0:
                raise ValueError(f"Negative transition probability: {state}->{nxt} = {prob}")


def _weighted_choice(distribution: Dict[State, float], rng: random.Random) -> State:
    roll = rng.random()
    cumulative = 0.0
    last_state = None
    for state, prob in distribution.items():
        cumulative += prob
        last_state = state
        if roll <= cumulative:
            return state
    return last_state  # defensive fallback from floating point edge cases


def simulate_chain(
    matrix: TransitionMatrix,
    initial_state: State,
    steps: int,
    seed: int | None = None,
) -> List[State]:
    """Simulate a Markov trajectory including the initial state."""
    validate_transition_matrix(matrix)
    if initial_state not in matrix:
        raise ValueError(f"Unknown initial state: {initial_state}")
    if steps < 0:
        raise ValueError("steps must be >= 0")

    rng = random.Random(seed)
    path = [initial_state]
    for _ in range(steps):
        path.append(_weighted_choice(matrix[path[-1]], rng))
    return path


def estimate_transition_matrix(
    states: Sequence[State],
    transitions: Iterable[Tuple[State, State]],
    laplace: float = 0.0,
) -> TransitionMatrix:
    """Estimate transition matrix from observed transitions."""
    state_list = list(states)
    if not state_list:
        raise ValueError("states cannot be empty")

    counts: Dict[State, Dict[State, float]] = {
        s: {t: float(laplace) for t in state_list} for s in state_list
    }

    for src, dst in transitions:
        if src not in counts or dst not in counts[src]:
            raise ValueError(f"Unknown transition ({src}->{dst})")
        counts[src][dst] += 1.0

    matrix: TransitionMatrix = {}
    for src in state_list:
        total = sum(counts[src].values())
        if total == 0:
            matrix[src] = {dst: 1.0 / len(state_list) for dst in state_list}
        else:
            matrix[src] = {dst: counts[src][dst] / total for dst in state_list}

    validate_transition_matrix(matrix)
    return matrix


def stationary_distribution(
    matrix: TransitionMatrix,
    iterations: int = 200,
) -> Dict[State, float]:
    """Approximate stationary distribution by power iteration."""
    validate_transition_matrix(matrix)
    states = list(matrix.keys())
    dist = {s: 1.0 / len(states) for s in states}

    for _ in range(iterations):
        new_dist = {s: 0.0 for s in states}
        for src in states:
            for dst, p in matrix[src].items():
                new_dist[dst] += dist[src] * p
        dist = new_dist

    total = sum(dist.values())
    return {s: v / total for s, v in dist.items()}
