# Persisting Data

### Containers are ephemerous and stateless

- You usually don't store data in containers
- Non-persistent data
  - Locally on a writable layer
  - It's the default, just write to the filesystem
  - When containers are destroyed, so the data inside them
- Persistent data
  - Stored outside the container in a Volume
  - A volume is mapped to a logical folder

## Volumes

- Maps a folder on the host to a logical folder in the container

### Volumes Cheat Sheet

```bash
docker create volume [volumeName]    # Creates a new volume
docker volume inspect [volumeName]   # Display the volume info
docker volume ls                     # Lists the volumes
docker volume rm [volumeName]        # Deletes a volume
docker volume prune                  # Deletes all volumes not mounted
```

### Mapping a volume

```bash
# create a volume
docker volume create myvol

# inspect the volume
docker volume inspect myvol

# list the volumes
docker volume ls

# run a container with a volume
docker run -d --name devtest -v myvol:/app nginx:latest
```

### Mapping to a local folder

```bash
# run a container with a volume
docker run -d --name devtest -v d:/test:/app nginx:latest

# inspect the container
docker inspect devtest
```

### Mapping to a local folder - test

```bash
# Open a terminal and create a volume
docker volume create myvol

# List the volumes
docker volume ls

# Run a Nginx container that will use the volume
docker run -d --name voltest -v myvol:/app nginx:latest

# Connect to the instance
docker exec -it voltest bash

# Let’s create a file in the volume using Nano
apt-get update
apt-get install nano

# Create a file in the app folder
cd app
nano test.txt

# Type something, save the file and exit Nano using:
CTRL-O
CTRL-X

# Detach from the instance:
exit

# Stop and remove the container
docker stop voltest
docker rm voltest

# Run it again and see if the file still exists
docker run -d --name voltest -v myvol:/app nginx:latest
docker exec -it voltest bash
cd app
cat test.txt

# Cleanup
docker volume rm myvol
docker stop voltest
docker rm voltest
```