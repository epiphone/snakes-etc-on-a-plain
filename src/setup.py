import os
import re
from distutils.core import setup
import py2exe

datafiles = []
dirs = ['', 'resources', 'resources/audio']
for directory in dirs:
    dirname = './' + directory
    for files in os.listdir(dirname):
        if (directory == ''):
            matchObj = re.search( r'map\d.txt', files, re.M|re.I)
            f1 = dirname + files
            if matchObj:
                f2 = directory, [f1]
                datafiles.append(f2)
        else:
            f1 =  dirname + '/' + files
            if os.path.isfile(f1):
                f2 = directory, [f1]
                datafiles.append(f2)

setup(windows = [{
        'script': 'game.py',
        'dest_base': 'snakes-etc-on-a-plain',
        'icon_resources': [(0, 'resources/icons/icon.ico')]
      }],
      name = 'snakes-etc-on-a-plain',
      data_files = datafiles,
      options = {
        'py2exe': {
            'dist_dir': '../release/win32',
            'dll_excludes': ['w9xpopen.exe'],
            'bundle_files': 1,
            'optimize': 2
      }
})

