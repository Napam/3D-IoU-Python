from iou3d import polygon_clip, get_3d_box, box3d_iou
import numpy as np 
from matplotlib import pyplot as plt 
from plotbox import plot_box, set_axes_equal

dim1 = [1,1,1]
dim2 = [1,1,1]
box1 = get_3d_box(dim1, [0,0,0], [0,0,0])
box2 = get_3d_box(dim2, [0,0,0], [0.5,0,0])

fig = plt.figure()
ax = fig.add_subplot(1,1,1,projection='3d')
set_axes_equal(ax)
ax.set_box_aspect([1,1,1])
ax.set(xlabel='x', ylabel='y', zlabel='z', xlim=(-2,2), ylim=(-2,2), zlim=(-2,2))

box3d_iou(box1, box2)

# plot_box(box1, dim1, ax, c='k')
# plot_box(box2, dim2, ax, c='r')
# plt.show()