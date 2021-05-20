from matplotlib import animation
from numpy.lib import poly
# from iou3d import get_3d_box, box3d_iou, get_rotation_matrix, polygon_clip
from ioulib import Box, iou
import numpy as np 
from itertools import combinations
from matplotlib import pyplot as plt 
from matplotlib.animation import FuncAnimation
from plotbox import set_axes_equal
from ioulib import plot_box, iou
import pymesh
        
def animate():
    fig = plt.figure(figsize=(10,10))
    ax1 = fig.add_subplot(2,1,1,projection='3d')
    ax2 = fig.add_subplot(2,1,2)
    ax2.set_ylabel('IoU')

    ax1.set_box_aspect([1,1,1]) # IMPORTANT - this is the new, key line
    ax1.set_proj_type('ortho') # OPTIONAL - default is perspective (shown in image above)
    set_axes_equal(ax1) # IMPORTANT - this is also required
    
    box1 = Box([0,0,0],[1,1,1],[0,0,0])
    box2 = Box([-2,0,0],[3,2,0.5],[0,0,0])

    n_frames = 120

    ious = []
    def update(i):
        print(f'\r\x1b[KFrame: {i+1} / {n_frames}', end="")
        plot_box(box1, ax1, c='b')
        plot_box(box2, ax1, c='r')
        box2.loc[0] += 0.05
        box2.rot += [0.025,0.04,0.1]
        box1.loc[0] += 0.01
        ious.append(iou(box1,box2))
        ax2.plot(ious, c='k')
        ax1.set(xlabel='x', ylabel='y', zlabel='z', xlim=(-2,2), ylim=(-2,2), zlim=(-2,2))
    anim = FuncAnimation(fig, update, interval=30, frames=n_frames, repeat=False)
    anim.save('test.mp4')
    print()

if __name__=='__main__':
    animate()