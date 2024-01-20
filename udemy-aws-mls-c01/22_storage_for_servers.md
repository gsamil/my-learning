# 242. Introduction to Storage

## Introduction
- **Objective**: Explore storage options for EC2 instances, focusing on block storage, file share, and object storage.

## Categories of Storage
1. **Block Storage**: 
   - Behaves like raw, unformatted hard drives.
   - Used for operating systems, databases, etc.
   - Types: Instance Store, Elastic Block Store (EBS).
2. **File Storage**: 
   - Network file shares, centralized file management.
   - Accessible irrespective of the EC2 instance.
   - AWS offerings: Elastic File System (EFS), FSx.
3. **Object Storage**: 
   - S3 service for file storage.
   - Accessible from anywhere.

## Block Storage
- **Instance Store**: 
   - Directly attached to the host computer.
   - Temporary storage (data lost on instance stop/termination).
   - Benefits: High performance, included in EC2 pricing.
   - Suitable for clusters (Hadoop, MongoDB).
   - Types: SSD-backed (for random IO, high IOPS) and HDD-backed (for sequential read/write, high throughput).
- **Elastic Block Store (EBS)**:
   - Not discussed in detail here.

## File Storage
- Centralized management for files.
- AWS solutions: EFS, FSx services.
- Automatically scalable.

## Use Cases
- **Instance Store**:
  - Ideal for high-performance applications.
  - Requires data replication for durability.
  - Used in scale-out solutions like Hadoop.
  - Can't be attached after instance launch.
  - Instance Types: 
    - Storage Optimized (D, H families: for dense storage, big data workloads).
    - I family: for high-frequency transaction systems, databases.

## Summary
- EC2 offers a variety of storage solutions tailored to different needs.
- Block storage (Instance Store and EBS) is key for operating systems and databases.
- File storage solutions (EFS, FSx) provide centralized file management.
- Object storage (S3) offers widely accessible file storage.
- Choice of storage depends on application requirements, performance needs, and durability considerations.

# 243. Elastic Block Store (EBS)

## Introduction
- **Purpose**: Understand Elastic Block Store (EBS) as a storage service for creating block device volumes.

## Characteristics of EBS
- **Location**: Managed by EBS service and external to the host computer.
- **Network Traffic**: I/O traffic goes over the network.
- **Persistence**: Considered persistent storage, suitable for long-term use.
- **Charges**: Separate storage charges in addition to EC2 instance pricing.

## Benefits of EBS
- **Flexibility**: Can stop/restart EC2 instances; persist storage volume after termination.
- **Portability**: Detach from one instance and attach to another within the same availability zone.
- **Backup**: Built-in capability for incremental backups, known as snapshots, stored in S3.
- **AMI Creation**: Use snapshots to create Amazon Machine Images (AMIs).

## Availability and Durability
- **Zone Specific**: Must specify an Availability Zone for the volume.
- **Replication**: Automatically replicated within the Availability Zone.
- **Disaster Recovery**: Use snapshots for restoration in different zones or regions.

## Use Cases
- Suitable for various applications: enterprise apps, databases, big data analytics, media workflows.
- Some overlap with instance store use cases; choice depends on application needs and software capabilities.

## Snapshots
- **Function**: Point-in-time backups, creating an image of the volume.
- **Incremental Backups**: Subsequent snapshots only copy changed blocks.
- **Consistency**: Flush data and quiesce filesystem before snapshotting.
- **Asynchronous**: Snapshots are created immediately but take time to complete.
- **Multi-Volume Snapshots**: Consistent snapshot across multiple volumes is possible.

## Instance and EBS Volume Mix
- Example: D2 extra large instance uses an 8 GB EBS boot device and 2 TB instance storage volumes.
- Possible to mix instance and EBS volumes for an instance.

## EBS Volume Types
1. **General Purpose (SSD)**: 
   - Balanced price-performance.
   - Ideal for small/medium databases, boot volumes, dev/test environments.
2. **Provisioned IOPS (SSD)**: 
   - Highest performance for latency-sensitive workloads.
   - Suitable for critical applications and large databases.
