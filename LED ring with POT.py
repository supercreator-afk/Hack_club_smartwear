import machine
import neopixel
import time

#setup

num_leds = 16
data_pin = 0
np = neopixel.NeoPixel(machine.Pin(data_pin), num_leds)

#main

pot = machine.ADC(26)

while True:
    raw = pot.read_u16()
    brightness = int((raw / 65535) * 255)

    for i in range(num_leds):
        np[i] = (brightness, brightness, brightness)  # white
    np.write()

    time.sleep(0.05)
