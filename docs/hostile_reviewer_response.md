# Hostile Reviewer Response

The strongest hostile review is correct that exact dependency sets are doing much of the work. The v2 stress shows that missing dependencies create false negatives and spurious dependencies create unnecessary invalidations.

The surviving contribution is the interface: cached plans should expose topology dependencies so map updates can decide cache validity more intelligently than raw delta thresholds.
