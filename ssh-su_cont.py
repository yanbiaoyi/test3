# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 09:43:56 2020

@author: Administrator
"""

import paramiko
import time

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    ssh.connect(hostname='192.168.123.178',port=22000,username='ufttt',password='86397576@ufttt')
     
    channel = ssh.invoke_shell()
     
    time.sleep(0.1)
     
    channel.send("su - \n")
    buff = ''
    while not buff.endswith('Password: '):
        resp = channel.recv(9999)
        buff += resp.decode('utf-8')
    #print(buff)
        
    channel.send("86397576@root")
    channel.send("\n")
    buff = ''
    while not buff.endswith('# '):
        resp = channel.recv(9999)
        buff += resp.decode('utf-8')
       
    #print(buff)
    print("----end----")
       
    #查看是否切换成功
    channel.send("whoami")
    channel.send("\n")
    # stdin,stdout,stdrr=ssh.exec_command('whoami')
    # print(stdout.read().decode('utf-8'))
    print("----end2----")
    buff = ''
    while not buff.endswith('#'):
        resp = channel.recv(9999)
        buff += resp.decode('utf-8')
    print(buff)
    ssh.close()
except paramiko.ssh_exception.AuthenticationException:
    print("Fail to login,ip username or password not correct")
    ssh.close()
    exit(-1)
    