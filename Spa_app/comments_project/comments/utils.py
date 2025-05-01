import random
import string
import io
from PIL import Image, ImageDraw, ImageFont
from django.core.files.base import ContentFile

def generate_captcha():
    chars = string.ascii_letters + string.digits
    text = ''.join(random.choices(chars, k=5))

    image = Image.new('RGB', (120, 40), color=(255, 255, 255))
    draw = ImageDraw.Draw(image)

    font = ImageFont.load_default()
    draw.text((10, 10), text, font=font, fill=(0, 0, 0))

    buffer = io.BytesIO()
    image.save(buffer, format='PNG')
    buffer.seek(0)

    return text, ContentFile(buffer.getvalue(), name='captcha.png')