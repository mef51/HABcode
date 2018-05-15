from gpiozero import Button, OutputDevice
from time import sleep
button = Button(14)
led = OutputDevice(2)

print ("Ready")
button.wait_for_press()
led.on()
print("pop!")
sleep(120)
print("Popping done")
led.off()