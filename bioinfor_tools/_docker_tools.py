#!/share/nas2/genome/biosoft/Python//3.7.3/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2023/7/18 17:00
# @Author : jmzhang
# @Email : jmzhang1911@gmail.com


from bioinfor_tools._cmd_runner import CmdRunner
import docker
import time
import logging


class DockerTools:
    def __int__(self, cmd, container_name):
        self.cmd = cmd
        self.container_name = container_name

    def check_container_status(self):
        client = docker.from_env()
        try:
            container = client.containers.get(self.container_name)
            return container.status
        except:
            return None

    def stop_container(self):
        client = docker.from_env()
        try:
            container = client.containers.get(self.container_name)
            container.stop()
        except:
            pass

    def running_then_kill(self, sleep=180):

        status = self.check_container_status()

        if status == "running":
            time.sleep(sleep)

        else:
            CmdRunner.cmd([self.cmd])
