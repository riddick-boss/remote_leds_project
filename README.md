# Remote leds project
#### Control leds by mobile app or by voice commands :rotating_light:

## General info
A project to use a mobile app and speech recognition to control, in this case, led lights (but it could be anything else - oven temperature, garage door, etc . . .  smart home in general).

This repo contains source code for Arduino, server and speech recognition functionality.

If you want to know more about mobile app contact me via Kremienowski33@gmail.com.

Python 3.6 recommended, but works fine on 3.9.

## Required Python packages installation

Install PyAudio:

- on Linux: ``` sudo apt install python3-pyaudio ```
- on Windows: ``` python -m pip install pyaudio ```
- on Mac: ``` brew install portaudio && pip install pyaudio ```

and then:

``` pip install -r requirements.txt ```

## Run with:

``` python3 launcher.py ``` 
from controls/ dir