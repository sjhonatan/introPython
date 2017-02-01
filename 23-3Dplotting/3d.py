"""
Jhonatan da Silva
Last Updated version :
Tue Jan 31 22:35:52 2017
Number of code lines: 
67
"""
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import FancyArrowPatch
import numpy as np
from mpl_toolkits.mplot3d import proj3d

#from mpl_toolkits.mplot3d import axes3d

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0, 0), (0, 0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        FancyArrowPatch.draw(self, renderer)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.set_xlim([0, 3])
ax.set_ylim([3, 0])
ax.set_zlim([0, 4])

xA = Arrow3D([0, .5], [0, 0], [0, 0], mutation_scale=20, lw=1, arrowstyle="->", color="r")
yA = Arrow3D([0, 0], [0, .5], [0, 0], mutation_scale=20, lw=1, arrowstyle="->", color="r")
zA = Arrow3D([0, 0], [0, 0], [0, .5], mutation_scale=20, lw=1, arrowstyle="->", color="r")

xB = Arrow3D([0, 0.5], [0.3, 0.3], [1, 1], mutation_scale=20, lw=1, arrowstyle="->", color="g")
yB = Arrow3D([0, 0], [0.3, .8], [1, 1], mutation_scale=20, lw=1, arrowstyle="->", color="g")
zB = Arrow3D([0, 0], [0.3, 0.3], [1, 1.5], mutation_scale=20, lw=1, arrowstyle="->", color="g")

xC = Arrow3D([0, .5], [1, 1], [2, 2], mutation_scale=20, lw=1, arrowstyle="->", color="b")
yC = Arrow3D([0, 0], [1, 1.5], [2, 2], mutation_scale=20, lw=1, arrowstyle="->", color="b")
zC = Arrow3D([0, 0], [1, 1], [2, 2.5], mutation_scale=20, lw=1, arrowstyle="->", color="b")

xD = Arrow3D([.5, 1], [2, 2], [1, 1], mutation_scale=20, lw=1, arrowstyle="->", color="y")
yD = Arrow3D([.5, .5], [2, 2.5], [1, 1], mutation_scale=20, lw=1, arrowstyle="->", color="y")
zD = Arrow3D([.5, .5], [2, 2], [1, 1.5], mutation_scale=20, lw=1, arrowstyle="->", color="y")

ax.add_artist(xA)
ax.add_artist(yA)
ax.add_artist(zA)

ax.add_artist(xB)
ax.add_artist(yB)
ax.add_artist(zB)

ax.add_artist(xC)
ax.add_artist(yC)
ax.add_artist(zC)

ax.add_artist(xD)
ax.add_artist(yD)
ax.add_artist(zD)

x = [0,0,0,.5]
y = [0,0.3,1,2]
z = [0,1,2,1]

ax.scatter(x,y,z,c='g',marker='o')
ax.plot_wireframe(x,y,z)
plt.savefig('rrr.png')
plt.show()
