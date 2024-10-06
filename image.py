import random
import textwrap
from PIL import Image, ImageDraw, ImageFont

WIDTH = HEIGHT = 500


def generate_joke_image(joke, image_file_name):
    joke_lines = []
    for joke_line in joke.split('\n'):
        joke_lines.extend(textwrap.wrap(joke_line, width=30))

    if len(joke_lines) > 9:
        indent_from_above = 70
    elif len(joke_lines) > 6:
        indent_from_above = 100
    else:
        indent_from_above = 150

    r = g = b = 0
    while r + g + b < 400:
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

    image = Image.new('RGB', (WIDTH, HEIGHT), (r, g, b))

    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('arial.ttf', size=25)

    line_spacing = 10
    for joke_line in joke_lines:
        _, _, line_width, line_height = draw.textbbox((0, 0), joke_line, font=font)
        draw.text(
            ((WIDTH - line_width) / 2, indent_from_above),
            joke_line,
            font=font,
            fill=(0, 0, 0),
        )
        indent_from_above += line_height + line_spacing

    image.save(image_file_name)
