# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Capacitive Touch example"""
import time
import board
import touchio


touch_pad0 = board.GP0


touch0 = touchio.TouchIn(touch_pad0)

while True:
    if touch0.value:
        print("Touched!")
    time.sleep(0.05)
