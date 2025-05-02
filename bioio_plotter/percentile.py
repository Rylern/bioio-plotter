class Percentile:
    """
    A simple class to represents a percentile rank.
    """
    def __init__(self, percentile_rank: float):
        """
        :param percentile_rank: the percentile rank, between 0 and 100 (e.g. a percentile rank of 50 represents the median)
        :raises ValueError: if the percentile rank is not between 0 and 100
        """
        if percentile_rank < 0 or percentile_rank > 100:
            raise ValueError("Invalid percentile_rank {0}: it must be between 0 and 100".format(percentile_rank))

        self._percentile_rank = percentile_rank

    def get_percentile_rank(self) -> float:
        return self._percentile_rank