3. **Throughput Optimized HDD**: 
   - Low-cost, high-throughput.
   - Used for big data workloads, data warehouses, log processing.
4. **Cold HDD**: 
   - Lowest cost, for infrequently accessed workloads.

## Pricing Comparison
- Example: Cost for storing 500 GB data for a month.
- Includes comparison of Provisioned IOPS at different capacities.

## Summary
- EBS provides persistent block storage solutions, replicating within Availability Zones for durability.
- Offers a range of volume types catering to different application needs.
- Key consideration: Balance between performance requirements and cost implications.

# 244. Elastic File System, FSx for Windows, FSx for Lustre

## Introduction
- **Purpose**: Understand file storage options on AWS for sharing content across servers.

## Use Cases
- **Content Sharing**: Ideal for sharing configuration files, data files, web content.
- **Media Workflows**: Useful in video editing, production, and media asset management.
- **User Private Space**: Create and manage private storage space for individual users.
- **Database Backups**: Facilitate backups by mounting shares to database servers.

## S3 vs. File Shares
- **S3 Integration**: Requires RESTful API calls.
- **File Shares**: Interact using standard filesystem commands, easier integration.

## AWS Managed File Shares
### 1. Elastic File System (EFS)
   - **OS Compatibility**: Linux-based EC2 instances.
   - **File System**: NFS file share.
   - **Features**: Traditional permission models, standard and infrequent access storage tiers, lifecycle management.

### 2. FSx for Windows
   - **OS Compatibility**: Windows-based EC2 instances.
   - **File System**: NTFS file system on SMB protocol.
   - **Features**: Integrates with Active Directory, manages access permissions.

### 3. FSx for Lustre
   - **OS Compatibility**: Linux-based systems.
   - **Modes**: Standalone high-performance file share or linked to S3 bucket.
   - **Use Cases**: High-performance computing, video processing, financial modeling.

## Key Benefits
- **Management**: Fully managed solutions with automatic scaling.
- **Durability & Availability**: High, with replication across multiple Availability Zones.
- **Access**: Can be accessed from on-premises systems via AWS Direct Connect or VPN.

## Summary
- AWS offers a range of storage solutions for EC2 instances including block storage (Instance Store and EBS) and file shares (EFS, FSx for Windows, FSx for Lustre).
- File shares facilitate easier integration for sharing files between servers, users, and on-premises systems, compared to S3.
- Each file share solution caters to specific needs and operating systems, providing high durability, availability, and ease of management.

# 245. Elastic Block Store (EBS) Encryption

## Introduction
- **Purpose**: Understand the encryption solutions for EBS volumes in AWS.
- **Reference**: [AWS EBS Encryption Documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html)

## Key Points
### 1. EBS Encryption Mechanism
   - Encrypts data-at-rest and data-in-transit between an EC2 instance and EBS storage.
   - Encryption and decryption operations occur on the servers hosting EC2 instances.

### 2. Encryption Key Options
   - **EBS Managed Keys**: Use account-specific master keys managed by EBS for encryption/decryption.
   - **Customer Master Key (CMK)**: Users can create and manage their own keys for encryption.

### 3. CMK Benefits and Use Cases
   - **Flexibility**: Different sets of volumes can be encrypted with different CMKs.
   - **Access Control**: Fine-grained policies control who accesses CMKs.
   - **Recommended for Sensitive Workloads**: Enhanced security and control over encryption keys.

### 4. Encryption Coverage
   - **Data Transfer**: Ensures secure data transfer from host to volume.
   - **Data-at-Rest**: All stored data is encrypted.
   - **Snapshots**: Encrypted automatically.
   - **Restored Volumes**: Remain encrypted.
   - **Key Flexibility**: Option to use different keys for copying snapshots and restoring volumes.

## Summary
- EBS encryption provides a comprehensive and straightforward solution for securing EBS volumes.
- Offers options between EBS-managed keys and user-managed CMKs, catering to different security needs.
- Ideal for protecting data in various states – at rest, in transit, and during snapshot operations.

