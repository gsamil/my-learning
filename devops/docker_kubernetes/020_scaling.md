# Scaling

## Horizontal Pod Autoscaling

- Uses the K8s Metrics Server
- Pods must have requests and limits defined
- The HPA checks the Metrics Server every 30 seconds
- Scale according to the min and max number or replicas defined
- Cooldown / Delay
  - Prevent racing conditions
  - Once a change has been made, HPA waits
  - By default, the delay on scale up events is 3 minutes, and the delay on scale down events is 5 minutes

### kubectl - HPA Cheat Sheet

```bash
# The imperative way
kubectl autoscale deployment [name] --cpu-percent=50 --min=3 --max=10

# The declarative way
kubectl apply -f [hap.yaml]

# Get the autoscaler status
kubectl get hpa [name]

# Delete the HPA
kubectl delete -f [hap.yaml]

# Delete the HPA
kubectl delete hpa [name]
```

