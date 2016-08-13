# Stuffly
Stuffly is an IoT app built during the Andela IoT Hackathon. It basically gives real time updates on temperature, humidity and air-pressure for a particular room. Through this, we can determine if a room is stuffy or not &mdash; hence the name **stuff**ly.

We've currently built a client Slack bot for Andela Slack Org which called _@stuffly_ through which you can interact with the IoT app.

## Schematic Diagram
Simple digram explaining our setup:

![stuffly-dgm-01](https://cloud.githubusercontent.com/assets/13568167/17643990/5cee937c-6183-11e6-8523-45bae93f9180.png)

## Setting Up Arduino

Download and install Arduino IDE for mac [here](https://www.arduino.cc/en/Main/Software).
This adds an Arduino directory (referred to as a sketchbook) into your Documents folder.
Go into libraries folder and clone the BME280 libraries

## Setting up BM8 libraries

Clone the BME280 repositories to your the sketchbook libraries directory.

```bash
cd Arduino/libraries

git clone git@github.com:adafruit/Adafruit_BME280_Library.git

git clone git@github.com:adafruit/Adafruit_Sensor.git
```



## Connect the board

The Arduino Uno, and Mega automatically draw power from either the USB connection to the computer or an external power supply. The power source is selected with a jumper, a small piece of plastic that fits onto two of the three pins between the USB and power jacks. Check that it's on the two pins closest to the USB port.

Connect the Arduino board to your computer using the USB cable. The green power LED (labelled PWR) should go on.

## Select the board
You'll need to select the entry in the Tools > Board menu that corresponds to your Arduino.

## Select your Serial Port

Select the serial device of the Arduino board from the Tools > Serial Port menu. On the Mac, this should be something with /dev/tty.usbmodem (for the Uno or Mega 2560) or /dev/tty.usbserial (for older boards) in it.

## Clone the Stuffly repo

Run this to clone the stuffly repo

```bash
git clone https://github.com/andela-anandaa/stuffly.git
```

Make the `read_arduino.sh` bash file executable
```bash
chmod u+x stuffly/arduino/read_arduino.sh
```

## Upload the sensor to the arduino board
Open `stuffly/arduino/arduino.ino` on the arduino IDE and click upload to push it on to the board.

Run `./read_arduino.sh` to read the temperature, humidity, air pressure levels to an sqlite database.


# Slack Bot

## Usage
You can send the following messages to @stuffly bot to get the states of various rooms:

- Is [room] stuffy?
- What is the temperature at [room]?
- What is the humidity at [room]?



## Dev
We are using the [slackbot] Python library.

`slackbot_settings.py` is excluded because of obscuring the `API_TOKEN`. However, this is the format:

```
API_TOKEN = "xoxb-xxxxxxxx"

PLUGINS = [
    'slackbot.plugins',
    'mybot.plugins'
]
```

# Credits
Big shout out to the _HackHeads_ team:

- [@andela-emabishi](https://github.com/andela-emabishi) (Team Lead)
- [@johnkariuki](https://github.com/johnkariuki)
- [@bernard-kanyolo](https://github.com/bernard-kanyolo)
- [@andela-anandaa](https://github.com/andela-anandaa)
