from .channel_display import ChannelDisplay


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
