import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.colors as color
import numpy as np
from matplotlib import style
from itertools import cycle

length = 1
diam = 1
n = np.int_(length/diam)
offset = 1/n
array = np.zeros(n)

array[0] = 0.5*offset
for i in range(1, n):
    array[i]=array[0]+i*offset

plt.figure()
currentAxis = plt.gca()
currentAxis.set_aspect('equal')
currentAxis.add_patch(patches.Rectangle((0,1),1,0,edgecolor='black',facecolor='none'))
for i in range(n):
    currentAxis.add_patch(patches.Circle(
        (array[i],1),radius=diam/2,edgecolor='black',facecolor='none')
                          )
plt.show()
