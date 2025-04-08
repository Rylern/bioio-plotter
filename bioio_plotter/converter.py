import numpy as np
from .lut import Lut


def convert_to_rgb(array: np.ndarray, lut: Lut, t: int = 0, z: int = 0) -> np.ndarray:
    """
    Transform the provided array to an image with RGB values plottable with matplotlib.

    :param array: the array containing the values to plot. It must have 5 dimensions (TCZYX) if not RGB, or 6 dimensions (TCZYXS) if RGB
    :param lut: the look-up table to use to convert the channels to colors
    :param t: the timepoint to consider. 0 by default
    :param z: the z-slice to consider. O by default
    :return: a 3-dimensional numpy array (YX3) containing the input array converted to an image with RGB values between 0 and 1. It can be
             given to matplotlib.pyplot.imshow
    :raises ValueError: if the input array has not 5 or 6 dimensions
    """
    if len(array.shape) == 5:
        is_rgb = False
        number_of_channels = array.shape[1]
    elif len(array.shape) == 6:
        is_rgb = True
        number_of_channels = array.shape[5]
    else:
        raise ValueError("Invalid array shape {0}: it must have 5 dimensions (TCZYX) or 6 dimensions (TCZYXS)".format(array.shape))

    array = np.moveaxis(array[t,0,z,...], [2], [0]) if is_rgb else array[t,:,z]
    array = array.astype(np.float32)
    
    channels = []
    for c in range(number_of_channels):
        channel_display = lut.get_channel_display(c)
        if channel_display is None:
            continue

        if channel_display.min is not None or channel_display.max is not None:
            array[c] = np.clip(array[c], channel_display.min, channel_display.max)

        min = np.min(array[c]) if channel_display.min is None else channel_display.min
        max = np.max(array[c]) if channel_display.max is None else channel_display.max
        array[c] = (array[c] - min) / (max - min)
    
        channels.append(np.array([channel_display.color[j] * array[c] for j in range(3)]))
    
    channels = np.array(channels)
    res = np.sum(channels, axis=0)
    res = np.clip(res, 0, 1)
    res = np.transpose(res, axes=[1, 2, 0])
    
    return res