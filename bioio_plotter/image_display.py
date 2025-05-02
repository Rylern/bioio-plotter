from .lut import Lut
from . import colors


class ImageDisplay:
    """
    A collection of look-up tables to render any image image to RGB.
    """
    def __init__(self, luts: list[Lut] | dict[int, Lut]):
        """
        :param luts: how to render each channel. Can be a list or a dict where luts[i] defines how to render the ith channel
        """
        if type(luts) is list:
            self._luts = {i: value for i, value in enumerate(luts)}
        else:
            self._luts = luts

    def get_lut(self, channel: int) -> Lut | None:
        """
        Get the look-up table of a channel.

        :param channel: the index of the channel whose look-up table should be retrieved
        :return: the look-up table of the channel, or None if this channel shouldn't be rendered 
        """
        return self._luts[channel] if channel in self._luts else None

    @staticmethod
    def create_rgb():
        """
        Create an image display for RGB images with values between 0 and 255.

        :return: an image display with three look-up tables (red, green, and blue) going from 0 to 255
        """
        return ImageDisplay([
            Lut(colors.RED, 0, 255),
            Lut(colors.GREEN, 0, 255),
            Lut(colors.BLUE, 0, 255)
        ])

    @staticmethod
    def create_grey_single_channel():
        """
        Create an image display for a single-channel image displaying shades of grey.

        :return: an image display with one black look-up table
        """
        return ImageDisplay([Lut(colors.BLACK)])