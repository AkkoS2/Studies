# bibliotecas
from moviepy.editor import *
import random

gif = (VideoFileClip("rikka" + '.mp4'))
gif.write_gif(f"./gifs/{random.randint(0, 16777215)}.gif")
print('done.')


# This is another very basic project, using the MoviePy library to convert videos into gifs
# MoviePy will use your computer CPU to convert the gif and then, wil save it in the specified
# folder with a random int value as it's name
