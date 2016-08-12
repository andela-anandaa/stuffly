import re

from slacker import Slacker

from slackbot.bot import Bot
from slackbot.bot import respond_to, listen_to

import bot_methods as bm

slack = Slacker('xoxb-22328931106-tACwqKP1LwOuwfvGcYD9qHyP')

sample_data = {
    'temp': 20,
    'humidity': 67,
    'air_pressure': 30
}

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


if __name__ == "__main__":
    print "==> I'm up and running :-D"
    main()
