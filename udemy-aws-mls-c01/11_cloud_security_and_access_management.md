# Cloud Security and Access Management

## Shared Responsibility Model, Compliance, Delegation, Federation (Lesson 115)

### AWS Shared Responsibility Model
- **AWS's Responsibility**: 
  - **Physical Infrastructure**: Regions, Availability Zones, and Edge Locations.
  - **Virtualization Infrastructure**: Physical host, storage, databases, networking.
  - **Managed Services Updates**: AWS manages updates and patching for services like RDS, DynamoDB, SageMaker.
- **Customer's Responsibility**:
  - Varies based on service usage.
  - In IaaS (e.g., EC2), customers manage guest OS, firewalls, and monitoring.
  - In managed services (e.g., S3), customers handle configuration, data access controls, and encryption settings.

### Compliance Standards
- AWS adheres to various global and industry-specific standards for data protection and infrastructure security.

### Identity and Access Management (IAM)
- **Identities**: Users, machines, or software requiring AWS resource access.
- **User Management**:
  - Root and IAM users for different job roles.
  - Principle of least privilege and separation of duty.
- **Cross-Account Access**: Managing access for users from different AWS accounts.
- **Delegation vs. Federation**:
  - **Delegation**: Managing access for AWS-created identities.
  - **Federation**: Managing access for identities outside of AWS (e.g., corporate credentials, social identities).
- **Application Access Scenarios**:
  - **Principle of Zero Trust**: Every AWS call must be authenticated and authorized.
  - **Examples**:
    - EC2 instances accessing S3/DynamoDB.
    - Container services needing AWS resource access.
    - AWS services (like CloudFormation) managing account resources.
    - On-premises systems interacting with AWS services.
  - **Exceptions**: Services allowing anonymous access (e.g., public S3 buckets).

## Credentials, MFA, Identity-based, Resources-based Policy (Lesson 116)

### Best Practices for User Management
- **Separate Accounts**: Create individual accounts for employees and grant only necessary privileges.
- **Credential Management**:
  - **Management Console Access**: User ID and password.
  - **SDK/CLI Access**: Access Key and Secret Access Key.
  - **Password and Access Key Rotation**: Regular rotation for security.
- **Multi-Factor Authentication (MFA)**:
  - Adds an extra security layer.
  - Recommended for critical users and root accounts.

### Access Management Methods
- **Identity-Based Policies**:
  - Attach permissions directly to users.
- **Resource-Based Policies**:
  - Attach permissions to resources.
  - Define who can access and what actions are allowed.
- **IAM Roles**:
  - Issue temporary credentials for defined access.

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
- **Example - Resource-Based Policy**:
  - Specific access to a named S3 bucket and its objects.
  - Includes `Principal` element to specify the allowed requesters.

### Principal Element in Resource-Based Policies
- **Identity-Based Policies**: Attached to end-users, principal is implicit.
- **Resource-Based Policies**: Must explicitly specify the principal.
  - Can be IAM users or other AWS accounts.
  ```
  ! IAM groups cannot be used as a principal (important for certification exams).
  ```

## Inline and Managed Policy, Amazon Resource Naming (ARN) Convention (Lesson 117)

### Policy Documents in AWS
- **Identity Management**:
  - Create individual user accounts.
  - Attach policies to users or groups.
  - Use groups for managing permissions efficiently.
- **Consistency Note**: IAM is eventually consistent; permission changes may take a few seconds.

### Types of Policies
- **Inline Policies**:
  - Directly attached to an entity (user, resource).
  - Example: S3 bucket policy.
  - Non-reusable and deleted with the entity.
- **Managed Policies**:
  - Standalone, named, reusable policies.
  - Attachable to users, groups, or roles.
  - Benefit: Versioning support.
- **AWS-Managed vs. Customer-Managed Policies**:
  - AWS-Managed: Predefined by AWS, updated with service changes.
  - Customer-Managed: Created and managed by the customer.

### AWS-Managed Policy Examples
- **Administrator Access**: Full access to all resources.
- **Database Administrator**: Tailored for DBA roles.
- **Data Scientist**: Specific to data science tasks.

