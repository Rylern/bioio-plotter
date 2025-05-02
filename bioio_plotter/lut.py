from dataclasses import dataclass
import numpy as np
from numbers import Number
from .percentile import Percentile


@dataclass
class Lut:
    """
    A look-up table to define how to render a channel.

    :param color: the RGB color (each component between 0 and 1) the channel should have
    :param min: if float, values of the image below this minimum should appear black. If percentile, values below the provided percentile should appear black.
                Can be None to use the minimum value of the image
    :param max: if float, values of the image above this maximum should have the color defined above. If percentile, values above the provided percentile should have the color defined above.
                Can be None to use the maximum value of the image
    :param gamma: the gamma value to apply a gamma correction
    """
    color: tuple[float, float, float]
    min: float | Percentile | None = None
    max: float | Percentile | None = None
    gamma: float = 1

    def get_min(self, array: np.ndarray) -> Number | None:
        """
        :param array: the array from which the percentile should be computed
        :return: self.min if it is a number, the percentile of the provided array if self.min is a percentile, or None
        """
        return Lut._get_extrema(self.min, array)

    def get_max(self, array: np.ndarray) -> Number | None:
        """
        :param array: the array from which the percentile should be computed
        :return: self.max if it is a number, the percentile of the provided array if self.max is a percentile, or None
        """
        return Lut._get_extrema(self.max, array)

    @staticmethod
    def _get_extrema(extrema: Number, array: np.ndarray):
        if isinstance(extrema, Number):
            return extrema
        elif isinstance(extrema, Percentile):
            return np.percentile(array, extrema.get_percentile_rank())
        else:
            return None
