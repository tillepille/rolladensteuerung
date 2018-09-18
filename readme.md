# Python HomeKit Shutter API

- Control a shutter or similar wich has a motor with two power lines with GPIO of a RaspberryPi
- Made to use with [homebridge](https://github.com/nfarina/homebridge/) and HTTP Plugins like [this](https://github.com/jeffreylanters/homebridge-http-window-covering)
- runs on Port 5000 (Flask default)
- mini-minimal web frontend (with [jquery](https://jquery.com))
- very minimal, not tested, no safety built-in
---
## Prerequisites
1. RaspberryPi with GPIO and Network
2. 1-2 relays, some jumper cables
3. Python with Flask installed ( `pip install flask` )
4. experience with working on high currents!


## What it can do

- Up
- Down
- Get Status (up / down as plain text)
- everythig between 0 and 100%
    - you have to get the factor for calculating the time for waiting by yourself, guessing is the only way at the moment

