import unicodedata as ud

from pydantic import BaseModel, field_validator
from pydantic_core.core_schema import ValidationInfo

from services.fonts import (
    CYRILLIC,
    CYRILLIC_DISPLAY,
    LATIN,
    LATIN_DISPLAY,
    all_fonts,
    cyrillic_fonts,
)


class TextToBannerRequest(BaseModel):
    cyrillic: bool = False
    font: str = "standard"
    text: str

    @field_validator("font")
    @classmethod
    def validate_font(cls, font: str, info: ValidationInfo) -> str:
        cyrillic = info.data.get("cyrillic", False)
        valid_fonts = cyrillic_fonts if cyrillic else all_fonts
        if font not in valid_fonts:
            raise ValueError(
                f"Invalid font: {font}. Available {CYRILLIC_DISPLAY if cyrillic else ''} fonts: {valid_fonts}"
            )
        return font

    @field_validator("text")
    @classmethod
    def validate_text_characters(cls, text: str, info: ValidationInfo) -> str:
        cyrillic = info.data.get("cyrillic", False)
        for char in text:
            if char.isspace():
                continue
            category = ud.category(char)
            if not category.startswith(("L", "N", "P", "S")):
                raise ValueError(
                    f"Invalid char: {char}. Only letters, digits, punctuation, symbols allowed."
                )
            if category.startswith("L"):
                expected_script = CYRILLIC if cyrillic else LATIN
                char_name = ud.name(char)
                if expected_script not in char_name:
                    raise ValueError(
                        f"Invalid char: {char}. "
                        f"Only {CYRILLIC_DISPLAY if cyrillic else LATIN_DISPLAY} letters allowed"
                    )
        return text
