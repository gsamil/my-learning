# Cloud Security and Access Management

## Shared Responsibility Model, Compliance, Delegation, Federation (Lesson 115)

### AWS Shared Responsibility Model
- **AWS's Responsibility**: Responsible for security **of** the cloud.
  - **Physical Infrastructure**: Regions, Availability Zones, and Edge Locations.
  - **Virtualization Infrastructure**: Physical host (compute), storage, databases, networking.
  - **Updating and Patching Managed Services**: RDS, DynamoDB, SageMaker.
- **Customer's Responsibility**: Responsible for security **in** the cloud.
  - Varies based on service usage.
  - In IaaS (e.g., EC2), customers manage guest OS, firewalls, and monitoring.
  - In managed services (e.g., S3), customers handle configuration, data access controls, and encryption settings.

### Identity and Access Management (IAM)
- **Identity**: Users, machines, or software requiring AWS resource access.
- **User Management**:
  - Root and IAM users for different job roles.
  - Principle of least privilege and separation of duty.
  - Create job role-specific users and grant only necessary permissions.
- **Cross-Account Resource Sharing**: Managing access for users from different AWS accounts.
  - **Delegation**: Managing access for AWS-created identities.
  - **Federation**: Managing access for identities outside of AWS (e.g., corporate credentials, social identities).
- **Application Access Scenarios**:
  - **Principle of Zero Trust**: Every AWS call must be authenticated and authorized.
  - **Only Exception**: Services allowing anonymous access (e.g., public S3 buckets).
  - **Examples**:
    - EC2 instances accessing S3/DynamoDB.
    - Container services needing AWS resource access.
    - AWS services (like CloudFormation) managing account resources.
    - On-premises systems interacting with AWS services.

## Credentials, MFA, Identity-based, Resources-based Policy (Lesson 116)

### Best Practices for User Management
- Create individual accounts for employees and grant only necessary privileges.
- **Credential Management**:
  - **Management Console Access**: User ID and password.
  - **SDK/CLI Access**: Access Key and Secret Access Key.
  - Regular rotation for both Password and Access Key.
- **Multi-Factor Authentication (MFA)**:
  - Adds an extra security layer.
  - Recommended for critical users and root accounts.

### Access Management Methods
- **Identity-Based Policies**: Attach permissions directly to users.
- **Resource-Based Policies**: Attach permissions to resources.
  - Define who can access and what actions are allowed.
- **IAM Roles**: Issue temporary credentials for defined access.

### Policy Structure
- **JSON Format**:
  - `Version`: Policy language version (current version: `2012-10-17`).
  - `Statement`: Defines permissions.
    - `Effect`: `Allow` or `Deny`.
    - `Action`: List of actions (API calls) allowed or denied.
    - `Resource`: Identifies resources the policy applies to.
- **Example - Identity-Based Policy**:
  - Read access to all S3 buckets/objects in an account.
  - AWS-managed policy: `AmazonS3ReadOnlyAccess`.
  ```
  {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Action": ["s3:Get*", "s3:List*"],
        "Resource": "*"
      }
    ]
  }
  ```
- **Example - Resource-Based Policy**:
  - Specific access to a named S3 bucket and its objects.
  - Includes `Principal` element to specify the allowed requesters.
  ```
  {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Action": ["s3:Get*", "s3:List*"],
        "Resource": [
          "arn:aws:s3:::my_bucket"
          ]
        "Sid": "Example",
        "Principal": {
          "AWS": [
            "arn:aws:iam::123456789012:user/Alice"
            ]
        },
      }
    ]
  }
  ```

  ```
  ! IAM groups cannot be used as a principal (important for certification exams).
  ```

## Inline and Managed Policy, Amazon Resource Naming (ARN) Convention (Lesson 117)

### Policy Documents in AWS
- Create individual user accounts.
- Attach policies to users or groups.
- Use groups for managing permissions efficiently.
- IAM is eventually consistent; permission changes may take a few seconds.

### Types of Policies
- **Inline Policies**:
  - Directly attached to an entity (user, resource).
  - Example: S3 bucket policy (Resource based inline policy)
  - Non-reusable and deleted with the entity.
