#!/bin/bash
masa="`date +%k:%M`"
mp3="$HOME/Music/Annoying_Alarm_Clock.wav" #change this
if [ $# != 1 ]; then
 echo "please insert alarm time [24hours format]"
 echo "example ./alarm 13:00 [will ring alarm at 1:00pm]"
 echo "example ./alarm 01:00 [will ring alarm at 1:00am]"
 exit;
fi

alarm=$1

#fix me with better regex >_<
#if [[ "$alarm" =~ ^[1-2]?[0-9]\:[0-5][0-9]$ ]]; then
if [[ "$alarm" =~ ^[0-2][0-9]\:[0-5][0-9]$ ]]; then
 echo "time now $masa"
 echo "alarm set to $alarm"
 echo "will play $mp3"
else
 echo "invalid clock format"
 echo "use HH:MM"
 exit;
fi

while [ $masa != $alarm ];do
#sleep 1 #wait 1 second
 masa="`date +%k:%M`" #update time
 sleep 1 #dont overload the cpu cycle
done

echo $masa
if [ $masa = $alarm ];then
 echo ringggggggg
 play $mp3 > /dev/null 2> /dev/null &
fi
exit