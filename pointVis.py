from util.vis.helper_tool import Plot
import numpy as np

xyzRgbLabel = np.load('data/004.npy')
print(xyzRgbLabel.shape)

xyzrgb = xyzRgbLabel[:, :6]
xyz = xyzRgbLabel[:, :3]
rgb = xyzRgbLabel[:, 3:6]
label = xyzRgbLabel[:, 6]
# print(xyzrgb)

Plot.draw_pc_sem_ins(xyz, label, None, 0.1, add_colors=rgb)
# Plot.draw_pc(xyzrgb)