### Policy Creation and Testing Tools
- **AWS Policy Generator**: Visual tool for creating policies.
- **AWS IAM User Guide**: Reference for common policy scenarios.
- **AWS Policy Simulator**: Test and verify policy effectiveness.

### Amazon Resource Naming (ARN)
- **Standard Format**: `arn:partition:service:region:account-id:resource`
- **Components**:
  - `Partition`: Group of AWS regions (e.g., AWS, AWS GovCloud, AWS China).
  - `Service`: AWS product/service (e.g., IAM, S3, SQS).
  - `Region`: AWS region (if applicable).
  - `Account ID`: AWS account identifier.
  - `Resource`: Specific resource identifier.
- **Examples**:
  - IAM User: `arn:aws:iam::account-id:user/Alice`
  - IAM Policy: `arn:aws:iam::account-id:policy/db_admin`
  - S3 Bucket: `arn:aws:s3:::my_bucket`
  - SQS Queue: `arn:aws:sqs:us-east-2:account-id:order-queue`

## Principal, Effect, Action, Resource, Not Clause (Lesson 118)

### Policy Version
- Every policy needs a `version` element.
- Current version: `2012-10-17` (Do not change arbitrarily).
- Update to a new version only when AWS releases it.

### Statement Elements
- **Effect**: Can be `Allow` or `Deny`.
- **Principal**: Specifies the identity (not needed for identity-based policies, required for resource-based policies).
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

### Policy Types
- **Identity-Based Policy**: Attached to AWS identities (users, groups, roles).
- **Resource-Based Policy**: Attached to AWS resources.

### Examples of Policy Types
- **Identity-Based Policy**: 
  - Allows all `Get` and `List` actions on any S3 resource in the user's account.
- **Resource-Based Policy**: 
  - Same actions but specifically attached to a particular S3 bucket.
  - Uses `Principal` to specify who can access the resource.

### Using Not Clauses
- **NotAction**: Matches all actions except specified ones.
- **NotResource**: Matches everything except specified resources.
- **NotPrincipal**: Matches all principals except specified ones (often used in `Deny` statements).

## Conditional Access, Implicit Deny, Explicit Allow and Deny, Permission Boundary (Lesson 119)

### S3 Bucket Access Control
#### IP Address-Based Restrictions
- **Objective**: Limit access to S3 buckets to the corporate network.
- **Method**: Use request context variables to deny requests not originating from specified IP addresses.
- **Principle**: Applies to all users; an explicit deny overrides an allow.
- **Outcome**: Centralized access control that is non-bypassable.

### EC2 Instances and S3 Access
#### VPC Endpoint-Based Restrictions
- **Issue**: EC2 instances access S3 over the public internet by default.
- **Solution**: Use VPC endpoints for private AWS network communication.
- **Policy Example**: Deny all requests not passing through the VPC endpoint.
- **Challenge**: Root account and administrators restricted without VPC endpoint access.

#### NotPrincipal Policy
- **Use Case**: Allow administrative access from anywhere.
- **Method**: Deny policy applies to everyone except specified accounts (e.g., root, specific IAM user).

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

### AWS Permission Management
#### Key Principles
- **Implicit Denial**: All requests are implicitly denied by default.
- **Explicit Allow vs Deny**: Explicit deny overrides allow.
- **Permission Boundaries**: Set maximum allowable permissions to prevent bypassing organizational controls.
  - **IAM Permission Boundaries**: Limit identity permissions.
  - **AWS Organization Service Control Policies**: Control multi-account actions.
  - **Session Policies**: Boundaries for temporary credentials.

## IAM Roles, Cross-account access options (Lesson 120)

### Application Access to AWS Services
#### Using IAM Roles for EC2 Instances
- **Scenario**: An EC2 instance requires access to S3.
- **Traditional Approach**: Treat the server as a user with IAM access key credentials.
  - **Challenges**: Security risks due to long-term credentials, difficult credential rotation.
