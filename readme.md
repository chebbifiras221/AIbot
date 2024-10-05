# Gemini Discord Bot
If you would like to try out this bot replace the variables inside of `config.ini` with your own discord id, discord sdk, and gemini sdk values.

## Google Gemini
https://ai.google.dev/ 

#### Pricing: https://ai.google.dev/pricing

#### Create API Key: https://aistudio.google.com/app/apikey

#### Google Gemini Docs: https://ai.google.dev/docs

Gemini Python Quick Start: \
https://ai.google.dev/tutorials/python_quickstart

```bash
pip install -q -U google-generativeai
```


## Installing discory.py library
Before we can make any bots, we first have to install the discord.py library. Here's how to do that:

Discord developer portal: \
https://discord.com/developers/applications

### On Windows:

Open up your Command Prompt (go the Windows Search Bar and type in "cmd")

Type in this command: 

```bash
py -3 -m pip install -U discord.py[voice]
```

if that doesn't work, try 
```bash
pip install -U discord.py[voice]
```

## Discord developer setup
discord developer portal: https://discord.com/developers/applications \
create `New Application` \
after applicaiton is created go to `Bot` tab and `Reset Token`

After the token is reset go to the `OAuth2` -> `URL Generator` tab and select the following Scopes and Bot Permissions:

Scopes:

- bot

Bot Permissions:
    
- Administrator

Generate the url

Invite bot to server.