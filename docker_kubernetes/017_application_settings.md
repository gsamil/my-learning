# Application Settings

## ConfigMaps

- Decouple and externalize configuration
- Referenced as environment variables
- Created from
  - Manifests
  - Files
  - Directories (containing one or more file)
- Static meaning that if you change values, the containers will have to be restarted to get them

**Map a Volume to a ConfigMap**

- Solve the static issue
- Updates to values are reflected in containers
- Each Key/Value pair is seen as a file in the mounted directory

### kubectl - ConfigMaps Cheat Sheet**

```bash
# The imperative way
kubectl create configmap literal-example --from-literal="city=Ann Arbor" --from-literal=state=Michigan

# The declarative way
kubectl apply -f [cf.yaml]

# From a file
kubectl create cm [name] --from-file=myconfig.txt

# From a folder
kubectl create cm [name] --from-file=config/

# List the ConfigMaps
kubectl get cm

# Save a ConfigMap in a YAML file
kubectl get cm [name] -o YAML

# Delete a ConfigMap
kubectl delete -f [cf.yaml]
```

## Secrets

- Stored as base64 encoded strings
- Not secure as base64 strings are not encrypted

### kubectl - Secrets Cheat Sheet

```bash
# The imperative way
kubectl create secret generic [secretName] --from-literal=STATE=Michigan

# The declarative way
kubectl apply -f [secret.yaml]

# List the Secrets
kubectl get secrets

# Save a Secret in a YAML file
kubectl get secrets [secretName] -o YAML

# Delete a secret
kubectl delete -f [secret.yaml]

# Delete a secret
kubectl delete secrets [secretName]
```

