import numpy as np
from bioio_plotter.lut import Lut
from bioio_plotter.percentile import Percentile


def test_get_min_when_None():
    lut = Lut(None, min=None)
    array = np.array([0, 1, 2])

    min = lut.get_min(array)

    assert min is None


def test_get_min_when_int():
    lut = Lut(None, min=3)
    array = np.array([0, 1, 2])
    expected_min = 3

    min = lut.get_min(array)

    assert expected_min == min


def test_get_min_when_float():
    lut = Lut(None, min=3.43)
    array = np.array([0, 1, 2])
    expected_min = 3.43

    min = lut.get_min(array)

    assert expected_min == min


def test_get_min_when_percentile():
    lut = Lut(None, min=Percentile(50))
    array = np.array([0, 1, 2])
    expected_min = 1

    min = lut.get_min(array)

    assert expected_min == min


def test_get_max_when_None():
    lut = Lut(None, max=None)
    array = np.array([0, 1, 2])

    max = lut.get_max(array)

    assert max is None


def test_get_max_when_int():
    lut = Lut(None, max=3)
    array = np.array([0, 1, 2])
    expected_max = 3

    max = lut.get_max(array)

    assert expected_max == max


def test_get_max_when_float():
    lut = Lut(None, max=3.43)
    array = np.array([0, 1, 2])
    expected_max = 3.43

    max = lut.get_max(array)

    assert expected_max == max


def test_get_max_when_percentile():
    lut = Lut(None, max=Percentile(50))
    array = np.array([0, 1, 2])
    expected_max = 1

    max = lut.get_max(array)

    assert expected_max == max
