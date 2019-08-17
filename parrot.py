import os
import json
from groupy.client import Client
from groupy import attachments
from flask import Flask, request
from groups import peeps



token = os.environ['gm_key']
client = Client.from_token(token)
bot_id = os.environ['bot_id']

app = Flask(__name__)
@app.route('/', methods=['POST'])
def post():
        data = request.get_json()
        gID = data['group_id']
        bot = bot_id
        group = client.groups.get(gID)
        msg = data['text']
        if data['sender_type'] != 'bot':
                if '@all' in msg:
                        at_all(bot, group)
        return "ok", 200

def at_all(bot, group):  ##sends mention to all members of group
        members = group.members
        user_ids = []
        loci = []
        text = ""
        pnt = 0

        for m in members:
                id = m.data['user_id']  ## pulls all user IDs
                name = "@" + m.data["nickname"] + " "  ##creats text variable for each member

                user_ids.append(id)  ## adds user to list

                n = [pnt, len(name)]  ## loci list of member
                loci.append(n) ## adds member and loci to list
                pnt += len(name)  ## goes to next available point in loci

                text += name  ## text variable added to list

        mention = {}  ## creates mention dictionary with userID as the key and loci as the value
        mention["user_ids"] = user_ids
        mention["loci"] = loci
        tag = attachments.Mentions(mention['loci'], mention['user_ids'])  ## creates mention attachments
