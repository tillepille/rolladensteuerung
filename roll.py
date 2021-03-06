#!flask/bin/python
# GPIO
from gpiozero import LED
from time import sleep
# REST
from flask import Flask, send_from_directory, jsonify

import config

rollade = LED(config.rollPin)
stopper = LED(config.stopperPin)

app = Flask(__name__)

#    rollade.off means its max up
#    rollade.on means its down completely
#    stop() cuts power on both sides, so its stopping
#    stopper.on is active stopping
#    stopper.off is essential for normal use

# init
stopper.off()
rollade.off()
currentHeight = 100
lastHeight = 100

def up():
    global currentHeight
    stopper.off()
    rollade.off()
    currentHeight = 100

def down():
    global currentHeight
    stopper.off()
    rollade.on()
    currentHeight = 0
    
# These factors are to edit by yourself in the config.py
def calculateDown(time):
    return time * config.downFactor

def calculateUp(time):
    if lastHeight == 0:
        return ((time * config.upFactor) + config.waitFromBottom)
    else:
        return time * config.upFactor

def goUpFor(percent):
    stopper.off()
    rollade.off()
    howLong = calculateUp(percent)
    print("goUpFor: " + str(howLong))
    sleep(howLong)
    stopper.on()

def goDownFor(percent):
    stopper.off()
    rollade.on()
    howLong = calculateDown(percent)
    print("goDownFor: " + str(howLong))
    sleep(howLong)
    stopper.on()

# routes for the webUI
@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/up')
def rollUp():
    up()
    return jsonify(position=currentHeight)

@app.route('/down')
def rollDown():
    down()
    return jsonify(position=currentHeight)

@app.route('/stop')
def stopRolling():
    stopper.on()
    return "stopped"

@app.route('/status')
def status():
    return jsonify(position=currentHeight)

# for homebridge / homekit integration
@app.route('/height/<int:des>')
def set_height(des):
    global currentHeight
    global lastHeight

    travel = int(abs(currentHeight - des))
    lastHeight = currentHeight
    currentHeight = des
    print("bisher: " + str(lastHeight) + " desired: " + str(currentHeight))
    print("ziel: " + str(des))
    if des == 100:
        up()
    elif des == 0:
        down()
    elif lastHeight < des:
        goUpFor(travel)
    else:
        goDownFor(travel)
    return jsonify(position=currentHeight)


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', threaded=False)
