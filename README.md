## Python Slackbot

This is old code that worked circa 2016 but works no longer. I keep it here for archival purposes, and to show Python code I wrote. It's also the most popular repo I've created. My other recent Python repo is [useful-python-scripts](https://github.com/julianeon/useful-python-scripts).

Original text below.

This standup bot is meant to be used with teams. It can be used as a 'virtual standup' bot, either to supplement or replace regular standups.

The bot goes through the users listed sequentially. If a user takes longer than the MAXIMUM_WAIT_TIME, it skips them. All the user updates are collated and printed to the designated room as the standup update. The time between the time you start the bot and the update to the room, then, depends roughly on how long people take to respond. Generally, for 3-4 few users, it will take 10-15 mins before the update hits the room.

Before a bot can speak to any user, the user must initiate a conversation with the bot; this only has to be done 1 time. The user can click on your bot and say anything (such as "hi") to satisfy this requirement.

## Explanation

You'll need to customize the constants to work with your team and Slack setup. At a minimum, you'll need to add your Slack token allowing your bot to post to your company's slack rooms.

For user ID's and DM channel ID's, you can use Slack's API tester. Search for the corresponding method, take the resulting URL and open it in your browser, and search for the terms you need (username, room name, etc.) For room names, you'll need either channels.list or groups.list, depending on whether it's a public or private room, respectively.

Add those ID's to the slack.yaml file using the format shown there, and the bot will be able to pull them from there going forward.

I usually run my bot script as a cronjob.

## Purpose

This is meant to be used as a template for other people to adapt and use to build their own bots.

## Installation

You'll need Python as this is a Python script.

Install the Slack client using:

pip install slackclient

Install yaml using:

pip install pyyaml

## License

MIT License

