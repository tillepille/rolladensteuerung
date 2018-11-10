# Python HomeKit Shutter API

- Control a shutter or similar wich has a motor with two power lines with GPIO of a RaspberryPi
- Made to use with [homebridge](https://github.com/nfarina/homebridge/) and HTTP Plugins like [this](https://github.com/jeffreylanters/homebridge-http-window-covering)
- runs on Port 5000 (Flask default)
- mini-minimal web frontend (with [jquery](https://jquery.com))
---
## Prerequisites
1. RaspberryPi with GPIO and Network
2. 2 relays, 4 jumper cables
3. Python with Flask and gpiozero installed ( `pip install flask gpiozero` )
4. **experience with working on high currents!**


## What it can do

- Up (also via frontend)
- Down (also via frontend)
- Get Status (0-100 as plain text)
- everythig between 0 and 100%
    - you have to get the factor for calculating the time for waiting by yourself, trial & error is the only way

## To Do
- nice Frontend
- Wiring sketch
