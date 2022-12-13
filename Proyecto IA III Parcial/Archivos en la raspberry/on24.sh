#!/bin/bash
echo 19 > /sys/class/gpio/export
echo out > /sys/class/gpio/gpio19/direction
echo 1 > /sys/class/gpio/gpio19/value

