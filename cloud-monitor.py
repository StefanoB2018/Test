import json
import time
import requests as req
from requests import get
from discord_webhook import DiscordEmbed, DiscordWebhook
import os

URL = 'https://discord.com/api/webhooks/1104425166366318724/sNM2A81tQdaboLkFlDvRlH8dMsL6RG66dTzAxHHM53IoVakCAKRdcK_dnDgoHAEBd8Cx'
keys = ['allPlayerList','winPlayerList','mapName','playerData','replayName']
beforeKeys = ["**Players:**\n","**Winners:**\n","**Chosen Map:**\n","**Player Stats:**\n","\n**Replay Name:**\n"]
count = 0
while True:
    try: 
        r = get('http://localhost:5000/api/get/event/GameOver')
        count += 1
        print("Get #" + str(count))
        response = r.text
        data = json.loads(response)
        s = ""
        data = json.loads(data[0])
        print(data, type(data))
        matchData = data['gameOverData']
        matchTime = str(data['gameTime'])
        replay = matchData['replayName']
        nomemappa = matchData['mapName']
        nomemappa = nomemappa.replace('_',' ')
        path = os.path.join(os.getcwd()+'/RW-HPS-2.1.0-M1/StartServer/data/replays/',replay)
        
        for i in range(len(keys)):
            if(i != 3):
                s += beforeKeys[i] 
                temp = matchData[keys[i]]
                if(i == 2 or i == 4):
                        s += '`' 
                for t in temp:
                    if(i != 2 and i != 4):
                        s += '`' 
                    s += str(t)
                    if(i != 2 and i != 4):
                        s += "`\n"
                if(i == 2 or i == 4):
                        s += '`' 
        s += '\n**Game time:**\n`'+ matchTime + 's`'
        print(s)
        payout ={
            'content': s
        }
        #req.post(URL,data=payout)
        time.sleep(10)
        webhook = DiscordWebhook(url=URL)
        
        f = open(path, "rb")
        embed = DiscordEmbed(title= nomemappa, description=s, color='03b2f8')
        webhook.add_embed(embed)
        webhook.add_file(file=f.read(), filename=replay)
        response = webhook.execute(remove_embeds=True, remove_files= True)
        f.close()
        time.sleep(2)
    except Exception as e:
        print("Empty")
        time.sleep(5)