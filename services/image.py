from fastapi import UploadFile
from PIL import Image
from PIL.Image import Resampling

from constants import MINIMAL_CHAR_RAMP, STD_CHAR_RAMP


def convert_image_to_image(
    image: UploadFile, width_pixels: int, num_chars: int, minimal
) -> str:
    img = Image.open(image.file)
    height_pixels = (
        width_pixels // 2
    )  # Because characters are twice as tall as they are wide
    img = img.resize((width_pixels, height_pixels), resample=Resampling.LANCZOS)

    # TODO: maybe explore using luma 709 and/or increasing contrast before converting
    img = img.convert("L")
    img.save("grayscale.png")

    if minimal:
        chars = MINIMAL_CHAR_RAMP
    else:
        chars = get_chars(num_chars)

    result = ""
    pixels = list(img.getdata())
    for y in range(img.height):
        for x in range(img.width):
            pxl = pixels[y * img.width + x]
            result += chars[pxl * (len(chars) - 1) // 255]
        result += "\n"

    return result


def get_chars(n: int) -> str:
    step = len(STD_CHAR_RAMP) // n
    return STD_CHAR_RAMP[::step][:n]
