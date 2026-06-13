# Submission Attack Log

## Attack: missed dependencies

Question: Does topology-aware invalidation survive incomplete dependency extraction?

Result: 20% missed dependencies reduce F1 to 0.862.

Decision impact: dependency extraction must be treated as a central limitation.

## Attack: spurious dependencies

Question: Does broad dependency extraction cause unnecessary invalidation?

Result: 10% spurious dependencies reduce precision to 0.903 and F1 to 0.949.

Decision impact: avoid claiming free robustness.

## Attack: combined extraction noise

Question: What happens with both missed and spurious dependencies?

Result: 10% missed plus 10% spurious dependencies reduce F1 to 0.873.

Decision impact: workshop-only.
