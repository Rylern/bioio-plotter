from dataclasses import dataclass


@dataclass
class Lut:
    """
    A look-up table to define how to render a channel.

    :param color: the RGB color (each component between 0 and 1) the channel should have
    :param min: values of the image below this minimum should appear black. Can be None to use the minimum value of the image
    :param max: values of the image above this maximum should have the color defined above. Can be None to use the maximum value of the image
    """
    color: tuple[float, float, float]
    min: float = None
    max: float = None
