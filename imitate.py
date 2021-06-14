import numpy as np
from matplotlib.image import imread
import importlib.util
import sys
import glob
from PIL import Image, ImageDraw
import string
import random

# from ..textdiagrams.geometry import *
sys.path.insert(0, '../text-diagrams/geometry')

class Geometry:
    pass

modules = ['point', 'line', 'polygon']
mlist = []
for m in modules:
    # path = f'../text-diagrams/geometry/{m}.py'
    # print(path)
    # spec = importlib.util.spec_from_file_location(m, path)
    # f = importlib.util.module_from_spec(spec)
    # spec.loader.exec_module(f)

    f = importlib.import_module(m)
    setattr(Geometry, m, f)
    mlist.append(f)

# for m in mlist:
#     spec.loader.exec_module(m)

G = Geometry

p = G.point.Point([1, 1])
p.print()

images = glob.glob('./sample-images/*.jpg')
image_data = imread(images[0])
print(image_data[0])
population = []

# generated = np.zeros_like(image_data)
height, width, channels = image_data.shape

for i in range(20):
    group = [[], None]
    dims = (width, height)
    generated = Image.new('RGB', dims, (255,)*3)
    d = ImageDraw.Draw(generated)
    for j in range(500):
        a = [None] * 2
        pos = np.random.randint([0, 0], dims, [2])
        # print(pos)
        text = random.choice(string.ascii_letters)
        color = [255, 0, 0]
        d.text(tuple(pos), text, fill=tuple(color))
        a = pos, text
        group[0].append(a)
    difference = np.abs(generated - image_data).mean()
    group[1] = difference
    population.append(group)

# generated.show()
generated.save('./result-image.png')
