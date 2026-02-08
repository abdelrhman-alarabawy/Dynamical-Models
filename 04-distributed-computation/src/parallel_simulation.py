"""Parallel trajectory simulation using only Python standard library."""

from __future__ import annotations

import multiprocessing as mp
import random
import time
from typing import Dict, List


def simulate_one(seed: int, steps: int = 1000) -> float:
    rng = random.Random(seed)
    x = 0.0
    for _ in range(steps):
        x = 0.95 * x + rng.gauss(0, 1)
    return x


def run_serial(num_tasks: int, steps: int) -> Dict[str, float | List[float]]:
    start = time.perf_counter()
    outputs = [simulate_one(seed=i, steps=steps) for i in range(num_tasks)]
    return {"seconds": time.perf_counter() - start, "outputs": outputs}


def run_parallel(num_tasks: int, steps: int, workers: int) -> Dict[str, float | List[float]]:
    start = time.perf_counter()
    with mp.Pool(processes=workers) as pool:
        outputs = pool.starmap(simulate_one, [(i, steps) for i in range(num_tasks)])
    return {"seconds": time.perf_counter() - start, "outputs": outputs}


if __name__ == "__main__":
    num_tasks = 500
    steps = 500
    workers = max(2, mp.cpu_count() // 2)

    serial = run_serial(num_tasks=num_tasks, steps=steps)
    parallel = run_parallel(num_tasks=num_tasks, steps=steps, workers=workers)

    print(f"serial:   {serial['seconds']:.4f}s")
    print(f"parallel: {parallel['seconds']:.4f}s (workers={workers})")
