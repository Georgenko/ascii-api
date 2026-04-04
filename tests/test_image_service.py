from io import BytesIO

import pytest
from fastapi import UploadFile

from constants import IHDR_BYTES_LENGTH
from services.image import validate_image


def make_upload_file(content: bytes) -> UploadFile:
    return UploadFile(file=BytesIO(content))


def test_valid_image():
    with open("tests/red-pixel.png", "rb") as f:
        content = f.read()
    f = make_upload_file(content)
    validate_image(f)


def test_fake_image_raises_400():
    from fastapi import HTTPException

    f = make_upload_file(b"not an image at all")
    with pytest.raises(HTTPException) as exc:
        validate_image(f)
    assert exc.value.status_code == 400


def test_empty_file_raises_400():
    from fastapi import HTTPException

    f = make_upload_file(b"")
    with pytest.raises(HTTPException) as exc:
        validate_image(f)
    assert exc.value.status_code == 400


def test_corrupted_image_raises_400():
    from fastapi import HTTPException

    corrupted_png = (
        b"\x89PNG\r\n\x1a\n" + b"\x00" * IHDR_BYTES_LENGTH
    )  # PNG magic bytes + malformed IHDR chunk
    f = make_upload_file(corrupted_png)
    with pytest.raises(HTTPException) as exc:
        validate_image(f)
    assert exc.value.status_code == 400
