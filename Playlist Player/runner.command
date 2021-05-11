#!/bin/bash

cd "`dirname "$0"`"
python ./player.py
pkill -f playmidi-single