import click
import json
import boto3
import botocore
import paramiko



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

def get_keypath():
    fptr = open("path.json")
    key_path = json.load(fptr).get("path")
    fptr.close()
    return key_path

@ec2.command()
@click.argument('ip_address')
def ssh_instance(ip_address):
    key_path = get_keypath()
    key = paramiko.RSAKey.from_private_key_file(key_path)
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:      
        client.connect(hostname=ip_address , username="ubuntu", pkey=key)
        print("Connected!")
        
        while True:
            cmd = input("$ ")
            if cmd == "exit":
                break

            stdin, stdout, stderr = client.exec_command(cmd)
           
            std_out = stdout.read().decode('utf-8')[:-1]
            # print("Type of output", type(std_out))
            # print("stdout", std_out == '')

            std_err = stderr.read().decode('utf-8')[:-1]
            # print("Type of output", type(std_err))
            # print("stderr", std_err == '')

            if std_out == "":
                print(std_err)
            else:
                print(std_out)

        client.close()
    
    except Exception as e:
        traceback.print_exc(e)



if __name__ == "__main__":
    ec2() 



 