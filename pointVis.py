from util.vis.helper_tool import Plot
import numpy as np

if __name__ == "__main__":
    
    xyzRgbLabel = np.load("data/004.npy")
    print(xyzRgbLabel.shape)

    # xyzrgb = xyzRgbLabel[:, :6]
    xyzs = xyzRgbLabel[:, :3]
    rgbs = xyzRgbLabel[:, 3:6]
    labels = xyzRgbLabel[:, 6]
    
    # plotInstance(xyzs, rgbs)
    # plotInstanceSeg(xyzs, labels)
    
    Plot.draw_pc_sem_ins(xyzs, labels, None, 0.2, add_colors=rgbs)
    # Plot.draw_pc(xyzRgbLabel[:, :6])