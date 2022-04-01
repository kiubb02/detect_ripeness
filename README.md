# Implementation

There are two Solutions given:
- Solution one: Color Hue
- Solution two: Labelled Data

The Color Hue solution is the more simple solution with which we could start working and testing already, meanwhile the Labelled Data Solution will take more time, especially since we have to collect more data to reach a well enough accuracy.

Working with the color alone is still really sensitive since a touch of red is already taken into consideration.
(View: result.png in Color-Hue Folder)
There we can see that it detects two "Ripe Strawberries" even tho I am just holding up one. 

Tutorial I followed for setting up a Model through Tensorflow: https://www.youtube.com/watch?v=yqkISICHH-U

# First Steps

## Requirements

For this Implementation to work u will need the following: 
- Numpy
- OpenCV 
- Python 3.x version
(The Version that worked best for me was 3.7)

## Installation of OpenCV (for Windows)

Installing OpenCV in ur Project IDE works with the following command: 
> pip install opencv-python

Importing the Module into the project is the following line:
> import cv2 as cv
