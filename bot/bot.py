import re
import random as rand

# from slacker import Slacker

from slackbot.bot import Bot
from slackbot.bot import respond_to, listen_to, default_reply

import bot_methods as bm


sample_data = {
    'temp': 20,
    'humidity': 67,
    'air_pressure': 30
}

# default replies
dr = [
    'Hey, I\'m Stuffly, I can help you know if a room is stuffy',
    'You know I\'m in private beta, I might not answer all of your questions :)',
    'Ask on Zhishi :-D',
    'Ask me, "what\'s the temperature?" I\'ll tell you :)'
]

def main():
    bot = Bot()
    bot.run()

@respond_to('sup', re.IGNORECASE)
@listen_to('sup', re.IGNORECASE)
def hi(message):
    message.reply('I think you are greeting me, hi :-)')
    # message.react('+1')

@respond_to('what\'s the temperature', re.IGNORECASE)
@respond_to('temperature', re.IGNORECASE)
@respond_to('temp', re.IGNORECASE)
def temp(message):
    message.reply('The temperature now is {}'.format(sample_data['temp']))
    # message.react('+1')

@default_reply
def my_default_hanlder(message):
    message.reply(dr[rand.randrange(0, len(dr))])

if __name__ == "__main__":
    print "==> I'm up and running :-D"
    main()
