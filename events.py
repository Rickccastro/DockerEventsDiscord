import docker
import datetime

client = docker.DockerClient(base_url='npipe:////./pipe/docker_engine')

for event in client.events(decode=True,filters = {"event": "die"}):
    container_id = event["id"]
    container_name = event["Actor"]["Attributes"]["name"]
    epoch_time = event["time"]  
    date_time = datetime.datetime.fromtimestamp(epoch_time)
    print("O container,%s (%s) foi finalizado às %s" % (container_name, container_id, date_time))
