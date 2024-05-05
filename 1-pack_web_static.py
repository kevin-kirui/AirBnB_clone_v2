#!/usr/bin/python3
"""
Fabric script to generate a .tgz archive
execute: fab -f 1-pack_web_static.py do_pack
"""

from datetime import datetime
from fabric.api import local

def do_pack():
    """
    Create a .tgz archive from the contents of the web_static folder.
    """
    time = datetime.now()
    archive = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    create = local('tar -cvzf versions/{} web_static'.format(archive))
    if create.succeeded:
        return archive
    else:
        return None
