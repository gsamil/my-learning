# Portainer

## Installation

### docker-compose.yml file

create this dir : `/opt/app_data/portainer`

```jsx
version: '3.1'

services:
  s_portainer:
    container_name: c_portainer
    image: portainer/portainer-ce
    ports:
      - 9443:9443
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - /opt/app_data/portainer:/data
```

Then

```jsx
docker-compose up -d
```

### Reference Video:

[Docker Portainer Kurulumu | Portainer   #15](https://youtu.be/nk24fldHnC0?list=PLRp4oRsit1bzGGClDYCplnGKYI6p-dDE1)
