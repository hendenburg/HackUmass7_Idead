#!bin/bash

if ls /dev/ | grep tty.usbmodem*
then
    echo The arduino is on.
fi