#!/usr/bin/python3
""" Fabric script that generates a .tgz archive from
    the contents of the web_static folder of your AirBnB Clone repo
"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """ generates a .tgz archive """

    local('mkdir -p versions')
    t_now = datetime.now()
    t_str = "{}{}{}{}{}{}".format(t_now.year, t_now.month, t_now.day,
                                  t_now.hour, t_now.minute, t_now.second)
    path = "versions/web_static_{}.tgz".format(t_str)
    local('tar -czvf {} web_static'.format(path))
    if os.path.exists(path):
        return path
    else:
        return None
