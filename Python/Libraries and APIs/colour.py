# bibliotecas
from PIL import Image
import random

value_int = random.randint(0, 16777215)
value_hex = str(hex(value_int))
value = '#' + value_hex[2:]

im = Image.new("RGB", (200, 150), value)
im.save(f"./colors/{value.upper()}.png")
print('done.')


# A Very basic color generator, with the only porpuse of studying the Pillow library.
# This generates a random Hexadecimal value and then uses Pillow to generate a image
# with the color code, and saves the color image with the HEX code as it's name in a specific folder
