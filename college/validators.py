from rest_framework.validators import ValidationError
from urllib.parse import urlparse


def validate_video_link(value):
    parsed_url = urlparse(value)

    # Проверяем, что URL корректный по наличию схемы ('http', 'https') и пути
    if not (parsed_url.scheme and parsed_url.path):
        raise ValidationError("Ссылка некорректна.")

    # Проверяем, что ссылка - это youtube.com или youtu.be
    if (
        "youtube.com" not in parsed_url.hostname and "youtu.be" not in parsed_url.hostname
    ):
        raise ValidationError("Разрешены только ссылки на youtube.com.")
