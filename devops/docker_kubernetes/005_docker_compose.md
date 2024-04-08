# Docker Compose

- Define and run multi-containers applications
- Define using YAML files
- Run using the docker CLI with the compose plugin
  - Docker compose
- Compose Specs
  - https://compose-spec.io

### Compose V2

- GA at DockerCon Live 2022
- Incorporates the docker compose command into the Docker CLI
  - You type docker compose instead of docker compose
  - Drop-in replacement for docker compose
  - docker compose commands maps directly to the docker compose ones
- Installed with Docker Desktop
  - Linux: apt-get install docker compose-plugin
- Written in Go
  - docker compose is written in Python
- In summary, it's simply a faster version of the good old docker compose tool that is shipped as a plugin instead of a Python app


### Use Cases

- Workloads that don't require a full orchestrator
- Development and tests
- Use of a service that can run Docker Compose files
  - Azure App Service
  - AWS ECS
  - Virtual machines

### Docker Compose Cheat Sheet

```bash
docker compose build                  # Build the images
docker compose start                  # Start the containers
docker compose stop                   # Stop the containers
docker compose up -d                  # Build and start
docker compose ps                     # List what's running
docker compose rm                     # Remove from memory
docker compose down                   # Stop and remove
docker compose logs                   # Get the logs
docker compose exec [container] bash  # Run a command in a container
```

### Compose V2 - New Commands

```bash
docker compose --project-name test1 up -d               # Run an instance as a project
docker compose -p test2 up -d                           # Shortcut
docker compose ls                                       # List running projects
docker compose cp [containerID]:[SRC_PATH] [DEST_PATH]  # Copy files from the container
docker compose cp [SRC_PATH] [containerID]:[DEST_PATH]  # Copy files to the container
```

### Example

```bash
# build the service
docker compose build

# builds, (re)creates, starts, attaches to containers for a service
docker compose up

# list the services
docker compose ps

# bring down what was created by UP
docker compose down
```

See [L09-04 Docker Compose](https://github.com/K8sAcademy/Fundamentals-HandsOn/blob/main/L09-04%20Docker%20Compose/Readme.md) if you want to see a full example.

## Compose Features

### Resource Limits

```yaml
services:
  redis:
    image: redis:alpine
    deploy:
      resources:
        limits:
          cpus: '0.50'
          memory: 150M
        reservations:
          cpus: '0.25'
          memory: 20M
```

### Environment Variables

```yaml
services:
  web:
    image: nginx:alpine
    environment:
      - DEBUG=1
      - FOO=BAR
```

### Networking

```yaml
services:
  web:
    image: nginx:alpine
    ports:
      - "8080:80"
  db:
    image: postgres
    ports:
      - "5432"
```

```yaml
services:
  web:
    image: nginx:alpine
    networks:
      - frontend
  app:
    image: myapp
    networks:
      - frontend
      - backend
  db:
    image: postgres
    networks:
      - backend
      - frontend
    
networks:
  frontend:
  backend:
```

### Dependence

```yaml
services:
  web:
    build: .
    depends_on:
      - db
  db:
    image: postgres
```

### Volumes - Named

```yaml
services:
  app:
    image: myapp
    depends_on:
      - db
  db:
    image: postgres
    volumes:
      - db-data:/etc/data
    networks:
      - back-tier
volumes:
  db-data:
```

### Volumes - Anonymous

```yaml
services:
  app:
    image: myapp
    depends_on:
      - db
  db:
    image: postgres
    volumes:
      - ./db:/etc/data
    networks:
      - back-tier
```

### Restart Policy

```yaml
services:
  app:
    image: myapp
    restart: always
    depends_on:
      - db
  db:
    image: postgres
    restart: always
```

- по
  - The default restart policy.
  - Does not restart a container under any circumstances.
- always
  - Always restarts the container until its removal.
- on-failure
  - Restarts a container if the exit code indicates an error.
- unless-stopped
  - Restarts a container irrespective of the exit code but will stop restarting when the service is stopped or removed.

