from .lut import Lut


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
