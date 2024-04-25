import pyvista as pv
import collections
import numpy as np
from util.vis.helper_tool import Plot

def plotInstance(xyzs, rgbs, labels):
    labelCounter = collections.Counter(labels)
    print(labelCounter)
    most_common = labelCounter.most_common(1)
    print(most_common)
    most_label = most_common[0][0]

    # get the instances of the most common label
    xyz = []
    rgb = []
    label = []
    for i in range(0, len(labels)):
        if labels[i] == most_label:
            xyz.append(xyzs[i])
            rgb.append(rgbs[i])
            # rgb.append(rgbs[i].tolist())
            label.append(labels[i])

    xyz = np.array(xyz)
    rgb = np.array(rgb)
    label = np.array(label)
    print(xyz.shape)

    cloud = pv.PolyData(xyz)
    pl = pv.Plotter()
    pl.add_points(cloud, scalars=rgb, point_size=8)
    pl.set_background('black')
    pl.show()

def plotInstanceSeg(xyzs, labels):
    clouds = {}
    for i in range(0, len(labels)):
        if str(labels[i]) not in clouds:
            clouds[str(labels[i])] = []
        clouds[str(labels[i])].append(xyzs[i])
    print(clouds.keys())
    label = list(clouds.keys())
    rgbs = Plot.random_colors(len(label), seed=2)

    pl = pv.Plotter()
    for i in range(len(label)):
        xyz = clouds[label[i]]
        xyz = np.array(xyz)
        print(i, xyz.shape)
        cloud = pv.PolyData(xyz)
        pl.add_points(cloud, point_size=5, color=rgbs[i], style='points_gaussian')

    pl.set_background('black')
    pl.show()
