import pytest
import numpy as np
from bioio_plotter.converter import convert_to_rgb
from bioio_plotter.lut import Lut, ChannelDisplay


def test_converter_with_invalid_shape():
    array = np.zeros((1, 1))
    lut = Lut([])

    with pytest.raises(ValueError):
        convert_to_rgb(array, lut)


def test_converter_with_non_rgb_image():
    non_rgb_image = np.array([[
        [[
            [0, 5, 9],
            [1, 7, 8]
        ]],
        [[
            [1, 15, 13],
            [1, 4, 5]
        ]]
    ]])
    lut = Lut([
        ChannelDisplay([1, 0, 1], 2, 6),
        ChannelDisplay([0, 1, 0], 1, 11)
    ])
    expected_array = np.array([
        [[0, 0, 0], [0.75, 1, 0.75], [1,   1, 1]],
        [[0, 0, 0], [1,  0.3,    1], [1, 0.4, 1]]
    ])

    array = convert_to_rgb(non_rgb_image, lut)

    np.testing.assert_almost_equal(array, expected_array)


def test_converter_with_rgb_image():
    rgb_image = np.array([[[[
        [[20, 17, 201],  [35, 186, 133], [39, 14, 85]],
        [[17, 174, 129], [198, 195, 74], [33, 43, 157]]
    ]]]])
    lut = Lut([
        ChannelDisplay([1, 0, 0], 20, 200),
        ChannelDisplay([0, 1, 0], 0, 255),
        ChannelDisplay([0, 0, 1], 50, 100)
    ])
    expected_array = np.array([
        [[0, 17/255, 1],  [15/180, 186/255, 1],     [19/180, 14/255, 0.7]],
        [[0, 174/255, 1], [178/180, 195/255, 0.48], [13/180, 43/255, 1]]
    ])

    array = convert_to_rgb(rgb_image, lut)

    np.testing.assert_almost_equal(array, expected_array)


def test_converter_with_complex_image():
    complex_image = np.array([
        [
            [
                [
                    [79, 79, 75],
                    [28, 62, 13]
                ],
                [
                    [32, 87, 52],
                    [89, 80, 71]
                ]
            ],
            [
                [
                    [37, 58, 92],
                    [25, 44, 58]
                ],
                [
                    [61, 78, 38],
                    [91, 62, 27]
                ]
            ]
        ],
        [
            [
                [
                    [73, 99, 85],
                    [83, 50, 65]
                ],
                [
                    [25, 24, 78],
                    [18, 60, 13]
                ]
            ],
            [
                [
                    [77, 96, 15],
                    [43, 90, 63]
                ],
                [
                    [23, 3, 74],
                    [61, 77, 1]
                ]
            ]
        ]])
    lut = Lut([
        ChannelDisplay([1, 0, 1], 20, 80),
        ChannelDisplay([0, 1, 0], 0, 100)
    ])
    t = 1
    z = 0
    expected_array = np.array([
        [[53/60, 0.77, 53/60], [1, 0.96, 1],     [1, 0.15, 1]],
        [[1, 0.43, 1],         [0.5, 0.9, 0.5],  [0.75, 0.63, 0.75]]
    ])

    array = convert_to_rgb(complex_image, lut, t=t, z=z)

    np.testing.assert_almost_equal(array, expected_array)


def test_converter_with_min_not_defined():
    image = np.array([[
        [[
            [0, 5, 9],
            [1, 7, 8]
        ]],
        [[
            [1, 15, 13],
            [1, 4, 5]
        ]]
    ]])
    lut = Lut([
        ChannelDisplay(color=[1, 0, 1], max=6),
        ChannelDisplay(color=[0, 1, 0], min=1, max=11)
    ])
    expected_array = np.array([
        [[0, 0, 0],     [5/6, 1, 5/6], [1, 1, 1]],
        [[1/6, 0, 1/6], [1, 0.3, 1],   [1, 0.4, 1]]
    ])

    array = convert_to_rgb(image, lut)

    np.testing.assert_almost_equal(array, expected_array)


def test_converter_with_max_not_defined():
    image = np.array([[
        [[
            [0, 5, 9],
            [1, 7, 8]
        ]],
        [[
            [1, 15, 13],
            [1, 4, 5]
        ]]
    ]])
    lut = Lut([
        ChannelDisplay(color=[1, 0, 1], min=2),
        ChannelDisplay(color=[0, 1, 0], min=1, max=11)
    ])
    expected_array = np.array([
        [[0, 0, 0], [3/7, 1, 3/7],   [1, 1, 1]],
        [[0, 0, 0], [5/7, 0.3, 5/7], [6/7, 0.4, 6/7]]
    ])

    array = convert_to_rgb(image, lut)

    np.testing.assert_almost_equal(array, expected_array)


def test_converter_with_channel_not_defined():
    image = np.array([[
        [[
            [0, 5, 9],
            [1, 7, 8]
        ]],
        [[
            [1, 15, 13],
            [1, 4, 5]
        ]]
    ]])
    lut = Lut({
        1: ChannelDisplay([0, 1, 0], 1, 11)
    })
    expected_array = np.array([
        [[0, 0, 0], [0, 1, 0],   [0, 1, 0]],
        [[0, 0, 0], [0, 0.3, 0], [0, 0.4, 0]]
    ])

    array = convert_to_rgb(image, lut)

    np.testing.assert_almost_equal(array, expected_array)