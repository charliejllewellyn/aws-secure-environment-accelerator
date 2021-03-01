### JSON 
<pre> 
{
    "global-options": {
        "<a href=#additional-cwl-regions>additional-cwl-regions</a>": "additional-cwl-regions", 
        "<a href=#additional-global-output-regions>additional-global-output-regions</a>": "List", 
        "<a href=#alz-baseline>alz-baseline</a>": "Boolean", 
        "<a href=#aws-config>aws-config</a>": "aws-config", 
        "<a href=#aws-org-master>aws-org-master</a>": "aws-org-master", 
        "<a href=#central-bucket>central-bucket</a>": "String", 
        "<a href=#central-log-services>central-log-services</a>": "central-log-services", 
        "<a href=#central-operations-services>central-operations-services</a>": "central-operations-services", 
        "<a href=#central-security-services>central-security-services</a>": "central-security-services", 
        "<a href=#cloudwatch>cloudwatch</a>": "cloudwatch", 
        "<a href=#ct-baseline>ct-baseline</a>": "Boolean", 
        "<a href=#default-cwl-retention>default-cwl-retention</a>": "String", 
        "<a href=#default-s3-retention>default-s3-retention</a>": "String", 
        "<a href=#iam-password-policies>iam-password-policies</a>": "iam-password-policies", 
        "<a href=#ignored-ous>ignored-ous</a>": "List", 
        "<a href=#keep-default-vpc-regions>keep-default-vpc-regions</a>": "List", 
        "<a href=#organization-admin-role>organization-admin-role</a>": "String", 
        "<a href=#reports>reports</a>": "reports", 
        "<a href=#scps>scps</a>": "List", 
        "<a href=#security-hub-frameworks>security-hub-frameworks</a>": "security-hub-frameworks", 
        "<a href=#ssm-automation>ssm-automation</a>": "List", 
        "<a href=#supported-regions>supported-regions</a>": "List", 
        "<a href=#vpc-flow-logs>vpc-flow-logs</a>": "vpc-flow-logs", 
        "<a href=#workloadaccounts-param-filename>workloadaccounts-param-filename</a>": "String", 
        "<a href=#workloadaccounts-prefix>workloadaccounts-prefix</a>": "String", 
        "<a href=#workloadaccounts-suffix>workloadaccounts-suffix</a>": "String"
    }
}</pre> 
### YAML 
<pre> 
global-options:
    <a href=#additional-cwl-regions>additional-cwl-regions</a>: additional-cwl-regions
    <a href=#additional-global-output-regions>additional-global-output-regions</a>: List
    <a href=#alz-baseline>alz-baseline</a>: Boolean
    <a href=#aws-config>aws-config</a>: aws-config
    <a href=#aws-org-master>aws-org-master</a>: aws-org-master
    <a href=#central-bucket>central-bucket</a>: String
    <a href=#central-log-services>central-log-services</a>: central-log-services
    <a href=#central-operations-services>central-operations-services</a>: central-operations-services
    <a href=#central-security-services>central-security-services</a>: central-security-services
    <a href=#cloudwatch>cloudwatch</a>: cloudwatch
    <a href=#ct-baseline>ct-baseline</a>: Boolean
    <a href=#default-cwl-retention>default-cwl-retention</a>: String
    <a href=#default-s3-retention>default-s3-retention</a>: String
    <a href=#iam-password-policies>iam-password-policies</a>: iam-password-policies
    <a href=#ignored-ous>ignored-ous</a>: List
    <a href=#keep-default-vpc-regions>keep-default-vpc-regions</a>: List
    <a href=#organization-admin-role>organization-admin-role</a>: String
    <a href=#reports>reports</a>: reports
    <a href=#scps>scps</a>: List
    <a href=#security-hub-frameworks>security-hub-frameworks</a>: security-hub-frameworks
    <a href=#ssm-automation>ssm-automation</a>: List
    <a href=#supported-regions>supported-regions</a>: List
    <a href=#vpc-flow-logs>vpc-flow-logs</a>: vpc-flow-logs
    <a href=#workloadaccounts-param-filename>workloadaccounts-param-filename</a>: String
    <a href=#workloadaccounts-prefix>workloadaccounts-prefix</a>: String
    <a href=#workloadaccounts-suffix>workloadaccounts-suffix</a>: String
</pre> 


<a name="keep-default-vpc-regions"></a> \
ASEA deletes default VPCs, this specifies regions where ASEA won't delete the default VPCs \
*Required*: Yes \
*Type*: List \
*Allowed Values*: Place holder for allowed values

<a name= "additional-cwl-regions" href="global-options/additional-cwl-regions.md">`additional-cwl-regions`</a> \
Display metrics from different Regions  \
*Required*: Yes \
*Type*: List\
*Allowed Values*: Place holder for allowed values

`default-s3-retention`  <a name="default-s3-retention"></a> \
Lifecycle policy for S3 \
*Required*: Yes \
*Type*: String \
*Allowed Values*: Place holder for allowed values

`central-bucket`  <a name="central-bucket"></a> \
Place holder text for what the parameter does \
*Required*: Yes \
*Type*: String \
*Allowed Values*: Place holder for allowed values

