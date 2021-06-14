import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread
import importlib.util
import sys
import glob
from PIL import Image, ImageDraw, ImageFont
import string
import random
import copy

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
# image_data = imread(images[0])
path = images[1]
print(path)
image_data = Image.open(path)
downscaled = np.array(image_data.size) * 0.1
image_data.thumbnail(downscaled)
# print(image_data[0])
population = []

# generated = np.zeros_like(image_data)
width, height = image_data.size
num = 10
history = []
generations = 100
parts = 20
dims = (width, height)
# font = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 40)
# font = ImageFont.load('arial.pil')
font = ImageFont.truetype('arial.ttf', 5)

for i in range(num):
    group = [[], None]
    generated = Image.new('RGB', dims, (255,)*3)
    d = ImageDraw.Draw(generated)
    for j in range(parts):
        a = [None] * 2
        pos = np.random.randint([0, 0], dims, [2])
        # print(pos)
        text = random.choice(string.ascii_letters)
        color = [255, 0, 0]
        # d.text(tuple(pos), text, fill=tuple(color), font=font)
        a = [pos, text, color]
        group[0].append(a)
    difference = np.abs(generated - np.array(image_data)).mean()
    group[1] = difference
    population.append(group)

for i in range(generations):
    population.sort(key=lambda x: x[1], reverse=False)
    # print(population)
    best = population[0]
    print(best[1])
    history.append(best[1])
    population = [copy.deepcopy(best) for n in range(num)]
    for j, g in enumerate(population):
        generated = Image.new('RGB', dims, (255,)*3)
        d = ImageDraw.Draw(generated)
        for l in g[0]:
            # print(l)
            l[0] += np.random.normal(0, 2, [2]).astype(int)
            l[0] %= dims
            l[2] += np.random.normal(0, 2, [3]).astype(int)
            l[2] %= [255] * 3

            pos, text, color = l
            d.text(tuple(pos), text, fill=tuple(color), font=font)
            c = [pos, pos+3]
            c = [tuple(w) for w in c]
            # d.rectangle(c, fill=tuple(color))

        difference = np.abs(generated - np.array(image_data)).mean()
        population[j][1] = difference


# generated.show()
generated.save('./result-image.png')
plt.plot(history)
plt.show()

# TODO: gradually upscale image
