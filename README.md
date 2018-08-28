# An SMS responder bot

Currently has backends for Nexmo, Jasmin coming soon.

## Overview
`app/main.py` contains a Flask web service which implements a 'webhook' for SMS delivery services, such as Nexmo.
Incoming messages are passed to the bot modules in `app/bots` to generate replies.

Have a look at [`app/bots/basebot.py`](app/bots/basebot.py) for a skeleton bot class with explanatory comments, and [`app/bots/storiesbot/py`](app/bots/storiesbot/py) for an example working bot.