- **Managed Policies**:
  - Standalone, named, reusable policies.
  - Attachable to users, groups, or roles.
  - Benefit: Versioning support.
- **AWS-Managed vs Customer-Managed Policies**:
  - AWS-Managed: Predefined by AWS, updated with service changes.
  - Customer-Managed: Created and managed by the customer.

### Amazon Resource Naming (ARN)
- **Standard Format**: `arn:partition:service:region:account-id:resource`
- **Components**:
  - `Partition`: Group of AWS regions (e.g., AWS, AWS GovCloud, AWS China).
  - `Service`: AWS product/service (e.g., IAM, S3, SQS).
  - `Region`: AWS region (if applicable).
  - `Account ID`: AWS account identifier.
  - `Resource`: Specific resource identifier.
- **Examples**:
  - IAM User: `arn:aws:iam::account-id:user/Alice` (no region for IAM resources)
  - IAM Policy: `arn:aws:iam::account-id:policy/db_admin`
  - S3 Bucket: `arn:aws:s3:::my_bucket`
  - SQS Queue: `arn:aws:sqs:us-east-2:account-id:order-queue`

## Principal, Effect, Action, Resource, Not Clause (Lesson 118)

### Policy Document Structure
- **Version**
  - Every policy needs a `version` element.
  - Current version: `2012-10-17` (Do not change arbitrarily).
  - Update to a new version only when AWS releases it.
- **Statement**
  - Permissions are allowed or denied using Statement.
  - A policy document can have one or more statements.
  - **Effect**: Can be `Allow` or `Deny`.
  - **Principal**: Specifies the identity 
    - Not needed for identity-based policies, required for resource-based policies.
    - Can't use IAM group as a principal.
    - Types:
      - Root user of an account: Use account number or explicit root user.
      - IAM users: Use ARN.
      - Roles: Specify role ARN.
      - AWS Services: Use service name.
      - Anonymous access: Use `*` (wildcard).
      - Federated users: Specify federated identity provider.
      - **Role Session Name**: Used for unique identification in role assumption.
  - **Action**: API calls for which permission applies (can use wildcards).
  - **Resource**: Resources for which permission applies.
  - **Variables**: Context variables for fine-grained control.

### Using Not Clauses
- **NotAction**: Matches all actions except specified ones.
- **NotResource**: Matches everything except specified resources.
- **NotPrincipal**: Matches all principals except specified ones (often used in `Deny` statements).

## Conditional Access, Implicit Deny, Explicit Allow and Deny, Permission Boundary (Lesson 119)

### Limit access to S3 buckets by IP
- **Method**: Use request context variables to deny requests not originating from specified IP addresses.
- **Outcome**: Centralized access control that is non-bypassable.
```
"Statement": [
  {
    "Effect": "Deny",
    "Action": "s3:*",
    "Resource": [
      "arn:aws:s3:::my_bucket",
      "arn:aws:s3:::my_bucket/*"
    ],
    "Principal": "*",
    "Condition": {
      "NotIpAddress": {
        "aws:SourceIp": "151.29.0.0/16"
      }
    }
  }
]
```

### VPC Endpoint Only Access
- EC2 instances access S3 over the public internet by default.
- We can use VPC endpoints for private AWS network communication.
- **Method**: Deny all requests not passing through the VPC endpoint.
- **Challenge**: Root account and administrators restricted without VPC endpoint access.
```
"Statement": [
  {
    "Effect": "Deny",
    "Action": "s3:*",
    "Resource": [
      "arn:aws:s3:::my_bucket",
      "arn:aws:s3:::my_bucket/*"
    ],
    "NotPrincipal": {
      "AWS": [
        "arn:aws:iam::123456789012:root",
        "arn:aws:iam::123456789012:user/Admin" # Admins can still access from anywhere
      ]
    }
    "Condition": {
      "StringNotEquals": {
        "aws:sourceVpce": "vpce-1a2b3c4d" # each VPC endpoint has a unique ID
      }
    }
  }
]
```

### Context Information in AWS Requests
- **Variables**: Timestamp, RequestedRegion, PrincipalTag, SecureTransport.
- **Applications**: Time-based restrictions, region-specific access, tag-based access, secure transport enforcement.

