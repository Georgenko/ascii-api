from pathlib import Path

BASE_DIR = Path(__file__).parent

TEMPLATES_DIR = BASE_DIR / "templates"
INDEX_HTML = TEMPLATES_DIR / "index.html"

DEFAULT_WIDTH_PIXELS = 128
STD_CHAR_RAMP = (
    "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
)
DEFAULT_NUM_CHARS = len(STD_CHAR_RAMP)
MINIMAL_CHAR_RAMP = "@#S%?*+;:,. "
