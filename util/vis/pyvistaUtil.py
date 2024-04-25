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
    cloud["point_colors"] = rgb
    pl = pv.Plotter()
    pl.add_points(cloud, point_size=8, rgb=True)
    pl.set_background("black")
    pl.show()


def plotInstanceSeg(xyzs, rgbs, labels, factor=1):
    clouds = {}
    clouds_rgb = {}
    for i in range(0, len(labels)):
        if str(labels[i]) not in clouds:
            clouds[str(labels[i])] = []
            clouds_rgb[str(labels[i])] = []
        clouds[str(labels[i])].append(xyzs[i])
        clouds_rgb[str(labels[i])].append(rgbs[i])
    print(clouds.keys())
    label = list(clouds.keys())
    rgbLabel = Plot.random_colors(len(label), seed=2) * np.array([factor])

    pl = pv.Plotter()
    for i in range(len(label)):
        xyz = clouds[label[i]]
        xyz = np.array(xyz)
        print(i, xyz.shape)
        rgb = clouds_rgb[label[i]]
        rgb = np.array(rgb)

        cloud = pv.PolyData(xyz)
        cloud["point_colors"] = rgb + rgbLabel[i]
        pl.add_points(cloud, point_size=5, rgb=True)

    pl.set_background("black")
    pl.show()