### Tag-Based Resource Access
- **Concept**: Attach business information as tags to resources.
- **Example**: Allow EC2 start/stop actions based on matching cost center tags.
- **Advantage**: Automatically updates access with changing business groups.
- **Type**: Attribute-based access control (ABAC).

### Access Management Approaches
#### Role-Based Access Control (RBAC)
- **Traditional Method**: Based on job roles, granting least privilege.
- **Challenge**: Does not scale well in rapidly growing organizations due to frequent policy updates.

#### Attribute-Based Access Control (ABAC)
- **Modern Approach**: Define permissions based on resource and principal tags.
- **Advantages**: Scales well, fewer policies, dynamic access control.
- **Example**: EC2 actions based on matching cost center tags.

### Policy Evaluation
- **Implicit Denial**: All requests are implicitly denied by default.
- **Explicit Allow vs Deny**: Explicit deny overrides allow.
- **Permission Boundaries**: Set maximum allowable permissions to prevent bypassing organizational controls.
  - **IAM Permission Boundaries**: Limit identity permissions.
  - **AWS Organization Service Control Policies**: Control multi-account actions.
  - **Session Policies**: Boundaries for temporary credentials.

## IAM Roles, Cross-account access options (Lesson 120)

### Application Access to AWS Resources : IAM Roles
- **Scenario**: An EC2 instance requires access to S3.
- **Traditional Approach**: Treat the server as a user with IAM access key credentials.
  - **Challenges**: Security risks due to long-term credentials, difficult credential rotation.
- **IAM Role Solution**: Attach a role to the EC2 instance for temporary credentials.
  - **Benefits**:
    - No long-term credentials on the server.
    - Automatic credential rotation.
    - Reduced security risks from credential leakage.

### Security Token Service (STS)
- **Function**: EC2 uses metadata service to obtain temporary credentials.
- **STS Role**: Generates temporary credentials through the AssumeRole API.
- **Integration**: AWS SDK and CLI support AssumeRole and credential management.

### Role Concepts
1. **Access Policy**: When you create a Role in IAM, you need to attach an Access Policy to it. Determines what the role can do (e.g., DynamoDB access).
2. **Trust Policy**: Specifies who can assume the role (e.g., EC2 service, Lambda, another AWS account).

#### Recommendations and Use Cases
- **AWS Recommendation**: Use IAM roles for EC2, AWS Lambda, and other AWS services.
- **On-Premises Applications**:
  - Use long-term credentials for AssumeRole API.
  - Access AWS resources with temporary credentials.

### Cross-Account Access Scenarios

#### Same Account Access
- Use identity-based and resource-based policies.

#### Cross-Account Scenarios
- **Resource-Based Policies**: Grant access to users or roles in other accounts.
- **IAM Roles**: Provide temporary credentials for accessing resources across accounts.

#### Cross-Account Access Examples
1. **S3 Bucket Access**:
   - Account B grants access to Account A through resource-based policies.
   - Account A delegates permission to its users or roles.
2. **Services Without Resource-Based Policies** (e.g., DynamoDB, Kinesis):
   - Account B creates a role with necessary permissions.
   - Account B allows Account A to assume the role.
   - Account A users get temporary credentials via STS AssumeRole API.

## Federation, SSO, SAML, Active Directory, AWS Organizations, Cognito (Lesson 121)

- When external identities are used for accessing AWS, we call it as **Federation**.

### Corporate Identity Federation

#### Single Account Access
- **Identity Providers**: AWS supports SAML 2.0 and Microsoft Active Directory.
- **Trust Establishment**: Create trust between IAM federation and corporate identity provider.
- **Process**:
  - Define job-specific IAM roles in AWS.
  - User authentication through corporate federation web interface.
  - Role mapping after successful authentication.

#### Federation Protocols (Identity Management Solutions)
- **SAML 2.0**: Security Markup Association Language, standard for exchanging identity and security information.
- **Integration with AWS**: Direct integration with SAML 2.0 compliant identity providers.
- **Microsoft Active Directory**: Managed directory service in AWS for Active Directory integration.

