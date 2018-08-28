# An SMS responder bot

Currently has backends for Nexmo, Jasmin coming soon.

## Overview
`main.py` contains a Flask web service which implements a 'webhook' for SMS delivery services, such as Nexmo.
Incoming messages are passed to the bot modules in `/bots` to generate replies.

Have a look at [`bots/basebot.py`](bots/basebot.py) for a skeleton bot class with explanatory comments, and [`bots/storiesbot/py`](bots/storiesbot/py) for an example working bot.
