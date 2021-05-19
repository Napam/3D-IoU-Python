import numpy as np 
from numpy.typing import ArrayLike
from matplotlib import pyplot as plt 

def clocksort(vertices: ArrayLike):
    '''
    Sorts 2D vertices into clockwise order, doesn't work for 3D+
    '''
    mean = np.mean(vertices, axis=0)
    vertices = vertices - np.mean(vertices, axis=0)
    vlist = [*vertices]
    v = vlist.pop()
    s = [v]
    while vlist:
        dots = vlist@v / (np.linalg.norm(vlist, axis=1) * np.linalg.norm(v))
        idx = dots.argmax()
        v = vlist.pop(idx)
        s.append(v)
    vertices[...] = s + mean
    return vertices

if __name__ == '__main__':
    thetas = np.linspace(0,2,64)*np.pi
    a = np.array([np.sin(thetas), np.cos(thetas)*0.5]) + 10
    a = a.T

    fig, (ax1, ax2) = plt.subplots(2,1)

    np.random.shuffle(a)
    ax1.plot(*a.T)
    ax1.set_aspect('equal')

    a = clocksort(a)
    ax2.plot(*a.T)
    ax2.set_aspect('equal')
    plt.show()