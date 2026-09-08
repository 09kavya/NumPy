"""
RGB Image Brightness
Given an image array of shape (H,W,3), add [10,20,30] to every pixel using broadcasting.
"""

import numpy as np
image = np.array([
    [[100, 120, 150],
     [50,  60,  70]],

    [[200, 180, 160],
     [20,  30,  40]]
])
add=np.array([10,20,30])
print(image+add)