#### AWS Organizations for Multiple Accounts
- **AWS Organizations**: Using a master account and organizational units (Org Units).
- **Features**:
  - Cost and billing management.
  - Service control policies for member accounts.
  - Resource sharing across accounts.
- **AWS Single Sign-On**: Centralized identity management across multiple accounts.

### Internet Identity Federation with Amazon Cognito

#### Integrating Social Identities
- **Providers**: Google, Facebook, Amazon, etc.
- **Service**: Amazon Cognito for mapping external identities to a single Cognito identity.
- **Process**:
  - Enable multiple identity providers with Cognito.
  - Establish trust between identity provider and Cognito.

#### Role Mapping and Access
- **Authenticated Users**: Mapped to an authenticated role.
- **Unauthenticated Users**: Mapped to an unauthenticated role for limited app access.
- **Temporary AWS Credentials**: Issued based on the mapped role.

#### Cognito - Supported Federation Protocols
- **Corporate Identity Federation**: SAML 2.0.
- **Internet Identity Federation**: OAuth 2.0, SAML 2.0, OpenID Connect.

## Labs

### Identity-based policy, Implicit Deny, Explicit Allow (Lesson 123)

1. Create a new S3 bucket.
2. Create a new IAM user (`alice`). Refer to Section 1.9 for how to create IAM users.
3. Use `aws configure --profile alice` to set up Alice's profile.
4. Enter access key and secret access key from the downloaded CSV file.
5. Run `aws s3 ls --profile alice` to list S3 buckets.
   - Expect an "access denied" error.
6. Add `AmazonS3ReadOnlyAccess` permission to Alice.
7. Alice can now view buckets from the management console.
8. Try uploading a file using Alice’s profile.
    ```
    aws s3 cp text.txt s3://samil-demo --profile alice
    ```
9. Expect an "access denied" error for 'PutObject', indicating no write access.

### Policy Generator, Managed Policy, Versions, Groups (Lesson 124)

#### Grant write access to Alice to S3
1. Select 'policies' from the IAM console then 'create policy'
    - Select S3 service, choose all S3 actions.
    - From Resources, add ARN to `bucket` : `samil-demo` and `samil-demo/*`
    - Name the policy as `custom-s3-access`
2. Edit the Policy JSON, remove the first statement.
    - Notice that now you have 2 versions of the policy.
3. Assign Policy to Alice: Attach the newly created custom policy 'custom-s3-access'.
4. Alice can now upload files to S3.

#### Grant Same Permissions to Another User

1. Create a new user 'bob' and configure CLI.
2. Remove the existing permissions from Alice.
3. Create a new user group 'ProjectAlpha' and attach the custom policy and 'AmazonS3ReadOnlyAccess' policy.
4. Add both Alice and Bob to the group.
5. Both Alice and Bob can now read and write to the bucket.

### Resource-based policy, Policy Generator, Principals (Lesson 126)

- In the previous lab, we used identity-based policies to grant access to users.
- In this lab, we will use resource-based policies to grant access to resources.

1. Remove the permissions that are attached to the 'ProjectAlpha' group.
2. Open S3 console with 'myadmin' session. Go to your bucket and select 'Permissions'.
3. Select 'Bucket Policy' and click 'Policy Generator'.
    - Type of Policy: S3 Bucket Policy.
    - **Effect**: Allow.
    - **Principal**: * (wildcard)
    - **AWS Service**: Amazon S3
    - **Actions**: All actions.
    - **ARNs**: Add bucket ARN : `arn:aws:s3:::samil-demo,arn:aws:s3:::samil-demo/*`
    - Click 'Add Statement' and then 'Generate Policy'.
    - Copy the generated policy and paste it in the bucket policy editor.
4. Try to add `ProjectAlpha` ARN as a Principal to the policy.
    ```json
    "Principal": {
      "AWS": "arn:aws:iam::587865868937:group/ProjectAlpha"
    }
    ```
    - Expect an error: `Invalid principal in policy`.
5. Confirm that both users can read the specified bucket.
    ```
    aws s3 ls s3://samil-demo --profile alice
    ```
