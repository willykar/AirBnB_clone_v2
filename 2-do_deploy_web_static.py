#!/usr/bin/python3
# Fabfile module called 2-do_deploy_web_static
from os.path import exists
from fabric.api import env
from fabric.api import put
from fabric.api import run

env.hosts = ["54.174.218.185", "54.210.173.234"]


def do_deploy(archive_path):
    """distributes an archive to your web servers

    Arguments:
        archive_path (str)
    Returns:
        if all operations have been done correctly
        Otherwise return False
    """
    if exists(archive_path) is False:
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except:
        return False
