# gm_at_all
Python Flask framework for a groupme bot that tags all members in a given group

Procfile and Runtime is set for Heroku deployment.

Steps to run:
1) Create GroupMe Developer account and receive API token/key.
2) Create a bot to be used to tag all members. Add relevant webhook/callback url for GroupMe group where bot will be deployed.
3) Create Heroku instance (view Heroku site for detailed instruction. CLI is easiest in this case.)
4) Add API key and bot ID to Heroku env variables. In current code they are labeled 'gm_key' and 'bot_id'.
