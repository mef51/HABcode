## The control everything sensors can be daisy chained together onto the I2C bus.

The setup to facilitate this is as follows:

# 1) Enable I2C

sudo raspi-config
Enable I2C under devices

# 2) Install smbus + dependencies

Follow dependency and smbus instructions here:
https://pypi.python.org/pypi/smbus-cffi/0.5.1

# Note:

It is suggested that the modules are heated (or powered) for 24 hours before use to achieve optimal peformance.

# Connection:

The brown wire is the ground, and the I2C connector should terminate above the HDMI port.

Ensure that the order is as follows:
Master Device -> Input (device 1) -> Output (device 1) -> Input (device 2) .....

## Methane

https://github.com/ControlEverythingCommunity/ADC121C_MQ4.git

## Ozone

https://github.com/ControlEverythingCommunity/ADC121C_MQ131