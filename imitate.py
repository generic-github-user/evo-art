import numpy as np
from matplotlib.image import imread
import importlib.util
import sys

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
