import numpy as np
from .image_display import ImageDisplay


def convert_to_rgb(array: np.ndarray, image_display: ImageDisplay, t: int = 0, z: int = 0) -> np.ndarray:
    """
    Transform the provided array with the provided image display to an image with RGB values plottable with matplotlib.

    :param array: the array containing the values to plot. It must have 5 dimensions (TCZYX) if not RGB, or 6 dimensions (TCZYXS) if RGB
    :param image_display: the image display to use to convert the channels to colors
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
        lut = image_display.get_lut(c)
        if lut is None:
            continue

        if lut.min is not None or lut.max is not None:
            array[c] = np.clip(array[c], lut.min, lut.max)

        min = np.min(array[c]) if lut.min is None else lut.min
        max = np.max(array[c]) if lut.max is None else lut.max
        array[c] = (array[c] - min) / (max - min)

        if lut.gamma != 1:
            array[c] = array[c] ** lut.gamma
    
        channels.append(np.array([lut.color[j] * array[c] for j in range(3)]))
    
    channels = np.array(channels)
    res = np.sum(channels, axis=0)
    res = np.clip(res, 0, 1)
    res = np.transpose(res, axes=[1, 2, 0])
    
    return res