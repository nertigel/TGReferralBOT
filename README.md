# TGReferralBOT for Telegram
This is a telegram token-bot based off the [Pyrogram](https://github.com/pyrogram/pyrogram) library in Python3. 
The bot allows to you to pass/refer people to your telegram user_id using an attached button without the need of a username.

# How it works

After sending `/start` to the bot, it should respond to you with a message containing a button which on press navigates to the `user_id` that was set in the `data.json` file.

# Installation

You can run this bot on your own, install the required lib by running this command: 

```bash
pip install pyrogram
```

# Configuration (data.json)

In the `data.json` file you will find `api_id` and `api_hash` variables, get your [API credentials from Telegram's official website](https://my.telegram.org/auth).
Change the `referal_user_id` variable to your desired user_id that you would like to be used for the button linking.

Now you can simply run the bot by running `main.py`
