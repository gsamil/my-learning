# Container Registry

### What are Container Registries?

- Central repositories for container images
- Private or/or public
- Docker Hub : hub.docker.com
- Microsoft
  - Azure Container Registry
  - Microsoft Container Registry (public images) : mcr.microsoft.com
- Amazon Elastic Container Registry
- Google Container Registry

### Publish to Docker Hub

```bash
# login to Docker Hub
docker login -u <username> -p <password>

# tag the image previously built
docker tag my_image k8sacademy/my_image:latest

# push the image
docker push k8sacademy/my_image:latest

# pull the image
docker pull k8sacademy/my_image:latest
```

See [L10-03 Push Express site to Docker Hub](https://github.com/K8sAcademy/Fundamentals-HandsOn/blob/main/L10-03%20Push%20Express%20site%20to%20Docker%20Hub/Readme.md) for more details.

