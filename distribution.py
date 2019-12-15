#!/usr/bin/env python3

import collections
from typing import Mapping, Tuple


class QuadDistribution:
    def __init__(self, distribution: Mapping[Tuple[int, int, int, int], int] = None):
        if distribution is None:
            distribution = {(0, 0, 0, 0): 1}
        self._distribution = distribution

    def _total(self) -> int:
        return sum(self._distribution.values())

    def mean(self) -> Tuple[float, float, float, float]:
        val_sum = [0, 0, 0, 0]
        for value, frequency in self._distribution.items():
            for i in range(0, 4):
                val_sum[i] = val_sum[i] + value[i] * frequency
        for i in range(0, 4):
            val_sum[i] /= self._total()
        return tuple(val_sum)

    def probability_above(self,
                          cutoff: Tuple[int, int, int, int] = (None, None, None, None)) -> float:
        hits = 0
        for (value, frequency) in self._distribution.items():
            for i, cut in enumerate(cutoff):
                if cut is not None and value[i] < cut:
                    # This does make the cut.
                    break
            # Executed when the loop terminates through exhaustion (not a break).
            else:
                hits += frequency
        return hits / self._total()

    def add(self, that: 'QuadDistribution') -> 'QuadDistribution':
        elements = collections.defaultdict(int)
        for value_i, frequency_i in self._distribution.items():
            for value_j, frequency_j in that._distribution.items():
                value = [0, 0, 0, 0]
                for i in range(0, 4):
                    value[i] = value_i[i] + value_j[i]
                frequency = frequency_i * frequency_j
                elements[tuple(value)] += frequency

        return QuadDistribution(elements)