- **IAM Role Solution**: Attach a role to the EC2 instance for temporary credentials.
  - **Benefits**:
    - No long-term credentials on the server.
    - Automatic credential rotation.
    - Reduced security risks from credential leakage.

#### EC2 Metadata Service and Security Token Service (STS)
- **Function**: EC2 uses metadata service to obtain temporary credentials.
- **STS Role**: Generates temporary credentials through the AssumeRole API.
- **Integration**: AWS SDK and CLI support AssumeRole and credential management.

### Setting Up IAM Roles
#### Components of an IAM Role
1. **Access Policy**: Determines what the role can do (e.g., DynamoDB access).
2. **Trust Policy**: Specifies who can assume the role (e.g., EC2 service, Lambda, another AWS account).

#### Recommendations and Use Cases
- **AWS Recommendation**: Use IAM roles for EC2, AWS Lambda, and other AWS services.
- **On-Premises Applications**:
  - Use long-term credentials for AssumeRole API.
  - Access AWS resources with temporary credentials.

### Cross-Account Access
#### Identity-Based and Resource-Based Policies
- **Within Account Access**: Use identity-based and resource-based policies.
- **Cross-Account Scenarios**:
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

### Corporate Identity Federation
#### Single Account Access
- **Identity Providers**: AWS supports SAML 2.0 and Microsoft Active Directory.
- **Trust Establishment**: Create trust between IAM federation and corporate identity provider.
- **Process**:
  - Define job-specific IAM roles in AWS.
  - User authentication through corporate federation web interface.
  - Role mapping after successful authentication.

#### Federation Protocols
- **SAML 2.0**: Security Markup Association Language, standard for exchanging identity and security information.
- **Integration with AWS**: Direct integration with SAML 2.0 compliant identity providers.
- **Microsoft Active Directory**: Managed directory service in AWS for Active Directory integration.

#### AWS Organizations for Multiple Accounts
- **Centralized Management**: Using a master account and organizational units (Org Units).
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

#### Supported Federation Protocols
- **Corporate Identity Federation**: SAML 2.0.
- **Internet Identity Federation**: OAuth 2.0, SAML 2.0, OpenID Connect.

## Lab - Identity-based policy, Implicit Deny, Explicit Allow (Lesson 123)

### Steps to Create an S3 Bucket
1. **Login**: Use the 'myadmin' user to log into AWS.
2. **Service Navigation**: Go to the S3 service under 'Services'.
3. **Bucket Creation**:
   - Choose a unique name (e.g., 'chandra-iam-demo').
   - Select a close region (e.g., Ohio).

### User Creation Process
1. **Service Navigation**: Under 'Services', open the IAM service console.
2. **User Creation**: Create two users, Alice and Bob.
3. **Access Types for Alice**:
   - Choose both programmatic access and AWS Management Console access.
   - Set a custom password without requiring a password reset.
4. **Permissions**: Initially, create the user without any permissions.
5. **Access Key Credentials**:
   - Download and securely save the access key credentials CSV file.

### Testing Access Restrictions
1. **Browser Sessions**:
   - Use different browsers for the admin user (Chrome) and Alice (Firefox).
2. **Access Test**: Attempt accessing S3 or other services with Alice’s credentials.
   - Expect an "access denied" error due to no granted permissions.

### Configuring Command Line Access
1. **Command Line Setup**: Use `aws configure --profile alice` to set up Alice's profile.
2. **Credential Input**: Enter access key and secret access key from the downloaded CSV file.
3. **Testing CLI Access**: Run `aws s3 ls --profile alice` to list S3 buckets.
   - Expect an "access denied" error.

### Granting Read Permissions to Alice
1. **Admin Actions**: In the myadmin session, navigate to Alice’s permissions.
2. **Policy Attachment**:
   - Use 'Attach existing policies directly'.
   - Select 'AmazonS3ReadOnlyAccess' policy.
3. **Testing Permissions**:
   - Alice can now view buckets from the management console.
   - CLI commands should list buckets (retry if errors occur).

