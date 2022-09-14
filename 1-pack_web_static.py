#!/usr/bin/python3
""" Fabric script that generates a .tgz archive from the contents of
the web_static folder, using the function do_pack """

from os import path
from fabric.api import local
from datetime import datetime


def do_pack():
    """ must return the archive path if the archive has been
    correctly generated """

    # datetime variable with format
    var_time = datetime.now().strftime("%Y%m%d%H%M%S")

    # Create folder versions if it doesn't exists
    local("mkdir -p versions")

    # Name crafting
    file_name = "versions/web_static_" + var_time

    # File compression
    local("tar -cvzf {}.tgz web_static".format(file_name))

    # Check if the compression was succesfull
    if path.isfile(file_name + ".tgz"):
        return file_name
    else:
        return None
