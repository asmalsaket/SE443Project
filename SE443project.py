#Asma Alsaket
#201306
import time
import docker

# Initialize Docker client
client = docker.from_env()

# Initialize single-node Docker
Swarm swarm = client.swarm.init() print("Docker Swarm initialized with ID:",swarm.id)
print("Docker Swarm name:", swarm.name)
print("Docker Swarm creation date:", swarm.attrs["CreatedAt"])

# Create overlay network
network = client.networks.create("se443_test_net", driver="overlay", scope="global", subnet="10.10.10.0/24")
print("Docker network created with ID:",network.id)
print("Docker network name:",network.name)
print("Docker network creation date:", network.attrs["CreatedAt"])

# Deploy broker service 
service = client.services.create("eclipse-mosquitto",name="broker",replicas = 3 ,restart policy={"Name": "always").networks=[network],
print("Broker service deployed with ID:"service.id)
print("Broker service name:",service.name)
print("Broker service replicas:", service.attrs["Spec"]["Mode"] ["Replicated"]["Replicas"])

# Deploy subscriber service 
service = client.services.create("efrecon/mqtt-client", name="subscriber",replicas = 3 ,restart_policy={"Name": "always"}, networks=[network],) 
print("Subscriber service deployed with ID:", service.id)
print("Subscriber service name:",service.name)
print("Subscriber service replicas:", service.attrs["Spec"]["Mode"] ["Replicated"]["Replicas"])

# Deploy publisher service 
service = client.services.create("efrecon/mqtt-client",name="publisher",replicas=3,restart_policy={"Name": "always"},networks=[network],ID:", service.id)
print("Publisher service name:",service.name)
print("Publisher service replicas:", service.attrs["Spec"]["Mode"]["Replicated"]["Replicas"])


# shut down and clean up
client.services.get("subscriber").remove()
print("\nSubs deleted")


client.services.get("publisher").remove()
print("\nPubl deleted ")




client.services.get("broker").remove()
print("\nBroker deleted")


client.networks.get("se443_test_net").remove()
print("\nNetwork deleted")



client.swarm.leave(force=True)
print("\nswarm deleted")