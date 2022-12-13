#!/bin/bash
echo 6 > /sys/class/gpio/export
echo out > /sys/class/gpio/gpio6/direction
echo 1 > /sys/class/gpio/gpio6/value

