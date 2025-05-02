from bioio_plotter.image_display import ImageDisplay
from bioio_plotter.lut import Lut
from bioio_plotter import colors


def test_image_display_creation_with_empty_dict():
    image_display = ImageDisplay({})

    lut = image_display.get_lut(0)

    assert lut is None


def test_image_display_creation_with_empty_list():
    image_display = ImageDisplay([])

    lut = image_display.get_lut(0)

    assert lut is None


def test_get_lut_with_list():
    luts = [
        Lut(colors.BLACK),
        Lut(colors.RED),
        Lut(colors.MAGENTA),
        Lut(colors.BLUE)
    ]
    channel = 2
    expected_lut = luts[channel]
    image_display = ImageDisplay(luts)

    lut = image_display.get_lut(channel)

    assert expected_lut == lut


def test_get_lut_with_dict():
    luts = {
        3: Lut(colors.BLACK),
        6: Lut(colors.RED),
        8: Lut(colors.MAGENTA),
        32: Lut(colors.BLUE)
    }
    channel = 6
    expected_lut = luts[channel]
    image_display = ImageDisplay(luts)

    lut = image_display.get_lut(channel)

    assert expected_lut == lut


def test_get_None_lut_with_list():
    luts = [
        Lut(colors.BLACK),
        Lut(colors.RED),
        Lut(colors.MAGENTA),
        Lut(colors.BLUE)
    ]
    channel = 8
    expected_lut = None
    image_display = ImageDisplay(luts)

    lut = image_display.get_lut(channel)

    assert expected_lut == lut


def test_get_None_lut_with_dict():
    luts = {
        3: Lut(colors.BLACK),
        6: Lut(colors.RED),
        8: Lut(colors.MAGENTA),
        32: Lut(colors.BLUE)
    }
    channel = 7
    expected_lut = None
    image_display = ImageDisplay(luts)

    lut = image_display.get_lut(channel)

    assert expected_lut == lut
