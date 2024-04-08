# Observability

Pod Crash vs App Crash

## Probes

- Startup probes
  - To know when a container has started
- Readiness probes
  - To know when a container is ready to accept traffic
  - A failing readiness probe will stop the application from receiving traffic
- Liveness probes
  - Indicates whether the code is running or not
  - A failing liveness probe will restart the container

