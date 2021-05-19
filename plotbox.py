import numpy as np 
from iou3d import get_3d_box
from itertools import combinations
from matplotlib import pyplot as plt 

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


def plot_box(box: np.ndarray, dims: np.ndarray, ax, **kwargs):
    combs = np.array(list(combinations(box, 2)))
    norms = np.linalg.norm(np.diff(combs, axis=1).reshape(-1,3), axis=1)
    for p1, p2 in combs[(abs(np.subtract.outer(norms, dims)) < 1e-6).any(1)]:
        ax.plot(*np.array([p1,p2]).T, **kwargs)

if __name__ == '__main__':
    box1 = get_3d_box([1,1,1], [0,0.1,0], [1,1,1])
    box2 = get_3d_box([1,2,3], [0,0.5,0], [0,0,0])

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1,projection='3d')
    ax.set(xlabel='x', ylabel='y', zlabel='z', xlim=(-2,2), ylim=(-2,2), zlim=(-2,2))
    plot_box(box1, [1,1,1],ax, c='k')
    plot_box(box2, [1,2,3],ax, c='r')

    set_axes_equal(ax)
    ax.set_box_aspect([1,1,1]) # IMPORTANT - this is the new, key line
    plt.show()