#!flask/bin/python

# GPIO
from gpiozero import LED
from time import sleep
# REST
from flask import Flask, render_template, send_from_directory

rollade = LED(17)
stopper = LED(27)

app = Flask(__name__)
'''
    rollade.off means its max up
    rollade.on means its down completely

    stop() cuts power on both sides, so its stopping
    stopper.on is active stopping
    stopper.off is essential for normal "normal" use

'''
# init
stopper.off()
rollade.off()
currentHeight = 100
lastHeight = 100

def getStatus():
    return str(currentHeight)

def up():
    stopper.off()
    rollade.off()
    return "up() full"


def down():
    stopper.off()
    rollade.on()
    return "down() full"

# This factor is to edit by yourself
def calculateDown(time):
    return time * 0.1

def calculateUp(time):
    if lastHeight == 0:
        return ((time * 0.115) + 4)
    else:
        return time * 0.115

def goUpFor(percent):
    stopper.off()
    rollade.off()
    howLong = calculateUp(percent)
    print("goUpFor: "+str(howLong))
    sleep(howLong)
    stopper.on()

def goDownFor(percent):
    stopper.off()
    rollade.on()
    howLong = calculateDown(percent)
    print("goDownFor: "+str(howLong))
    sleep(howLong)
    stopper.on()


# routes for the webUI
@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')
#    return render_template("indexOLD.html")

@app.route('/up')
def rollUp():
    return up()

@app.route('/down')
def rollDown():
    return down()

@app.route('/stop')
def stopRolling():
    stopper.on()
    return "stopped"

@app.route('/status')
def status():
    return getStatus()

# for homebridge / homekit integration
@app.route('/height/<int:des>')
def set_height(des):
    global currentHeight
    global lastHeight

    travel = int(abs(currentHeight - des))
    lastHeight = currentHeight
    currentHeight = des

    print(str(lastHeight)+" "+str(currentHeight)+" bisher : desired")

    if des == 100:
        print("completely up")
        return up()
    if des == 0:
        print("completely down")
        return down()
    if lastHeight < des:
        goUpFor(travel)
        return str(travel)
    else:
        goDownFor(travel)
        return str(travel)

if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0')
