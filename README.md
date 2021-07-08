# Discord-Message-Live-Feed

### Discord Message Live Feed is a program that uses the Twitter and Discord APIs, to keep a Twitter account updated live of all messages sent on a Discord server.

## How to use

### 1. Set up a Twitter developer account
Firstly, if you haven't already, register a Twitter acount on https://twitter.com.
Secondly, apply for a Twitter developer account on https://developer.twitter.com/en/apply-for-access.

### 2. Create a Twitter API project
Create a Twitter API project (and app, in the project) on https://developer.twitter.com/en/portal/dashboard.

### 3. Create a Discord bot
If you don't already have a Discord account, go create on at https://discord.com. If (or when) you have an account, go to https://discord.com/developers/applications and create a new application. Go to the 'Bot' settings tab and click 'Add Bot'.
After you've created the bot, go to the 'OAuth2' settings tab and select 'bot' in 'Scopes'. Then, copy the link underneath, it looks something like this: https://discord.com/api/oauth2/authorize?client_id=xxxxxxxxxxxxxxxxxx&permissions=0&scope=bot. Use the link you copied to invite the bot to your Discord server. It needs no permissions, except being able to read messages.

### 4. Set up the program
Download the code, and input the token from the Discord application's 'Bot' settings tab and your Twitter project keys (to obtain your Twitter project keys go to the project settings tab, and click the key besides your app) into the auth.py file.

### 5. Run the program
Make sure you have Python 3.x installed, preferably the latest version - https://www.python.org/. If they're not already installed, install the following pip libraries:

| Library | PyPI                                 | Website                              |
| ------- | ------------------------------------ | ------------------------------------ |
| tweepy  | https://pypi.org/project/tweepy/     | https://www.tweepy.org/              |
| discord | https://pypi.org/project/discord.py/ | https://github.com/Rapptz/discord.py |
| pytz    | https://pypi.org/project/pytz        | https://pythonhosted.org/pytz/       |

At last, run the MLF.py file using Python and watch the magic happen!
