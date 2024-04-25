from util.vis.helper_tool import Plot
import numpy as np
import collections
import pyvista as pv

xyzRgbLabel = np.load('data/004.npy')
print(xyzRgbLabel.shape)

xyzrgb = xyzRgbLabel[:, :6]
xyzs = xyzRgbLabel[:, :3]
rgbs = xyzRgbLabel[:, 3:6]
labels = xyzRgbLabel[:, 6]
# print(xyzrgb)

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
        label.append(labels[i])

xyz = np.array(xyz)
rgb = np.array(rgb)
label = np.array(label)
print(xyz.shape)

# Plot.draw_pc_sem_ins(xyz, label, None, 0.1, add_colors=rgb)
# Plot.draw_pc(xyzrgb)

cloud = pv.PolyData(xyz)

# cloud to mesh
volume = cloud.delaunay_3d(alpha=2.0)
shell = volume.extract_geometry()

pl = pv.Plotter()
pl.add_mesh(volume, color='red', opacity=1)
pl.set_background('black')
pl.show()