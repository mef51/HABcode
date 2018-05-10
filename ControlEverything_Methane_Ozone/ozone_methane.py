import smbus
import datetime

# Get I2C bus
bus = smbus.SMBus(1)


### METHANE

# ADC121C_MQ4 address, 0x50(80)
# Read data back from 0x00(00), 2 bytes
# raw_adc MSB, raw_adc LSB
data = bus.read_i2c_block_data(0x50, 0x00, 2)

# Convert the data to 12-bits
raw_adc = (data[0] & 0x0F) * 256 + data[1]
ppm_methane = (10000.0 / 4095.0) * raw_adc + 200


### OZONE

# ADC121C_MQ131 address, 0x5a(90)
# Read data back from 0x00(00), 2 bytes
# raw_adc MSB, raw_adc LSB
data = bus.read_i2c_block_data(0x5a, 0x00, 2)

# Convert the data to 12-bits
raw_adc = (data[0] & 0x0F) * 256 + data[1]
ppm_ozone = (1.99 * raw_adc) / 4096.0 + 0.01

# Write to csv
with open("methane.csv", "a") as output_file:
    cur_time = str(datetime.datetime.now()).split()
    output_file.write("%s,%s,%.3f\n" % (cur_time[0], cur_time[1], ppm_methane))

with open("ozone.csv", "a") as output_file:
    cur_time = str(datetime.datetime.now()).split()
    output_file.write("%s,%s,%.3f\n" % (cur_time[0], cur_time[1], ppm_ozone))

