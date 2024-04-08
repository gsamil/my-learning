# Gitlab CI/CD

## Gitlab Runner Configuration

### install gitlab runner to linux

[Install GitLab Runner manually on GNU/Linux | GitLab](https://docs.gitlab.com/runner/install/linux-manually.html)

### register a runner in linux

[Registering runners | GitLab](https://docs.gitlab.com/runner/register/index.html)

### after registration is complete

```jsx
sudo gitlab-runner verify
sudo gitlab-runner run
```

### install docker to ubuntu

[How To Install and Use Docker on Ubuntu 22.04  | DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-22-04)

### How to delete a gitlab-runner

[How do I delete/unregister a GitLab runner](https://stackoverflow.com/questions/66616014/how-do-i-delete-unregister-a-gitlab-runner)

    💡 If you change a runner, don’t forget to update tags on gitlab-ci.yml file

### References

- This is the tutorial I followed : [Gitlab CI/CD for Docker, Python Flask, AWS ECS Dev Ops | Gitlab CI/CD Docker Deployment on AWS ECS](https://youtu.be/vb7w7jnkD2s) (This is all the information you need to deploy a python app to a server with gitlab ci/cd)

- [GITLAB CI CD FULL COURSE IN 3 HOURS  | Gitlab CI CD From Zero To Hero](https://youtu.be/Typ9U6k6g5s?list=PLVx1qovxj-am2q9M8mC2CmMUfrxZGoZ9J)