### Attempting to Upload a File
1. **Upload Command**: Try uploading a file using Alice’s profile.
   - Use `aws s3 cp [local file name] [S3 destination] --profile alice`.
2. **Result**: Expect an "access denied" error for 'PutObject', indicating no write access.

## Lab - Policy Generator, Managed Policy, Versions, Groups (Lesson 124)

### Granting Write Access to Alice
#### Creating a Managed Policy
1. **Navigation**: Select 'policies' from the IAM console.
2. **Policy Creation**:
   - Use policy editor to grant permissions.
   - Select S3 service, choose all S3 actions.
   - Restrict full access to a single bucket using ARN.

#### Policy Review and Editing
- **Initial Policy Review**: Two statements; one unnecessary for the lab.
- **Policy Editing**:
  - Edit in JSON tab, remove the first statement.
  - Keep only one statement granting full access to the specified bucket.

#### Policy Assignment
- **Assign Policy to Alice**: Attach the newly created custom policy 'custom-s3-access'.
- **Outcome**: Alice has read access to all buckets and read-write access to the specified bucket.

#### Testing Access
- **File Upload Test**: Successfully upload a file to S3 using Alice's profile.

### Adding User Bob and Managing Permissions
#### User Creation
- **Create Bob**: Grant programmatic and management console access without initial permissions.
- **Configure CLI**: Set up Bob in the command line using `aws configure --profile bob`.
- **Permission Test**: Access denied for Bob when listing S3 buckets.

#### Using Groups for Scalable Permission Management
1. **Group Creation**:
   - Create a group named 'ProjectAlpha'.
   - Attach 'AmazonS3ReadOnlyAccess' and 'custom-s3-access' policies.
2. **User Management**:
   - Remove direct permissions from Alice.
   - Add both Alice and Bob to 'ProjectAlpha' group.
3. **Outcome**: Both Alice and Bob have read-write access to the specified bucket.

## [Q&A] Console Changes - Policy - How to allow access to Bucket and Object (Lesson 125)

### Steps to Create an S3 Access Policy
#### Policy Creation
1. **Navigation**: Access the policy creation section in the AWS console.
2. **Service Selection**: Choose S3.

#### Setting Up Permissions
- **S3 Actions**: Allow all S3 actions.
- **Resources**:
  - **Bucket**: Specify the bucket name.
  - **Object**: Indicate the bucket and use a wildcard for all objects (`bucket_name/*`).

#### Adding the ARN
- **Bucket**: Add the ARN for the specific bucket (e.g., `Chandra` in this example).
- **Object**: Add the ARN for objects in the bucket.

## Lab - Resource-based policy, Policy Generator, Principals (Lesson 126)

### Removing Identity-Based Permissions
1. **Context**: Alice and Bob currently have read-write access to a specific bucket.
2. **Action**: Remove permissions attached to the 'ProjectAlpha' group.
3. **Outcome**: Both users lose their access.

### Granting Access with Resource-Based Policy
#### Using S3 Service Console
1. **Access**: Open S3 console with 'myadmin' session.
2. **Bucket Selection**: Choose the appropriate bucket (e.g., 'chandra-iam-demo').
3. **Policy Setup**: Under 'Permissions' tab, select 'Bucket Policy'.

#### Creating Policy
1. **Policy Generator**: Use it to create a new S3 Bucket Policy.
2. **Configuration**:
   - **Effect**: Allow.
   - **Principal**: Wild card (all users), to be refined later.
   - **Actions**: All actions.
   - **ARNs**: Add bucket ARN and a separate ARN for all objects in the bucket.

#### Policy Modification
1. **Copy and Paste**: Generated policy into the bucket policy editor.
2. **Modification**: Change the principal to specify individual users (Alice and Bob) instead of a group.

#### Validating and Saving Policy
1. **Validation Issues**:
   - Case sensitivity issue with 'AWS' in principal key.
   - Groups not recognized as valid principals.
2. **Resolution**: Specify individual user ARNs in a list.
3. **Confirmation**: Policy passes validation and is saved.

### Testing Access
1. **Check Access**: Confirm that Alice and Bob can read and write to the bucket.
