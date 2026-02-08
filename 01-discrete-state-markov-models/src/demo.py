"""Run a complete practical example for discrete-state Markov models."""

from collections import Counter

from markov_chain import estimate_transition_matrix, simulate_chain, stationary_distribution


if __name__ == "__main__":
    transition_matrix = {
        "Visitor": {"Visitor": 0.55, "Trial": 0.35, "Subscriber": 0.05, "Churned": 0.05},
        "Trial": {"Visitor": 0.10, "Trial": 0.45, "Subscriber": 0.35, "Churned": 0.10},
        "Subscriber": {"Visitor": 0.02, "Trial": 0.06, "Subscriber": 0.87, "Churned": 0.05},
        "Churned": {"Visitor": 0.05, "Trial": 0.10, "Subscriber": 0.00, "Churned": 0.85},
    }

    path = simulate_chain(transition_matrix, initial_state="Visitor", steps=50, seed=7)
    print("Sample trajectory (first 15 states):", path[:15])

    observed_transitions = list(zip(path[:-1], path[1:]))
    estimated = estimate_transition_matrix(
        states=list(transition_matrix.keys()),
        transitions=observed_transitions,
        laplace=1.0,
    )

    print("\nEstimated matrix (from trajectory with Laplace smoothing):")
    for src, row in estimated.items():
        rounded = {dst: round(p, 3) for dst, p in row.items()}
        print(f"  {src}: {rounded}")

    stationary = stationary_distribution(transition_matrix)
    print("\nApprox stationary distribution:", {k: round(v, 3) for k, v in stationary.items()})

    counts = Counter(path)
    print("Observed proportions:", {k: round(v / len(path), 3) for k, v in counts.items()})
