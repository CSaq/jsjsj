from util.vis.helper_tool import Plot
from util.vis.pyvistaUtil import plotInstance, plotInstanceSeg
import numpy as np

if __name__ == "__main__":
    
    xyzRgbLabel = np.load("data/004.npy")
    print(xyzRgbLabel.shape)

    xyzs = xyzRgbLabel[:, :3]
    rgbs = xyzRgbLabel[:, 3:6]
    labels = xyzRgbLabel[:, 6]
    
    # plotInstance(xyzs, rgbs, labels)
    plotInstanceSeg(xyzs, rgbs, labels, factor=0.2)
    