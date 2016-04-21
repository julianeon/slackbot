## Synopsis

This standup bot is meant to be used with teams. It can be used as a 'virtual standup' bot, either to supplement or replace regular standups.

The bot goes through the users listed sequentially. If a user takes longer than the MAXIMUM_WAIT_TIME, it skips them. All the user updates are collated and printed to the designated room as the standup update. The time between the time you start the bot and the update to the room, then, depends roughly on how long people take to respond. Generally, for 3-4 few users, it will take 10-15 mins before the update hits the room.

Before a bot can speak to any user, the user must initiate a conversation with the bot; this only has to be done 1 time. The user can click on your bot and say anything (such as "hi") to satisfy this requirement.

## Explanation

You'll need to customize the constants to work with your team and Slack setup. At a minimum, you'll need to add your Slack token allowing your bot to post to your company's slack rooms.

For user ID's and DM channel ID's, you can use Slack's API tester. Search for the corresponding method, take the resulting URL and open it in your browser, and search for the terms you need (username, room name, etc.) For room names, you'll need either channels.list or groups.list, depending on whether it's a public or private room, respectively.

Add those ID's to the slack.yaml file using the format shown there, and the bot will be able to pull them from there going forward.

I usually run my bot script as a cronjob.

## Motivation

This is meant to be a template that other people can adapt and use to build their own bots.

## Installation

You'll need Python as this is a Python script.

Install the Slack client using:

pip install slackclient

Install yaml using:

pip install pyyaml

## Contributors

Created by Julian Martinez. Email questions or comments to julianeon@yahoo.com.

## License

The MIT License

Copyright (c) 2016 Julian Martinez julianeon@yahoo.com

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
