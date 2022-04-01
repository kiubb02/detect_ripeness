# Program detecting ripeness based on object detection (NN - Model)
# In our Case ==> Live Object Detection/Recognition

# %matplotlib inline
###############################################
#                    IMPORTS                  #
###############################################
from __future__ import division
import numpy as np
# import opencv module
import cv2
import matplotlib
from matplotlib import colors
from matplotlib import pyplot as plt
import pandas as pd


# define a video capture object
vid = cv2.VideoCapture(0)

while (True):

    # Capture the video frame
    # by frame
    ret, frame = vid.read()

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # how will we quit it in the actual application?
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()