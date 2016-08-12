#!/bin/bash
# Data Slam Script v0.1
# User define Function (UDF)
LogLine(){
  query="insert into state (id, location, timestamp, temperature, pressure, altitude, humidity) values (NULL, 'valhala', `date +%s`, ${line}"
  echo $query
  sqlite3 arduino.db3 "insert into state (id, location, timestamp, temperature, pressure, altitude, humidity) values (NULL, 'valhala', `date +%s`, ${line}"
}
### Main script stars here ###
# Store file name
FILE=""

# Make sure we get file name as command line argument
# Else read it from standard input device
stty -f /dev/cu.usbmodem1411 cs8 9600 ignbrk -brkint -icrnl -imaxbel -opost -onlcr -isig -icanon -iexten -echo -echoe -echok -echoctl -echoke noflsh -ixon -crtscts
if [ "$1" == "" ]; then
   FILE="/dev/cu.usbmodem1411"
else
   FILE="$1"
   # make sure file (serial device) exist and is readable
   if [ ! -f $FILE ]; then
  	echo "$FILE : does not exists"
  	exit 1
   elif [ ! -r $FILE ]; then
  	echo "$FILE: can not read"
  	exit 2
   fi
fi
# Create Database if it does not exist

if [ ! -f "stuffly.db" ]; then
  	echo "Creating database"
        sqlite3 arduino.db3 "CREATE TABLE state (id	INTEGER PRIMARY KEY AUTOINCREMENT, humidity	REAL, temperature	REAL, pressure	REAL, altitude	REAL, location TEXT, timestamp INTEGER);"
fi
exec 3<&0
exec 0<"$FILE"
while true
do

	# use $line variable to process line in processLine() function
	while read -r line
        do
              LogLine $line
        done
       usleep 50000 # This delay can be changed to match the delay of the Arduino
done
exec 0<&3
exit 0
