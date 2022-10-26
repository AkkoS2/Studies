# bibliotecas
from rembg import remove
from PIL import Image
import easygui as eg

path_input = eg.fileopenbox(title='Choose the image that you want')
path_output = eg.filesavebox(title='Where you want to save it?', filetypes='.png')

original = Image.open(path_input)
edited = remove(original)
edited.save(path_output)

# A Simple background remover, it can work well most of the time with real life pictures and
# does not work well with anime pictures, the results may be awkward but still can
# generate some weird results in general, although they are funny sometimes
