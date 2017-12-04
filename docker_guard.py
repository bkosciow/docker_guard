import docker
import json

BANNED_PORTS = [
	'3306/tcp', '9200/tcp', '5601/tcp'
]
CLIENT = docker.from_env()

def decode(e):
	try:
		message = json.loads(e)
	except ValueError:
		message = None
		
	return message

def validate_ports(container):
	for port in BANNED_PORTS:
		if container.attrs['NetworkSettings'] id not None and
		 container.attrs['NetworkSettings']['Ports'] is not None and
		 port in container.attrs['NetworkSettings']['Ports'] and 
		 container.attrs['NetworkSettings']['Ports'][port] is not None:
			print("Port {} exposed on {}".format(port, container.name))
			print(container.attrs['NetworkSettings']['Ports'])
			print ("\n");
			container.stop()


def run_listener():
	for event in CLIENT.events():
		event = decode(event.decode())
		if event is not None and event['Type'] == 'container' and event['Action'] == 'start':
			id = event['id']
			c = CLIENT.containers.get(id)
			validate_ports(c)

def run_check():
	for container in CLIENT.containers.list():
		validate_ports(container)
		
run_check()
run_listener()
