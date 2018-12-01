#!/usr/bin/python 
import paramiko

#wrong change

server_list=['localhost']
mount_point = '/dev/xvda2'
threashold = 90

def check_disk(server,mount_point):
        s = paramiko.SSHClient()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        s.connect(server, username='root', password='pass@123',
                allow_agent=False,look_for_keys=False)
        err,out,ins = s.exec_command("df -h")
        ss=out.read()
        #print ss
        for line in ss.split('\n'):
                #print(line.split()[0])
                if len(line.split()) > 0:
                        if line.split()[0] == mount_point:
                                #print(line.split()[0])
                                #print(line.split()[4])
                                return int(line.split()[4].rstrip('%'))

for server in server_list:
        print(server)
        disk_usage=check_disk(server,mount_point)
        print disk_usage
        if disk_usage > threashold:
                print('Sending email')
        else:
                print('All is well')