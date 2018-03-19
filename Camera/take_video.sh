#!/bin/bash

# 6 hours = 21600000 ms
# 1640x1232 video
# 15MBit/s bit rat
# vs, video stabilization
# 30 fps 

# A 1 minute video is ~10 MB so a 6 hour video will be ~ 3.6 GB, which is no problem
# for our SD card.

## Capture video
raspivid -t 60000 -vs -w 1640 -h 1232 -fps 30 -b 15000000 -o flight.h264 

## Wrap the raw video with an MP4 container: 
# MP4Box -add flight_0.h264 flight_0.mp4