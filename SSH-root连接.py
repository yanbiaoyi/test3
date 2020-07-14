# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 09:12:47 2020

@author: Administrator
"""
import paramiko

#创建实例化SSHClient
ssh = paramiko.SSHClient()

#自动添加策略，保存服务器的主机名和密钥信息，如果不添加，那么不再本地Konw_hosts文件中记录的主机将无法连接
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#连接SSH服务器，以用户名和密码进行认证
ssh.connect(hostname='192.168.211.129',port=22,username='root',password='rootroot')

#打开Channel并执命令
stdin,stdout,stdrr=ssh.exec_command('df -h')#stdout为正确输出，stderr为错误输出，同时是有1个变量有值

#打印执行结果
print(stdout.read().decode('utf-8'))

#关闭SSHClient
ssh.close()