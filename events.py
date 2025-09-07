import docker

client = docker.DockerClient(base_url='npipe:////./pipe/docker_engine')

for event in client.events(decode=True):
    print(event)
