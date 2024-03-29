# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import adafruit_adxl34x

i2c = board.I2C()  # uses board.SCL and board.SDA
print(dir(adafruit_adxl34x))
# For ADXL343
accelerometer = adafruit_adxl34x.ADXL343(i2c)
# For ADXL345
# accelerometer = adafruit_adxl34x.ADXL345(i2c)

accelerometer.enable_motion_detection()
# alternatively you can specify the threshold when you enable motion detection for more control:
# accelerometer.enable_motion_detection(threshold=10)

while True:
    print("%f %f %f" % accelerometer.acceleration)
    print(dir(accelerometer))
    break
    print("Motion detected: %s" % accelerometer.events["motion"])
    time.sleep(0.5)