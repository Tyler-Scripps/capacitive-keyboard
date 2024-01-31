# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Capacitive Touch example"""
import time
import board
import touchio

from collections import deque

import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

pins = [board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11, board.GP12, board.GP13, board.GP14, board.GP15, board.GP16, board.GP17, board.GP18, board.GP19, board.GP20, board.GP21, board.GP22, board.GP26, board.GP27, board.GP28]

keycodes = [None, None, Keycode.Q, Keycode.W, Keycode.E, Keycode.R, Keycode.T, Keycode.U, Keycode.I, Keycode.O, Keycode.P, Keycode.LEFT_BRACKET, Keycode.A, Keycode.S, Keycode.D, Keycode.F, Keycode.G, Keycode.J, Keycode.K, Keycode.L, Keycode.SEMICOLON, Keycode.QUOTE, Keycode.C, Keycode.V, Keycode.N, Keycode.M]

touch_objs = []

for i in range(26):
    touch_objs.append(touchio.TouchIn(pins[i]))

time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)  # We're in the US :)

keyStates = []
for i in range(26):
    keyStates.append(False)

buttonStates = []

for i in range(26):
    buttonStates.append(deque())
    for  j in range(3):
        buttonStates[i].append(0)

while True:
    for i in range(26):
        if touch_objs[i].value:
            print("key", i, "touched")

        buttonStates[i].append(touch_objs[i].value)
        buttonStates[i].popleft()
    time.sleep(0.05)
