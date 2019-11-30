# monitoring
script which sends random monitoring data to wavefront



1. Create a lambda using the following code
2. set the execution role that has write permissions to s3
3. Click "add trigger" and choose  Cloudwatch events
4. on next screen from rule dropdown  select "create a new rule"
5. input a rule name  and select rule type  as "schedule expression" and in the field type " rate(1 minute)" and then click "add

Set the following environmental variables :

Bucket Name <your S3 bucket name>
tag_env   <your tag>
tag_source <sml-lam>

you shoud be able to see wavefront time series metric with the metric name :
custom.api.simpleml.utilization

Using which you can create a dashboard


