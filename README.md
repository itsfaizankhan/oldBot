# (Deprecated) Discord Bot
This is my biggest bot so far and has most amount of features. It is tested on `Python 3.8.6` and hopefully runs on later versions as well.

I'm really new to this stuff so you might wanna puke after looking at the code.
Also feel free to steal it and make it your own! (Why am I even saying this. Those who wanna copy will copy anyways. LOL)

Note that `Procfile`, `requirements.txt` and `runtime.txt` are necessary if you're deploying the bot on Heroku.

# Installation
There isn't a lot that needs to be done. Make sure you have active internet connection.
I recommend using a virtual environment you wanna host it locally and then you can use the following command to install the dependencies.
```
pip install -r /path/to/requirements.txt
```
### Requirements

1. `discord.py-1.5.1`

2. `python-dotenv`

3. (OPTIONAL) `discord-pretty-help`

Replaces the default help command with a cool looking one.

Note: If you want the default help command or using your own custom one, then remove-

a. `help_command=PrettyHelp()` from `Bot()` in `main.py`.

b. `from pretty_help import PrettyHelp` in `main.py`.

## DO NOT REVEAL YOUR BOT TOKEN BY ANY MEANS
