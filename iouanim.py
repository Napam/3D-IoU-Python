from matplotlib import animation
from numpy.lib import poly
from iou3d import get_3d_box, box3d_iou, get_rotation_matrix, polygon_clip
import numpy as np 
from itertools import combinations
from matplotlib import pyplot as plt 
from matplotlib.animation import FuncAnimation
from plotbox import set_axes_equal, plot_box
        
def animate():
    fig = plt.figure(figsize=(10,10))
    ax1 = fig.add_subplot(2,1,1,projection='3d')
    ax2 = fig.add_subplot(2,1,2)

    ax1.set_box_aspect([1,1,1]) # IMPORTANT - this is the new, key line
    ax1.set_proj_type('ortho') # OPTIONAL - default is perspective (shown in image above)
    set_axes_equal(ax1) # IMPORTANT - this is also required
    dim1 = [1,1,1]
    dim2 = [2,0.5,0.5]
    box1 = get_3d_box(dim1, [0,0,0], [1,0,0])
    box2 = get_3d_box(dim2, [0,0,0], [0,0,0])
    R = get_rotation_matrix([0,0.1,0])

    ious = []
    def update(i):
        ax1.clear()
        plot_box(box1, dim1, ax1, c='b')
        box2[...] = (box2-box2.mean(0))@R.T + box2.mean(0)
        box2[:,0] += 0.02
        plot_box(box2, dim2, ax1, c='r')
        ious.append(box3d_iou(box1,box2)[0])
        ax2.plot(ious, c='k')
        ax1.set(xlabel='x', ylabel='y', zlabel='z', xlim=(-2,2), ylim=(-2,2), zlim=(-2,2))

    anim = FuncAnimation(fig, update, interval=10, frames=180, repeat=False)
    plt.show()


if __name__=='__main__':
    animate()