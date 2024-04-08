# Services

- We need to make the calls between pods dynamic
- A service is another type of K8s object
- Pod IPs are unreliable but service IPs are
- Durable (unlike pods)
  - Static IP address
  - Static DNS name
  - [servicename].[namespace].svc.cluster.local
- Services are ways to access pods
- Target pods using selectors
 
In kubernetes, we can use these services: ClusterIP (default), NodePort, LoadBalancer (L4), Ingress (L7)

## ClusterIP

- ClusterIP is the default service
- Visibility
  - Cluster internal
- Port
  - The port the service is listening to
- TargetPort
  - Redirecting to the port the pod(5) are listening to
- Load balanced using round robin
  - Session affinity is configurable
- When to use
  - To provide a durable way to communicate with pods inside the

### kubectl - ClusterIP Cheat Sheet (Applies to NodePort too)

```bash
# Create a service to expose a pod
kubectl expose po [podName] --port=80 --target-port=8080 --name=frontend

# Create a service to expose a deployment
kubectl expose deploy [deployName] --port=80 --target-port=8080

# Deploy the service
kubectl apply -f [definition.yaml]

# Get the services list
kubectl get svc

# Get extra info
kubectl get svc -o wide

# Describe the service
kubectl describe svc [serviceName]

# Delete the service
kubectl delete -f [definition.yaml]

# Delete the service using its name
kubectl delete svc [serviceName]
```

## NodePort

- NodePort extend the ClusterIP service
- Visibility
  - Internal and external
- NodePort
  - The port the service is listening to externally
  - Statically defined, or dynamically taken from a range between 30000-32767
- Port
  - The port the service is listening to internally
- TargetPort
  - Redirecting to the port the pod(s) are listening to
- Must have public IP addresses
- Use any Node IP + nodePort to access the service

## Load Balancing

- Layer 4 Load Balancing
  - Operating at the transport level (TCP)
  - Unable to make decisions based on content
  - Simple algorithms such as round-robin routing
- Layer 7 Load Balancing
  - Operates at the application level (HTTP, SMTP, etc)
  - Able to make decisions based on the actual content of each message
  - More intelligent load balancing decisions and content optimizations
    - Routing rules
