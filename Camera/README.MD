# The camera modules can be controlled via shell or python.

The setup to facilitate this is as follows:

## Setup: enable the camera

sudo raspi-config

Enable camera under devices


This is the only step required to get the cameras operational.

Documentation can be found here:
https://www.raspberrypi.org/documentation/raspbian/applications/camera.md


## Suggested video settings:

6 hours = 21600000 ms

1640x1232 video

15MBit/s bit rat

vs, video stabilization

30 fps 

## Tested with the above settings:

2 hr recording =  2.56 GB
4 hr recording = 12.45 GB

## Video formating:

Using MP4Box
