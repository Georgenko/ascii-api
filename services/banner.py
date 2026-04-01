import pyfiglet

from models.text_to_banner import TextToBannerRequest


def convert_text_to_banner(request: TextToBannerRequest) -> str:
    banner = pyfiglet.figlet_format(request.prompt, font=request.font)
    return f"Font: {request.font}\n\n{banner}"
