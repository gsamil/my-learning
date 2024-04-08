# Storage & Persistence

## Volumes

- We need to store data outside the container in a Volume
- Volumes let containers store data into external storage systems
- Vendors create plugins for their storage systems according to the Container Storage Interface
- Two ways to create storage
  - Static and dynamic

### Storage - Static Way

- Persistent Volumes
  - Represent a storage resource
  - Cluster wide
  - Provisioned by an administrator
- Persistent Volume Claim
  - A one-to-one mapping to a persistent volume
- One or more pods can use a Persistent Volume Claim
- Can be consumed by any of the containers within the pod

**Reclaim Policy**

- Delete
  - Delete the data upon pods deletion
  - The default
- Retain
  - Keeps the data upon pods deletion

**Access Modes**

- ReadWriteMany
  - The volume can be mounted as read-write by many pods
- ReadOnlyMany
  - The volume can be mounted read-only by many pods
- ReadWriteOnce
  - The volume can be mounted as read-write by a single pod
  - The other pods are in read-only mode
  - The one that has mounted the volume first will be able to write

**Persistent Volume States**

- Available :A free resource that is not yet bound to a claim
- Bound : The volume is bound to a claim
- Released : The claim has been deleted, but the resource is not yet reclaimed by the cluster
- Failed : The volume has failed its automatic reclamation

**kubectl - Persistent Volume Cheat Sheet**

```bash
# Deploy the PVs and PVCs
kubectl apply -f [definition.yaml]

# Get the PV list
kubectl get pv

# Get the PVC list
kubectl get pvc

# Describe the PV
kubectl describe pv [pvName]

# Describe the PVC
kubectl describe pvc [pvcName]

# Delete the PVs and PVCs
kubectl delete -f [definition.yaml]

# Delete the pv using its name
kubectl delete pv [pvName]

# Delete the pvc using its name
kubectl delete pvc [pvcName]
```

### Storage - Dynamic Way

**Storage Class**

- Describes the "classes" of storage offered by the admin
- An abstraction on top of an external storage resource
- No need to set a capacity
- Eliminates the need for the admin to pre-provision a persistent volume

**Reclaim Policy**

- Delete
  - Delete the data upon pods deletion
  - The default
- Retain
  - Keeps the data upon pods deletion

**Access Modes**

- ReadWriteMany
  - The volume can be mounted as read-write by many pods
- ReadOnlyMany
  - The volume can be mounted read-only by many pods
- ReadWriteOnce
  - The volume can be mounted as read-write by a single pod
  - The other pods are in read-only mode
  - The one that has mounted the volume first will be able to write


**kubectl - Storage Class Cheat Sheet**

```bash
# Deploy the StorageClass or PVC
kubectl apply -f [definition.yaml]

# Get the StorageClass list
kubectl get sc

# Get the PVC list
kubectl get pvc

# Describe the StorageClass
kubectl describe sc [className]

# Delete the SC and PVC
kubectl delete -f [definition.yaml]

# Delete the SC using its name
kubectl delete sc [className]

# Delete the PVC using its name
kubectl delete pvc [pvcName]
```
