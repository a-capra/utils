#!/bin/bash

mp3="$HOME/Music/Annoying_Alarm_Clock.wav" #change this
echo play $mp3 > /tmp/.myjob
more /tmp/.myjob

at 7:30 -f /tmp/.myjob

rm /tmp/.myjob