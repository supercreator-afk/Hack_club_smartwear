Entry 1, May 24, 2025

Concept, glove or gloves with gyroscope, accelerometer, flex sensors, and maybe more

gloves will be the control input to a raspberry pi that will display information onto a small OLED screen and use a prism to reflect that into the eye
the oled will be able to display text and low res images, the hope is to have an ai who can provide short answers and maybe some basic games like pong
potential add ons, ai assistant, camera, microphone, speakers

how i will acheieve this,

for the gloves i will use an MPU6050 module for the gyroscope and accelerometer, 4.5 inch flex sensors for finger bend tracking, likely an ESP32 to connect it to a seperate unit where all the processing will happen
for the glasses i will use a .96 inch OLED display to display small text and use a prism setup(or something similar idk yet) to reflect the text into the glasses lens without obstructing the view



Entry 2, May 26, 2025

Ive begun working on a simple light to go on the gloves, its a ring of 16 RGBLEDs and the brightness is controlled by a potentiometer, might soon be changed to gesture control. 
schematic for the basic light will be found at https://i.postimg.cc/KYpGRGG2/Screenshot-2025-05-26-231923.png 
code will be found in /Glove_light_1_code
