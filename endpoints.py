from fastapi import APIRouter, UploadFile
from fastapi.responses import HTMLResponse, PlainTextResponse

from constants import DEFAULT_NUM_CHARS, DEFAULT_WIDTH_PIXELS, INDEX_HTML
from models.text_to_banner import TextToBannerRequest
from services.banner import convert_text_to_banner
from services.fonts import (
    all_fonts,
    cyrillic_fonts,
)
from services.image import convert_image_to_image

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def root():
    return INDEX_HTML.read_text()


@router.get("/fonts")
async def get_fonts(cyrillic: bool = False):
    if cyrillic:
        return f"All cyrillic fonts are: {cyrillic_fonts}"
    return f"All fonts are: {all_fonts}"
    # TODO instead of returning only the font names you can return a sample text with all fonts


@router.post("/text-to-banner", response_class=PlainTextResponse)
async def text_to_banner(request: TextToBannerRequest):
    return convert_text_to_banner(request)


@router.post("/image-to-image", response_class=PlainTextResponse)
async def image_to_image(
    image: UploadFile,
    width_pixels: int = DEFAULT_WIDTH_PIXELS,
    num_chars: int = DEFAULT_NUM_CHARS,
):  # TODO: add validation
    return convert_image_to_image(image, width_pixels, num_chars)
