import torch
import numpy as np
import matplotlib.pyplot as plt

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

r = 0.29
level = 5
xl = torch.tensor([30.0])
yl = torch.tensor([190.0])
xr = torch.tensor([330.0])
yr = torch.tensor([190.0])
xl = xl.to(device)
yl = yl.to(device)
xr = xr.to(device)
yr = yr.to(device)

for i in range(level - 1):
    nextxl = xl.clone()
    nextxr = xr.clone()
    nextyl = yl.clone()
    nextyr = yr.clone()

    xl_1 = nextxl
    yl_1 = nextyl
    xr_1 = 0.333 * nextxr + 0.667 * nextxl
    yr_1 = 0.333 * nextyr + 0.667 * nextyl

    xl_2 = xr_1
    yl_2 = yr_1
    xr_2 = 0.5 * nextxr + 0.5 * nextxl - r * (nextyl - nextyr)
    yr_2 = 0.5 * nextyr + 0.5 * nextyl + r * (nextxl - nextxr)

    xl_3 = xr_2
    yl_3 = yr_2
    xr_3 = 0.667 * nextxr + 0.333 * nextxl
    yr_3 = 0.667 * nextyr + 0.333 * nextyl

    xl_4 = xr_3
    yl_4 = yr_3
    xr_4 = nextxr
    yr_4 = nextyr

    xleft = torch.cat([xl_1, xl_2, xl_3, xl_4])
    yleft = torch.cat([yl_1, yl_2, yl_3, yl_4])
    xright = torch.cat([xr_1, xr_2, xr_3, xr_4])
    yright = torch.cat([yr_1, yr_2, yr_3, yr_4])
    xl, yl, xr, yr = xleft, yleft, xright, yright

fig = plt.figure()
xl = xleft.cpu().numpy()
yl = yleft.cpu().numpy()
xr = xright.cpu().numpy()
yr = yright.cpu().numpy()
for i in range(len(xl)):
    plt.plot([xl[i], xr[i]], [yl[i], yr[i]], color='red', linewidth=1)
plt.gca().set_facecolor('black')
plt.axis('equal')
plt.axis('off')
plt.show()
