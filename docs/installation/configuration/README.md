### JSON 
<pre> 
{
    "<a href=#global-options>global-options</a>": "global-options", 
    "<a href=#mandatory-account-configs>mandatory-account-configs</a>": "mandatory-account-configs", 
    "<a href=#organizational-units>organizational-units</a>": "organizational-units", 
    "<a href=#replacements>replacements</a>": "replacements", 
    "<a href=#workload-account-configs>workload-account-configs</a>": "workload-account-configs"
}</pre> 
### YAML 
<pre> 
<a href=#global-options>global-options</a>: global-options
<a href=#mandatory-account-configs>mandatory-account-configs</a>: mandatory-account-configs
<a href=#organizational-units>organizational-units</a>: organizational-units
<a href=#replacements>replacements</a>: replacements
<a href=#workload-account-configs>workload-account-configs</a>: workload-account-configs
</pre> 


<a name= "mandatory-account-configs" href="mandatory-account-configs.md">`mandatory-account-configs`</a> \

*Required*: Yes \
*Type*: mandatory-account-configs \
Landing zones have a concept of core accounts that provides functions that span across many AWS accounts. For example, shared services, networking, security, logging etc. This section allows you to define your core accounts and customise there configuration. \
<a name= "organizational-units" href="organizational-units.md">`organizational-units`</a> \
This section deploys and configures the organisational units used by the accelerator.  \
*Required*: Yes \
*Type*: organizational-units \

<a name= "replacements" href="replacements.md">`replacements`</a> \
Place holder text for what the parameter does \
*Required*: Yes \
*Type*: replacements \
*Allowed Values*: Place holder for allowed values

<a name= "global-options" href="global-options.md">`global-options`</a> \
Configuration values that apply to global settings for the accelerator or default values that will be used in other sections are set here. \

For example details of the buckets used by the accelerator to store customisable configuration files such as SCP's or IAM policies or settings such as default CloudWatch log retention for accounts that are created by the accelerator.\
*Required*: Yes \
*Type*: global-options \
*Allowed Values*: Place holder for allowed values

<a name= "workload-account-configs" href="workload-account-configs.md">`workload-account-configs`</a> \
Landing zone support the creation of non-core accounts used to support the actual worklods being deployed into the environment. This section allows you to define your workload accounts and their configuration. \
*Required*: Yes \
*Type*: workload-account-configs \
*Allowed Values*: Place holder for allowed values
