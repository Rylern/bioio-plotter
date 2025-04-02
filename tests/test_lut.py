from bioio_plotter.lut import Lut, ChannelDisplay
from bioio_plotter import colors


def test_lut_creation_with_empty_dict():
    lut = Lut({})

    channel_display = lut.get_channel_display(0)

    assert channel_display is None


def test_lut_creation_with_empty_list():
    lut = Lut([])

    channel_display = lut.get_channel_display(0)

    assert channel_display is None


def test_get_channel_display_with_list():
    channel_displays = [
        ChannelDisplay(colors.BLACK),
        ChannelDisplay(colors.RED),
        ChannelDisplay(colors.MAGENTA),
        ChannelDisplay(colors.BLUE)
    ]
    channel = 2
    expected_channel_display = channel_displays[channel]
    lut = Lut(channel_displays)

    channel_display = lut.get_channel_display(channel)

    assert expected_channel_display == channel_display


def test_get_channel_display_with_dict():
    channel_displays = {
        3: ChannelDisplay(colors.BLACK),
        6: ChannelDisplay(colors.RED),
        8: ChannelDisplay(colors.MAGENTA),
        32: ChannelDisplay(colors.BLUE)
    }
    channel = 6
    expected_channel_display = channel_displays[channel]
    lut = Lut(channel_displays)

    channel_display = lut.get_channel_display(channel)

    assert expected_channel_display == channel_display


def test_get_None_channel_display_with_list():
    channel_displays = [
        ChannelDisplay(colors.BLACK),
        ChannelDisplay(colors.RED),
        ChannelDisplay(colors.MAGENTA),
        ChannelDisplay(colors.BLUE)
    ]
    channel = 8
    expected_channel_display = None
    lut = Lut(channel_displays)

    channel_display = lut.get_channel_display(channel)

    assert expected_channel_display == channel_display


def test_get_None_channel_display_with_dict():
    channel_displays = {
        3: ChannelDisplay(colors.BLACK),
        6: ChannelDisplay(colors.RED),
        8: ChannelDisplay(colors.MAGENTA),
        32: ChannelDisplay(colors.BLUE)
    }
    channel = 7
    expected_channel_display = None
    lut = Lut(channel_displays)

    channel_display = lut.get_channel_display(channel)

    assert expected_channel_display == channel_display
