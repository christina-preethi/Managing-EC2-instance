import click
import json
import boto3

@click.group()
def ec2():
    pass

@ec2.command()
@click.argument('path')
def set_key(path):
    path_dict = {"path":path}
    
    path_file = open("path.json", "w")
    json.dump(path_dict, path_file, indent=4)
    
    path_file.close()

@ec2.command()
def list_instances():
    ec2 = boto3.resource('ec2')
    for instance in ec2.instances.all():
        print(instance.id, end="\t")
        print(instance.public_ip_address, end="\t")
        print(instance.state.get("Name"))

client = boto3.client('ec2')
@ec2.command()
@click.argument('instanceid')
def start_instance(instanceid):   
    response = client.start_instances(InstanceIds=[instanceid])   
    
    start = response.get("StartingInstances")
    current_state = start[0].get("CurrentState").get("Name")
    print(current_state)

@ec2.command()
@click.argument('my_instance_id')
def stop_instance(my_instance_id):
    # to stop instance
    response = client.stop_instances(InstanceIds=[my_instance_id])
    stop = response.get("StoppingInstances")
    current_state = stop[0].get("CurrentState").get("Name")
    print(current_state)


if __name__ == "__main__":
    ec2() 


 