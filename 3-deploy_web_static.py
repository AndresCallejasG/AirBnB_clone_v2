#!/usr/bin/python3
""" Fabric script for web deployment
"""
from fabric.api import local, put, run, env
from datetime import datetime
import os

env.hosts = ["34.75.237.146", "35.196.182.11"]


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


def do_deploy(archive_path):
    """ distributes an archive to your web servers """
    if not os.path.exists(archive_path):
        return False

    try:
        put(archive_path, "/tmp/")

        file = archive_path.split("/")[-1]
        path = "/data/web_static/releases/{}".format(file.split(".")[0])
        run("mkdir {}".format(path))
        run("tar -zxvf /tmp/{} -C {}/".format(file, path))

        run("rm /tmp/{}".format(file))
        run("mv {}/web_static/* {}/".format(path, path))
        run("rm -rf {}/web_static".format(path))
        run("rm -rf /data/web_static/current")
        run("ln -sf {} /data/web_static/current".format(path))
        print("New version deployed!")
        return True
    except:
        return False


def deploy():
    """ call do_pack and do_deploy full deploy """
    path = do_pack()
    if path:
        return do_deploy(path)
    else:
        return False
