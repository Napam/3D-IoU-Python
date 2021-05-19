from matplotlib import animation
from iou3d import get_3d_box, box3d_iou, clocksort, is_clockwise
import numpy as np 
from itertools import combinations
from matplotlib import pyplot as plt 
from matplotlib.animation import FuncAnimation


def set_axes_equal(ax):
    '''Make axes of 3D plot have equal scale so that spheres appear as spheres,
    cubes as cubes, etc..  This is one possible solution to Matplotlib's
    ax.set_aspect('equal') and ax.axis('equal') not working for 3D.

    Input
      ax: a matplotlib axis, e.g., as output from plt.gca().
    '''

    x_limits = ax.get_xlim3d()
    y_limits = ax.get_ylim3d()
    z_limits = ax.get_zlim3d()

    x_range = abs(x_limits[1] - x_limits[0])
    x_middle = np.mean(x_limits)
    y_range = abs(y_limits[1] - y_limits[0])
    y_middle = np.mean(y_limits)
    z_range = abs(z_limits[1] - z_limits[0])
    z_middle = np.mean(z_limits)

    # The plot bounding box is a sphere in the sense of the infinity
    # norm, hence I call half the max range the plot radius.
    plot_radius = 0.5*max([x_range, y_range, z_range])

    ax.set_xlim3d([x_middle - plot_radius, x_middle + plot_radius])
    ax.set_ylim3d([y_middle - plot_radius, y_middle + plot_radius])
    ax.set_zlim3d([z_middle - plot_radius, z_middle + plot_radius])

def plot_box(box: np.ndarray, ax, **kwargs):
    combs = np.array(list(combinations(box, 2)))
    combs_normalized = (combs - combs.mean(0)) / (combs.std(0))
    # combs_normalized = combs
    dots = np.array([v1@v2 for v1,v2 in combs_normalized])
    for p1, p2 in combs[dots > 0.5]:
        ax.plot(*np.array([p1,p2]).T, **kwargs)
        
def animate():
    fig = plt.figure()
    ax1 = fig.add_subplot(2,1,1,projection='3d')
    ax2 = fig.add_subplot(2,1,2)

    ax1.set_box_aspect([1,1,1]) # IMPORTANT - this is the new, key line
    ax1.set_proj_type('ortho') # OPTIONAL - default is perspective (shown in image above)
    set_axes_equal(ax1) # IMPORTANT - this is also required
    box1 = get_3d_box([1,1,1], [0,0,0], [1,0,0])
    # box2 = get_3d_box([1,1,1], [0.6,0,0], [-0.5,-1,0])
    box2 = get_3d_box([2,2,2], [0,0,0], [-0.5,0,0])

    ious = []

    def update(i):
        ax1.clear()
        plot_box(box1, ax1, c='b')
        box2[:,0] += 0.06
        plot_box(box2, ax1, c='r')
        ious.append(box3d_iou(box1,box2)[0])
        ax2.plot(ious, c='k')
        ax1.set(xlabel='x', ylabel='y', zlabel='z', xlim=(-2,2), ylim=(-2,2), zlim=(-2,2))

    anim = FuncAnimation(fig, update, interval=10, frames=50, repeat=False)
    plt.show()


if __name__=='__main__':
    animate()
    box1 = get_3d_box([1,1,1], [0,0,0], [1,0,0])
    box2 = get_3d_box([1,1,1], [0,0,0], [1,0,0])
    print(box3d_iou(box1,box2))