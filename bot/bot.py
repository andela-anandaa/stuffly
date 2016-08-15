import re
import random as rand

# from slacker import Slacker

from slackbot.bot import Bot
from slackbot.bot import respond_to, listen_to, default_reply

import bot_methods as bm

# default replies
dr = [
    'Hey, I\'m Stuffly, I can help you know if a room is stuffy',
    'You know I\'m in private beta, I might not answer all of your questions :)',
    'BTW, did you attend the IoT hackathon? :)',
    'Ask me, "what\'s the temperature?" I\'ll tell you :)'
]

def main():
    bot = Bot()
    bot.run()

@respond_to('stuffy', re.IGNORECASE)
@listen_to('stuffy', re.IGNORECASE)
def hi(message):
    message.reply('I can tell you if a room is stuffy')

@respond_to('what is the temp[a-z]* .* (.*[^?])')
@listen_to('what is the temp[a-z]* .* (.*[^?])')
def temp(message, loc):
    _temp = bm.temperature(loc)
    if _temp:
        message.reply('The temperature at {} now is {} degrees Celsius'.format(loc, _temp))
    else:
        message.reply('We don\'t have a sensor currently at {}'.format(loc))

@respond_to('what is the humidity .* (.*[^?])', re.IGNORECASE)
@listen_to('what is the humidity .* (.*[^?])', re.IGNORECASE)
def humidity(message, loc):
    _humidity = bm.humidity(loc)
    if _humidity:
        message.reply('The humidity at {} now is {}%'.format(loc, _humidity))
    else:
        message.reply('We don\'t have a sensor at {}'.format(loc))

@respond_to('Is (.*) stuffy\[?]?', re.IGNORECASE)
@listen_to('Is (.*) stuffy\[?]?', re.IGNORECASE)
def stuffy(message, loc):
    st = bm.is_stuffy(loc)
    if st == True:
        message.reply('Yes, {} is stuffy :('.format(loc))
    elif st == False :
        message.reply('No, {} is okay :)'.format(loc))
    else:
        message.reply('We don\'t have a sensor at {}'.format(loc))

@default_reply
def my_default_hanlder(message):
    message.reply(dr[rand.randrange(0, len(dr))])

if __name__ == "__main__":
    print "==> I'm up and running :-D"
    main()