`organization-admin-role`  <a name="organization-admin-role"></a> \
This roles gets created in every account and allows you to switch into this role from the root account for management \
*Required*: Yes \
*Type*: String \
*Allowed Values*: Place holder for allowed values

<a name= "vpc-flow-logs" href="global-options/vpc-flow-logs.md">`vpc-flow-logs`</a> \
Configuration for the collection of VPC flow logs \
*Required*: Yes \
*Type*: vpc-flow-logs \
*Allowed Values*: Place holder for allowed values

`alz-baseline`  <a name="alz-baseline"></a> \
Set to true when installing ASEA on top of ALZ \
*Required*: Yes \
*Type*: Boolean \
*Allowed Values*: True | False

<a name= "aws-org-master" href="global-options/aws-org-master.md">`aws-org-master`</a> \
Provide the name of the ogranizational management account, this ties to the actual details of the account in mandatory-account-configs \
*Required*: Yes \
*Type*: aws-org-master \
*Allowed Values*: Place holder for allowed values

`scps`  <a name="scps"></a> \
Name of the different SCPs that will be used. This list maps each SPC's json with a referentiable name \
*Required*: Yes \
*Type*: List \
*Allowed Values*: Place holder for allowed values

<a name= "cloudwatch" href="global-options/cloudwatch.md">`cloudwatch`</a> \
Define the metrics that will be collected by Cloudwatch \
*Required*: Yes \
*Type*: cloudwatch \
*Allowed Values*: Place holder for allowed values

<a name= "central-log-services" href="global-options/central-log-services.md">`central-log-services`</a> \
Configuration for log archive services \
*Required*: Yes \
*Type*: central-log-services \
*Allowed Values*: Place holder for allowed values

<a name= "aws-config" href="global-options/aws-config.md">`aws-config`</a> \
Config rules for AWS Config, the list in this file is from the NIST 800-53 conformance package \
other packages available at https://docs.aws.amazon.com/config/latest/developerguide/conformancepack-sample-templates.html \
*Required*: Yes \
*Type*: aws-config \
*Allowed Values*: Place holder for allowed values

`default-cwl-retention`  <a name="default-cwl-retention"></a> \
Amount of days to retain CW logs \
*Required*: Yes \
*Type*: String \
*Allowed Values*: Place holder for allowed values

`ct-baseline`  <a name="ct-baseline"></a> \
Place holder text for what the parameter does \
*Required*: Yes \
*Type*: Boolean \
*Allowed Values*: True | False

`workloadaccounts-suffix`  <a name="workloadaccounts-suffix"></a> \
Suffix to add to created work-load accounts \
*Required*: Yes \
*Type*: String \
*Allowed Values*: Place holder for allowed values

<a name= "iam-password-policies" href="global-options/iam-password-policies.md">`iam-password-policies`</a> \
Password policies for IAM \
*Required*: Yes \
*Type*: iam-password-policies \
*Allowed Values*: Place holder for allowed values

<a name= "security-hub-frameworks" href="global-options/security-hub-frameworks.md">`security-hub-frameworks`</a> \
https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards.html \
*Required*: Yes \
*Type*: security-hub-frameworks \
*Allowed Values*: Place holder for allowed values

<a name= "central-security-services" href="global-options/central-security-services.md">`central-security-services`</a> \
Security services to be provisioned in the security account \
*Required*: Yes \
*Type*: central-security-services \
*Allowed Values*: Place holder for allowed values

<a name= "reports" href="global-options/reports.md">`reports`</a> \
Usage reports supported a this moment \
*Required*: Yes \
*Type*: reports \
*Allowed Values*: Place holder for allowed values

`ssm-automation`  <a name="ssm-automation"></a> \
For remediation actions to be invoked from Config-rules \
*Required*: Yes \
*Type*: List \
*Allowed Values*: Place holder for allowed values

`ignored-ous`  <a name="ignored-ous"></a> \
Write any your pre-existing OUs here, the ASEA need to be told explicitly about these in order to ignore them \
*Required*: Yes \
*Type*: List \
*Allowed Values*: Place holder for allowed values

<a name= "central-operations-services" href="global-options/central-operations-services.md">`central-operations-services`</a> \
Configuration for the Operations account \
*Required*: Yes \
*Type*: central-operations-services \
*Allowed Values*: Place holder for allowed values

`workloadaccounts-param-filename`  <a name="workloadaccounts-param-filename"></a> \
Configuration file for the workload accounts, this gives you the ability to split the config file into several files if you prefer to \
*Required*: Yes \
*Type*: String \
*Allowed Values*: Place holder for allowed values

`additional-global-output-regions`  <a name="additional-global-output-regions"></a> \
Place holder text for what the parameter does \
*Required*: Yes \
*Type*: List \
*Allowed Values*: Place holder for allowed values

`supported-regions`  <a name="supported-regions"></a> \
regions that will be monitored and logged by the core services \
*Required*: Yes \
*Type*: List \
*Allowed Values*: Place holder for allowed values

`workloadaccounts-prefix`  <a name="workloadaccounts-prefix"></a> \
Prefix that will be added to workload account names \
*Required*: Yes \
*Type*: String \
*Allowed Values*: Place holder for allowed values

