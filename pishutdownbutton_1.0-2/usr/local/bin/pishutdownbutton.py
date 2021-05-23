#!/usr/bin/env python3

import RPi.GPIO as GPIO
import os
import glob
import subprocess

ioPin = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(ioPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.wait_for_edge(ioPin, GPIO.FALLING)

dir_path = os.path.dirname(os.path.realpath(__file__))
tasks = sorted(glob.glob(dir_path + "/pishutdownbutton.d/*.sh"))

for task in tasks:
    subprocess.call(task, shell=False)
