from dataclasses import dataclass


@dataclass
class ChannelDisplay:
    """
    Simple class to define how to render a channel.

    :param color: the RGB color (each component between 0 and 1) the channel should have
    :param min: values of the image below this minimum should appear black. Can be None to use the minimum value of the image
    :param max: values of the image above this maximum should have the color defined above. Can be None to use the maximum value of the image
    """
    color: tuple[float, float, float]
    min: float = None
    max: float = None


class Lut:
    """
    A look-up table to render any image image to RGB.
    """
    def __init__(self, channels_displays: list[ChannelDisplay] | dict[int, ChannelDisplay]):
        """
        :param channels_displays: how to render each channel. Can be a list or a dict where channels_displays[i] defines how to render the ith channel
        """
        if type(channels_displays) is list:
            self._channels_displays = {i: value for i, value in enumerate(channels_displays)}
        else:
            self._channels_displays = channels_displays

    def get_channel_display(self, channel: int) -> ChannelDisplay | None:
        """
        Get the display information about a channel.

        :param channel: the index of the channel whose display information should be retrieved
        :return: the display information the channel should have, or None if this channel shouldn't be rendered 
        """
        return self._channels_displays[channel] if channel in self._channels_displays else None
