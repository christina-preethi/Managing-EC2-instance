# Managing-EC2-instance
AWS CLI is a tool that lets you manage your AWS services without actually logging into AWS console.
It provides numerous general commands to manage your EC2 instance but, since I need few customized commands,
I’ve written this script that lets me manage my instances without logging into AWS console.

<h3>Description: </h3>
Following are the commands I’ve created to manage EC2 instance:
<h3>1. Command: ec2 set-key PATH</h3>
The parameter PATH is the absolute path to your private key. This path is taken as input and is written into a JSON file. This path will be used later to SSH into the instances.
<h3>2. Command: ec2 list-instances</h3>
This command lets you list all your instances, including the ones that are stopped, their state and public IP address as well. This is done by making “instances.all” API call using Boto3.
<h3>3. Command: ec2 start-instance INSTANCE_ID</h3>
INSTANCE ID here refers to the instance id of the particular instance which you wish to be started. It is taken as input and used as a parameter to make the “start_instances” API call.
<h3>4. Command: ec2 stop-instance INSTANCE_ID</h3>
The parameter is the id of that particular instance that needs to be stopped. It is done by making the “stop_instances” API call.
<h3>5. Command: ec2 ssh-instance IP_ADDRESS</h3>
This command is used to SSH into EC2. The key path that is saved in a JSON file using the set-key command is used here. A connection is created by using “paramiko.SSHClient()” . Then we make the “connect” API call that connects to the EC2 instance and authenticate using the set key. It takes parameters like username, hostname and key_path. On successful authentication, you would enter into SSH REPL(Read Evaluate Print Loop) following which you can execute any commands and the result will be displayed in the same terminal.
<br/>

<br/><h3>Finally, now I am using my script to manage my instances.</h3>
