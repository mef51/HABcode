import picamera
import datetime
from time import sleep

camera = picamera.PiCamera()

## Camera options
# camera.sharpness = 0
# camera.contrast = 0
# camera.brightness = 50
# camera.saturation = 0
# camera.ISO = 0
camera.video_stabilization = True
# camera.exposure_compensation = 0
# camera.exposure_mode = 'auto'
# camera.meter_mode = 'average'
# camera.awb_mode = 'auto'
# camera.image_effect = 'none'
# camera.color_effects = None
# camera.rotation = 0
# camera.hflip = False
# camera.vflip = False
# camera.crop = (0.0, 0.0, 1.0, 1.0)

def take_picture(c):
	c.capture(str(datetime.datetime.now()) + '.jpg')


# will record either for 4 hours or until an interrupt
# if an interrupt occurs the previous video will still be saved
def take_video(c):
	c.start_recording(str(datetime.datetime.now()) + '.h264')
	sleep(60*60*4) # record for 4 hours
	c.stop_recording()

take_video(camera)


