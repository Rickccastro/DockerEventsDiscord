import docker
import datetime
import requests
import os
from dotenv import load_dotenv

load_dotenv()

discord_url = os.getenv("DISCORD_URL")



client = docker.DockerClient(base_url='npipe:////./pipe/docker_engine')
webhook_url = discord_url

for event in client.events(decode=True,filters = {"event": "die"}):
    container_id = event["id"]
    container_name = event["Actor"]["Attributes"]["name"]
    epoch_time = event["time"]  
    date_time = datetime.datetime.fromtimestamp(epoch_time)  

    payload = {"content": "O container %s (%s) foi finalizado às %s" % (container_name, container_id, date_time)}

    print (payload)
    requests.post(webhook_url, data=payload)







  

